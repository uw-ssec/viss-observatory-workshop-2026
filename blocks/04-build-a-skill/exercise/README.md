# Exercise: Build Your Own Subagent

By the end of this exercise you will have **a working Claude Code
subagent you wrote yourself**, runnable from Claude Code in a JupyterHub
terminal.

The worked examples in [`.claude/agents/`](../../../.claude/agents/)
(`scientific-python-reviewer` and `docstring-writer`) are your reference.
Read them, copy patterns, then make something different.

You won't get the prompt right on the first try, and you're not meant to.
Steps 1–3 set you up; steps 4–6 are where you edit, run, and adjust until
the agent behaves.

## 1. Setup (1 min)

Open a terminal in JupyterHub, `cd` to the repo root, and copy the template
into the agents directory. The name is how you call the agent, so pick a
sensible one.

```bash
cp blocks/04-build-a-skill/exercise/my-agent.md.template \
   .claude/agents/my-agent.md
```

(Replace `my-agent` with whatever you want to call your agent. Examples:
`error-explainer`, `style-checker`, `assumption-checker`.)

## 2. Pick a target (1 min)

What code (or data, or notebook) will your agent run against? Pick
whichever gets you to "running" fastest:

**Your own work** — a snippet of code, a notebook, a CSV from your lab, a transcript. This is the most useful target if you brought something. The pattern is identical regardless of domain (physical science, ML, behavioral / social science, bio, stats, qualitative work).

No code of your own? Use `sci_units` or the Block 3 dataset, or drop a
notebook or CSV from your lab into a scratch folder. The point is the
*pattern*, not the example.

## 3. Pick a job (1 min)

What does your agent do? See [`ideas.md`](ideas.md) for 30+ starting ideas
across categories: code review, code generation, refactoring, HCI /
experiment analysis, general research, behavioral / social science / stats,
experiment management, onboarding.

Or invent your own. The good first ones are **narrow** ("review against
one specific guideline", "explain one specific kind of error") rather than
ambitious ("become a full agent for my project").

## 4. Edit the agent (8-10 min)

Your first pass doesn't have to be complete, just enough to run.
Open `.claude/agents/my-agent.md` (in the JupyterHub file browser or editor)
and fill in the TODOs:

| Field | Guidance |
|---|---|
| `name` | The identifier you call the agent by. Match the filename minus `.md`. Lowercase letters and hyphens. |
| `description` | One line saying what it does and when to use it. Claude reads this to decide when to delegate, so make it specific. |
| `tools` | Start narrow. `Read, Grep, Glob` is read-only and safe. Add `Edit` (and `Write` for new files) only if your agent needs to modify code. Add `Bash` only if it needs to run shell (e.g., `pytest`). Leave `tools` out entirely and the agent gets every tool, which defeats the point. |
| Persona / what you do | A few sentences setting role, then a numbered list of steps. Be specific. Vague prompts produce vague behavior. |
| What you do NOT do | The constraints are as important as the instructions. "Do not edit files outside `tests/`" is a real safety lever. |
| Output format | Show an example of what good output looks like. Concrete examples beat abstract descriptions. The agent's final message is all the main conversation gets back, so ask for a complete report. |

**Pattern to copy:** look at `.claude/agents/scientific-python-reviewer.md` for a read-only agent and `.claude/agents/docstring-writer.md` for an agent that edits files.

## 5. Try it (3-5 min)

Run the agent and watch what it actually does, noting anything it got wrong.

1. In the terminal at the repo root, run `claude` (or keep using the session
   you already have open; new agent files are picked up without a restart).
2. Call your agent by name. Type `@` and pick `agent-my-agent` from the list,
   or say it in words: *"Use the my-agent subagent to ..."*. If it isn't
   listed, see [Troubleshooting](#troubleshooting).
3. Type a query that exercises your agent. The subagent works in its own
   context and hands a report back to the main conversation.

Example queries depending on what you built:
- For a reviewer: *"@agent-my-agent review `blocks/01-landscape/demo/starter/src/sci_units/converters.py`."*
- For a docstring writer: *"Add docstrings to `blocks/01-landscape/demo/starter/src/sci_units/converters.py`."*
- For an assumption checker: *"Check the normality assumption on `blocks/03-research-loop/demo-hci/starter/data.csv`."*
- For an error explainer: *"Explain this traceback: <paste>."*

## 6. Iterate (back to step 4)

Did your agent do what you expected? If not, match what you saw to a fix:

- **Behavior too vague?** Tighten the steps in your system prompt.
- **Wrong tool used?** Adjust the `tools` list.
- **Output format off?** Add a more concrete example to the "Output format" section.
- **Agent being too cautious or too eager?** Add explicit "do NOT" constraints.

Change one thing at a time, then re-run. Two or three passes is normal;
stop when it's good enough to be useful. This is the same prompt
engineering behind the Block 3 research-loop skills in `.claude/skills/`.

## 7. Stretch: take it further

If your agent is working and you've still got time, pick one of these.
Each is ~10-20 min, none are required, all are good office-hours starting
points. Expect to iterate on these the same way as steps 4–6.

### Stretch A — Promote your agent to a skill

A **skill** (`.claude/skills/<name>/SKILL.md`) is the next primitive up
from an agent: it can bundle scripts and resources and load on demand.
The fields are slightly different (YAML frontmatter with `name` and
`description`; markdown body) but the *shape* is identical to a
subagent: persona + steps + tools + output format. See the worked
Block 3 research-loop skills in [`.claude/skills/`](../../../.claude/skills/).

1. Make `.claude/skills/<your-skill-name>/` at the repo root.
2. Copy the skeleton into it and fill in the TODOs (or paste the body from your agent):

```bash
mkdir -p .claude/skills/my-skill
cp blocks/04-build-a-skill/exercise/my-skill.SKILL.md.template \
   .claude/skills/my-skill/SKILL.md
```

3. Ask for it in plain language, or run it directly as `/my-skill`. No restart
   needed.

Same handful of fields, different file path. That's the "primitives are
just structured prompts" claim from Block 1, made concrete.

### Stretch B — Chain two agents with a slash command

Agents are good for one-job interactions. **Slash commands**
(`.claude/commands/*.md`) are good for one-shot orchestrations
("review this, then fix what you found"). The `.claude/commands/` folder
already has a few worked commands to copy from.

1. Copy the skeleton into the commands directory:

```bash
cp blocks/04-build-a-skill/exercise/my-command.md.template \
   .claude/commands/review-and-fix.md
```

2. Fill in the body — e.g. *"First, use the scientific-python-reviewer subagent on `$ARGUMENTS`. Then use the docstring-writer subagent to add the missing docstrings it found."*
3. Invoke it with `/review-and-fix path/to/code.py`. Whatever you type after
   the command name replaces `$ARGUMENTS`.

Slash commands are the one-shot cousin of the Block 3 research-loop skills:
where a skill is a multi-step capability the agent auto-selects, a command
is a templated `/slash` prompt you fire deliberately.

### Stretch C — Add path-scoped instructions

The fourth primitive. **Rules** (`.claude/rules/*.md`)
aren't invoked at all — Claude Code loads them whenever it reads or edits a
file matching their `paths` glob. They're the place for "always do X in files
like this" rules. See the worked examples in
[`.claude/rules/`](../../../.claude/rules/).

1. Copy the skeleton into the rules directory:

```bash
cp blocks/04-build-a-skill/exercise/my-rule.md.template \
   .claude/rules/my-rules.md
```

2. Set `paths` to the files your rules govern (e.g. `"**/tests/**/*.py"`) and
   fill in the bullet list of conventions.
3. Ask Claude to work on a matching file — the rules load with no invocation.
   Rules are read at load time, so start a fresh `claude` session after adding
   one.

## 8. Show it off

If your agent works and you have a few minutes left, share it:
- Volunteer for the show-and-tell (instructor will ask).
- Paste the agent into the workshop chat / Slack / wherever.
- Save it to your own GitHub fork to keep using after the workshop.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Agent doesn't show up after `@` | Confirm the file ends in `.md`, lives in `.claude/agents/` at the repo root, and that you started `claude` from the repo root. Quit (`/exit`) and run `claude` again. |
| Agent appears but won't load | Check the YAML frontmatter, common issues are missing quotes around the description or a missing `name`. The first line should be `---` exactly. |
| Agent runs but ignores your prompt rules | The system prompt is too vague. Make the numbered steps more specific. Add a "do NOT" line for behaviors you've seen go wrong. |
| Agent tries to edit files but isn't allowed | Add `Edit` (and `Write` for new files) to the `tools` list in frontmatter. |
| Agent needs to ask you questions mid-task | Subagents can't hold a back-and-forth. Run it as the whole session instead: `claude --agent my-agent`. |
| Agent runs forever | Add a max-iterations note in the system prompt: *"After at most 5 tool calls, summarize what you've done and stop."* |

If something else breaks, ask an instructor, that's exactly what they're
circulating for.
