---
type: Fact
title: astrowidget input format and API
description: "astrowidget SkyWidget reads an xarray Zarr cube with SKY(time,frequency,polarization,l,m) and a newline-separated FITS WCS header string; SIN projection only."
tags: [astrowidget, wcs, zarr, visualization]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T18:31:30Z" }
status: stable
---

## Facts (astrowidget 0.2.0, PyPI, BSD-3, alpha)

- anywidget + inline WebGL2 bundle; no server extension.
- **Sky background:** set `sky.background_survey = "DSS"` (or WISE, 2MASS,
  Planck, a HiPS id) **before the widget is displayed**; the JS reads it at
  render time and loads aladin-lite 3.7.3-beta from esm.sh plus CDS HiPS tiles,
  so it needs internet. Without it the area outside the image is black panels.
  `sky.opacity` (e.g. 0.8) lets the survey show through. Verified in JupyterLab
  4.6: DSS stars surround the radio field and Aladin's readout matches CRVAL.
  This is what "projected onto the sky" means for Cordero's demo.
- Input: xarray Dataset with `SKY(time, frequency, polarization, l, m)`.
  `get_wcs(ds)` looks for, in order: per-time `wcs_header_str` variable,
  `SKY.attrs["fits_wcs_header"]`, `ds.attrs["fits_wcs_header"]`, 0-D
  `wcs_header_str`.
- The header string must parse with `Header.fromstring(s, sep="\n")`. Build
  it with `WCS(hdr).celestial.to_header().tostring(sep="\n")`;
  `WCS.to_header_string()` (no newlines) fails with a CONTINUE-card
  VerifyError.
- Shader projects **SIN** only (matches OVRO all-sky images); other
  projections are an open issue.
- Usage: `ds = open_dataset(path)`; `w = SkyWidget(); w.set_dataset(ds)`;
  set `colormap`, `stretch`, `auto_scale(lo, hi)`; step with
  `update_slice(t, f)`; `goto(SkyCoord, fov=...)`. `set_dataset` downsamples
  to 512 px.
- Known open issues include HiPS background drift when panning and a
  JupyterLab bundle-rendering report; rehearse rendering on the real hub and
  keep a screenshot fallback.
- A headless smoke test (synthetic SIN FITS to Zarr to SkyWidget) passed;
  `update_slice` index read-back looked wrong headless and needs a live check.

## Sources

Clone of ovro-lwa/astrowidget (222be34) and a scratch smoke test, 2026-10-15.

# Related Concepts
- [External projects this workshop depends on](connected-projects.md): published package from ovro-lwa
