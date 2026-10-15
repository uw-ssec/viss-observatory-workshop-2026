# Bugs
* [fits_to_zarr_xradio: EQUINOX crash on ICRS input; WCS not stored for astrowidget](converter-equinox-and-wcs.md) - ovro-lwa-portal's converter forces RADESYS=FK5 without EQUINOX (xradio KeyError on ICRS files) and its output lacks the fits_wcs_header astrowidget needs; convert.py works around both.
* [astrowidget: update_slice resets the colour scale](astrowidget-update-slice-resets-scale.md) - In astrowidget 0.2.0, SkyWidget.update_slice resets vmin/vmax and time_idx/freq_idx read back as 0, so re-apply auto_scale after changing slice.
