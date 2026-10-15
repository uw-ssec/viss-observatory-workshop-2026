---
type: Requirement
title: Disclose LLM data collection to participants
description: "Gateway traffic is logged under UW IRB via enterprise cloud accounts; participants must be told at login, and EU/GDPR applicability for Florence is still being checked."
tags: [irb, consent, gdpr, llmoxie]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T17:39:37Z" }
status: stable
---

## Requirements

- LLM traffic goes through the LLMoxie gateway on enterprise Bedrock/Azure
  accounts (no consumer accounts); interactions are logged anonymously under
  a UW IRB.
- Participants must be told: the hub login page states that logging in
  provisions an API key and that anonymized LLM interaction data is
  collected.
- GDPR applicability for the EU venue is an open question; UW can switch off
  trace collection if required.
- Participants should not send private or restricted data through the
  gateway.

## Sources

Granola meetings 2026-09-18, 2026-10-06, 2026-10-13, 2026-10-14.

# Related Concepts
- [LLMoxie gateway as used by the workshop](../architecture/llmoxie-gateway.md): data collected by the gateway
