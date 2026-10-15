"""Verify that a Zarr cube faithfully represents the FITS images it came from.

Every check compares the Zarr store against the **original** FITS files (never
against the converter's intermediate copies), so a bug anywhere in the pipeline
shows up here.

Checks:

1. inventory   one frequency plane per input file, one time per DATE-OBS
2. frequency   Zarr frequencies equal the header frequencies, sorted ascending
3. time        Zarr time (MJD) equals the header MJD-OBS
4. pixels      every plane is bit-identical to its FITS image (Zarr is l x m,
               i.e. the FITS array transposed)
5. wcs         the stored celestial WCS maps pixels to the same sky positions
               as the FITS WCS (to within 0.1 pixel)
6. coords      the right_ascension / declination coordinate arrays agree with
               the FITS WCS (to within 0.1 pixel)
7. beam        BEAM major/minor/pa equal BMAJ/BMIN/BPA (unit conversion only)
8. astrowidget astrowidget can find and parse the WCS

Usage (from the repo root)::

    python .github/skills/fits-to-zarr/scripts/verify.py INPUT_DIR ZARR_PATH \
        [--report docs/verify-<slug>.md]

Exits 0 when every check passes, 1 otherwise. Prints a JSON summary last.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


def _sample_pixels(nx: int, ny: int) -> list[tuple[int, int]]:
    """Corners, edge midpoints and centre, as 0-based (x, y)."""
    xs, ys = (0, nx // 2, nx - 1), (0, ny // 2, ny - 1)
    return [(x, y) for x in xs for y in ys]


def verify(input_dir: Path, zarr_path: Path) -> list[Check]:
    import xarray as xr
    from astropy import units as u
    from astropy.coordinates import SkyCoord
    from astropy.io import fits
    from astropy.wcs import WCS

    files = sorted(input_dir.glob("*.fits"))
    ds = xr.open_zarr(zarr_path)
    checks: list[Check] = []

    headers = [fits.getheader(f) for f in files]
    freqs_fits = np.array([float(h.get("RESTFREQ", h.get("CRVAL3"))) for h in headers])
    order = np.argsort(freqs_fits)

    # 1. inventory
    n_times = len({h["DATE-OBS"] for h in headers})
    ok = ds.sizes["frequency"] == len(files) and ds.sizes["time"] == n_times
    checks.append(
        Check(
            "inventory",
            ok,
            f"{len(files)} FITS files, {n_times} DATE-OBS value(s) -> Zarr has "
            f"{ds.sizes['frequency']} frequency plane(s), {ds.sizes['time']} time(s)",
        )
    )

    # 2. frequency
    freqs_zarr = ds["frequency"].values
    same = freqs_zarr.shape == freqs_fits.shape and np.allclose(
        freqs_zarr, freqs_fits[order], rtol=0, atol=1.0
    )
    ascending = bool(np.all(np.diff(freqs_zarr) > 0))
    checks.append(
        Check(
            "frequency",
            same and ascending,
            f"{freqs_zarr.min() / 1e6:.6f}-{freqs_zarr.max() / 1e6:.6f} MHz, "
            f"matches headers to 1 Hz: {same}, strictly ascending: {ascending}",
        )
    )

    # 3. time
    mjd_fits = sorted({float(h["MJD-OBS"]) for h in headers})
    mjd_zarr = ds["time"].values
    ok = len(mjd_zarr) == len(mjd_fits) and np.allclose(mjd_zarr, mjd_fits, atol=1e-6)
    checks.append(
        Check(
            "time",
            ok,
            f"Zarr MJD {[round(float(t), 6) for t in mjd_zarr]} vs header {[round(t, 6) for t in mjd_fits]}",
        )
    )

    # 4. pixels (every plane)
    mismatched = []
    for idx_zarr, idx_file in enumerate(order):
        data = np.squeeze(fits.getdata(files[idx_file])).astype(np.float32)
        plane = ds["SKY"].isel(time=0, frequency=idx_zarr, polarization=0).values
        if plane.shape != data.T.shape or not np.array_equal(plane, data.T, equal_nan=True):
            diff = np.nanmax(np.abs(plane - data.T)) if plane.shape == data.T.shape else "shape"
            mismatched.append(f"{files[idx_file].name} (max |diff| {diff})")
    checks.append(
        Check(
            "pixels",
            not mismatched,
            f"{len(files) - len(mismatched)}/{len(files)} planes bit-identical to FITS (transposed)"
            + (f"; mismatched: {', '.join(mismatched[:3])}" if mismatched else ""),
        )
    )

    # 5. wcs
    src = WCS(headers[order[0]]).celestial
    pix_deg = float(np.max(np.abs(src.wcs.cdelt)))
    tol = 0.1 * pix_deg * u.deg
    hdr_str = ds["SKY"].attrs.get("fits_wcs_header")
    if not hdr_str:
        checks.append(Check("wcs", False, "SKY.attrs['fits_wcs_header'] is missing"))
    else:
        dst = WCS(fits.Header.fromstring(hdr_str, sep="\n"))
        ny, nx = np.squeeze(fits.getdata(files[order[0]])).shape
        pts = _sample_pixels(nx, ny)
        xs, ys = np.array(pts).T
        a = src.pixel_to_world(xs, ys).icrs
        b = dst.pixel_to_world(xs, ys).icrs
        worst = a.separation(b).max().to(u.arcsec)
        frames = f"{src.wcs.radesys or '?'} -> {dst.wcs.radesys or '?'}"
        checks.append(
            Check(
                "wcs",
                worst < tol.to(u.arcsec),
                f"max offset {worst:.4f} over {len(pts)} test pixels "
                f"(tolerance {tol.to(u.arcsec):.3f} = 0.1 px); frame {frames}",
            )
        )

    # 6. coords (l index = FITS x, m index = FITS y)
    if "right_ascension" in ds.coords and "declination" in ds.coords:
        ny, nx = np.squeeze(fits.getdata(files[order[0]])).shape
        pts = _sample_pixels(nx, ny)
        ra = np.array([float(ds["right_ascension"][x, y]) for x, y in pts])
        dec = np.array([float(ds["declination"][x, y]) for x, y in pts])
        unit = ds["right_ascension"].attrs.get("units", "deg")
        frame = ds["right_ascension"].attrs.get("frame", "icrs")
        stored = SkyCoord(ra * u.Unit(unit), dec * u.Unit(unit), frame=frame).icrs
        xs, ys = np.array(pts).T
        expect = src.pixel_to_world(xs, ys).icrs
        worst = stored.separation(expect).max().to(u.arcsec)
        checks.append(
            Check(
                "coords",
                worst < tol.to(u.arcsec),
                f"right_ascension/declination ({frame}, {unit}) max offset {worst:.4f} vs FITS WCS",
            )
        )
    else:
        checks.append(
            Check("coords", True, "no right_ascension/declination coords stored (skipped)")
        )

    # 7. beam
    if "BEAM" in ds:
        unit = u.Unit(ds["BEAM"].attrs.get("units", "rad"))
        beam = ds["BEAM"].isel(time=0, polarization=0).values * unit
        want = np.array([[h["BMAJ"], h["BMIN"], h["BPA"]] for h in headers])[order] * u.deg
        maj_min_ok = np.allclose(
            beam[:, :2].to_value(u.deg), want[:, :2].to_value(u.deg), rtol=1e-3
        )
        bpa_diff = np.abs(((beam[:, 2] - want[:, 2]).to_value(u.deg) + 90) % 180 - 90)
        checks.append(
            Check(
                "beam",
                bool(maj_min_ok and np.all(bpa_diff < 0.5)),
                f"BMAJ/BMIN agree to 0.1%: {maj_min_ok}; BPA max diff {bpa_diff.max():.3f} deg",
            )
        )

    # 8. astrowidget
    try:
        from astrowidget.wcs import get_wcs

        w = get_wcs(ds)
        checks.append(Check("astrowidget", True, f"get_wcs OK ({', '.join(w.wcs.ctype)})"))
    except Exception as exc:  # noqa: BLE001 - report any failure as a failed check
        checks.append(Check("astrowidget", False, f"get_wcs failed: {exc}"))

    return checks


def to_markdown(input_dir: Path, zarr_path: Path, checks: list[Check]) -> str:
    overall = "PASS" if all(c.passed for c in checks) else "FAIL"
    rows = "\n".join(
        f"| {c.name} | {'PASS' if c.passed else 'FAIL'} | {c.detail} |" for c in checks
    )
    return (
        f"# Verification: {zarr_path.name}\n\n"
        f"- Source FITS: `{input_dir}`\n- Zarr store: `{zarr_path}`\n\n"
        f"## Overall: {overall}\n\n| check | result | evidence |\n|---|---|---|\n{rows}\n"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("zarr_path", type=Path)
    parser.add_argument("--report", type=Path, help="write a markdown report here")
    args = parser.parse_args(argv)

    checks = verify(args.input_dir, args.zarr_path)
    md = to_markdown(args.input_dir, args.zarr_path, checks)
    print(md)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(md)
    passed = all(c.passed for c in checks)
    print(json.dumps({"passed": passed, "failed": [c.name for c in checks if not c.passed]}))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
