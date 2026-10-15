# Forward-modeled DSA spectral cube: agent guidance

A small radio-astronomy imaging dataset used as the running scenario in **Block 3**
of the "Coding with AI Agents" workshop. The task is to turn a folder of FITS
images into one Zarr cube, **prove the conversion is faithful**, and view it on
the sky. Read this file first.

## Paths and where to write artifacts

The workshop repo is normally open at its **root**, so use repo-root-relative paths:

- **Input FITS (read-only):** the first of these that exists. The data is
  **not** in git.
  1. the folder named by the `FITS_DATA_DIR` environment variable;
  2. on the workshop JupyterHub, the folder under
     `~/s3/schmidt-observatory-system/nov26-symposium/` that holds the
     `mockfm_nl_cube_ch*.fits` files (a read-only mount of the shared S3
     bucket; read it in place, do not copy it);
  3. `.data/TSOS_Science_Symposium/` at the repo root.
- **Zarr output:** `blocks/03-research-loop/demo/output/dsa-cube.zarr`
  (git-ignored; regenerate it any time).
- **Write every workflow artifact to `blocks/03-research-loop/demo/docs/`**
  (create it if needed): the profile, the conversion record, and the
  verification report. **Do NOT write to the repo's top-level `docs/`.**
- **Slug:** `dsa-cube` (so `docs/profile-dsa-cube.md`, `docs/convert-dsa-cube.md`,
  `docs/verify-dsa-cube.md`).

These artifacts are meant to be **committed**
(`git add blocks/03-research-loop/demo/docs/`) as the audit trail of what was
converted and how it was checked.

## What this data is

A **forward-modeled** spectral-line image cube for DSA (the Deep Synoptic
Array), made for the Schmidt Sciences observatory symposium: a simulated sky
passed through the instrument model. The band sits just below the 1420.4 MHz HI
line. It is simulated: use it to learn the workflow, not to draw scientific
conclusions.

- 26 FITS files, **one frequency channel each**:
  `mockfm_nl_cube_chNN_<freq>MHz.fits`, channels `00`-`25`.
- Each image is **926 x 1076 pixels** (`NAXIS1` x `NAXIS2`) with two degenerate
  axes (`FREQ`, `STOKES`) of length 1.
- Sky projection `RA---SIN` / `DEC--SIN`, phase centre RA 170.0 deg,
  Dec +39.7006 deg, pixel size 1 arcsec, frame `RADESYS = 'ICRS'`, **no `EQUINOX`**.
- Frequencies 1415.2386-1418.4886 MHz in 130 kHz steps (`CRVAL3` = `RESTFREQ`).
- One observation time for every file (`DATE-OBS` 2028-07-28T22:20:18.066,
  `MJD-OBS` 61980.9308).
- Units `BUNIT = 'JY/BEAM'`; each file has its own restoring beam (`BMAJ`,
  `BMIN`, `BPA` in degrees).
- The filenames carry the frequency with a decimal point and no timestamp, so
  **group by header values, not filenames**.

## Conventions

- **Use the `fits-to-zarr` skill and its scripts.** Do not hand-write a
  converter. The skill wraps the production OVRO-LWA converter
  (`ovro_lwa_portal.fits_to_zarr_xradio.convert_fits_dir_to_zarr`).
- **The FITS files are read-only.** Never modify, move, or delete them.
- **Conversion is not done until `verify.py` passes.** Report every failed check
  with its evidence; never edit a script to make a check pass.
- **Expected deviation:** the converter relabels the frame as FK5 (J2000). The
  verification measures the resulting sky offset; anything well under 0.1 pixel
  (0.1 arcsec here) is acceptable and should be stated, not hidden.
- **Expected layout:** `SKY(time=1, frequency=26, polarization=1, l=926, m=1076)`;
  `l` runs along the FITS x axis and `m` along y, so each Zarr plane is the FITS
  image **transposed**.

## Out of scope for this demo

- Science analysis of the cube. The notebook's section 4 makes a moment-0 map
  and a spectrum from the verified Zarr; the conversion task does not.
- Re-gridding, re-projecting, or changing the data values.
- Uploading the Zarr anywhere.

## How to verify a run

Re-run the verifier and confirm every row says PASS:

```bash
python .github/skills/fits-to-zarr/scripts/verify.py <input FITS folder from above> \
    blocks/03-research-loop/demo/output/dsa-cube.zarr
```
