# Repository Map

**Load when:** you need to know what this repository is, where a file lives, or
what CI runs against it.

## Repository Overview

The materials for **"Coding with AI Agents: A Hands-On Workshop for
Scientists"**, a ~2-hour workshop from the UW Scientific Software Engineering
Center (SSEC). Participants work in a GitHub Codespace; Copilot Chat is pointed
at the workshop's LiteLLM gateway by a custom OAI-compatible Copilot extension.
Repo tooling (agent rules, pre-commit, CI) was adopted from
[uw-ssec/project-template](https://github.com/uw-ssec/project-template).

**Repository Stats:**

- **Type:** Workshop materials (Marp slides, Jupyter notebooks, small Python
  packages)
- **Languages:** Markdown, Python 3.12, Jupyter, shell
- **Workshop environment:** uv (`pyproject.toml`, `uv.lock`)
- **Maintainer tooling:** Pixi v0.49.0+ (`pixi.toml`, `pixi.lock`)
- **Platform:** GitHub Codespaces (participants); macOS (osx-arm64) and Linux
  (linux-64, linux-aarch64) for maintainers
- **License:** MIT

## Project Structure & Key Files

```
.
├── blocks/                      # The four workshop blocks (layout is load-bearing; don't restructure)
│   ├── 01-landscape/            # Slides + agent-loop notebook; demo/starter/ is the sci_units package
│   ├── 02-how-it-works/         # Slides + model-swap notebook
│   ├── 03-research-loop/        # Slides + FITS-to-Zarr agent notebook (demo/) and the older HCI stats demo (demo-hci/)
│   ├── 04-build-a-skill/        # Slides + capstone exercise templates
│   └── _shared/slides.css       # Marp theme (registered in .vscode/settings.json)
├── docs/                        # Workshop outline, pre-block checklists, audience Q&A, stats reference
├── workshop_agent/              # Agent loop + tools extracted from Block 1's notebook (keep in sync)
├── .devcontainer/               # Participant Codespace: uv env, Jupyter kernel, LLMoxie/LiteLLM gateway, OAI Copilot VSIX
├── .github/
│   ├── copilot-instructions.md  # Workshop content conventions (also read by Copilot)
│   ├── agents/ prompts/ skills/ instructions/  # WORKSHOP CONTENT: Copilot customization gallery (Blocks 3-4)
│   ├── ISSUE_TEMPLATE/          # Issue templates (bug, feature, docs, onboard, etc.)
│   ├── pull_request_template.md # PR template (requires pre-commit checks)
│   ├── dependabot.yml           # Dependabot config for GitHub Actions
│   ├── release.yml              # Release notes configuration
│   └── workflows/               # zizmor workflow linting, Copilot cloud agent setup
├── .agents/
│   ├── rules/                   # MAINTAINER TOOLING: on-demand rules referenced by AGENTS.md
│   └── skills/                  # Maintainer skills (/commit, /create-pr, /okf-memory, ...)
├── .claude/
│   └── skills -> ../.agents/skills  # Symlink so Claude Code discovers the skills
├── knowledge/                   # OKF project memory, managed by the okf CLI (okf-memory skill)
├── .vscode/                     # Recommended extensions, Marp theme registration
├── pyproject.toml               # uv: workshop dependencies, ruff, pytest config
├── uv.lock                      # uv lock file (auto-generated; Dockerfile builds from it)
├── pixi.toml                    # Pixi: maintainer tooling only (pre-commit, gh, okf, onboard)
├── pixi.lock                    # Pixi lock file (auto-generated, don't manually edit)
├── .pre-commit-config.yaml      # Pre-commit hook configuration
├── AGENTS.md                    # Entry point for AI assistants
├── CLAUDE.md                    # Points Claude Code at AGENTS.md (@AGENTS.md)
├── AI_POLICY.md                 # AI-assisted contribution policy
├── CODE_OF_CONDUCT.md           # Contributor Covenant v2.0
├── CONTRIBUTING.md              # Contribution guidelines (references Conventional Commits)
├── LICENSE                      # MIT License
├── README.md                    # Workshop overview (participant-facing)
└── onboarded.md                 # Empty file (excluded from pre-commit)
```

## Continuous Integration & Validation

**GitHub Actions:** `.github/workflows/zizmor.yml` runs
[zizmor](https://github.com/zizmorcore/zizmor) static analysis to lint workflow
files for security issues. Changes to anything under `.github/workflows/` must
keep this check passing.

**Copilot cloud agent:** `.github/workflows/copilot-setup-steps.yml` prepares
the GitHub Copilot coding agent's environment: the Pixi tooling env from
`pixi.lock` (plus warm pre-commit hook environments) and the uv workshop env
from `uv.lock`. Copilot reads `AGENTS.md` and `.agents/skills/` on its own.

**Pre-commit.ci Integration:** The `.pre-commit-config.yaml` includes a `ci:`
section, suggesting integration with https://pre-commit.ci for automated PR
checks. Verify if enabled on the repository.

**Dependabot:** Configured to update GitHub Actions weekly (groups all action
updates together).

**Tests:** `uv run pytest` (testpaths = `blocks/`, configured in
`pyproject.toml`). Not yet wired into CI.

## Further Reading

For more information on SSEC best practices, see:
https://rse-guidelines.readthedocs.io/en/latest/llms-full.txt
