---
name: update-router
description: "Synchronize skill-issue's route catalog and the root AGENTS.md entry section with the actual skills, disciplines, and stack map. Use after a capability is added, changed, moved, or removed, or when discovery instructions are stale."
version: "0.1.1"
updated: "2026-10-25"
author:
  - "Josua Mittelstaedt"
references:
  - "Garry Tan"
  - "OpenAI"
type: "discipline"
status: "draft"
---

# Update Router

## Scope

Maintain the root guide and [skill-issue catalog](../../skills/skill-issue/SKILL.md) within the calling workflow.

### Boundaries

Maintain discovery only; do not repair capabilities or the map, install integrations, invoke the router or create-skill, or run background watchers. Final evaluation and lifecycle decisions remain with the caller.

If required discovery inputs or the router are missing or unreadable, markers are invalid, or generated content conflicts with manual instructions, stop before writing and report the dependency or conflict. Preserve unrelated and concurrent edits; reread changed inputs before applying. Never guess section boundaries or overwrite a conflicting manual rule.

## Inputs

Use the repository root, changed paths and types, authorized scope, and available map-update evidence. Resolve stack paths from the root and Markdown links from their containing file. Routine maintenance needs no preference interview.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Establish what exists

Read the current map, root [AGENTS instructions](../../AGENTS.md) when present, complete skill-issue instructions, [AGENTS template](templates/AGENTS.md), and all `skills/*/SKILL.md` files. Read supporting files only for scope, exclusions, or invocation policies affecting selection.

Actual instructions establish availability; the map supplies grouping and relationships. Include substantive drafts, even when unmapped. Exclude empty folders, map-only entries, metadata-only files, and scaffolds. Discover candidates only from `skills/*/SKILL.md`, classifying them by their `type` metadata; research copies and other repository resources are not routes. Report map discrepancies to the caller.

### 2. Maintain the catalog

Prepare only the body inside skill-issue's `agent-stack:route-catalog` markers, including availability notes and neighboring-intent examples. Preserve everything outside them, including metadata, selection rules, and handoffs.

Group skills by task where useful, followed by discipline fallbacks. Derive each entry's outcome, natural examples or synonyms, relative link, and nearest overlap or exclusion from its instructions. Skills remain primary entry points; direct discipline use follows its scope. Honor explicit-only policies. Omit skill-issue itself; allow update-router for maintenance. No route targets a guideline or restarts routing recursively.

Update changed entries; remove stale links and examples. Preserve useful examples and existing ordering; sort new peers by slug. Avoid timestamps and equivalent rewrites. For an empty group, give a brief availability statement instead of an empty table or invented route. Summarize planned availability without cataloging every empty folder.

### 3. Maintain the root entry section

Prepare only the body inside AGENTS' `agent-stack:entry` markers. Keep it compact: repository purpose, map link, when to consult skill-issue, and a folder guide reflecting actual contents, including reserved or empty directories. Explain that mapped resources may be planned, research copies are excluded, and files do not install native host integrations. Keep capability examples in skill-issue; exclude personal and host configuration.

For missing AGENTS, adapt the template with repository details and supplied project instructions. Preserve existing content outside the markers byte for byte. If neither marker exists, append the section without replacing manual routing prose.

### 4. Apply and return

Prepare both nonempty bodies before writing. Use [the section helper](scripts/sections.mjs), passing JSON on stdin with string fields `entry` and `catalog`, without marker lines:

```sh
node skills/update-router/scripts/sections.mjs /absolute/path/to/stack < /absolute/path/to/temporary-bodies.json
```

It requires Node.js and an existing skill-issue file, validates both candidates before writing, preserves surrounding content, rejects malformed markers, and skips unchanged writes. For missing AGENTS it creates a title and entry; retain project instructions outside that section. Without Node.js, apply the same marker validation and preservation rules using file tools. Keep temporary inputs outside the repository and remove them afterward.

## Output

Return changed or unchanged paths, added/changed/removed routes, map discrepancies, and remaining gaps. Report partial writes and which files need recovery; the helper writes files separately, not transactionally. Unchanged inputs should produce no changes.
