# Block 3: Further Reading

A small, curated list. Optimized for *applying* what we just demoed
(structured skill workflows, verification, failure-mode awareness) to real research work.

## The workflow we used

- **[`.github/skills/`](../../.github/skills/)**: the workshop skills, each a `SKILL.md`. The demo uses `profile-dataset` and `fits-to-zarr` (whose `scripts/convert.py` and `scripts/verify.py` do the deterministic work); the statistical-analysis loop (`plan-analysis`, `explore-data`, `statistical-tests`, `draft-report`, `validate-analysis`) runs on the text-entry study in [`demo-hci/`](demo-hci/). They ship in-repo, no plugin to install. Read them as the reference for Block 4.
- UW SSEC's [`rse-plugins`](https://github.com/uw-ssec/rse-plugins) is a separate project that packages similar research-engineering skills (including Zarr and xarray ones) as agent plugins.

## FITS, Zarr, and the sky

- **[ovro-lwa-portal](https://github.com/ovro-lwa/ovro-lwa-portal)**: the OVRO-LWA library whose `fits_to_zarr_xradio.convert_fits_dir_to_zarr` the `fits-to-zarr` skill wraps (also `ovro-ingest convert` on the command line).
- **[astrowidget](https://github.com/ovro-lwa/astrowidget)**: the Zarr-native Jupyter widget we used to project the cube onto the sky.
- **[Zarr](https://zarr.dev/)** and **[xarray: reading and writing Zarr](https://docs.xarray.dev/en/stable/user-guide/io.html#zarr)**: chunked, compressed, lazily loaded N-dimensional arrays, and the labelled-array layer on top.
- **[astropy.io.fits](https://docs.astropy.org/en/stable/io/fits/)** and **[astropy.wcs](https://docs.astropy.org/en/stable/wcs/)**: reading FITS headers and turning pixels into sky coordinates — what `verify.py` uses to check the conversion.
- **[FITS World Coordinate System papers](https://fits.gsfc.nasa.gov/fits_wcs.html)**: the reference for `CTYPE`, `CRVAL`, `CDELT`, projections like `SIN`, and frames like ICRS vs FK5.

## Choosing and reporting statistical tests (the `demo-hci/` loop)

- **[scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html)**: the reference for the tests in the demo — `shapiro`, `friedmanchisquare`, `wilcoxon`, and friends. The module index doubles as a "which test exists?" map.
- **[statsmodels](https://www.statsmodels.org/stable/index.html)**: repeated-measures ANOVA (`AnovaRM`), and `stats.multitest.multipletests` for Holm/Bonferroni correction.
- **[Choosing the right statistical test (UCLA IDRE)](https://stats.oarc.ucla.edu/other/mult-pkg/whatstat/)**: a decision-table for matching a test to your design — exactly the judgment `plan-analysis` is trying to encode. The single best link for "I have this design, what test?"
- **[Lakens, *Calculating and Reporting Effect Sizes*](https://doi.org/10.3389/fpsyg.2013.00863)**: why a p-value alone isn't a result. Effect sizes + CIs are a workshop convention for a reason.

## Analysis in HCI specifically (the `demo-hci/` loop)

- **[Cairns, *Doing Better Statistics in Human-Computer Interaction*](https://doi.org/10.1017/9781108685139)**: the practitioner book on getting HCI experiment analysis right (within-subjects designs, non-parametric tests, the mistakes everyone makes).
- **[Transparent Statistics in HCI](https://transparentstats.github.io/guidelines/)**: community guidelines spelling out reviewer expectations (report effect sizes, correct for multiple comparisons, don't dichotomize p). Good for "what will a reviewer want?"

## On agent failure modes

- **[Cognition AI: Don't build multi-agents](https://cognition.ai/blog/dont-build-multi-agents)**: sober counterpoint to the "let's build a swarm" instinct. Reinforces "agents are coworkers, not magic."
- **[Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)**: read this once a year. The vocabulary in the workshop comes mostly from here.
- **[Aider: How to use Aider effectively](https://aider.chat/docs/usage/tips.html)**: pragmatic field notes from one of the longest-running OSS coding agents — concentrated wisdom about scope, prompts, and when to intervene.

## On reproducibility and version control

- **[Software Carpentry](https://software-carpentry.org/lessons/) / [Code Refinery](https://coderefinery.org/lessons/)**: not agent-specific, but the practices that *make agent-driven analysis trustworthy* (small commits, version control hygiene, scripted analyses) are exactly what these lessons teach.
- **[The Turing Way](https://the-turing-way.netlify.app/)**: a community handbook on reproducible research — a good home base for "how should my analysis be organized so someone (or an agent) can re-run it?"

---

If you find a great resource that should be here, open a PR.
