# Agent Stack Versions

This file records the coordinated version of the Agent Stack and snapshots the versions of its independently maintained capabilities and references.

## Current stack version

| Field | Value |
| --- | --- |
| Version | `0.51.0` |
| Status | `experimental` |
| Recorded | `2026-11-13` |
| Release date | Not released |

The stack version describes the compatibility of the skills, disciplines, and guidelines adopted together. It does not replace their individual versions or imply that draft components are approved or stable. `0.32.0` separates canonical `src/` authoring from generated self-contained distributions, introduces stable-only dependency gates, and moves runtime state outside installed packages. It also requires Ship to rebuild Agent Stack after release preparation and check the generated candidate before each commit. This is a breaking source-path migration; public packages remain unavailable until their lifecycle gates pass. `0.33.0` requires Release Agent Stack to build full local preview packages for every ship operation and eligible stable release packages before handoff. `0.34.0` promotes Translate, Write, Compose Voice Profile, Think Deeper, Think Harder, Ask User Question, Research, Research Literature, and the Dutch, English, French, and German language guides to stable 1.0.0 contracts. `0.35.0` promotes Spawn Evals and the versioned Research and Research Literature reference dependencies to stable 1.0.0 so the three research workflows have stable dependency closures. `0.36.0` reframes the README for entrepreneurs, documents the current candidate catalog, and explains local preview installation and stack structure. `0.37.0` renames the Write discipline identifier from `natural-writing` to `write`, a breaking change for direct selections, dependency declarations, and references. `0.38.0` adds the stable Compose Career Profile skill and reusable template. `0.39.0` changes Ship to require explicit user authorization before it creates a Git branch. `0.39.1` makes preview catalog validation derive its package count from eligible entries. `0.40.0` adds stable Draft Cover Letter and its stable voice-profile reference. `0.41.0` adds stable Create CV with an EB Garamond PDF generator. `0.42.0` adds the stable Setup Career Stack workflow and updates career application routing and personalized letter-voice guidance. `0.43.0` adds stable Answer Interview and its voice profile, routes career application questions through it, and archives supplied job descriptions in career application folders. `0.44.0` gives career workflows one shared voice profile, self-contained workspace operations and review helpers, and keeps draft and QA artifacts outside final application folders. `0.48.0` adds experimental Audit Accessibility, Audit UX, and Audit Design with nested reports and coordinated remediation. The stack has not been released. 0.44.1 shortens the README into consistent capability quick starts and documents GitHub installation for Codex and Claude Code. 0.45.0 adds stable Setup Agent Stack for global host routing and promotes its required Skill Issue router to stable 1.0.0.

Shipping includes experimental and stable components with non-draft required and conditional dependencies, including guidance. Drafts are excluded. Experimental stacks may produce release packages at `0.y.z`; stable stacks require `1.0.0` or later. Inclusion preserves each component’s lifecycle status.

## Component versions

Component versions and statuses below are snapshots of each artifact's frontmatter. The artifact frontmatter remains authoritative. Templates and files without a substantive version are excluded.

| Component | Path | Version | Status |
| --- | --- | --- | --- |
| Reference | `src/guidelines/aesthetics/accessibility.md` | `0.3.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/colour.md` | `0.3.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/composition.md` | `0.3.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/haptics.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/iconography.md` | `0.3.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/infographics.md` | `0.1.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/interaction.md` | `0.3.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/motion.md` | `0.3.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/reference.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/sound.md` | `0.2.0` | `experimental` |
| Reference | `src/guidelines/aesthetics/typography.md` | `0.3.0` | `experimental` |
| Reference | `src/guidelines/changelog/reference.md` | `0.1.0` | `experimental` |
| Reference | `src/guidelines/coding/mermaid.md` | `0.3.0` | `experimental` |
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
| Skill | `src/skills/answer-interview/SKILL.md.tmpl` | `2.0.1` | `stable` |
| Discipline | `src/skills/ask-user-question/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Skill | `src/skills/audit-accessibility/SKILL.md.tmpl` | `0.1.1` | `experimental` |
| Skill | `src/skills/audit-design/SKILL.md.tmpl` | `0.2.1` | `experimental` |
| Skill | `src/skills/audit-ux/SKILL.md.tmpl` | `0.1.1` | `experimental` |
| Discipline | `src/skills/browse-skills/SKILL.md.tmpl` | `1.1.0` | `experimental` |
| Skill | `src/skills/build/SKILL.md.tmpl` | `0.1.0` | `experimental` |
| Discipline | `src/skills/check-colour-contrast/SKILL.md.tmpl` | `1.1.0` | `stable` |
| Skill | `src/skills/compose-career-profile/SKILL.md.tmpl` | `1.1.1` | `stable` |
| Skill | `src/skills/compose-voice-profile/SKILL.md.tmpl` | `1.1.0` | `stable` |
| Reference | `src/skills/compose-voice-profile/references/professional-voice-profile.md` | `2.0.0` | `stable` |
| Discipline | `src/skills/convert-colour/SKILL.md.tmpl` | `1.1.0` | `stable` |
| Skill | `src/skills/create-cv/SKILL.md.tmpl` | `2.0.1` | `stable` |
| Skill | `src/skills/create-docs/SKILL.md.tmpl` | `0.6.0` | `experimental` |
| Reference | `src/skills/create-docs/references/nextra-docs.md` | `0.2.0` | `experimental` |
| Skill | `src/skills/create-guidelines/SKILL.md.tmpl` | `0.6.0` | `experimental` |
| Skill | `src/skills/create-skill/SKILL.md.tmpl` | `0.14.0` | `experimental` |
| Skill | `src/skills/draft-cover-letter/SKILL.md.tmpl` | `2.0.1` | `stable` |
| Discipline | `src/skills/mind-wandering/SKILL.md.tmpl` | `0.2.0` | `experimental` |
| Discipline | `src/skills/pre-mortem/SKILL.md.tmpl` | `0.2.0` | `experimental` |
| Discipline | `src/skills/quit-the-yap/SKILL.md.tmpl` | `0.3.0` | `experimental` |
| Discipline | `src/skills/release-agent-stack/SKILL.md.tmpl` | `0.8.0` | `experimental` |
| Discipline | `src/skills/research-literature/SKILL.md.tmpl` | `1.0.0` | `stable` |
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
| Skill | `src/skills/research/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Reference | `src/skills/research/references/artifacts.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research/references/cli.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research/references/csl/README.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research/references/export.md` | `1.0.0` | `stable` |
| Reference | `src/skills/research/references/workflow.md` | `1.0.0` | `stable` |
| Skill | `src/skills/setup-agent-stack/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Skill | `src/skills/setup-career-stack/SKILL.md.tmpl` | `2.0.1` | `stable` |
| Skill | `src/skills/ship/SKILL.md.tmpl` | `0.10.0` | `experimental` |
| Discipline | `src/skills/show-me-your-work/SKILL.md.tmpl` | `0.2.0` | `experimental` |
| Router | `src/skills/skill-issue/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Discipline | `src/skills/spawn-evals/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Discipline | `src/skills/think-deeper/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Discipline | `src/skills/think-harder/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Skill | `src/skills/translate/SKILL.md.tmpl` | `1.0.0` | `stable` |
| Discipline | `src/skills/update-changelog/SKILL.md.tmpl` | `0.3.0` | `experimental` |
| Discipline | `src/skills/update-map/SKILL.md.tmpl` | `0.3.0` | `experimental` |
| Discipline | `src/skills/update-router/SKILL.md.tmpl` | `0.2.0` | `experimental` |
| Discipline | `src/skills/write/SKILL.md.tmpl` | `2.0.0` | `stable` |

## Versioning and maintenance

The stack follows the repository's [versioning policy](src/guidelines/versioning/reference.md) and uses `MAJOR.MINOR.PATCH`. While the stack is at `0.y.z`, use patch increments for compatible corrections and minor increments for additions or breaking changes. The highest compatibility impact in a coordinated release determines the stack increment.

Component versions remain independently maintained according to their own contracts. Do not bump every component just because the stack version changes. Before a coordinated release, review the changes, confirm component versions have been updated where needed, refresh this inventory from frontmatter, and verify the stack version against the release tag if one is created. Use an ISO `YYYY-MM-DD` date for a release; keep the date as `Not released` until the stack is actually released. Record detailed change history in a changelog if one is introduced.
