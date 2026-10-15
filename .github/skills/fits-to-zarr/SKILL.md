---
name: fits-to-zarr
description: 'Convert a folder of radio-astronomy FITS images (one image per frequency channel and/or time) into a single analysis-ready Zarr cube with the production OVRO-LWA converter, then verify the Zarr against the original FITS — inventory, frequencies, times, every pixel, WCS/sky coordinates, beam — and record the result in docs/. Use when someone has FITS images and wants them as one chunked, lazily-loadable Zarr/xarray dataset (e.g. to slice a cube or view it in astrowidget).'
argument-hint: '[FITS folder] [output folder]'
---

# FITS to Zarr (convert, then verify)

Turn a folder of FITS images into one Zarr cube **and prove the conversion is
faithful**. A conversion that "ran" is not a conversion that worked: a
transposed axis, a dropped channel, or a shifted sky position all look fine
until someone does science on them.

The deterministic work lives in two scripts next to this file. **Run them; do
not rewrite them.** Your job is to choose the inputs, run the steps in order,
read the evidence, and write it up.

- `scripts/convert.py` wraps the OVRO-LWA production converter
  (`ovro_lwa_portal.fits_to_zarr_xradio.convert_fits_dir_to_zarr`).
- `scripts/verify.py` checks the Zarr against the **original** FITS.

## Artifacts directory

Write every artifact to — and read prior-phase artifacts from — the **artifacts
directory**: `docs/` at the project root by default, or the exact path `AGENTS.md`
specifies if it sets one. Wherever this skill writes `docs/...` below,
it means *inside that directory*.

## Critical directive

- **The FITS files are read-only.** Never edit, move, or delete them. The
  convert script works on staged copies.
- **Do not invent metadata.** If a header value is missing or inconsistent
  across files (different image sizes, phase centres, or beams that make no
  sense), stop and report it rather than guessing.
- **Do not hand-write a converter** or "fix" the scripts to make a check pass.
  A failed verification is a finding to report, not something to edit away.

## Process

1. **Read `AGENTS.md`** (if present) for the data location, output location, and
   naming slug.
2. **Look before converting.** List the FITS files and read a couple of headers
   (`astropy.io.fits.getheader`). Note: image size, `CTYPE1/2` (projection),
   `CRVAL1/2` (phase centre), `RADESYS`/`EQUINOX`, the frequency keyword
   (`CRVAL3`/`RESTFREQ`), `DATE-OBS`, `BMAJ`/`BMIN`, `BUNIT`. Confirm every file
   has the same image size and phase centre.
3. **Convert** (from the repo root):

   ```bash
   python .github/skills/fits-to-zarr/scripts/convert.py <FITS folder> <output folder> --zarr-name <slug>.zarr
   ```

   It stages copies of the FITS (adding `EQUINOX = 2000.0` where it is missing,
   because the converter labels the frame FK5 and needs an equinox), groups files
   by `DATE-OBS` and header frequency, writes the cube, and attaches the
   celestial WCS where astrowidget reads it (`SKY.attrs["fits_wcs_header"]`).
   The last line it prints is a JSON summary; keep it.
4. **Verify** against the original FITS:

   ```bash
   python .github/skills/fits-to-zarr/scripts/verify.py <FITS folder> <output folder>/<slug>.zarr --report docs/verify-<slug>.md
   ```

   Exit code 0 means every check passed. Read every row, not just the verdict.
5. **Open the result once** with `xarray.open_zarr` and confirm the dimensions
   `(time, frequency, polarization, l, m)` and the `SKY` variable look right.
6. **Write the artifact** `docs/convert-<slug>.md` (structure below) and give a
   short summary in chat: what was converted, where it is, and whether
   verification passed.

## Artifact structure (`docs/convert-<slug>.md`)

```
# FITS to Zarr: <dataset>

## Input
- Folder: <path> — <N> files, <image size>, <projection>, phase centre <RA, Dec>
- Frequencies: <min>–<max> MHz, <N> channels, <spacing>; times: <DATE-OBS values>
- Notes from the headers: <frame/equinox, units, anything unusual>

## Output
- Zarr: <path> (<size on disk>)
- Dimensions: <dims and sizes>; chunks: <chunking>
- Converter: ovro_lwa_portal.fits_to_zarr_xradio.convert_fits_dir_to_zarr (via scripts/convert.py)

## Verification: PASS | FAIL
Report: [verify-<slug>.md](verify-<slug>.md)
- <one line per check, with the key number>

## Deviations and caveats
- <e.g. frame relabelled ICRS -> FK5 J2000 by the converter; offset measured: ...>
- <anything you did differently from this skill, and why>

## Next
- View it: astrowidget `SkyWidget().set_dataset(open_dataset("<zarr>"))`
```

## Constraints

- Run the scripts with the project's Python environment (`uv run python ...`
  in a uv checkout, plain `python` on the JupyterHub).
- If `convert.py` fails, report the error and the header facts from step 2.
  Do not retry with modified scripts.
- If `verify.py` reports a failure, say which check failed and with what
  evidence. The conversion is **not done** until verification passes.
- Next phase: view the cube in astrowidget (see the block's notebook), or hand
  off with the `handoff` skill.
