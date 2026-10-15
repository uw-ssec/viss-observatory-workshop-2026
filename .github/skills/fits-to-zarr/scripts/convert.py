"""Convert a folder of single-channel FITS images into one Zarr cube.

Wraps ``ovro_lwa_portal.fits_to_zarr_xradio.convert_fits_dir_to_zarr`` (the
production OVRO-LWA converter) with the three adjustments a non-OVRO dataset
needs, then makes the store readable by astrowidget:

1. **Staging copies.** The source FITS are never modified. Each file is copied to
   ``<out_dir>/staged_fits/`` and, if it has no ``EQUINOX``, gets
   ``EQUINOX = 2000.0``. The converter rewrites ``RADESYS`` to ``FK5`` and xradio
   then requires an equinox; ICRS inputs (like the DSA cube) have none.
2. **Header-based grouping.** Time comes from ``DATE-OBS`` and frequency from the
   header, not from OVRO-style filenames.
3. **astrowidget WCS.** The converter stores one FITS header string per plane
   (``fits_header_str``). astrowidget looks for a celestial WCS in
   ``SKY.attrs["fits_wcs_header"]``, so we attach it (metadata only).

Usage (from the repo root)::

    python .github/skills/fits-to-zarr/scripts/convert.py INPUT_DIR OUT_DIR \
        --zarr-name cube.zarr [--chunk-lm 512]

Prints a JSON summary on the last line of stdout.
"""

from __future__ import annotations

import argparse
import json
import logging
import shutil
import sys
from pathlib import Path


def stage_inputs(input_dir: Path, staged_dir: Path) -> tuple[list[Path], list[str]]:
    """Copy FITS to a staging folder, adding EQUINOX where missing."""
    from astropy.io import fits

    files = sorted(input_dir.glob("*.fits"))
    if not files:
        raise SystemExit(f"No *.fits files found in {input_dir}")
    staged_dir.mkdir(parents=True, exist_ok=True)
    notes = []
    for src in files:
        dst = staged_dir / src.name
        shutil.copy2(src, dst)
        with fits.open(dst, mode="update") as hdul:
            hdr = hdul[0].header
            if "EQUINOX" not in hdr:
                hdr["EQUINOX"] = (2000.0, "added by fits-to-zarr staging")
                notes.append(src.name)
    return files, notes


def attach_wcs_for_astrowidget(zarr_path: Path) -> str:
    """Store the first plane's celestial WCS where astrowidget reads it."""
    import xarray as xr
    import zarr
    from astropy.io.fits import Header
    from astropy.wcs import WCS

    ds = xr.open_zarr(zarr_path)
    raw = ds["fits_header_str"].values.ravel()[0]
    text = (raw.decode() if isinstance(raw, bytes) else str(raw)).rstrip("\x00 ")
    celestial = WCS(Header.fromstring(text, sep="\n")).celestial
    header_str = celestial.to_header().tostring(sep="\n")

    group = zarr.open_group(str(zarr_path), mode="r+")
    group["SKY"].attrs["fits_wcs_header"] = header_str
    zarr.consolidate_metadata(str(zarr_path))
    return header_str


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("input_dir", type=Path, help="folder of *.fits images (read-only)")
    parser.add_argument("out_dir", type=Path, help="where to write the .zarr store")
    parser.add_argument("--zarr-name", default="cube.zarr")
    parser.add_argument("--chunk-lm", type=int, default=512, help="spatial chunk size")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")
    # The converter warns once per file when it falls back to header metadata,
    # which is exactly what we asked for here.
    logging.getLogger("ovro_lwa_portal").setLevel(logging.ERROR)

    from ovro_lwa_portal.fits_to_zarr_xradio import convert_fits_dir_to_zarr

    out_dir = args.out_dir
    staged_dir = out_dir / "staged_fits"
    if staged_dir.exists():
        shutil.rmtree(staged_dir)
    sources, equinox_added = stage_inputs(args.input_dir, staged_dir)

    zarr_path = convert_fits_dir_to_zarr(
        staged_dir,
        out_dir,
        zarr_name=args.zarr_name,
        fixed_dir=out_dir / "fixed_fits",
        chunk_lm=args.chunk_lm,
        rebuild=True,
        time_key_source="header",
        group_metadata_source="fits",
        cleanup_fixed_fits=True,
    )
    attach_wcs_for_astrowidget(Path(zarr_path))
    # Intermediate copies only; the Zarr store is the product.
    shutil.rmtree(staged_dir)
    shutil.rmtree(out_dir / "fixed_fits", ignore_errors=True)

    summary = {
        "input_dir": str(args.input_dir),
        "n_input_files": len(sources),
        "zarr_path": str(zarr_path),
        "equinox_added_to": len(equinox_added),
        "converter": "ovro_lwa_portal.fits_to_zarr_xradio.convert_fits_dir_to_zarr",
    }
    print(json.dumps(summary))
    return 0


if __name__ == "__main__":
    sys.exit(main())
