---
type: Fact
title: "OVRO-LWA FITS-to-Zarr and astrowidget: the backstory"
description: Why the OVRO-LWA project moved FITS image cubes to Zarr and why astrowidget exists; the narrative motivating Block 3.
tags: [ovro-lwa, zarr, fits, astrowidget, narrative]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T17:39:35Z" }
status: stable
---

## What happened

- SSEC (Cordero) worked with Casey Law's Caltech radio astronomy group on
  OVRO-LWA: post-processed FITS image cubes were converted to Zarr/xarray so
  the data could be sliced and lazily loaded (Dask) instead of reading whole
  files, at the cost of larger storage. Repeated operations became xarray
  accessor methods. The engagement unlocked about 96 TB of data.
- WCS is not native to Zarr: the pixel-to-RA/Dec transform was built into
  the package and verified against the astronomers' expectations (a sign
  error in the projection had to be corrected), which is a concrete
  "verify what the agent wrote" story.
- **astrowidget** exists because ipyaladin only took FITS (forcing Zarr to
  FITS round trips) and had a rendering bug buried in its dependencies. A
  Zarr-native widget reusing the useful sky-rendering ideas was prototyped
  and shipped quickly with agents, outside the original scope.
- Casey's team now uses skills and agents themselves.

## Teaching use

Use this as the Block 3 motivation: why FITS to Zarr, why verification of
the coordinates matters, and how agents made an out-of-scope tool feasible.

## Sources

Granola meetings 2026-09-08 (project retrospectives), 2026-09-18 (with Andy
Connolly), 2026-10-13 (with Justin Payan).
