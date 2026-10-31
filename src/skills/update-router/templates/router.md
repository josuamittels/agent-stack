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
type: "router"
status: "draft" # draft, experimental, stable, or deprecated
---

# [name, format: Skill Name]

Select the smallest sufficient skill or workflow
for the user's requested outcome.

## Routing rules
- Prefer a skill the user explicitly requested.
- Use task intent and current state, not keyword matches alone.
- Keep independent requests separate.
- Ask only when ambiguity materially changes the route.
- Handle straightforward requests directly when no skill adds value.

## Route catalog
| Situation | Route | Reason |
|---|---|---|
| [situation] | [skill] | [reason] |

## Ambiguous cases
Explain how to distinguish neighboring routes.

## Handoff
State whether to invoke the selected skill or recommend it. Pass the relevant request, artifacts, constraints, and current state.

## Missing capability
If the selected skill is unavailable, report the limitation and choose a supported fallback without expanding scope.
