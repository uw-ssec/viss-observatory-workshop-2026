# Block 4: Build Your Own Skill (Capstone)

## Learning goals

By the end of this block, an attendee can:

1. Read a Claude Code subagent file and identify which line corresponds to which **anatomy concept** from Block 1 (LLM backbone, tool use, project memory, system prompt).
2. **Write** a subagent end-to-end: pick a job, write a focused system prompt, choose a narrow tool list, save it to `.claude/agents/`, and invoke it from Claude Code.
3. **Iterate** on an agent that almost works: tighten the prompt, add explicit constraints, narrow or broaden the tool list.
4. Map the same agent pattern to **other primitives** (slash commands for one-shots, like `eda-summary` or `scaffold-package`; skills for multi-step capabilities, like the Block 3 research loop; MCP servers if they want to add new tools).

## What's in this folder

```
04-build-a-skill/
  README.md            # this file
  slides.md            # Marp slides
  resources.md         # Claude Code subagent, command, skill, rule, and MCP docs
  exercise/
    README.md                            # participant-facing step-by-step
    my-agent.md.template                 # SKELETON to copy + fill in (the main task)
    my-command.md.template               # SKELETON for a slash command (stretch B)
    my-skill.SKILL.md.template           # SKELETON for a skill (stretch A)
    my-rule.md.template                  # SKELETON for path-scoped rules (stretch C)
    ideas.md                             # 30+ starter agent ideas
```

### Run the exercise

Participants follow [`exercise/README.md`](exercise/README.md). Instructors
circulate. The exercise's troubleshooting table covers the common
"my agent doesn't appear" / "agent runs but does the wrong thing" issues.
