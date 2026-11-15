---
name: "changelog-standard"
description: "Standard for creating and maintaining clear, consistent project changelogs and release notes. Consult when adding, reviewing, or preparing changelog entries."
version: "0.1.0"
created: "2026-10-25"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Olivier Lacan"
  - "GitHub"
  - "Tom Preston-Werner"
type: "reference"
status: "experimental"
---

# Changelog Standard

Use this standard when a project needs a durable record of notable changes. A changelog helps users and maintainers understand what changed between versions and what they may need to do. It is a curated summary for people, not a copy of the commit history.

Follow an established project format when its release tooling, compatibility promises, or contributor instructions depend on it. Otherwise, use the defaults below. A project may use Semantic Versioning, calendar versioning, date-based releases, or another scheme; state the scheme near the top of the changelog and apply it consistently.

## Choose the record

Keep one canonical changelog in the repository. Name it `CHANGELOG.md` by default. Preserve an established name such as `HISTORY`, `NEWS`, or `RELEASES` when people and tooling already rely on it.

Keep a changelog distinct from release announcements:

- The changelog is the ongoing, complete record of notable changes across versions.
- Release notes are a release-specific announcement, selected from the changelog and expanded with context, upgrade steps, or audience-specific framing.

Use the changelog as the source for release notes. A platform's generated notes can help draft a release announcement, but review them and keep the repository changelog as the durable record.

For a monorepo, keep a central changelog when releases and user-facing changes are coordinated across the repository. Use package-level changelogs when packages have independent versions, release schedules, or audiences; add a central summary when users need to understand a combined release without reading every package log.

A long changelog can remain one file while it is easy to search and maintain. If you archive history, move only old releases that no longer need routine edits. Keep the current changelog and each archive linked to the other so readers can find the full history. Never discard releases that users may still need to reference.

## Structure and order

Start with `# Changelog`, a short preamble identifying the format and versioning scheme, then an `Unreleased` section. Keep releases newest first. Give every published version a release date in ISO `YYYY-MM-DD` format. Keep `Unreleased` undated. If the project has no discrete versions, record dated notable changes under `Unreleased`.

Use the six standard change types below in this order. Omit categories with no entries rather than leaving empty headings. Keep this order consistent across releases.

| Heading | Use for |
| --- | --- |
| `Added` | New user-visible features or capabilities. |
| `Changed` | Changes to existing behavior, defaults, supported environments, or workflows. |
| `Deprecated` | Supported behavior that will be removed or replaced. State the planned removal version or date and the recommended alternative. |
| `Removed` | Behavior or capability removed in this release. Identify what users lose and the replacement when one exists. |
| `Fixed` | Corrected behavior that previously did not work as intended. |
| `Security` | Changes that address vulnerabilities and need security-specific attention. |

Classify by what happened, not by the files touched or the implementation method. Use `Fixed` when correcting a defect; use `Changed` when intentionally changing behavior. A dependency update belongs under the category that describes its effect on users, and can be omitted when it has no meaningful user impact. A known issue is not a change; document it with the affected release or issue tracker, and add it to `Fixed` when resolved. Avoid adding catch-all headings such as `Other`, `Internal`, `Maintenance`, or `Performance`; state meaningful improvements under `Changed` and leave routine internal work out.

For tools that use another release scheme, retain the project's actual version labels and say what they mean. Use a short release summary before the categories only when it clarifies the main theme or a major adoption decision.

## Write useful entries

Write each entry for a reader deciding whether to upgrade or how to use the project. Start with the user-visible outcome, then add the affected area, condition, or reason when it helps. Prefer active, plain language and concrete nouns. Explain technical terms that the intended reader may not know. Link to a migration guide, advisory, documentation, issue, or pull request when the link helps the reader take action or verify detail.

A useful entry answers the relevant questions:

- What changed for users, operators, or developers?
- Which feature, command, API, configuration, or environment does it affect?
- What should someone do next, if action is needed?

Write one bullet per coherent, reader-noticeable change. Combine implementation steps that produce one outcome; separate changes when readers need to understand or act on them independently. Do not enumerate commits, files, implementation steps, or contributor activity.

| Weak entry | Better entry |
| --- | --- |
| `- Updated export code.` | `- CSV exports now preserve leading zeroes in account IDs.` |
| `- Fixed login.` | `- Fix sign-in failures when an account email contains a plus sign.` |
| `- Added caching.` | `- Dashboard summaries load faster on repeat visits because results are cached for 60 seconds.` |
| `- Refactored the parser.` | Omit if the refactor has no user-visible effect; otherwise describe the outcome, such as `- Invalid configuration now reports the field name and expected value.` |

Use consistent punctuation and Markdown. Use inline code for literal commands, APIs, options, paths, and configuration keys. Keep bullets concise; use a nested bullet only when a short sub-list is clearer than a sentence. Do not add links solely to decorate an entry.

## Communicate breaking changes and risk

Mark a breaking entry with `**Breaking:**` at the start of the bullet, under its normal category. Say what interface or behavior changes, who is affected, and the shortest useful upgrade action. Link to a migration guide when the steps are lengthy. Do not create a separate breaking-changes category that hides an entry from `Changed` or `Removed`.

```markdown
### Changed

- **Breaking:** `client.request()` now returns a response object instead of the response body. Read `response.body` to access the previous value; see the [migration guide](docs/migrate-v3.md).
```

When a project follows Semantic Versioning, align the release version with the compatibility impact: incompatible public API changes require a major increment; backward-compatible features use a minor increment; backward-compatible fixes use a patch increment. The changelog marker explains the user impact even when the version already signals a major release.

Announce deprecations before removing support. Say what will be removed, when it is expected to happen, and what to use instead. Keep the deprecation in its own release entry so users have a chance to adapt before a later `Removed` entry.

For a security fix, publish details in coordination with the project's security disclosure process. Include the affected product or versions, the practical impact, the fixed version, and a link to the published advisory where available. Put a CVE identifier first when one has been assigned. Do not publish exploit details or unannounced vulnerability information before the coordinated disclosure is ready; link to the advisory for sensitive technical detail.

If a release is withdrawn, keep its historical entry and mark the version `[YANKED]` with a short reason and a link to the replacement or fix. Do not erase a release that users may already have installed.

## Maintain and release the log

Add or revise a draft entry when the user-facing effect is clear. If details are uncertain, verify the behavior from the code, documentation, or change author before stating a claim. Avoid reconstructing a complete changelog from commit messages alone.

At release time:

1. Review changes since the prior release and confirm every notable user-facing change is represented once.
2. Rewrite draft entries for clarity, combine related implementation work, and remove routine changes that do not affect readers.
3. Check categories, breaking markers, deprecations, security disclosure timing, version, release date, and links.
4. Move the `Unreleased` entries into the new version section, add the release date, and create a fresh `Unreleased` section at the top.
5. Derive platform release notes from the published changelog section. Review generated summaries for omissions, duplicates, inaccurate claims, and irrelevant pull requests.

Keep old release entries available. Correct an omission or materially misleading statement when found; for a published correction, make the correction visible in version control and mention when useful that the historical entry was amended. Do not rewrite old entries to conceal a regression or make a release appear different from what shipped.

Automation may check Markdown structure, links, ordering, and date syntax or move sections during release preparation. It may draft entries from pull requests or commits, but a maintainer must curate the result for completeness, accuracy, usefulness, and disclosure timing. Do not require a changelog line for every code change; that encourages noise.

## Example

This example uses SemVer and reference links to compare tags. Replace the project name, URLs, version scheme, and entries with real project details. Pin the Keep a Changelog reference to the format revision the project follows.

```markdown
# Changelog

All notable changes to Acme CLI are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/2.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add `acme sync --dry-run` to preview changes without writing files.

## [2.1.0] - 2026-10-25

### Added

- Add JSON output to `acme report` for use in automated workflows.

### Fixed

- Preserve Unicode characters in exported CSV files.

## [2.0.0] - 2026-09-12

### Changed

- **Breaking:** Configuration files now use `output_dir` instead of `destination`. Rename the key before upgrading.

### Deprecated

- Mark `--legacy-config` for removal in 3.0.0. Convert the file with `acme config migrate`.

[Unreleased]: https://github.com/acme/cli/compare/v2.1.0...HEAD
[2.1.0]: https://github.com/acme/cli/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/acme/cli/releases/tag/v2.0.0
```

A comparison link for each release helps readers inspect its exact changes. Use the repository host's equivalent links, and preserve the project's tag naming convention.
