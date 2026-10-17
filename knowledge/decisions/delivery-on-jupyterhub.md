---
type: Decision
title: "Deliver the Florence tutorial on the Schmidt JupyterHub, not Codespaces"
description: The tutorial runs on a 2i2c Schmidt events JupyterHub with JupyterAI and Claude Code via the LLMoxie gateway; Codespaces + Copilot Chat is superseded for this event.
tags: [infrastructure, jupyterhub, codespaces, jupyterai, nbgitpuller]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-17T01:27:00Z" }
status: stable
---

## Decision (2026-10-06, confirmed 2026-10-14)

- Day 1 and the hackathon days share one **2i2c-run Schmidt events
  JupyterHub**. Participants log in with a shared password (any username,
  email by convention); walk-ins are fine.
- LLM access: JupyterAI chat panel plus the **Claude Code CLI** in the image.
  The LiteLLM proxy key is provisioned automatically (JupyterHub LiteLLM auth
  helper / login flow), so participants just type `claude` with no OAuth or
  Node install. A script sets Claude's `settings.json` to the allowed model.
- Content arrives via an **nbgitpuller** link (hub, repo, target notebook),
  chosen over baking a git pull into the image build. nbgitpuller pulls content
  only, so **every dependency must be in the hub image**.
- Dependencies are PR'd into the shared image repo (`environment.yml`): base
  set from this repo's `pyproject.toml`, plus Block 3's secondary deps
  (xarray, zarr, astropy, astrowidget, ...), which Cordero supplies.
- Until the image is updated, build content in this repo; move upstream to
  the Schmidt-org repo later.

## Superseded

- 2026-09-11 and 2026-09-18 plans kept GitHub Codespaces + Copilot Chat +
  per-participant gateway keys (sign-up form, GitHub team), with a separate
  Schmidt hub for observatory data. Running VS Code inside the hub was
  rejected then as unknown effort. Superseded on 2026-10-06 when the event
  moved to a single hub.

## Open questions

- How JupyterAI (as opposed to Claude Code) picks up skills is untested.

## Resolved (2026-10-15)

- Skills on the hub: **symlinks are enough** (Cordero). Workshop skills used by
  Block 3 are symlinked into `.agents/skills/` (`fits-to-zarr`,
  `profile-dataset`, `handoff` -> `../../.github/skills/<name>`), and
  `.claude/skills` already points at `.agents/skills`, so Claude Code finds
  them; Copilot still reads `.github/skills/`.
- The Block 3 notebook was executed end to end headlessly and in a real
  JupyterLab 4.6 session; the astrowidget view renders.

## Copilot and Codespaces removed (2026-10-16)

Cordero, after Vani hit Codespaces-era instructions while testing on the hub:

- The `.github/` Copilot copies of the gallery (`agents/`, `prompts/`,
  `instructions/`), `copilot-instructions.md` and the Copilot cloud-agent
  workflow were deleted. Content conventions moved to
  `.agents/rules/workshop-content.md`; `.github/skills/` stays as the
  canonical skills folder, linked into `.claude/skills/`.
- `.devcontainer/` stays only as the fallback if the hub is down, with the
  OAI-compatible Copilot VSIX, its settings and the LLMoxie session setup
  removed. It has no coding agent installed.
- Markdown on the hub opens in the text editor by default; the fix is a hub
  image setting (Markdown Preview as the default viewer), not repo content.
- Unconfirmed: which environment variables the hub sets for the gateway. The
  Block 1 and 2 notebooks read `LITELLM_BASE_URL` and `LITELLM_API_KEY`.

## Sources

Granola meetings 2026-09-11, 2026-09-18, 2026-10-06, 2026-10-14.

# Related Concepts
- [Observatory workshop event: Florence, Nov 3-5 2026](../facts/observatory-event.md): infrastructure chosen for this event
- [LLMoxie gateway as used by the workshop](../architecture/llmoxie-gateway.md): models reach the hub through the gateway
