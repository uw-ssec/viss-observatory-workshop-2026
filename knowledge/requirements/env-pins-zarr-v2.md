---
type: Requirement
title: Environment pins for astrowidget (zarr v2)
description: "Block 3 pins: ovro-lwa-portal from git @809aaf4, astrowidget 0.2.0, zarr>=2.18.7,<3 (xarray resolves to 2025.12), Python 3.12 via .python-version, requires-python <3.14; lock written with uv 0.6.14."
tags: [dependencies, uv, zarr, xarray, python-version]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T18:17:55Z" }
status: stable
governance: constraint
code_refs: [pyproject.toml, uv.lock]
---

## Constraint

```toml
requires-python = ">=3.12,<3.14"
"astrowidget==0.2.0", "ovro-lwa-portal", "zarr>=2.18.7,<3"
[tool.uv.sources]
ovro-lwa-portal = { git = "https://github.com/ovro-lwa/ovro-lwa-portal", rev = "809aaf4" }
```

`.python-version` = 3.12. Resolved: xarray 2025.12.0, zarr 2.18.7, numcodecs
0.15.1, astropy 7.2.2, dask 2025.12.0, xradio 0.0.60, python-casacore 3.8.1
(Linux only), pandas 3.0.3, numpy 2.4.4. `nbclient` is in the dev group.

## Why

- ovro-lwa-portal from git: the `time_key_source="header"` option the skill
  needs is not in the v0.1.0 PyPI release.
- astrowidget and ovro-lwa-portal need zarr v2; xarray 2026.4+ breaks zarr 2;
  zarr 2.18.6 + numcodecs 0.16+ crashes on import; numcodecs 0.15 has no
  Python 3.14 wheels.
- The lock is written with **uv 0.6.14** (the Dockerfile's version, lock
  revision 1) so `uv sync --locked` in the image can read it. Newer uv writes
  a newer lock revision.
- The same pins must go into the hub image `environment.yml`.

## macOS gap

xradio only declares python-casacore on non-darwin platforms and there is no
macOS wheel, so the converter cannot run in a plain `uv sync` on macOS. For
local work on a Mac use a conda-forge env (`python-casacore` is on
conda-forge for osx-arm64) or the hub. The hub and Codespaces are Linux.

## Sources

uv 0.6.14 resolution and `uv lock --check`, 2026-10-15; scratch-env runs.

# Related Concepts
- [astrowidget input format and API](../facts/astrowidget-usage.md): astrowidget's zarr v2 requirement drives the pins
- [Deliver the Florence tutorial on the Schmidt JupyterHub, not Codespaces](../decisions/delivery-on-jupyterhub.md): same pins must land in the hub image
