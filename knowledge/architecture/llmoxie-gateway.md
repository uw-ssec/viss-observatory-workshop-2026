---
type: Architecture
title: LLMoxie gateway as used by the workshop
description: "Participants reach models through SSEC's LLMoxie LiteLLM gateway: one key, many models, per-user budgets, auth by GitHub team; live demos should have a fallback."
tags: [llmoxie, litellm, gateway, models]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T17:39:37Z" }
status: stable
code_refs: [.devcontainer/devcontainer.json]
---

## Shape

- Layers: cloud inference (Azure AI Foundry, AWS Bedrock, open models), a
  LiteLLM proxy with MLflow tracing, harnesses (Copilot Chat via the
  OAI-compatible extension in Codespaces; JupyterAI and Claude Code on the
  hub), and context engineering (skills/plugins).
- One API key per participant works across models, with per-user daily
  budgets and an event-wide ceiling; keys are tied to a GitHub team or the hub
  login.
- Codespaces needed the model list written into the devcontainer settings
  (`oaicopilot.models`); VS Code does not discover gateway models on its own.
- The gateway has served about 60 concurrent workshop users with overflow
  capacity.

## Risks

- Failed requests were seen in a live demo in early October; have a fallback
  model or path for live demos.
- Model choice matters for skills: weaker default models in Copilot handled
  tool calls and skill triggering poorly in team tests. Name recommended
  models in participant instructions.

## Sources

Granola meetings 2026-09-20, 2026-09-21, 2026-10-06, 2026-10-14;
`.devcontainer/devcontainer.json`.

# Related Concepts
- [External projects this workshop depends on](../facts/connected-projects.md): LLMoxie is a connected SSEC project
