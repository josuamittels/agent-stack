---
name: update-map
description: "Maintain the agent stack map as skills, disciplines, guidelines, templates, and their documented relationships change. Use for an explicit map update or during an authorized Agent Stack release."
version: "0.3.0"
created: "2026-10-27"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references: []
type: "discipline"
status: "experimental"
---

# Update Map

Keep the [stack map](../../map.mmd) aligned with real resources and the instructions that connect them. Treat the user's explicit map preferences and the current map's established conventions as controlling; use the [Mermaid guidelines](../../guidelines/coding/mermaid.md) for syntax and general practice where they do not conflict.

## Scope

Update map nodes, groups, styles, and relationships within the requested scope. An explicit request to edit the map authorizes that edit. During an Agent Stack release, [Release Agent Stack](../release-agent-stack/SKILL.md) coordinates map maintenance before router maintenance.

### Boundaries

Do not infer an operational dependency from topical similarity, a folder, a map node, or a catalog entry. Do not create, move, or rewrite source resources unless the caller authorized that work. Do not update the routing catalog as a side effect of an ordinary map edit; return the completed map to Release Agent Stack when it owns the release sequence. Preserve unrelated working-tree changes.

## Inputs

Use the requested map change, repository root, current map, affected resources and their instructions, relevant caller handoffs, and the current file state. Resolve Markdown links from their containing file.

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/SKILL.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/SKILL.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Inspect the map and source resources

Read the Mermaid reference and inspect the complete map, including its frontmatter, comments, node declarations, edges, classes, subgraph styles, and current changes. Read the affected skills, disciplines, and guidelines to establish their actual type and handoffs.

Check the filesystem before coloring a resource as implemented. A folder alone does not establish a capability. A process node without a substantive `SKILL.md`, or a document node whose file is missing, folder is empty, or body is only a placeholder, remains white. A usable document can be blue while its lifecycle status is `draft`; status alone does not mean that it is unfinished. Treat scaffold tokens such as `[name]`, `[conventions]`, and `...` as unfinished content.

### 2. Preserve the map's groups and title style

Keep skills inside the outer `SKILLS` subgraph and the existing domain subgraphs. Keep disciplines in the `DISCIPLINES` subgraph. Keep references and guidelines inside the outer `GUIDELINES` subgraph and their matching category subgraphs. Keep decision nodes outside these resource groups where they are now.

Use uppercase subgraph titles without bold formatting. Give nested subgraphs white backgrounds so their contents remain distinct. Use the existing rounded section class. Keep node labels concise, in title case, and free of directory paths.

### 3. Apply the established node shapes and colors

Use the current shared classes and the map's established meanings:

| Resource | Shape syntax and color |
| --- | --- |
| Agent entry | Stadium `(["Agent"])`, green `#DFF7A5`. |
| Implemented skill | Process rectangle `["Skill"]`, green `#DFF7A5`, only when a substantive `SKILL.md` exists. |
| Implemented discipline | Process rectangle `["Method"]`, yellow `#FFE99A`; use the hexagon `{{Method}}` for a conditional discipline. |
| Planned or unfinished process | Keep the intended process or conditional shape, but use white `#FFFFFF` until its `SKILL.md` is substantive. |
| Decision | Diamond `{"Question?"}`, lavender `#C9CEF4`. |
| Existing single document | `@{ shape: doc }`, active blue `#B3E5FC`. |
| Existing collection of documents | `@{ shape: docs }`, active blue `#B3E5FC`. Use this for a grouped set of guideline files, such as Aesthetics. |
| Existing template | `@{ shape: tag-doc }`, active blue `#B3E5FC`. |
| Existing internal storage | `@{ shape: win-pane }`, active blue `#B3E5FC`. |
| Missing, empty, or unfinished document resource | Keep its intended document shape, but use white `#FFFFFF` until the document content is complete. |

Use navy `#002B3D` for text, outlines, and connections. Keep existing shape identities when recoloring a resource. Do not color a planned skill or unfinished document as active merely because it has a directory or placeholder file. Preserve the legend comments and shared class assignments when these meanings change.

### 4. Derive connections from explicit handoffs

Use `-->` for a required invocation or ordered transition. Use `-.-` for dotted reference lines without arrowheads to guidelines, templates, and other resources where the map shows a consultation or association. Use `---` for grouping or membership lines. Keep reference lines distinct from invocation arrows. Use navy lines; do not add red arrows.

Use one arrow from a skill subgraph when every skill in that subgraph has the same documented handoff. Do not repeat that arrow from each skill node. If only some skills use the resource, connect those nodes individually. For example, route the WRITING subgraph to Natural Writing when its member skills all use that method. Do not add direct links from individual writing skills to Natural Writing as well.

Connect a workflow to the skill or discipline that directly performs the handoff. If that helper owns its references, show the chain through the helper instead of adding direct links from every caller to those references. Natural Writing owns its language-guideline references. Skills that use Natural Writing connect to it; Natural Writing connects to the applicable language documents.

Keep templates and guideline references dotted and without arrowheads. Preserve the established connections from design skills, Image Tools, and Video Tools to Aesthetics; connect a grouped reference to its individual files with plain lines. Keep Documentation dotted to Create Docs. Do not connect Ship directly to the Changelog document: Ship invokes Update Changelog for release notes.

Keep Spawn Evals behind the `Has Objective Criteria?` decision. Eligible skill groups lead to that decision, which leads to Spawn Evals; Create Skill leads to the decision for package preparation. Do not connect skill nodes directly to Spawn Evals. Preserve the current unlabeled chain from `SKILLS` through `Missing Information?`, Think Harder, and Ask User Question; do not add Yes/No or “Still Missing” labels.

During an authorized Agent Stack release, preserve the sequence Ship → Release Agent Stack → Update Map → Update Router. Do not make Create Skill or Create Guidelines direct triggers for map or router maintenance. Outside that release sequence, Update Map does not invoke Update Router unless the user explicitly requests it.

### 5. Keep routes short and readable

Preserve the current Mermaid ELK configuration, `LINEAR_SEGMENTS` placement strategy, and linear edge curves unless the user asks to change them. Keep arrows as direct as the renderer permits, with as few bends and crossings as practical. Prefer a valid group-level connection over duplicated member arrows. Do not add hidden ordering edges or reverse real dependencies to force a layout. Keep edge labels off unless the user asks for them or they are required to explain an exceptional relationship.

### 6. Clean up affected map entries

Reuse stable identifiers. When moving or removing a resource, update its node declaration, group, edges, class, and section style together. Avoid duplicate nodes and edges. Remove unused class definitions when no nodes use them. Keep inactive nodes white rather than removing a planned resource that the user wants visible.

### 7. Verify and return

Compare the changed nodes, groups, styles, and edges with the source instructions and the requested conventions. Check that existing resources use active colors, missing or unfinished resources remain white, each resource is in the right subgraph, and no duplicate or obsolete links remain.

Parse and render the complete saved map with a compatible Mermaid viewer and layout engine when available. Inspect node shapes, active and white fills, subgraph backgrounds, arrowheads, and the longest routes. Keep temporary previews and dependencies outside the repository. If parsing or rendering is unavailable, report that limitation and state which static checks you completed.

## Output

Return the map path, changed nodes and relationships, checks actually performed, and any remaining verification gap. When Release Agent Stack owns the release, return the finished map update to it; do not claim router maintenance unless that step was performed.
