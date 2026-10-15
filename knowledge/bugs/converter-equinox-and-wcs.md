---
type: Bug
title: "fits_to_zarr_xradio: EQUINOX crash on ICRS input; WCS not stored for astrowidget"
description: "ovro-lwa-portal's converter forces RADESYS=FK5 without EQUINOX (xradio KeyError on ICRS files) and its output lacks the fits_wcs_header astrowidget needs; convert.py works around both."
tags: [ovro-lwa-portal, xradio, wcs, astrowidget, workaround]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T18:17:55Z" }
status: stable
---

## Symptoms (ovro-lwa-portal @809aaf4, xradio 0.0.60)

1. `_fix_headers` sets `RADESYS = 'FK5'` but never adds `EQUINOX`. xradio's
   FITS reader then needs `EQUINOX` for non-ICRS frames and raises
   `KeyError: "Keyword 'EQUINOX' not found."`. OVRO files evidently carry an
   equinox; the DSA files (ICRS, no EQUINOX) do not.
2. The written store has per-plane `fits_header_str` but no
   `SKY.attrs["fits_wcs_header"]` / `wcs_header_str`, so astrowidget's
   `get_wcs` fails ("No WCS header found"). The converter sets
   `fits_wcs_header` in memory but it does not survive the write.
3. The converter leaves one reference-grid FITS in `fixed_dir`.

## Workarounds in `.github/skills/fits-to-zarr/scripts/convert.py`

- Stage copies of the inputs and add `EQUINOX = 2000.0` where missing (the
  originals stay untouched). Effect of the ICRS -> FK5 J2000 relabel:
  0.0139 arcsec on this data, measured by `verify.py`.
- After conversion, copy the first plane's celestial WCS into
  `SKY.attrs["fits_wcs_header"]` (`Header.fromstring(s, sep="\n")`) and
  reconsolidate metadata.
- Remove the staging and fixed-FITS folders.

## Upstream

Not yet reported to ovro-lwa/ovro-lwa-portal; worth an issue (ask Cordero
before filing).

## Sources

Scratch runs on the DSA mock cube, 2026-10-15.

# Related Concepts
- [fits-to-zarr skill: wrap a minimal converter, then verify the output](../decisions/fits-to-zarr-skill.md): workarounds live in the skill's convert.py
