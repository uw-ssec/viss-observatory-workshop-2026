---
type: Fact
title: What ovro-lwa-portal source_review.ipynb actually does
description: "source_review.ipynb does no conversion: it opens a cluster Zarr store and runs a Panel/astrowidget source-review app; the converter is fits_to_zarr_xradio.py."
tags: [ovro-lwa, source-review, fits-to-zarr]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T17:40:06Z" }
status: stable
---

## source_review.ipynb (ovro-lwa-portal `notebooks/`, last changed b9c625d)

- Opens a large Stokes-I Zarr store on the OVRO cluster (`/fast/...`,
  `/lustre/...` paths) and builds `SourceReview` (`viz/source_review_app.py`).
- User picks a source (RA/Dec or name via `known_sources.yaml`, astropy
  name lookup, NASA/IPAC extragalactic database fallback); the app computes a time x frequency heatmap via
  the `radport` accessor (`dynamic_spectrum` / `patch_statistic`), and clicking
  a cell shows that slice in an astrowidget `SkyWidget` over a HiPS background
  served by a portal Jupyter server extension.
- It cannot run in the workshop as-is: cluster paths, HiPS extension, large
  data, Dask settings for big workers.

## Where conversion really lives

- `src/ovro_lwa_portal/fits_to_zarr_xradio.py`:
  `convert_fits_dir_to_zarr(input_dir, out_dir, ...)`, plus the
  `ovro-ingest convert` CLI. Fixes headers, reads via a private xradio
  function, regrids subbands, concatenates on `frequency`, appends on `time`.
- Output: `SKY` with dims `(time, frequency, polarization, l, m)`, `time` in
  MJD, `frequency` in Hz, WCS stored as a FITS header string
  (`wcs_header_str` variable and `fits_wcs_header` attrs), chunks of 1 in
  time and `chunk_lm` (1024 default) in l/m.
- Input conventions: filenames like `YYYYMMDD_HHMMSS_<N>MHz_...-I-image.fits`;
  time from `DATE-OBS`, frequency from `RESTFREQ`/`RESTFRQ`/`CRVAL3`/`FREQ`;
  files with missing/zero beam (`BMAJ`/`BMIN`) are dropped.
- `notebooks/fits2zarr.ipynb` is a simpler older version but imports a
  non-public sibling package.

## Sources

Shallow clone of ovro-lwa-portal main (809aaf4), 2026-10-15.

# Related Concepts
- [External projects this workshop depends on](connected-projects.md): lives in ovro-lwa-portal
