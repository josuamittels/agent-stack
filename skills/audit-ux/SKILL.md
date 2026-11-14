---
name: audit-ux
description: Audit how well a supplied design, interface, or information
  artifact serves its users' jobs, needs, expectations, and tasks. Clarify
  unresolved customer context, include an accessibility sub-audit, and fill a
  modular UX report with evidence, prioritized improvements, and validation
  actions.
license: MIT
metadata:
  version: 0.1.1
  status: experimental
  stack-version: 0.52.0
  distribution: release
---

# audit-ux

Read and apply [the complete bundled workflow](references/_stack/skills/audit-ux/instructions.md) before doing the task. Load its linked resources when instructed.

Resolve `AGENT_STACK_ROOT` to this package’s absolute `references/_stack` directory before running command examples (set it explicitly in the command environment). Source references beginning `src/skills/`, `src/guidelines/`, or `src/evals/` map to the corresponding directories under `AGENT_STACK_ROOT` with `src/` removed. This location supplies instructions and checker resources; it is not the caller’s project. Files authored for a target project belong in that project, never in the installed package. Use bundled dependency snapshots for internal handoffs, even if another version is installed separately. Read them in the current context when native invocation cannot guarantee the bundled version. Do not fetch required instructions online or treat private files as separately installed skills. Save configuration and runtime state outside this package.
