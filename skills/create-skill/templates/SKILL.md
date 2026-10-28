---
name: "[name-slug]" # Replace with a lowercase, hyphenated skill name.
description: "[description]" # Compact capability description and activation conditions.
version: "[version]" # X.Y.Z
created: "[today]" # YYYY-MM-DD
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

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/SKILL.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/SKILL.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

Information how to follow the workflow, use of subagents, etc.

### 1. Establish [necessary fact].

Continue when [checkable condition].

### 2. Produce [artifact or change].

Follow [relevant constraints].

…

### N. Validate implementation

When invoked as a helper, return to the owning workflow without separate evaluation. For a skill with meaningful, deterministic, task-specific checks, invoke [Spawn Evals](../spawn-evals/SKILL.md) once with a structured invocation record containing the original request, resolved constraints and their source, complete UTF-8 outputs, and machine-readable evidence. Its objective package in `evals/<skill-name>/` defines only those checks. Report PASS, FAIL, or NOT PASSED — UNVERIFIED with the failing or unavailable verification steps. Do not use model judges, sub-agents, qualitative assessments, weighted scores, or synthetic scenarios. If no package exists for an objectively checkable skill, report NOT PASSED — UNVERIFIED; do not create one during an ordinary skill invocation. If no meaningful objective check is possible for this skill, omit this entire validation section and all Spawn Evals references from the skill.

## Output
Required deliverable and essential fields.
