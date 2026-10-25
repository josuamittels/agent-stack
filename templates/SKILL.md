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

If you miss relevant information, first invoke [think-harder](../disciplines/think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../disciplines/ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

Information how to follow the workflow, use of subagents, etc.

### 1. Establish [necessary fact].

Continue when [checkable condition].

### 2. Produce [artifact or change].

Follow [relevant constraints].

…

### N. Validate implementation

When invoked as a helper, return to the owning workflow without separate evaluation. Otherwise invoke [spawn-evals](../disciplines/spawn-evals/SKILL.md). Pass the original requirements, necessary input context, completed output, observable evidence, and one evaluation ID bound to the request. Use live mode once for this completed result; keep domain-specific criteria in `evals/<skill-name>/`. Do not evaluate callers or nested helpers, refresh suites, repair, or retry. Report good or not good and material gaps, then stop.

## Output
Required deliverable and essential fields.

## Boundaries
Task-specific approval points and stopping conditions.
