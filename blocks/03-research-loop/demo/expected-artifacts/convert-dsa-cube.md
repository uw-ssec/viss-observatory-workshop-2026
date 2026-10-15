# FITS to Zarr: forward-modeled DSA spectral cube

## Input
- Folder: `.data/TSOS_Science_Symposium` — 26 files, 926 x 1076 pixels,
  `RA---SIN` / `DEC--SIN`, phase centre RA 170.0 deg, Dec +39.7006 deg
- Frequencies: 1415.238592-1418.488592 MHz, 26 channels, 130 kHz spacing;
  one time (`DATE-OBS` 2028-07-28T22:20:18.066)
- Notes from the headers: frame `ICRS` with no `EQUINOX`; `BUNIT` Jy/beam;
  per-channel restoring beam (~2.89 x 2.23 arcsec, PA ~90 deg)

## Output
- Zarr: `blocks/03-research-loop/demo/output/dsa-cube.zarr` (97 MB on disk)
- Dimensions: `SKY(time=1, frequency=26, polarization=1, l=926, m=1076)`,
  float32, Jy/beam; plus `BEAM(time, frequency, polarization, beam_param)` in
  radians, per-plane `fits_header_str`, and `right_ascension` / `declination`
  coordinates (FK5, degrees)
- Chunks: `(1, 4, 1, 232, 269)` along `(time, frequency, polarization, l, m)`
- Converter: `ovro_lwa_portal.fits_to_zarr_xradio.convert_fits_dir_to_zarr`
  (via `.github/skills/fits-to-zarr/scripts/convert.py`, grouping by header
  `DATE-OBS` and frequency)

## Verification: PASS
Report: [verify-dsa-cube.md](verify-dsa-cube.md)
- inventory: 26 files -> 26 frequency planes, 1 time
- frequency: matches headers to 1 Hz, strictly ascending
- time: MJD 61980.930765 in both
- pixels: 26/26 planes bit-identical to the FITS images (transposed)
- wcs: max sky offset 0.0139 arcsec over 9 test pixels (tolerance 0.1 arcsec)
- coords: stored RA/Dec agree with the FITS WCS to 0.0139 arcsec
- beam: BMAJ/BMIN/BPA reproduced (unit conversion only)
- astrowidget: WCS found and parsed

## Deviations and caveats
- `EQUINOX = 2000.0` was added to **staged copies** of all 26 files (the
  originals are untouched). The converter relabels the frame as FK5 and xradio
  then requires an equinox; without it the conversion crashes.
- Frame relabelled ICRS -> FK5 (J2000) by the converter. Measured effect: 0.0139
  arcsec, about 1/70 of a pixel. Acceptable for this demo; state it if the cube
  is used for astrometry.
- The celestial WCS was copied into `SKY.attrs["fits_wcs_header"]` (metadata
  only) so astrowidget can read it; the converter stores WCS per plane in
  `fits_header_str`.

## Next
- View it: astrowidget `SkyWidget().set_dataset(open_dataset("blocks/03-research-loop/demo/output/dsa-cube.zarr"))`
