# Workshop Content Conventions

**Load when:** writing or editing workshop material: slides, notebooks, block
READMEs, starter code, or the `.claude/` gallery.

The material is for **"Coding with AI Agents: A Hands-On Workshop for
Scientists"**. Optimize for **clarity, reproducibility, and teaching value**.
Participants run it on the event JupyterHub, with Claude Code in a terminal.

## Conventions

- **Python 3.12.** Use the standard library where reasonable.
- **Package manager: `uv`.** Run things as `uv run <cmd>`; add dependencies with
  `uv add <pkg>`. Do not write `pip install` instructions in workshop material
  unless explaining why we _aren't_ using it.
- **Code style: `ruff`** (configured in `pyproject.toml`).
- **Notebooks:** every code cell is preceded by a markdown cell that explains
  _why_ the code exists. A notebook reads top to bottom as a teaching document,
  not a script with comments.
- **Slides:** Marp-flavored markdown, previewed and presented with the **Marp
  for VS Code** extension (theme in `blocks/_shared/slides.css`).
- **No emojis** in workshop material unless an instructor explicitly asks for
  one.
- **`workshop_agent/`** is the agent loop from Block 1's notebook, packaged so
  Blocks 2-4 can import it. The notebook stays the teaching source of truth;
  keep the two in sync if you change either.

## When writing workshop content

- Be opinionated. The workshop's stance is that **all coding agents work the
  same way under the hood**; reinforce that thread.
- Prefer durable, transferable concepts to product-specific trivia. Other tools
  (Copilot, Cursor, OpenCode) may appear as comparisons; the hands-on path is
  Claude Code.
- Show, don't tell. Reach for an example or a tiny runnable snippet before
  prose.
- Keep examples self-contained inside `blocks/0N-*/demo/`.

## The gallery (Block 4)

`.claude/agents/`, `.claude/commands/` and `.claude/rules/` hold the worked
subagents, slash commands and path-scoped rules, indexed in the root
`README.md`. The workshop skills live in `.github/skills/` and are linked into
`.claude/skills/` (via `.agents/skills/`). When asked what a gallery file does,
read it directly.

## Things to avoid

- Don't add dependencies without a reason: on the hub every workshop dependency
  must also go into the shared hub image.
- Don't restructure the `blocks/` layout; the four-block structure is
  load-bearing.
- Don't introduce a JavaScript build step. Slides need no CLI invocation.
