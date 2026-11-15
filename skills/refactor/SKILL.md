---
name: refactor
description: Audit and refactor codebases and interacting component libraries.
  Plan architecture, component consolidation, variants, conventions, and legacy
  removal; implement in themed commits on refactor branches when requested.
license: MIT
metadata:
  version: 0.1.1
  status: experimental
  stack-version: 0.54.0
  distribution: release
---

# refactor

Read and apply [the complete bundled workflow](references/_stack/skills/refactor/instructions.md) before doing the task. Load its linked resources when instructed.

Resolve `AGENT_STACK_ROOT` to this package’s absolute `references/_stack` directory before running command examples (set it explicitly in the command environment). Source references beginning `src/skills/`, `src/guidelines/`, or `src/evals/` map to the corresponding directories under `AGENT_STACK_ROOT` with `src/` removed. This location supplies instructions and checker resources; it is not the caller’s project. Files authored for a target project belong in that project, never in the installed package. Use bundled dependency snapshots for internal handoffs, even if another version is installed separately. Read them in the current context when native invocation cannot guarantee the bundled version. Do not fetch required instructions online or treat private files as separately installed skills. Save configuration and runtime state outside this package.
