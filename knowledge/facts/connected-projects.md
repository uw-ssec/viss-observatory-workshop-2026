---
type: Fact
title: External projects this workshop depends on
description: "Public projects connected to the workshop: LLMoxie gateway, oai-compatible-copilot, project-template, rse-plugins, ovro-lwa-portal and astrowidget."
tags: [dependencies, ecosystem, llmoxie, ovro-lwa, astrowidget]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T17:39:35Z" }
status: stable
---

## Projects

| Project | Role here |
| --- | --- |
| [uw-ssec/llmoxie](https://github.com/uw-ssec/llmoxie) | SSEC AI gateway (LiteLLM proxy + MLflow, formerly LLMaven). One API key, many models, budgets, IRB-governed tracing. |
| [uw-ssec/oai-compatible-copilot](https://github.com/uw-ssec/oai-compatible-copilot) | VS Code extension that points Copilot Chat at the gateway; pinned by SHA256 in `.devcontainer/`. |
| [uw-ssec/llmoxie-rse-sandbox](https://github.com/uw-ssec/llmoxie-rse-sandbox) | Source of the devcontainer pattern (rebased from pixi onto uv). |
| [uw-ssec/project-template](https://github.com/uw-ssec/project-template) | Maintainer tooling adopted in PR #1 (AGENTS.md, rules, skills, OKF, pre-commit). |
| [uw-ssec/rse-plugins](https://github.com/uw-ssec/rse-plugins) | SSEC agent plugins (incl. Zarr data-format, Zarr chunking, xarray skills); referenced, not a dependency. |
| [ovro-lwa/ovro-lwa-portal](https://github.com/ovro-lwa/ovro-lwa-portal) | OVRO-LWA library: FITS-to-Zarr converter, `radport` accessor, `notebooks/source_review.ipynb`. |
| [ovro-lwa/astrowidget](https://github.com/ovro-lwa/astrowidget) | Zarr-native anywidget that projects radio images onto the celestial sphere; Cordero's package, on PyPI. |

## Sources

Repo-history research and README/devcontainer references, 2026-10-15.
