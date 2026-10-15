# Dataset profile: forward-modeled DSA spectral cube

## Summary
A forward-modeled spectral-line image cube for DSA (the Deep Synoptic Array),
stored as 26 FITS files with one frequency channel each. Every file images the
same 926 x 1076 pixel patch of sky at the same observation time, so the dataset
is one snapshot across 26 adjacent frequencies near 1.4 GHz. It is synthetic
(per `AGENTS.md`), intended for practice, not science.

## Shape & structure
- 26 files, `mockfm_nl_cube_chNN_<freq>MHz.fits`, channels `00`-`25`; one image
  HDU each.
- Each image is 4-D: `NAXIS1 = 926` (RA), `NAXIS2 = 1076` (Dec), `NAXIS3 = 1`
  (`FREQ`), `NAXIS4 = 1` (`STOKES`); 32-bit float (`BITPIX = -32`).
- One file = one frequency channel of the same field at the same time.

## Header keywords
| keyword | value | varies across files? |
|---|---|---|
| `CTYPE1` / `CTYPE2` | `RA---SIN` / `DEC--SIN` | no |
| `CRVAL1` / `CRVAL2` | 170.0 / 39.700565526891 deg (phase centre) | no |
| `CDELT1` / `CDELT2` | -0.000277778 / 0.000277778 deg (1 arcsec pixels) | no |
| `CRPIX1` / `CRPIX2` | 463.0 / 539.0 | no |
| `RADESYS` | `ICRS` | no |
| `EQUINOX` | **absent** | — |
| `CRVAL3` (= `RESTFRQ` = `RESTFREQ`) | 1415238592.02 Hz (ch00) to 1418488592.02 Hz (ch25), 130 kHz steps | yes, one channel per file |
| `DATE-OBS` / `MJD-OBS` | 2028-07-28T22:20:18.066 / 61980.9308 | no |
| `BUNIT` | `JY/BEAM` | no |
| `BMAJ` / `BMIN` | 2.888-2.895 / 2.228-2.235 arcsec | slightly, per channel |
| `BPA` | 90.14-90.19 deg | slightly, per channel |
| `TELESCOP` / `OBJECT` | `DSA` / `NL full-time spectral synthesis` | no |
| `SPECSYS` | `LSRK` | no |

## Observations a conversion must account for
- The frequency is in the header (`CRVAL3`); the filename repeats it with a
  decimal point, which OVRO-style filename parsing does not expect. Group by
  header values.
- All 26 files share one `DATE-OBS`: the cube has one time step and 26
  frequency planes.
- The frame is `ICRS` with no `EQUINOX`. A tool that relabels the frame as FK5
  will need an equinox.
- Image size, projection, pixel scale and phase centre are identical across
  files; only frequency and (slightly) the beam vary.
- Sampled channel 00: values from -0.00105 to 0.0548 Jy/beam, no NaNs.

## References
- `.data/TSOS_Science_Symposium/*.fits` — the 26 channel images (headers read
  with `astropy.io.fits.getheader`; pixel data sampled for channel 00 only)
- `blocks/03-research-loop/demo/AGENTS.md` — data description, paths, and
  conversion conventions
