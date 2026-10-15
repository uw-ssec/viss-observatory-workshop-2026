---
type: Bug
title: "astrowidget: update_slice resets the colour scale"
description: "In astrowidget 0.2.0, SkyWidget.update_slice resets vmin/vmax and time_idx/freq_idx read back as 0, so re-apply auto_scale after changing slice."
tags: [astrowidget, visualization, quirk]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T18:17:55Z" }
status: stable
---

## Behaviour (astrowidget 0.2.0)

- `SkyWidget.update_slice(t, f)` recomputes `vmin`/`vmax`, discarding any
  `auto_scale(...)` or manual limits set earlier. The displayed image does
  change to the new slice.
- After `update_slice(0, 20)`, `time_idx`/`freq_idx` still read back as 0.
- `auto_scale(lo, hi)` takes percentiles of the current slice. For a
  noise-dominated radio image, `auto_scale(50, 99.9)` (median to bright tail)
  shows emission far better than the default 2-98 or 1-99.5.

## Handling in the Block 3 notebook

Call `sky.auto_scale(50, 99.9)` again after every `update_slice`.

## Sources

Headless inspection and a live JupyterLab 4.6 check, 2026-10-15.

# Related Concepts
- [astrowidget input format and API](../facts/astrowidget-usage.md): quirk of the astrowidget API
