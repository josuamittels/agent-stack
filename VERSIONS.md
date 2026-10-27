# Agent Stack Versions

This file records the coordinated version of the Agent Stack and snapshots the versions of its independently maintained capabilities and references.

## Current stack version

| Field | Value |
| --- | --- |
| Version | `0.9.0` |
| Status | `draft` |
| Recorded | `2026-10-27` |
| Release date | Not released |

The stack version describes the compatibility of the skills, disciplines, and guidelines adopted together. It does not replace their individual versions or imply that draft components are approved or stable. `0.9.0` adds comprehensive accessibility guidance covering functional needs, EU legal scoping, design and implementation, assistive technology, design systems, evaluation, and ongoing operations; the stack has not been released.

## Component versions

Component versions and statuses below are snapshots of each artifact's frontmatter. The artifact frontmatter remains authoritative. Templates and files without a substantive version are excluded.

| Component | Path | Version | Status |
| --- | --- | --- | --- |
| Skill | `skills/compose-voice-profile/SKILL.md` | `0.1.0` | `draft` |
| Skill | `skills/create-guidelines/SKILL.md` | `0.3.0` | `draft` |
| Skill | `skills/create-skill/SKILL.md` | `0.9.0` | `experimental` |
| Skill | `skills/natural-writing/SKILL.md` | `0.4.1` | `draft` |
| Skill | `skills/research/SKILL.md` | `0.7.0` | `draft` |
| Skill | `skills/ship/SKILL.md` | `0.3.0` | `draft` |
| Skill | `skills/skill-issue/SKILL.md` | `0.2.0` | `draft` |
| Skill | `skills/translate/SKILL.md` | `0.4.1` | `draft` |
| Discipline | `disciplines/ask-user-question/SKILL.md` | `0.1.0` | `draft` |
| Discipline | `disciplines/browse-skills/SKILL.md` | `1.0.0` | `draft` |
| Discipline | `disciplines/mind-wandering/SKILL.md` | `0.1.1` | `draft` |
| Discipline | `disciplines/pre-mortem/SKILL.md` | `0.1.0` | `draft` |
| Discipline | `disciplines/quit-the-yap/SKILL.md` | `0.1.0` | `draft` |
| Discipline | `disciplines/release-agent-stack/SKILL.md` | `0.1.0` | `draft` |
| Discipline | `disciplines/research-literature/SKILL.md` | `0.5.0` | `draft` |
| Reference | `disciplines/research-literature/references/journal-selection.md` | `0.2.0` | `draft` |
| Reference | `disciplines/research-literature/references/openalex-docs.md` | `0.2.0` | `draft` |
| Discipline | `disciplines/spawn-evals/SKILL.md` | `0.9.0` | `draft` |
| Discipline | `disciplines/think-deeper/SKILL.md` | `0.1.0` | `draft` |
| Discipline | `disciplines/think-harder/SKILL.md` | `0.1.0` | `draft` |
| Discipline | `disciplines/update-changelog/SKILL.md` | `0.2.0` | `draft` |
| Discipline | `disciplines/update-map/SKILL.md` | `0.1.1` | `draft` |
| Discipline | `disciplines/update-router/SKILL.md` | `0.1.1` | `draft` |
| Guideline | `guidelines/aesthetics/accessibility.md` | `0.1.0` | `draft` |
| Guideline | `guidelines/aesthetics/iconography.md` | `0.1.0` | `draft` |
| Guideline | `guidelines/aesthetics/typography.md` | `0.1.0` | `draft` |
| Guideline | `guidelines/changelog/reference.md` | `0.1.0` | `draft` |
| Guideline | `guidelines/coding/mermaid.md` | `0.2.0` | `draft` |
| Guideline | `guidelines/coding/python.md` | `0.1.0` | `draft` |
| Guideline | `guidelines/coding/sql.md` | `0.1.0` | `draft` |
| Guideline | `guidelines/coding/typescript.md` | `0.1.0` | `draft` |
| Guideline | `guidelines/git/reference.md` | `0.1.0` | `draft` |
| Guideline | `guidelines/languages/dutch.md` | `0.1.0` | `draft` |
| Guideline | `guidelines/languages/english.md` | `0.1.0` | `draft` |
| Guideline | `guidelines/languages/french.md` | `0.1.0` | `draft` |
| Guideline | `guidelines/languages/german.md` | `0.1.0` | `draft` |
| Guideline | `guidelines/versioning/reference.md` | `0.1.0` | `draft` |

## Versioning and maintenance

The stack follows the repository's [versioning policy](guidelines/versioning/reference.md) and uses `MAJOR.MINOR.PATCH`. While the stack is at `0.y.z`, use patch increments for compatible corrections and minor increments for additions or breaking changes. The highest compatibility impact in a coordinated release determines the stack increment.

Component versions remain independently maintained according to their own contracts. Do not bump every component just because the stack version changes. Before a coordinated release, review the changes, confirm component versions have been updated where needed, refresh this inventory from frontmatter, and verify the stack version against the release tag if one is created. Use an ISO `YYYY-MM-DD` date for a release; keep the date as `Not released` until the stack is actually released. Record detailed change history in a changelog if one is introduced.
