---
name: ship
description: Ship a reviewed change by following the target repository's
  release, changelog, test, and Git workflow. Use when asked to ship, release,
  push, or create or update a pull request.
license: MIT
metadata:
  version: 0.9.0
  status: experimental
  stack-version: 0.50.0
  distribution: release
---

# ship

Read and apply [the complete bundled workflow](references/_stack/skills/ship/instructions.md) before doing the task. Load its linked resources when instructed.

Resolve `AGENT_STACK_ROOT` to this package’s absolute `references/_stack` directory before running command examples (set it explicitly in the command environment). Source references beginning `src/skills/`, `src/guidelines/`, or `src/evals/` map to the corresponding directories under `AGENT_STACK_ROOT` with `src/` removed. This location supplies instructions and checker resources; it is not the caller’s project. Files authored for a target project belong in that project, never in the installed package. Use bundled dependency snapshots for internal handoffs, even if another version is installed separately. Read them in the current context when native invocation cannot guarantee the bundled version. Do not fetch required instructions online or treat private files as separately installed skills. Save configuration and runtime state outside this package.
