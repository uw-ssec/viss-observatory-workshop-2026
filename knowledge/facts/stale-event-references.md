---
type: Fact
title: Stale text to fix for the observatory event
description: Several files still describe the ISS/Codespaces delivery and must be updated for the Florence JupyterHub event.
tags: [todo, docs, cleanup]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-17T01:29:12Z" }
status: stable
code_refs: [docs/workshop-outline.md, .github/ISSUE_TEMPLATE/config.yml, pyproject.toml]
---

## Known stale references (as of 2026-10-15)

- `docs/workshop-outline.md` still names the Interdisciplinary Science
  Summit in Raleigh, the schmidt-sciences team link and old contacts.
- `.github/ISSUE_TEMPLATE/config.yml` links GitHub Discussions, but Issues
  and Discussions are disabled on this repo.
- `pyproject.toml` project name is `coding-with-agents-workshop`; only
  `pixi.toml` uses `viss-observatory-workshop-2026`.
- The Contact section of `docs/workshop-outline.md` still lists the earlier
  delivery's contacts; the instructor list was updated on 2026-10-16.

## Fixed (2026-10-16)

- The Codespaces + Copilot Chat assumptions in README, the block READMEs,
  slides, notebooks, docs, rules and `.devcontainer/` were rewritten for
  Claude Code on the JupyterHub, and the outline's event, prerequisites and
  Block 3 description were updated. Copilot still appears where it is
  compared with other tools (Block 1 landscape, audience Q&A, resources).

## Sources

Repo inspection and repo-history research, 2026-10-15.

# Related Concepts
- [Repository lineage and past deliveries](repo-lineage.md): leftovers from earlier deliveries
- [Deliver the Florence tutorial on the Schmidt JupyterHub, not Codespaces](../decisions/delivery-on-jupyterhub.md): text that assumes the superseded Codespaces delivery
