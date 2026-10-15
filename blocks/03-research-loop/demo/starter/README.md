# Starter data: forward-modeled DSA spectral cube

The FITS images for this demo are **not stored in git** (26 files, about 100 MB).

- **On the workshop JupyterHub** the data is provided for you in the shared,
  read-only S3 mount under `~/s3/schmidt-observatory-system/nov26-symposium/`;
  the notebook finds it there on its own (`FITS_DATA_DIR`, if set, wins).
- **Anywhere else**, put the 26 `mockfm_nl_cube_chNN_<freq>MHz.fits` files in
  `.data/TSOS_Science_Symposium/` at the repo root (that folder is git-ignored),
  or point `FITS_DATA_DIR` at the folder that holds them.

See [`../AGENTS.md`](../AGENTS.md) for what the data is.
