---
name: "[name-slug]" # Replace with a lowercase, hyphenated skill name.
description: "[description]" # Compact capability description and activation conditions.
version: "[version]" # X.Y.Z
updated: "[today]" # YYYY-MM-DD
author:
  - "[author name]" # Example: Josua Mittelstaedt
references: # One author name per item, ordered by relevance.
  - "[author name]" # Example: Lauren Tan
type: "skill"
status: "draft" # draft, experimental, stable, or deprecated
---

# [name, format: Skill Name]

...

## Scope

Use for/when...
For [adjacent task], use [other skill].

## Inputs

Require...

Refer to `guidelines/...` to...

### Default Procedures

If you miss relevant information, first invoke `disciplines/think-harder`, passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use `disciplines/ask-user-question` to inquire the missing information.

Stack paths in backticks are relative to the repository root, identified by `templates/SKILL.md` and `map.mmd`. Use the host's invocation mechanism when available; otherwise read and apply the destination's instructions in context. Reading a file does not establish a separate agent invocation.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

Information how to follow the workflow, use of subagents, etc.

### 1. Establish [necessary fact].

Continue when [checkable condition].

### 2. Produce [artifact or change].

Follow [relevant constraints].

…

### N. Validate implementation

Invoke [spawn-evals](../disciplines/spawn-evals/SKILL.md). Pass the original requirements, necessary input context, completed output, observable evidence, and an invocation ID. Use its verdict as final validation; keep domain-specific checks in `evals/<skill-name>/`. Report the score, acceptability, and material gaps alongside the requested output.

## Output
Required deliverable and essential fields.

## Boundaries
Task-specific approval points and stopping conditions.
