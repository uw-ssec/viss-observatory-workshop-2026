---
type: Fact
title: Repository lineage and past deliveries
description: "This repo forks schmidt-sciences TSOS, which forks the schmidt-sciences ISS workshop repo; PR and issue numbers in commit subjects refer to those other repos."
tags: [history, forks, github]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T17:39:36Z" }
status: stable
---

## Fork chain

uw-ssec/viss-observatory-workshop-2026 (created 2026-10-15) forks
schmidt-sciences/viss-agentic-ai-workshop-tsos-2026 (2026-10-08, no new
commits), which forks schmidt-sciences/viss-agentic-ai-workshop-iss-2026 (root
of the GitHub fork network). The true original was
uw-ssec/viss-agentic-ai-workshop-iss-2026-old (2026-04-20, now archived).
Work flowed from the uw-ssec working fork to schmidt-sciences via PRs, which
is why the log shows "Merge pull request #N from uw-ssec/main".

## Past deliveries

- Interdisciplinary Science Summit (ISS), Raleigh/Durham, June 2026,
  Codespaces + Copilot Chat + LLMoxie gateway.
- UW-hosted workshop on June 17 2026 (uw-ssec-workshops/coding-with-agents-workshop).
- Event-specific wording was stripped on 2026-06-16 so one codebase serves
  every event.

## Gotchas

- PR numbers in commit subjects belong to other repos: #14 is the archived
  `-old` repo; #1/#5/#6/#7 are schmidt-sciences ISS; #4 and #5 in some
  subjects are uw-ssec fork issues. PR #1 in this repo adopted
  uw-ssec/project-template.
- Nothing upstream is newer than this repo's base (a9ee5d9).

## Sources

`gh repo view` fork metadata, repo activity API, git log of all repos in the
family.

# Related Concepts
- [How the workshop material evolved, and why](content-evolution.md): history of the repos where these content decisions were made
