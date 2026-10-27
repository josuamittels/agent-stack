---
name: "release-agent-stack"
description: "Apply Agent Stack repository release rules to VERSIONS.md, the component inventory, lifecycle delivery gate, and capability discovery files. Invoke only when the Agent Stack identity markers match."
version: "0.1.0"
updated: "2026-10-26"
author:
  - "Josua Mittelstaedt"
references: []
type: "discipline"
status: "draft"
---

# Release Agent Stack

Apply Agent Stack-specific release metadata and delivery rules for the general [Ship](../../skills/ship/SKILL.md) skill. Return the exact edits and delivery route to Ship; do not perform Git commits, pushes, PR creation, merges, tags, or publication here.

## Scope

Use only when Ship has confirmed both the root `AGENTS.md` marker `agent-stack:entry` and the expected `VERSIONS.md`, `map.mmd`, `skills/`, and `guidelines/` structure.

### Boundaries

- Do not apply these rules to a different repository, even if it contains a file named `VERSIONS.md`.
- Do not change the stack lifecycle status or set a release date unless the user explicitly requested that transition or release and supplied enough evidence to record it accurately.
- Do not bump every component version because the stack version changes. Component frontmatter remains authoritative.
- Leave commits, push, PR creation, and other Git delivery actions to Ship.

## Inputs

Use the confirmed repository root and identity evidence, original ship request, exact task change set, working-tree and branch state, current `VERSIONS.md`, and any proposed version or lifecycle transition.

Read the [Git guide](../../guidelines/git/reference.md), [Versioning guide](../../guidelines/versioning/reference.md), current [`VERSIONS.md`](../../VERSIONS.md), `AGENTS.md`, `map.mmd`, and the affected capability instructions. Read [Update Map](../update-map/SKILL.md) and [Update Router](../update-router/SKILL.md) only when the affected capabilities require those updates.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Confirm identity and current release record

Recheck the root `AGENTS.md` marker and all expected structure before editing. If any check fails or is ambiguous, stop and tell Ship not to apply Agent Stack rules.

Read the current stack version, lifecycle status, `Recorded` date, release date, and component table. Validate the version and status against the Versioning guide. If the record is malformed or internally inconsistent, stop before editing and report the exact mismatch.

### 2. Classify and update the stack version

For a non-empty, authorized coordinated stack release, compare the proposed changes with the current stack contract and choose the largest required SemVer increment:

- At `0.y.z`, use patch for compatible corrections and minor for additions or breaking changes; identify breaking changes explicitly.
- At `1.0.0` or later, use patch for compatible corrections, minor for compatible additions or deprecations, and major for incompatible changes.

Do not bump for an empty change set. Do not treat commits or saves alone as releases. If the compatibility impact cannot be established from the changes and repository policy, return the unresolved decision to Ship before editing.

Update the stack version and `Recorded` date in `VERSIONS.md`. Keep the current lifecycle status. Leave `Release date` as `Not released` until an actual release date is authorized and known. Stable status requires version `1.0.0` or later; stop on an inconsistent stable version rather than silently changing status or version to hide it.

### 3. Refresh the component inventory

Read each independently versioned skill, discipline, and guideline under the corresponding top-level directories, including nested reference Markdown with valid substantive `version` and `status` frontmatter. Preserve each artifact’s own frontmatter as the source of truth. Refresh the table with its component kind, path, version, and status.

Exclude templates, source copies, evaluation schemas, files without substantive version metadata, and placeholders such as `[version]`. Do not infer a component version from a directory name or a stack bump. Compare every inventory row with its source frontmatter and confirm no eligible artifact is missing or duplicated.

### 4. Check capability discovery when needed

If this release adds, removes, moves, or changes a skill or discipline’s dependencies, compare the affected nodes and edges in `map.mmd` with the actual instructions. Invoke [Update Map](../update-map/SKILL.md) for any required map change. Then invoke [Update Router](../update-router/SKILL.md) when capability availability, scope, or routing examples changed. Pass the completed map update to Update Router.

For changes that do not affect capability discovery, do not edit the map or router. Preserve unrelated content and report any pre-existing discrepancies without silently expanding the release scope.

### 5. Return the delivery route to Ship

Return the current and proposed stack version, lifecycle status, changed paths, inventory reconciliation result, capability-map/router updates, unresolved decisions, and delivery route:

| Stack lifecycle status | Delivery route |
| --- | --- |
| `draft` or `experimental` | Local commits only. No push or PR/MR. |
| `stable` or `deprecated` | Push a topic branch and create or update a PR/MR. Ship stops before merge, tag, or publication. |

Treat any unknown or unsupported status as a blocker. Do not derive lifecycle status from the numeric version.

## Output

Return the identity check, current and proposed versions, status, exact `VERSIONS.md` changes, inventory comparison, applicable map/router results, required delivery route, and any blocker to Ship. Distinguish checks performed from checks Ship still needs to run.
