---
type: Requirement
title: Block 3 data must be small and stay off git
description: "Block 3 uses a forward-modeled DSA cube (26 FITS, ~104 MB), never in git; on the hub it is read in place from the read-only S3 mount under ~/s3/schmidt-observatory-system/nov26-symposium/."
tags: [data, fits, s3, network, block-3]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T21:00:02Z" }
status: stable
---

## Requirements

- Dataset (resolved 2026-10-15): a **forward-modeled DSA spectral-line cube**, 26 FITS
  files `mockfm_nl_cube_chNN_<freq>MHz.fits`, one channel each, 926 x 1076
  pixels, `RA---SIN`/`DEC--SIN` at RA 170.0, Dec +39.70, 1 arcsec pixels,
  1415.24-1418.49 MHz in 130 kHz steps, one `DATE-OBS`, `RADESYS = ICRS`
  with no `EQUINOX`, Jy/beam. About 104 MB total.
- The data is **not in git** (repo is public; sharing permission not
  established). Locally it lives in `.data/TSOS_Science_Symposium/`
  (gitignored); the notebook and AGENTS.md read `FITS_DATA_DIR` first.
- The Zarr output (`blocks/03-research-loop/demo/output/`, ~97 MB) is
  gitignored and regenerated in seconds.
- Venue network is new and untestable; keep data on the hub, avoid runtime
  downloads. astrowidget background surveys and astropy name lookups need
  internet; the notebook uses explicit coordinates.

## Hub location (2026-10-15)

- Every hub server mounts the shared S3 bucket read-only (NFS) at
  `~/s3/schmidt-observatory-system/`, with subfolders including `dsa/` and an
  empty `nov26-symposium/`. Block 3 reads the FITS in place from a folder under
  `nov26-symposium/`; nothing is downloaded. The Zarr is written to the
  participant's home (the mount is read-only; `convert.py` stages copies).
- Lookup order in the notebook and `AGENTS.md`: `FITS_DATA_DIR`, then any folder
  under `nov26-symposium/` holding `mockfm_nl_cube_ch00_*.fits`, then
  `.data/TSOS_Science_Symposium/`.
- Open: the cube is **not yet uploaded** to `nov26-symposium/` (as of
  2026-10-15); someone with bucket write access must put it there.

## Superseded

- The Oct 8 plan named OVRO-LWA image cubes for the tutorial; the data
  actually supplied is the DSA mock cube.

## Sources

Header inspection of the supplied files, 2026-10-15; Granola meetings
2026-10-08 and 2026-10-14.

# Related Concepts
- [fits_to_zarr_xradio: EQUINOX crash on ICRS input; WCS not stored for astrowidget](../bugs/converter-equinox-and-wcs.md): the DSA data's ICRS frame triggers the EQUINOX bug
