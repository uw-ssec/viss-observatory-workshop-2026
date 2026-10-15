---
type: Fact
title: "How the workshop material evolved, and why"
description: "Past content decisions: Copilot Chat as the only harness, rse-plugins submodule rejected, Block 3 rewritten as an in-repo skills loop, instructor notes removed."
tags: [history, block-3, copilot, skills]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T17:39:35Z" }
status: stable
---

## Decisions already made upstream (keep unless deliberately revisited)

- **One harness: Copilot Chat.** Claude Code, the Copilot CLI and agent
  plugins were removed from the devcontainer; all agentic work is exposed at
  repo level through `.github/` (uw-ssec ...-old issues #15/#17; commits
  7b01de2, b291151, 1a543cb, 64f75fd).
- **rse-plugins as a submodule was rejected.** schmidt-sciences ISS PR #2
  was merged then reverted by force-push on 2026-06-09; PR #3 (skills via npx)
  was closed. Resources now describe rse-plugins as a separate project.
- **Block 3 = in-repo skills research loop** (schmidt-sciences ISS PR #5):
  seven skills in `.github/skills/` (profile-dataset, plan-analysis,
  explore-data, statistical-tests, draft-report, validate-analysis, handoff)
  on a synthetic HCI text-entry dataset, with `demo/expected-artifacts/` as a
  fallback when live runs fail. It replaced an earlier prompt-file loop on a
  simple climate model.
- **Instructor notes removed** (PR #7); essentials live in slides, READMEs
  and `docs/` (common-audience-questions, pre-block-checklists). Do not
  reintroduce per-block instructor-notes files.
- **Models:** Opus dropped, Claude Sonnet 4.6 default plus Haiku 4.5
  (1d3a576). Use `LITELLM_BASE_URL` (not `LITELLM_API_BASE`).
- Block 1's notebook ships unexecuted on purpose; the Dockerfile sets no
  WORKDIR because the mount path differs per fork.

## Sources

Commit history and PRs across the repo family; see
[repo-lineage](repo-lineage.md).
