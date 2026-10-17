# AGENTS.md

Guidance for AI assistants (Claude Code, Codex, Cursor, Copilot, Gemini CLI, and
any other agent harness) working with this repository.

**This file is the entry point and is deliberately short.** It carries only what
every agent needs before doing anything. Detailed rules and conventions live as
separate files under [`.agents/rules/`](.agents/rules/) and are loaded on demand
— read the one whose trigger matches your current task, not all of them.

## What this repo is

The material for **"Coding with AI Agents: A Hands-On Workshop for
Scientists"**: Marp slides, demo notebooks, and starter code organized as four
blocks under `blocks/`. Participants run it on the event JupyterHub, with Claude
Code in a terminal. Content conventions (notebooks as teaching documents, no
emojis, keep the four-block layout) live in
[`.agents/rules/workshop-content.md`](.agents/rules/workshop-content.md) —
follow them when editing workshop material.

Note the two agent-customization trees:

- `.claude/agents|commands|rules/` and the gallery skills in `.github/skills/`
  are **workshop content** — the Claude Code gallery participants study in
  Block 4. Edit them as teaching material.
- `.agents/` (rules and skills, symlinked from `.claude/skills`) is **maintainer
  tooling** for working on this repo, except the gallery skills it links in from
  `.github/skills/` so Claude Code can load them.

## Non-negotiables

These apply to every task, in every session:

1. **Two package managers, each with one job.** The workshop's Python
   environment (notebooks, `sci_units`, `workshop_agent`, tests) is managed by
   **uv**: `uv run <cmd>`, `uv add <pkg>`. Repo tooling (pre-commit, `gh`,
   `okf`) is managed by **Pixi**: run `pixi install` before any other Pixi
   command. Never invoke `pip`, `conda`, or `venv` directly, and never add
   workshop runtime dependencies to `pixi.toml`. See
   [pixi-environments.md](.agents/rules/pixi-environments.md).
2. **Verify before you claim.** Never report work as complete, fixed, or passing
   without having run the check and read its output. The minimum gate here is
   `pixi run pre-commit-all`; when Python code changed, also `uv run pytest`.
3. **Change surgically.** Every changed line must trace directly to the request.
   Don't refactor, reformat, or "improve" adjacent code you weren't asked to
   touch.
4. **Ask instead of assuming.** If the request has multiple readings or
   something is unclear, stop and name it — before implementing, not after.
5. **Never open a PR** without working through
   [`.agents/rules/contribution-discipline.md`](.agents/rules/contribution-discipline.md)
   in full, including human review of the complete diff.

## Rule Index

Load the rule file whose trigger matches what you are about to do.

| Rule file                                                                      | Load when                                                                                      |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| [working-agreement.md](.agents/rules/working-agreement.md)                     | Starting any implementation, refactor, or bugfix — the behavioral baseline                     |
| [contribution-discipline.md](.agents/rules/contribution-discipline.md)         | About to commit, open a PR, or asked to "contribute" / "fix some issues"                       |
| [pixi-environments.md](.agents/rules/pixi-environments.md)                     | Running any command, adding a dependency, or editing `pixi.toml` / `pyproject.toml`            |
| [pre-commit-and-quality.md](.agents/rules/pre-commit-and-quality.md)           | Committing, preparing a PR, or claiming checks pass                                            |
| [repository-map.md](.agents/rules/repository-map.md)                           | You need to know what this repo is, where a file lives, or what CI runs                        |
| [workshop-content.md](.agents/rules/workshop-content.md)                       | Writing or editing workshop material: slides, notebooks, block READMEs, the `.claude/` gallery |
| [onboarding.md](.agents/rules/onboarding.md)                                   | First-time setup, or helping a new contributor get started                                     |
| [troubleshooting.md](.agents/rules/troubleshooting.md)                         | A documented command fails or behaves unexpectedly                                             |
| [mkdocs-okf-knowledge-bundle.md](.agents/rules/mkdocs-okf-knowledge-bundle.md) | Setting up mkdocs to render an OKF-managed knowledge bundle in this repo (optional pattern)    |

## Provenance

The behavioral and contribution rules are adapted from two upstream sources and
generalized for this repository:

- [obra/superpowers](https://github.com/obra/superpowers) `CLAUDE.md` — agent
  contribution discipline (`contribution-discipline.md`).
- [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)
  `CLAUDE.md` — behavioral guidelines that reduce common LLM coding mistakes
  (`working-agreement.md`).

## Trust These Instructions

These instructions were generated through comprehensive exploration and testing
of the repository. Commands have been validated to work correctly. **Only
perform additional searches if:**

- You need information not covered by `AGENTS.md` or `.agents/rules/`
- Instructions appear outdated or produce errors
- You're implementing functionality that changes the build system

For routine tasks (adding files, making code changes, running checks), follow
these instructions directly without additional exploration.
