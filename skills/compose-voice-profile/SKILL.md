---
name: compose-voice-profile
description: Compose a detailed, evidence-backed brand or author voice profile
  from user direction, research, guides, writing samples, visual references, and
  market context. Use when the user wants a reusable voice profile or
  tone-of-voice guide.
license: MIT
metadata:
  version: 1.1.0
  status: stable
  stack-version: 0.51.0
  distribution: release
---

# compose-voice-profile

Read and apply [the complete bundled workflow](references/_stack/skills/compose-voice-profile/instructions.md) before doing the task. Load its linked resources when instructed.

Resolve `AGENT_STACK_ROOT` to this package’s absolute `references/_stack` directory before running command examples (set it explicitly in the command environment). Source references beginning `src/skills/`, `src/guidelines/`, or `src/evals/` map to the corresponding directories under `AGENT_STACK_ROOT` with `src/` removed. This location supplies instructions and checker resources; it is not the caller’s project. Files authored for a target project belong in that project, never in the installed package. Use bundled dependency snapshots for internal handoffs, even if another version is installed separately. Read them in the current context when native invocation cannot guarantee the bundled version. Do not fetch required instructions online or treat private files as separately installed skills. Save configuration and runtime state outside this package.
