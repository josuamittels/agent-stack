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

### Boundaries

Task-specific approval points and stopping conditions.

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

When invoked as a helper, return to the owning workflow without separate evaluation. For a skill with meaningful, deterministic, task-specific checks, invoke [Spawn Evals](../disciplines/spawn-evals/SKILL.md) once with a structured invocation record containing the original request, resolved constraints and their source, complete UTF-8 outputs, and machine-readable evidence. Its objective package in `evals/<skill-name>/` defines only those checks. Report PASS, FAIL, or NOT PASSED — UNVERIFIED with the failing or unavailable verification steps. Do not use model judges, sub-agents, qualitative assessments, weighted scores, or synthetic scenarios. If no package exists for an objectively checkable skill, report NOT PASSED — UNVERIFIED; do not create one during an ordinary skill invocation. If no meaningful objective check is possible for this skill, omit this entire validation section and all Spawn Evals references from the skill.

## Output
Required deliverable and essential fields.
