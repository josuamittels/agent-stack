---
name: "release-agent-stack"
description: "Apply Agent Stack repository release rules to VERSIONS.md, the component inventory, lifecycle delivery gate, and capability discovery files. Invoke only when the Agent Stack identity markers match."
version: "0.8.0"
created: "2026-10-26"
updated: "2026-11-13"
author:
  - "Josua Mittelstaedt"
references: []
type: "discipline"
status: "experimental"
---

# Release Agent Stack

Apply Agent Stack-specific release metadata and delivery rules for the general [Ship](../ship/instructions.md) skill. Return the exact edits, delivery route, and applicable post-push installation procedure to Ship; do not perform Git commits, pushes, PR creation, merges, tags, or publication here.

## Scope

Use only when Ship has confirmed both the root `AGENTS.md` marker `agent-stack:entry` and the expected `VERSIONS.md`, `map.mmd`, `src/skills/`, and `src/guidelines/` structure.

### Boundaries

- Do not apply these rules to a different repository, even if it contains a file named `VERSIONS.md`.
- Do not change the stack lifecycle status or set a release date unless the user explicitly requested that transition or release and supplied enough evidence to record it accurately.
- Do not bump every component version because the stack version changes. Component frontmatter remains authoritative.
- Leave commits, push, PR creation, and other Git delivery actions to Ship.

## Inputs

Use the confirmed repository root and identity evidence, original ship request, exact task change set, working-tree and branch state, current `VERSIONS.md`, and any proposed version or lifecycle transition. Read [Create Docs](../create-docs/instructions.md) for the required documentation handoff on every release.

Read the [Git guide](../../guidelines/git/reference.md), [Versioning guide](../../guidelines/versioning/reference.md), current `VERSIONS.md` in the target repository, `AGENTS.md`, `map.mmd`, and the affected capability instructions. Read [Update Map](../update-map/instructions.md) and [Update Router](../update-router/instructions.md) only when the affected capabilities require those updates.

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/instructions.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/instructions.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Confirm identity and current release record

Recheck the root `AGENTS.md` marker and all expected structure before editing. If any check fails or is ambiguous, stop and tell Ship not to apply Agent Stack rules.

Read the current stack version, lifecycle status, `Recorded` date, release date, and component table. Validate the version and status against the Versioning guide. If the record is malformed or internally inconsistent, stop before editing and report the exact mismatch.

### 2. Classify and update the stack version per commit

Treat each planned non-empty Ship commit as its own stack revision. Classify each commit's change group against the stack contract and calculate its increment from the version produced by the preceding commit in the plan. Choose the largest required SemVer increment for that commit:

- At `0.y.z`, use patch for compatible corrections and minor for additions or breaking changes; identify breaking changes explicitly.
- At `1.0.0` or later, use patch for compatible corrections, minor for compatible additions or deprecations, and major for incompatible changes.

Do not bump for an empty change set. This per-commit rule is an Agent Stack release requirement: every planned non-empty commit must include its own stack version increment, rather than sharing one bump across multiple implementation commits. Commits and saves alone do not create a release revision; each increment records the substantive change group committed with it. If the compatibility impact cannot be established from a commit group's changes and repository policy, return the unresolved decision to Ship before editing.

For each planned commit, update the stack version and `Recorded` date in `VERSIONS.md` to the state that commit will record. Include those edits with that commit's substantive changes; do not create one final aggregate version-only commit. Keep the current lifecycle status. Leave `Release date` as `Not released` until an actual release date is authorized and known. Stable status requires version `1.0.0` or later; stop on an inconsistent stable version rather than silently changing status or version to hide it.

### 3. Refresh the component inventory for each commit

For every planned commit, determine the component inventory state after that commit's changes and refresh the `VERSIONS.md` table in that same commit. Read each independently versioned skill, discipline, router, guideline, and reference under the canonical `src/` directories, including nested reference Markdown with valid substantive `version` and `status` frontmatter. Preserve each artifact’s own frontmatter as the source of truth. Refresh the table with its component kind, path, version, and status.

Exclude generated root `skills/`, `dist/`, templates, research source copies, evaluation schemas, files without substantive version metadata, and placeholders such as `[version]`. Do not infer a component version from a directory name or a stack bump. Compare every inventory row with its source frontmatter and confirm no eligible artifact is missing or duplicated.

Before preparing a push, review the exact delivery change set for new or changed independently versioned components. Include experimental and stable components without changing their lifecycle labels. Retain deprecated components only for compatibility and preserve their deprecation information. Exclude draft components from shipped packages and from the requested delivery change set; do not promote a draft merely to make a package pass. A draft required or conditional dependency, including versioned guidance, blocks its consumer until the dependency is explicitly promoted or removed from that consumer's contract. Source-only authoring scaffolds and owned templates are not independently shipped capabilities. Keep unrelated changes out of the delivery.

### 4. Check capability discovery when needed

If this release adds, removes, moves, or changes a skill or discipline’s dependencies, compare the affected nodes and edges in `map.mmd` with the actual instructions. Invoke [Update Map](../update-map/instructions.md) for any required map change. Then invoke [Update Router](../update-router/instructions.md) when capability availability, scope, or routing examples changed. Pass the completed map update to Update Router.

For changes that do not affect capability discovery, do not edit the map or router. Preserve unrelated content and report any pre-existing discrepancies without silently expanding the release scope.

### 5. Update user documentation for every release

Invoke [Create Docs](../create-docs/instructions.md) on every release, after the final release change set, version and inventory state, and any map or router updates are established, but before returning the candidate to Ship. Pass the exact release changes, affected components and workflows, authoritative source files, final component versions and statuses, removals or moves, and the current documentation site. Reuse the repository's existing docs mode and structure.

Update pages, navigation, links, or cards to match changes people will experience when using Agent Stack. Run Create Docs even when the release appears internal-only; let its source review establish whether the user-facing documentation needs a change. Keep release, contribution, and maintenance procedures out of end-user docs unless they are part of the product users operate. Return the documentation paths and Create Docs verification results to Ship. Include those edits in the matching release change group; if they require a separate planned commit, apply the per-commit version and inventory rules to it too. Do not defer the documentation pass until after the release is delivered.

### 6. Build the skill packages

After the matching commit candidate's source, release metadata, discovery, and documentation updates are settled, run these commands from the confirmed repository root, in order:

```sh
npm run build
npm run build:preview
```

Run the full preview build without `--skill`, so it includes every public candidate. The shipping build refreshes committed `skills/` and installation documentation with eligible experimental and stable components; the preview build creates self-contained skill folders, individual and full-stack ZIPs, native plugin packages, marketplace catalogs, and `SHA256SUMS` under `dist/preview/distribution/`. Preview output stays local and ignored by Git. Local previews may include drafts and are not the shipping catalog. An empty shipping catalog does not prevent preview packaging.

When stack status is `experimental`, `stable`, or `deprecated`, also run the command below. A stable stack still requires version `1.0.0` or later; an experimental stack may ship at `0.y.z`.

```sh
npm run package
```

This creates the eligible shipping distribution under `dist/release/`. Preserve its non-draft dependency, freshness, and nonempty-catalog gates. A draft stack receives local preview artifacts only. Package generation preserves stack and component lifecycle labels; an experimental release does not imply a stable contract.

Verify every checksum entry in each distribution produced by this step against the actual archive bytes. Record the exact commands, results, candidate version, preview and release output paths, and archive counts. Stop and return the failure to Ship if any required build, package, or checksum verification fails or is unavailable. Repeat this step if subsequent candidate changes affect generated output. Never upload, tag, publish, or create a Git commit as part of package generation.

### 7. Return the delivery route to Ship

Return the current version and the sequential proposed version after each planned commit, lifecycle status, changed paths grouped by commit, inventory reconciliation for each commit, capability-map/router updates, documentation changes and Create Docs verification results, package-build commands and outcomes, output paths and checksum verification, any authorized post-push Codex refresh from step 8, unresolved decisions, and delivery route:

Apply the component-status gate in step 3 before any push. Draft components remain excluded; promotion requires an explicit lifecycle decision.

| Stack lifecycle status | Delivery route |
| --- | --- |
| `draft` | Local commits only. No push or PR/MR. |
| `experimental`, `stable`, or `deprecated` | Push a topic branch and create or update a PR/MR. Ship stops before merge, tag, or publication. |

Treat any unknown or unsupported status as a blocker. Do not derive lifecycle status from the numeric version.

### 8. Define the authorized post-push Codex refresh

When the user or repository instructions authorize global Codex installation and updates, return this procedure to Ship as a required completion step after a successful push. Reuse standing authorization for the same repository and host. A release request alone does not authorize host installation in other projects. Skip this step for local-only delivery or a failed push.

Use the successfully pushed commit and its generated `skills/catalog.json` as the installation source and eligible name list. Include newly shipped experimental and stable skills and refresh the rest of that shipping catalog, retaining deprecated packages only as allowed by its compatibility policy. Exclude drafts, blocked consumers, source templates, and preview packages. Resolve the verified Git repository source to that exact pushed revision rather than a moving branch or the dirty checkout.

Inventory the global Codex installation with `npx --yes skills list -g -a codex --json`. Refresh with the skills CLI's `add` command, using the verified repository source at the pushed revision, `-g`, `-a codex`, `-y`, and `--skill` followed by the eligible names. When source discovery matches the shipping catalog exactly, `--skill '*'` is equivalent. Use the documented source syntax supported by the available CLI. Avoid `--all`, which selects other agents too. A blanket `skills update` does not discover newly added skills and its agent selection may extend beyond Codex. This source-scoped reinstall updates existing packages and installs new ones together.

Verify the command result, rerun the global Codex inventory, and compare each installed package's complete file set and bytes with its generated package at the pushed commit. Inspect the actual destination reported by the CLI rather than assuming a host directory. Preserve unrelated and manually installed skills, system skills, and other hosts. Report a conflicting installation or shadowing duplicate instead of deleting it automatically.

Return the source revision, commands and results, installed or refreshed names, actual destinations, and any failure to Ship. Installation becomes available to Codex on the next turn. If refreshing fails after a successful push, preserve the delivered commit and retry the installation within scope. Report delivery and installation separately until both required steps succeed.

## Output

Return the identity check, current and proposed versions, status, exact `VERSIONS.md` changes, inventory comparison, applicable map/router results, required delivery route, and any blocker to Ship. Distinguish checks performed from checks Ship still needs to run. Return the completed package-build evidence with the final per-commit candidate to Ship. Ship reviews generated output and executes the final required checks before committing, then completes any authorized Codex refresh after pushing; report package generation separately from those pending checks.

## Distribution readiness

The build catalog is `src/catalog.yaml`. Public packages include experimental and stable skills with non-draft required/conditional dependency closures, including versioned guidance; deprecated components remain available for compatibility. Drafts are excluded. `npm run package` requires a non-draft stack and a nonempty shipping catalog; stable stacks additionally require version 1.0 or later. Every Agent Stack ship operation builds full local preview packages under `dist/preview/`; non-draft operations additionally build `dist/release/`. Neither operation publishes the packages or promotes lifecycle status. Publication, tags, and marketplace submission remain separately authorized actions. Generated copies are not independent version inventory entries.
