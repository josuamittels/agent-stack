---
name: update-map
description: "Maintain the agent stack resource map after skills, disciplines, guidelines, templates, or their explicit dependencies change. Use when adding, moving, renaming, removing, or reconnecting stack resources."
version: "0.1.1"
updated: "2026-10-25"
author:
  - "Josua Mittelstaedt"
references: []
type: "discipline"
status: "draft"
---

# Update Map

## Scope

Keep the [stack map](../../map.mmd) aligned with changed stack resources and their operational relationships. Apply this method within the calling workflow.

### Boundaries

Change only the authorized resources and relationships in the map. Preserve unrelated work; do not add dependencies or evaluation requirements merely to make the diagram consistent. The caller retains final evaluation, lifecycle decisions, and discovery maintenance.

## Inputs

Use the changed paths and resource types, relevant instructions and callers, added or obsolete relationships, and authorized scope. Resolve Markdown links from their containing file.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Inspect the change

Read the [Mermaid guidelines](../../guidelines/coding/mermaid.md) for notation, styling, layout, and verification. Inspect the existing map and changed resources' actual instructions, including affected callers.

Use the map's legend, placement, labels, shapes, and shared classes for its established conventions and deviations from the guidelines. Preserve grouping, configuration, identifiers, and unrelated edits unless restructuring is authorized. For a new map, use the guidelines' defaults.

### 2. Update affected resources and connections

Add, move, rename, or remove the affected resources. Reuse existing identifiers; place new content in the matching section, creating a section only when none fits. Apply the existing conventions for that resource type, including router connections to skill sections. Keep planned resources distinguishable from implemented capabilities; visibility alone establishes no dependency.

Derive each execution connection from instructions requiring the caller to invoke a capability or load a reference. Draw direct dependencies through their owning caller; add an additional direct connection only when independently required. Exclude topical similarity, research records, source URLs, evaluation evidence, repair coordination, and router catalog mentions.

Preserve the map's distinction between membership, invocation, guideline consultation, and validation, using its legend and shared edge classes. Keep default shared disciplines such as Think Harder and Ask User Question visible without incoming, outgoing, or membership connections.

Include validation links only for skills whose actual instructions call the evaluator, including conditional or approval-gated calls. Templates and catalog entries alone do not establish a validation handoff. Omit evaluator self-loops and repair-only connections. Reuse validation edge identifiers and styling; ensure general edge styling does not override them. Recompute style indices if the map uses numeric edge references.

Remove obsolete nodes, connections, and class references within scope. Update affected membership and routing when moving or removing resources; avoid duplicate nodes and connections.

### 3. Verify and return

Compare affected nodes and connections with the source instructions and requested changes. Check placement, direct dependencies, special connection conventions, and cleanup; confirm default shared disciplines remain unconnected.

Follow the guidelines' validation procedure on the complete saved map, including configuration and styles. Parse it, render with a compatible viewer and layout engine when available, and inspect the result, including validation styling and arrowheads. Keep temporary previews and dependencies outside the repository. Report unavailable rendering or other verification gaps without claiming unperformed checks.

## Output

Return the map path, changed resources and relationships, checks actually performed, and remaining gaps to the caller.
