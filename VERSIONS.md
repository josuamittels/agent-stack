# Agent Stack Versions

This file records the coordinated version of the Agent Stack and snapshots the versions of its independently maintained capabilities and references.

## Current stack version

| Field | Value |
| --- | --- |
| Version | `0.24.0` |
| Status | `draft` |
| Recorded | `2026-10-28` |
| Release date | Not released |

The stack version describes the compatibility of the skills, disciplines, and guidelines adopted together. It does not replace their individual versions or imply that draft components are approved or stable. `0.24.0` adds experimental repository documentation generation through Create Docs, with basic Markdown and interactive Nextra modes, bundled setup resources, objective navigation checks, and updated discovery. The stack has not been released.

## Component versions

Component versions and statuses below are snapshots of each artifact's frontmatter. The artifact frontmatter remains authoritative. Templates and files without a substantive version are excluded.

| Component | Path | Version | Status |
| --- | --- | --- | --- |
| Reference | `guidelines/aesthetics/reference.md` | `0.1.0` | `experimental` |
| Guideline | `guidelines/aesthetics/accessibility.md` | `0.2.0` | `experimental` |
| Guideline | `guidelines/aesthetics/colour.md` | `0.2.0` | `experimental` |
| Guideline | `guidelines/aesthetics/composition.md` | `0.2.0` | `experimental` |
| Guideline | `guidelines/aesthetics/haptics.md` | `0.2.0` | `experimental` |
| Guideline | `guidelines/aesthetics/iconography.md` | `0.2.0` | `experimental` |
| Guideline | `guidelines/aesthetics/interaction.md` | `0.2.0` | `experimental` |
| Guideline | `guidelines/aesthetics/motion.md` | `0.2.0` | `experimental` |
| Guideline | `guidelines/aesthetics/sound.md` | `0.2.0` | `experimental` |
| Guideline | `guidelines/aesthetics/typography.md` | `0.2.0` | `experimental` |
| Guideline | `guidelines/changelog/reference.md` | `0.1.0` | `experimental` |
| Reference | `guidelines/docs/reference.md` | `0.1.0` | `experimental` |
| Guideline | `guidelines/coding/mermaid.md` | `0.2.0` | `experimental` |
| Guideline | `guidelines/coding/python.md` | `0.1.0` | `experimental` |
| Guideline | `guidelines/coding/sql.md` | `0.1.0` | `experimental` |
| Guideline | `guidelines/coding/typescript.md` | `0.1.0` | `experimental` |
| Guideline | `guidelines/git/reference.md` | `0.1.0` | `experimental` |
| Guideline | `guidelines/languages/dutch.md` | `0.1.0` | `experimental` |
| Guideline | `guidelines/languages/english.md` | `0.1.0` | `experimental` |
| Guideline | `guidelines/languages/french.md` | `0.1.0` | `experimental` |
| Guideline | `guidelines/languages/german.md` | `0.1.0` | `experimental` |
| Guideline | `guidelines/versioning/reference.md` | `0.1.0` | `experimental` |
| Guideline | `guidelines/wireframes/reference.md` | `0.1.0` | `experimental` |
| Discipline | `skills/ask-user-question/SKILL.md` | `0.2.0` | `experimental` |
| Discipline | `skills/browse-skills/SKILL.md` | `1.1.0` | `experimental` |
| Discipline | `skills/check-colour-contrast/SKILL.md` | `1.1.0` | `stable` |
| Skill | `skills/compose-voice-profile/SKILL.md` | `0.2.0` | `experimental` |
| Discipline | `skills/convert-colour/SKILL.md` | `1.1.0` | `stable` |
| Skill | `skills/create-docs/SKILL.md` | `0.1.0` | `experimental` |
| Reference | `skills/create-docs/references/nextra-docs.md` | `0.1.0` | `experimental` |
| Skill | `skills/create-guidelines/SKILL.md` | `0.5.0` | `experimental` |
| Skill | `skills/create-skill/SKILL.md` | `0.13.0` | `experimental` |
| Discipline | `skills/mind-wandering/SKILL.md` | `0.2.0` | `experimental` |
| Discipline | `skills/natural-writing/SKILL.md` | `0.6.0` | `experimental` |
| Discipline | `skills/pre-mortem/SKILL.md` | `0.2.0` | `experimental` |
| Discipline | `skills/quit-the-yap/SKILL.md` | `0.3.0` | `experimental` |
| Discipline | `skills/release-agent-stack/SKILL.md` | `0.4.0` | `experimental` |
| Discipline | `skills/research-literature/SKILL.md` | `0.6.0` | `experimental` |
| Reference | `skills/research-literature/references/journal-selection.md` | `0.2.0` | `experimental` |
| Reference | `skills/research-literature/references/openalex-docs.md` | `0.2.0` | `experimental` |
| Skill | `skills/research/SKILL.md` | `0.8.0` | `experimental` |
| Skill | `skills/ship/SKILL.md` | `0.6.0` | `experimental` |
| Discipline | `skills/show-me-your-work/SKILL.md` | `0.2.0` | `experimental` |
| Router | `skills/skill-issue/SKILL.md` | `0.6.0` | `experimental` |
| Discipline | `skills/spawn-evals/SKILL.md` | `0.9.0` | `experimental` |
| Discipline | `skills/think-deeper/SKILL.md` | `0.2.0` | `experimental` |
| Discipline | `skills/think-harder/SKILL.md` | `0.2.0` | `experimental` |
| Skill | `skills/translate/SKILL.md` | `0.5.0` | `experimental` |
| Discipline | `skills/update-changelog/SKILL.md` | `0.3.0` | `experimental` |
| Discipline | `skills/update-map/SKILL.md` | `0.3.0` | `experimental` |
| Discipline | `skills/update-router/SKILL.md` | `0.2.0` | `experimental` |

## Versioning and maintenance

The stack follows the repository's [versioning policy](guidelines/versioning/reference.md) and uses `MAJOR.MINOR.PATCH`. While the stack is at `0.y.z`, use patch increments for compatible corrections and minor increments for additions or breaking changes. The highest compatibility impact in a coordinated release determines the stack increment.

Component versions remain independently maintained according to their own contracts. Do not bump every component just because the stack version changes. Before a coordinated release, review the changes, confirm component versions have been updated where needed, refresh this inventory from frontmatter, and verify the stack version against the release tag if one is created. Use an ISO `YYYY-MM-DD` date for a release; keep the date as `Not released` until the stack is actually released. Record detailed change history in a changelog if one is introduced.
