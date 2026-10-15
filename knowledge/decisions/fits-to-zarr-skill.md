---
type: Decision
title: "fits-to-zarr skill: wrap a minimal converter, then verify the output"
description: "The fits-to-zarr skill runs ovro-lwa-portal's fits_to_zarr_xradio converter via scripts/convert.py, then scripts/verify.py checks the Zarr against the original FITS."
tags: [skill, fits-to-zarr, verification, block-3, block-4]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T18:17:55Z" }
status: stable
code_refs: [".github/skills/**"]
---

## Decision (Cordero, 2026-10-15)

- The skill **runs the production converter**
  `ovro_lwa_portal.fits_to_zarr_xradio.convert_fits_dir_to_zarr` and then
  **verifies the conversion succeeded**. The agent runs the skill's scripts; it
  does not write its own converter.
- Layout: `.github/skills/fits-to-zarr/SKILL.md` plus
  `scripts/convert.py` (stage copies, convert with header-based grouping,
  attach astrowidget WCS) and `scripts/verify.py` (compare Zarr to the
  original FITS).
- `verify.py` checks inventory, frequencies (1 Hz), time (MJD), **every pixel of
  every plane** (bit-identical, Zarr = FITS transposed), WCS and stored RA/Dec
  (0.1 px tolerance), beam, and astrowidget readability; exit 0 only if all
  pass. A negative test (one altered pixel, WCS removed) fails as expected.
- Output uses PASS/FAIL words, not emoji (notebook convention).
- Skill-authoring rules followed: description with an explicit "Use when"
  trigger, deterministic steps in scripts, the FITS are read-only, never edit
  a script to make a check pass.

## Superseded

- 2026-10-15 (earlier the same day, from technical research): teach a minimal
  astropy + xarray converter instead of depending on ovro-lwa-portal, to avoid
  python-casacore and a private xradio API. Rejected by Cordero in favour of
  running the real converter.

## Sources

Cordero's direction, 2026-10-15; implementation and tests in this repo.

# Related Concepts
- [What ovro-lwa-portal source_review.ipynb actually does](../facts/source-review-notebook.md): reference converter and notebook pattern
- [astrowidget input format and API](../facts/astrowidget-usage.md): output layout must match what astrowidget reads
