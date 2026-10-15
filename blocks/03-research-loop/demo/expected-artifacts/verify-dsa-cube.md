# Verification: dsa-cube.zarr

- Source FITS: `.data/TSOS_Science_Symposium`
- Zarr store: `blocks/03-research-loop/demo/output/dsa-cube.zarr`

## Overall: PASS

| check | result | evidence |
|---|---|---|
| inventory | PASS | 26 FITS files, 1 DATE-OBS value(s) -> Zarr has 26 frequency plane(s), 1 time(s) |
| frequency | PASS | 1415.238592-1418.488592 MHz, matches headers to 1 Hz: True, strictly ascending: True |
| time | PASS | Zarr MJD [61980.930765] vs header [61980.930765] |
| pixels | PASS | 26/26 planes bit-identical to FITS (transposed) |
| wcs | PASS | max offset 0.0139 arcsec over 9 test pixels (tolerance 0.100 arcsec = 0.1 px); frame ICRS -> FK5 |
| coords | PASS | right_ascension/declination (fk5, deg) max offset 0.0139 arcsec vs FITS WCS |
| beam | PASS | BMAJ/BMIN agree to 0.1%: True; BPA max diff 0.000 deg |
| astrowidget | PASS | get_wcs OK (RA---SIN, DEC--SIN) |
