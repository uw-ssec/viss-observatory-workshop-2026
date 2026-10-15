---
marp: true
theme: workshop
paginate: true
title: "Block 4 - Build Your Own Skill"
description: "Coding with AI Agents"
---

<!-- _class: lead -->

# Build Your Own Skill

## Block 4: Capstone


---

## The whole workshop, in one slide

| Block | Takeaway |
|---|---|
| 1. Landscape | All coding agents have the same anatomy: LLM + tools + memory + loop. |
| 2. How it works | Triage failures: **prompt problem** vs **training problem**. The prompt is your lever. |
| 3. Workflows | **Workflows are reusable skills** that are structured and auditable. The agent picks one or you invoke it. |
| 4. **Now** | Write one. |

--
> The next 25 minutes are practice.

---


## Commands vs. skills vs. agents (all in `.claude/`)

Three primitives, same idea (a markdown file = instructions + tools), different shapes:

| | **Slash command** | **Skill** | **Subagent** |
|---|---|---|---|
| **Folder** | `.claude/commands/*.md` | `.claude/skills/<name>/SKILL.md` | `.claude/agents/*.md` |
| **Invoked** | You type `/name` | Claude auto-picks (or `/name`) | `@agent-name`, "use the X subagent", or Claude delegates |
| **Input** | `$ARGUMENTS` after the command | Natural-language context (+ `argument-hint`) | The task Claude hands it |
| **Best for** | One-shot repeatable task | A multi-step capability (can bundle scripts) | A focused persona with a fixed tool list and its own context |
| **Lifespan** | One turn | One task | One delegated task (or the whole session with `claude --agent`) |
| **Example here** | `eda-summary`, `scaffold-package` | the 6 research-loop skills | `docstring-writer`, `research-data-scientist` |

> They **compose**: `research-data-scientist` (an *agent*) drives the seven *skills* in
> order. Pick the smallest primitive that does the job — most of the time that's a
> command or a skill, not a whole agent.

> The fourth primitive, **rules** (`.claude/rules/*.md`), is never invoked: Claude
> loads them when it touches a file matching their `paths` glob.

---

## Your turn (~15 min)

1. **Copy** the template:
    ```bash
    cp blocks/04-build-a-skill/exercise/my-agent.md.template \
       .claude/agents/my-agent.md
    ```
2. **Pick** a target, the `sci_units` package, the Block 3 FITS cube, the text-entry dataset in `blocks/03-research-loop/demo-hci/`, or your own code.
3. **Pick** a job, see `exercise/ideas.md`, or invent your own.
4. **Edit** the file: name, description, tools, system prompt, constraints.
5. **Run** `claude` in a JupyterHub terminal at the repo root (new agents are picked up live).
6. **Call** it with `@agent-my-agent ...` and **iterate**.

Full instructions: [`blocks/04-build-a-skill/exercise/README.md`](../../blocks/04-build-a-skill/exercise/README.md)

> Instructors circulating. **Get something narrow working** before
> trying to make it broader. Ship a boring agent that runs over an
> ambitious agent that doesn't.

---

## Wrap-up

You now have:

- A mental model that survives the next product release from a frontier AI lab
- A concrete agentic workflow you've seen run on real data
- A subagent you wrote yourself that **lives in your repo**, ready for any Claude Code session


> Thank you for spending the afternoon with us.
