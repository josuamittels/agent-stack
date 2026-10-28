---
name: "update-changelog"
description: "Create, update, or prepare a repository changelog from verified changes. Use when the user asks to record changes, maintain CHANGELOG.md, or prepare a changelog release section."
version: "0.3.0"
created: "2026-10-25"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Olivier Lacan"
  - "GitHub"
type: "discipline"
status: "experimental"
---

# Update Changelog

Create or update a project's changelog so readers can understand notable changes and their effect. Use this discipline when the user asks to create, update, repair, or prepare a changelog section. Ship invokes this discipline for every requested ship operation so it can assess the verified change set; record only notable user-facing changes and omit routine internal work.

## Scope

Use this method for a repository changelog or its established package-level changelogs. It covers the durable change record and its release section. It does not own commit messages, pull request descriptions, or release announcements. When the user asks only for announcement copy, use the existing changelog as source material and do not edit it unless asked.

The changelog guideline defines entry content and format. This discipline defines how to inspect the project, decide what to edit, preserve work, and verify the result.

### Boundaries

Do not commit, tag, publish, or create a hosted release unless the user separately asks and repository instructions permit that action. Do not change code, documentation, or translated changelogs to make an entry true. Do not backfill broad history, invent content, edit unrelated release sections, or expose undisclosed security details.

## Inputs

Use the repository root and user-requested change scope. A requested commit range, version, release date, package, or section is optional; infer it from the task and repository when the evidence is clear. Treat the user's explicit scope and project release instructions as controlling.

Read [the changelog standard](../../guidelines/changelog/reference.md) before editing. It provides the default file structure, entry categories, writing rules, release curation, and examples. Read [versioning guidelines](../../guidelines/versioning/reference.md) when selecting or recording a release version or when compatibility impact affects that choice. Read [Git guidelines](../../guidelines/git/reference.md) when repository state or partial staging affects how you inspect changes or preserve work.

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/SKILL.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/SKILL.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Establish the file and change scope

Read repository instructions that govern the changelog, releases, packages, or documentation. Inspect the existing changelog and find the repository's canonical path. Preserve an established name and format. For a monorepo, inspect root and package changelogs when package release instructions indicate separate ownership.

Inspect the working-tree status before interpreting diffs. Preserve staged, unstaged, and untracked work. Use the user's stated range when provided. Otherwise identify changes that belong to the requested task, using the relevant diff, history, pull requests, or source documents as evidence. Do not treat all changes in the checkout as in scope just because they are present.

If the project has no changelog and the user asks to create or update one, create the canonical file at the documented project location. Otherwise default to `CHANGELOG.md` in the repository root. Do not reconstruct a long release history unless the user asks for backfill and the repository provides enough evidence.

Continue when the target file, intended change range, and applicable project conventions are clear. If independent package changelogs or release sources conflict, preserve supported work and report the unresolved scope before making a guess.

### 2. Verify change facts

Read the changes themselves and any directly relevant documentation, tests, issue or pull request context, or release metadata. Use commit messages and generated release notes to find evidence, then verify the behavior from the diff or authoritative project sources.

For each possible entry, identify the user-visible effect, affected interface or workflow, and any action readers need to take. Keep only notable changes. Combine implementation steps that produce one reader-visible outcome, and split changes that require different reader actions. Omit internal work with no meaningful reader effect.

Do not invent behavior, compatibility, version numbers, release dates, package ownership, or security status. If a claim cannot be verified, omit it or report it as an evidence gap. If the remaining verified changes still support a useful update, make that update and state what could not be confirmed.

### 3. Choose the section

Add ordinary in-progress changes under the project's `Unreleased` section. Do not create a dated version section unless the user requests a release or repository instructions clearly establish that this task prepares one.

For a requested release, use the supplied version and actual release date. If either is missing, inspect the project's version source, tags, release configuration, and versioning policy. Consult the versioning guide where needed. Ask about a missing value only when repository evidence cannot resolve it and the release section depends on it; otherwise finish the verified unreleased update and identify the missing release detail.

Update a published historical entry only for an explicit correction or a clearly requested historical update. Preserve its release identity and make the correction reviewable in the diff. Do not change unrelated historical sections.

### 4. Edit the smallest appropriate section

Add or revise the relevant entries under the correct categories in the existing format. If creating a new file, use the changelog standard's header and `Unreleased` structure, then add verified release history only within the requested scope.

Place each notable change once. Preserve correct existing entries and reference links. Update link references only when a version heading or comparison relationship changes. Keep package-specific prefixes, translations, generated docs, or release scripts only when repository instructions require them and they are within scope.

For a security fix, follow the repository's disclosure process. Include only information approved for public disclosure, and link to a published advisory when available. Do not expose unannounced vulnerability details.

### 5. Verify the saved change

Review the changelog diff and confirm each new or changed statement maps to evidence gathered in step 2. Check that:

- The entry describes a user-relevant outcome rather than a commit or implementation task.
- Each change appears once and under a suitable category.
- Breaking changes, deprecations, removals, migration actions, and security details are handled as the changelog standard requires.
- Section placement, release order, version, date, Markdown links, and local formatting match the project.
- No unrelated or staged user changes were overwritten or included by accident.

Run a repository changelog-specific check if the project provides one and it applies to the edited file. Do not run the full test suite solely because a changelog changed. Report checks that were unavailable or could not confirm a claim.

## Output

Report the changelog path, whether it was created or updated, the notable changes recorded and their sections, the evidence or range used, and any unresolved facts or checks. State when the requested change produced no notable entries, and explain the evidence for that choice.
