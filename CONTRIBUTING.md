# Contributing to the Coding with AI Agents Workshop

Thank you for your interest in contributing to **Coding with AI Agents: A
Hands-On Workshop for Scientists**! This guide provides step-by-step
instructions to set up the project locally. Follow these guidelines to get
started.

Read our
[Code of Conduct](https://github.com/uw-ssec/code-of-conduct/blob/main/CODE_OF_CONDUCT.md)
to keep our community approachable and respectable.

## Pull Requests

We welcome contributions! Please follow these guidelines when submitting a Pull
Request:

- It may be helpful to review
  [this tutorial](https://www.dataschool.io/how-to-contribute-on-github/) on how
  to contribute to open source projects. A typical task workflow is:

  - [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the
    code repository specified in the task and
    [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    it locally.
  - Review the repo's README.md and CONTRIBUTING.md files to understand what is
    required to run and modify this code.
  - Create a branch in your local repo to implement the task.
  - Commit your changes to the branch and push it to the remote repo.
  - Create a pull request, adding the task owner as the reviewer.

- Please follow the
  [Conventional Commits](https://github.com/uw-ssec/rse-guidelines/blob/main/conventional-commits.md)
  naming for pull request titles.

Your contributions make this project better—thank you for your support! 🚀

## Development

### Prerequisites

This repository uses two tools, each with one job:

- **uv** manages the workshop's Python environment (notebooks, `sci_units`,
  `workshop_agent`, tests). This is what participants use in the Codespace.
- **Pixi** manages maintainer tooling: pre-commit, the GitHub CLI, the `okf`
  project-memory CLI, and onboarding.

The Codespace (`.devcontainer/`) already has uv set up. To work locally, install
both.

#### Install uv

Install [uv](https://docs.astral.sh/uv/) by following the
[installation instructions](https://docs.astral.sh/uv/getting-started/installation/),
then create the workshop environment:

```bash
uv sync
uv run pytest
```

Add workshop dependencies with `uv add <package>` and commit the updated
`uv.lock`.

#### Install Pixi

Pixi is used in this project to manage the maintainer tooling environment and to
set up some convenient ways to run tools within it.

To get started, install [Pixi](https://pixi.sh/latest/) using either the
[instructions on their website](https://pixi.sh/latest/#installation), or the
commands below:

**macOS/Linux:**

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

### Configure pre-commit

PRs will fail style and formatting checks as configured by
[pre-commit](https://pre-commit.com/), but you can set up your local repository
such that precommit runs every time you commit. This way, you can fix any errors
before you send out pull requests!

#### Configure pre-commit to run on every commit

Then, once Pixi is installed, run the following command to set up pre-commit
checks on every commit

```
pixi run pre-commit-install
```

#### Manually run pre-commit on non-committed files

```
pixi run pre-commit
```

#### Manually run pre-commit on all files

```
pixi run pre-commit-all
```

### Access `ssec` CLI

The `ssec` CLI contains some convenience functions for setting up and working
with this repository. More information about the tool can be found here:
https://github.com/uw-ssec/ssec-cli

#### Set up autocompletions

```
pixi run ssec-setup
```

#### Run `ssec` command

```
pixi run ssec <options>
```

#### Run `ssec` command with autocompletion

Open Pixi shell

```
pixi shell
```

Start typing :)

```
ssec <tab>
```
