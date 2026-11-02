# Agent Stack Versions

This file records the coordinated version of the Agent Stack and snapshots the versions of its independently maintained capabilities and references.

## Current stack version

| Field | Value |
| --- | --- |
| Version | `0.37.0` |
| Status | `experimental` |
| Recorded | `2026-11-02` |
| Release date | Not released |

The stack version describes the compatibility of the skills, disciplines, and guidelines adopted together. It does not replace their individual versions or imply that draft components are approved or stable. `0.32.0` separates canonical `src/` authoring from generated self-contained distributions, introduces stable-only dependency gates, and moves runtime state outside installed packages. It also requires Ship to rebuild Agent Stack after release preparation and check the generated candidate before each commit. This is a breaking source-path migration; public packages remain unavailable until their lifecycle gates pass. `0.33.0` requires Release Agent Stack to build full local preview packages for every ship operation and eligible stable release packages before handoff. `0.34.0` promotes Translate, Write, Compose Voice Profile, Think Deeper, Think Harder, Ask User Question, Research, Research Literature, and the Dutch, English, French, and German language guides to stable 1.0.0 contracts. `0.35.0` promotes Spawn Evals and the versioned Research and Research Literature dependency references to stable 1.0.0 so the three research workflows have stable dependency closures. `0.36.0` reframes the root README for entrepreneurs, documents the current candidate catalog, and explains local preview installation and stack structure. `0.37.0` renames the Write discipline identifier from `natural-writing` to `write`, a breaking change for direct selections, dependency declarations, and references. The stack has not been released.

## Component versions

Component versions and statuses below are snapshots of each artifact's frontmatter. The artifact frontmatter remains authoritative. Templates and files without a substantive version are excluded.

| Component | Path | Version | Status |
| --- | --- | --- | --- |
| Reference | `src/guidelines/aesthetics/accessibility.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/colour.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/composition.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/haptics.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/iconography.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/interaction.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/motion.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/reference.md` | `0.1.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/sound.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/typography.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/changelog/reference.md` | `0.1.0` | `experimental` |
| Reference | `src/guidelines/coding/mermaid.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/coding/python.md` | `0.1.0` | `experimental` |
| Reference | `src/guidelines/coding/sql.md` | `0.1.0` | `experimental` |
| Reference | `src/guidelines/coding/typescript.md` | `0.1.0` | `experimental` |
| Reference | `src/guidelines/docs/reference.md` | `0.1.0` | `experimental` |
| Reference | `src/guidelines/git/reference.md` | `0.1.0` | `experimental` |
| Reference | `src/guidelines/languages/dutch.md` | `1.0.0` | `stable` |
| Reference | `src/guidelines/languages/english.md` | `1.0.0` | `stable` |
| Reference | `src/guidelines/languages/french.md` | `1.0.0` | `stable` |
| Reference | `src/guidelines/languages/german.md` | `1.0.0` | `stable` |
| Reference | `src/guidelines/versioning/reference.md` | `0.1.0` | `experimental` |
| Reference | `src/guidelines/wireframes/reference.md` | `0.1.0` | `experimental` |
| Discipline | `src/skills/ask-user-question/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Discipline | `src/skills/browse-skills/SKILL.md.tmpl` | `1.1.0` | `experimental` |
| Discipline | `src/skills/check-colour-contrast/SKILL.md.tmpl` | `1.1.0` | `stable` |
| Skill | `src/skills/compose-voice-profile/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Discipline | `src/skills/convert-colour/SKILL.md.tmpl` | `1.1.0` | `stable` |
| Reference | `src/skills/create-docs/references/nextra-docs.md` | `0.2.0` | `experimental` |
| Skill | `src/skills/create-docs/SKILL.md.tmpl` | `0.5.0` | `experimental` |
| Skill | `src/skills/create-guidelines/SKILL.md.tmpl` | `0.6.0` | `experimental` |
| Skill | `src/skills/create-skill/SKILL.md.tmpl` | `0.14.0` | `experimental` |
| Discipline | `src/skills/mind-wandering/SKILL.md.tmpl` | `0.2.0` | `experimental` |
| Discipline | `src/skills/write/SKILL.md.tmpl` | `2.0.0` | `stable` |
| Discipline | `src/skills/pre-mortem/SKILL.md.tmpl` | `0.2.0` | `experimental` |
| Discipline | `src/skills/quit-the-yap/SKILL.md.tmpl` | `0.3.0` | `experimental` |
| Discipline | `src/skills/release-agent-stack/SKILL.md.tmpl` | `0.6.0` | `experimental` |
| Reference | `src/skills/research-literature/references/arxiv-docs.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research-literature/references/crossref-docs.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research-literature/references/databases.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research-literature/references/google-scholar-search.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research-literature/references/journal-selection.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research-literature/references/openalex-docs.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research-literature/references/pubmed-docs.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research-literature/references/qualification-gate.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research-literature/references/secondary-discovery.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research-literature/references/semantic-scholar-docs.md` | `1.0.0` | `stable` |
| Discipline | `src/skills/research-literature/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Reference | `src/skills/research/references/artifacts.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research/references/cli.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research/references/csl/README.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research/references/export.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research/references/workflow.md` | `1.0.0` | `stable` |
| Skill | `src/skills/research/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Skill | `src/skills/ship/SKILL.md.tmpl` | `0.7.0` | `experimental` |
| Discipline | `src/skills/show-me-your-work/SKILL.md.tmpl` | `0.2.0` | `experimental` |
| Router | `src/skills/skill-issue/SKILL.md.tmpl` | `0.6.2` | `experimental` |
| Discipline | `src/skills/spawn-evals/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Discipline | `src/skills/think-deeper/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Discipline | `src/skills/think-harder/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Skill | `src/skills/translate/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Discipline | `src/skills/update-changelog/SKILL.md.tmpl` | `0.3.0` | `experimental` |
| Discipline | `src/skills/update-map/SKILL.md.tmpl` | `0.3.0` | `experimental` |
| Discipline | `src/skills/update-router/SKILL.md.tmpl` | `0.2.0` | `experimental` |

## Versioning and maintenance

The stack follows the repository's [versioning policy](src/guidelines/versioning/reference.md) and uses `MAJOR.MINOR.PATCH`. While the stack is at `0.y.z`, use patch increments for compatible corrections and minor increments for additions or breaking changes. The highest compatibility impact in a coordinated release determines the stack increment.

Component versions remain independently maintained according to their own contracts. Do not bump every component just because the stack version changes. Before a coordinated release, review the changes, confirm component versions have been updated where needed, refresh this inventory from frontmatter, and verify the stack version against the release tag if one is created. Use an ISO `YYYY-MM-DD` date for a release; keep the date as `Not released` until the stack is actually released. Record detailed change history in a changelog if one is introduced.
