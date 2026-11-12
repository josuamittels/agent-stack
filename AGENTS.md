# Agent Stack

## …

<!-- BEGIN agent-stack:entry -->
## Agent stack guide

This repository contains Mento's reusable agent capabilities and supporting resources. See [the stack map](map.mmd) for organization and dependencies; actual instruction files establish availability.

At the start of a new task, or when its intended outcome changes, read [skill-issue](src/skills/skill-issue/SKILL.md.tmpl) to select a capability. Honor explicit user choices and project instructions. After selection, follow the destination's workflow and handoffs without restarting routing at each step. Handle explicit direct-answer requests directly.

| Location | Role |
| --- | --- |
| `skills/` | Generated experimental and stable public packages; drafts excluded; never edit directly. |
| `src/catalog.yaml` | Public candidates, dependencies, and resource declarations. |
| `scripts/` | Build and packaging tools. |
| `dist/` | Ignored local previews and release artifacts. |
| `src/skills/` | Task workflows and reusable methods. `type: skill` and `type: discipline` distinguish them; load the selected SKILL.md.tmpl when needed. |
| `src/guidelines/` | Language, design, and technical references loaded by their consuming workflows; never route destinations. |
| `src/skills/*/templates/` | Authoring scaffolds kept beside the capability that uses them. |
| `src/evals/` | Objective rubrics and checker scripts for skills with meaningful script-verifiable checks; qualitative-only skills have no evaluator handoff or package. |
| `sources/` | Local research and third-party examples; exclude these copies from capability discovery. |
| `agents/` | Reserved for future agent definitions; currently empty. |
| `playbooks/` | Draft workflow outlines, including `playbooks/startup.md`. |

Skill-issue lists usable instruction files, including drafts. Empty folders and map-only entries are planned. Paths here provide navigation and do not install native host integrations; use a supported host invocation when available, otherwise read and apply the selected local instructions in context.

During an authorized stack release, [release-agent-stack](src/skills/release-agent-stack/SKILL.md.tmpl) coordinates any required map and router refresh for capability or routing changes. Preserve manual instructions outside the markers.
<!-- END agent-stack:entry -->

## Hosted documentation

Whenever this repository's documentation changes, build and publish the updated website at `https://agents.mittels.org`. The owner has authorized routine repeat deployments to this existing destination; do not ask again for the same build/upload operation. Follow Create Docs' deployment reference, using `npm run deploy` from `docs/` with an available Python 3.10+ interpreter on PATH.

The local hosting profile is `src/skills/create-docs/.env.local`. It is ignored and is not a public skill resource. The publisher builds the static export and search index before uploading over explicit FTPS. It preserves unrelated remote files and records deployment results under `.local/docs-deploy/`. Verify the live site, nested routes, and search after publication. A failed or partial upload remains incomplete until resolved. A different destination or a conflicting remote file outside the managed site is a separate decision.

## Git delivery

Ship authorized changes in this repository by committing and pushing directly to `main`. This is the owner's standing delivery preference and overrides the topic-branch and pull-request defaults in Ship and Release Agent Stack. Do not ask again for confirmation of this route. Keep unrelated work out of commits and complete the required release checks before pushing.
