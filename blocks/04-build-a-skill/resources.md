# Block 4: Further Reading

Curated. The first three are the docs you'll actually need; everything
else is "going further."

## The primitives we used

- **Claude Code: [Subagents](https://code.claude.com/docs/en/sub-agents)**: the official docs for the file format we just used (`.claude/agents/*.md`): frontmatter fields, tool names, and how to invoke one. Bookmark this.
- **Claude Code: [Skills](https://code.claude.com/docs/en/skills)**: a folder (`.claude/skills/<name>/SKILL.md`) that bundles instructions, and optionally scripts and resources, for a multi-step capability, loaded on demand. The same page covers slash commands (`.claude/commands/*.md`), the simpler one-shot primitive, and `$ARGUMENTS`. See the Block 3 research-loop skills in `.claude/skills/` and the worked commands in `.claude/commands/`.
- **Claude Code: [Memory](https://code.claude.com/docs/en/memory)**: `CLAUDE.md` / `AGENTS.md` for project-wide conventions, and `.claude/rules/*.md` with a `paths` glob for path-scoped rules. See `.claude/rules/` for worked examples.

## Going further with Claude Code

- **Claude Code: [MCP](https://code.claude.com/docs/en/mcp)**: the next step up if you want to give Claude brand-new tools (read from your database, query an internal API, etc.). Higher ceiling, more setup.
- **Anthropic: [Model Context Protocol](https://modelcontextprotocol.io/)**: the underlying open standard. Worth understanding if you want your tools to work in Claude Code AND Copilot AND Cursor.

## The same idea in other tools

- **GitHub Copilot: [Custom agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents), [prompt files](https://code.visualstudio.com/docs/copilot/customization/prompt-files), [agent skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills), and [custom instructions](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses)**: the same four primitives in VS Code. This repo keeps Copilot versions of every gallery file in `.github/agents/`, `.github/prompts/`, `.github/skills/`, and `.github/instructions/`; diff them against `.claude/` to see how little changes between tools.
- **Cursor: [Custom rules and modes](https://docs.cursor.com/)**: for participants who use Cursor day-to-day.
- **Aider: [Conventions and prompts](https://aider.chat/docs/usage/conventions.html)**: the OSS alternative; same patterns, smaller surface area.

## Related reading: agent workflows and design patterns

- **[`rse-plugins`](https://github.com/uw-ssec/rse-plugins)**: a separate, unrelated UW SSEC project that packages similar research-engineering skills as Claude Code plugins.
- **[Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)**: the most-quoted paper on agent design patterns. Read once a year.
- **[Cognition: Don't build multi-agents](https://cognition.ai/blog/dont-build-multi-agents)**: the counter-cultural pushback. Worth reading before you build something baroque.

## Office hours and follow-up

- This workshop's repository is yours to keep. Fork it; bring your subagents home.
- Office hours next day: come with the code or data you actually want to use this on.
- Mailing list for ongoing community: ask the workshop organizers, exact link to be confirmed.

---

If you find a great resource that should be here, open a PR.
