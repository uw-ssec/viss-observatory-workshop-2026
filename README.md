# Coding with AI Agents: A Hands-On Workshop for Scientists

This repository contains the slides, demos, and hands-on notebooks for a ~2-hour workshop teaching scientists how AI coding agents work and how to use them well in research software engineering.

## Workshop structure

The workshop is organized into four 30-minute-ish blocks.

| # | Block | Folder | Format |
|---|---|---|---|
| 1 | The AI Coding Agent Landscape | [`blocks/01-landscape/`](blocks/01-landscape/) | Slides + demo notebook |
| 2 | How It Actually Works (post-training & tool calling) | [`blocks/02-how-it-works/`](blocks/02-how-it-works/) | Slides + model-swap notebook |
| 3 | Agent-Driven Research Software Engineering | [`blocks/03-research-loop/`](blocks/03-research-loop/) | Slides + FITS-to-Zarr agent notebook |
| 4 | Build Your Own Skill (capstone) | [`blocks/04-build-a-skill/`](blocks/04-build-a-skill/) | Slides + hands-on custom-agent build |

Each block folder follows a similar layout:

```
blocks/0N-name/
  README.md            # what this block teaches
  slides.md            # Marp slides (includes demo prompts)
  resources.md         # curated further reading
  demo/                # runnable code, starter files, notebooks
```

## Tools used

- **Copilot Chat in VSCode / Codespaces**: The Codespace ships a custom **OAI-compatible Copilot** extension ([`uw-ssec/oai-compatible-copilot`](https://github.com/uw-ssec/oai-compatible-copilot)) that points Copilot Chat at the workshop's AI gateway, so you pick the workshop's models in the model picker with no Copilot subscription or setup.
- **Copilot Chat Skills** for Block 3's research loop: `profile-dataset`, `plan-analysis`, `explore-data`, `statistical-tests`, `draft-report`, `validate-analysis`, `handoff` ship **in-repo** as [`.github/skills/<name>/SKILL.md`](.github/skills/) and run in the same Copilot Chat panel (agent mode). The agent auto-selects a skill from its `description`, or you invoke one by name.
- **Claude Models (via the workshop's gateway)**: the model backend, fronting Claude Sonnet 4.6 and Claude Haiku 4.5. Copilot Chat and the notebooks hit the same gateway. The notebooks use the **`litellm` Python SDK**, so the same agent loop works against any other model the gateway fronts.
- **Python 3.12 + `uv`**: environment and package management.
- **Marp**: slides as markdown.

You don't need anything installed locally: everything runs in a GitHub Codespace.

## Agent customization gallery

The [`.claude/`](.claude/) folder is a **worked gallery** of ways to customize an AI coding agent for research software engineering with Claude Code. It pairs with Block 4 ("Build Your Own Skill"): read these as references, and then write your own. Everything there is plain markdown but contains **structured prompts, tool lists, and project context**. The same ideas port to Copilot, Cursor rules, and other coding agent harnesses: the [`.github/`](.github/) folder keeps the GitHub Copilot version of every gallery file, so you can compare the two formats side by side.

### The five primitives

| Primitive                | Folder                           | Invoked                                  | Best for                                     |
| ------------------------ | -------------------------------- | ---------------------------------------- | -------------------------------------------- |
| **Project memory**       | `CLAUDE.md` / `AGENTS.md`        | Always on                                | Conventions every session should know        |
| **Path-scoped rules**    | `.claude/rules/*.md`             | Auto, by `paths` glob                    | Rules for a file type (notebooks, tests)     |
| **Subagents**            | `.claude/agents/*.md`            | `@agent-<name>`, or Claude delegates     | A focused persona with a narrow tool list    |
| **Slash commands**       | `.claude/commands/*.md`          | `/name` slash command                    | A repeatable one-shot task                   |
| **Skills**               | `.claude/skills/<name>/SKILL.md` | On demand (auto or `/name`)              | A multi-step capability that bundles scripts |

> **Note on layout:** `.claude/skills` is a link to `.agents/skills/`, where the
> workshop skills sit (as links into `.github/skills/`) next to the maintainer
> skills. Any agent harness that reads `.agents/` or `.claude/` sees the same set.

### Mapped to the research-software lifecycle


| Lifecycle phase           | What it is                                          | Primitive | Location                                                                           |
| ------------------------- | --------------------------------------------------- | --------- | ---------------------------------------------------------------------------------- |
| Data conversion (Block 3) | FITS images → verified Zarr cube (`fits-to-zarr`)   | skill     | [`.claude/skills/`](.claude/skills/)                                               |
| Full analysis loop        | Orchestrate the seven research-loop skills          | agent     | [`research-data-scientist`](.claude/agents/research-data-scientist.md)             |
| Project setup             | Flat script → installable package (plan)            | command   | [`scaffold-package`](.claude/commands/scaffold-package.md)                         |
| Data / EDA                | First look at a dataset                             | command   | [`eda-summary`](.claude/commands/eda-summary.md)                                   |
| Implementation / planning | Read-only thinking partner, then hand off           | agent     | [`research-pair`](.claude/agents/research-pair.md)                                 |
| Testing / validation      | Focused pytest tests for a target                   | command   | [`write-tests`](.claude/commands/write-tests.md)                                   |
| Reproducibility           | Audit for paths, seeds, pinned env                  | agent     | [`reproducibility-auditor`](.claude/agents/reproducibility-auditor.md)             |
| Documentation             | Add NumPy-style docstrings                          | agent     | [`docstring-writer`](.claude/agents/docstring-writer.md)                           |
| Code review               | Review vs Scientific Python guidelines              | agent     | [`scientific-python-reviewer`](.claude/agents/scientific-python-reviewer.md)       |
| Packaging / publication   | Draft `CITATION.cff` + release notes                | command   | [`citation-and-release`](.claude/commands/citation-and-release.md)                 |
| Conventions (notebooks)   | Notebook-as-teaching-document rules                 | rule      | [`notebooks.md`](.claude/rules/notebooks.md)                                       |
| Conventions (tests)       | pytest + `uv` conventions                           | rule      | [`tests.md`](.claude/rules/tests.md)                                               |

### How to try them on the JupyterHub

Open a terminal, `cd` to the repo root, and run `claude`. Then:

- **Agents:** type `@` and pick one (e.g. `@agent-reproducibility-auditor`
  followed by a file), or ask in words: "use the reproducibility-auditor
  subagent on ...". For the conversational `research-pair`, run the whole
  session as that agent: `claude --agent research-pair`.
- **Commands:** type `/` and pick one (e.g. `/eda-summary`), or pass the
  input: `/write-tests sci_units.converters`.
- **Skills:** ask in plain language ("profile the text-entry dataset in
  `blocks/03-research-loop/demo-hci/starter/`") and the matching research-loop skill
  (here `profile-dataset`) loads on demand.
- **Rules:** ask Claude to work on a notebook or a file under `tests/` and they
  apply automatically.


## Repo conventions

- One folder per block, reusable layout.
- All Python work goes through `uv` (`uv run pytest`, `uv add <pkg>`, etc.).
- Notebooks are written to be read top-to-bottom as a teaching document, not just executed.
- Slides are written for the **Marp for VS Code** extension (preinstalled in the Codespace). Open any `slides.md` and click the preview icon.


## Maintaining this repository

> **Participants can skip this section.** Nothing here is needed to follow the workshop.

The repo tooling is adapted from [`uw-ssec/project-template`](https://github.com/uw-ssec/project-template):

- **uv** owns the workshop's Python environment (`pyproject.toml`, `uv.lock`), and **[Pixi](https://pixi.sh)** owns maintainer tooling (`pixi.toml`): pre-commit, the GitHub CLI, and the `okf` project-memory CLI. Run `pixi install`, then `pixi run pre-commit-install`; run `pixi run pre-commit-all` before opening a PR.
- [`AGENTS.md`](AGENTS.md) (and `CLAUDE.md`, which imports it) is the entry point for AI agents working **on** this repo. It points to on-demand rules in [`.agents/rules/`](.agents/rules/).
- [`.agents/skills/`](.agents/skills/) holds maintainer skills (`commit`, `create-pr`, `okf-memory`, ...), linked from `.claude/skills`. The participant-facing gallery skills live in `.github/skills/` and are linked in alongside them.
- [`knowledge/`](knowledge/) is OKF project memory, read and written with `pixi run okf`.

See [CONTRIBUTING.md](CONTRIBUTING.md), and the [AI Policy](AI_POLICY.md) if you use AI tools while contributing.

## Contact

- **Anshul Tambay**, UW SSEC, [anshul37@uw.edu](mailto:anshul37@uw.edu)
