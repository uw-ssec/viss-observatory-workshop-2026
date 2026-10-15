---
type: Fact
title: Stale text to fix for the observatory event
description: Several files still describe the ISS/Codespaces delivery and must be updated for the Florence JupyterHub event.
tags: [todo, docs, cleanup]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T17:39:36Z" }
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
- README, `.github/copilot-instructions.md` and the block READMEs assume
  Codespaces + Copilot Chat; the event now runs on JupyterHub (see
  [delivery-on-jupyterhub](../decisions/delivery-on-jupyterhub.md)).

## Sources

Repo inspection and repo-history research, 2026-10-15.

# Related Concepts
- [Repository lineage and past deliveries](repo-lineage.md): leftovers from earlier deliveries
- [Deliver the Florence tutorial on the Schmidt JupyterHub, not Codespaces](../decisions/delivery-on-jupyterhub.md): text that assumes the superseded Codespaces delivery
