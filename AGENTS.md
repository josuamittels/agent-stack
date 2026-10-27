# Agent Stack

## …

<!-- BEGIN agent-stack:entry -->
## Agent stack guide

This repository contains Mento's reusable agent capabilities and supporting resources. See [the stack map](map.mmd) for organization and dependencies; actual instruction files establish availability.

At the start of a new task, or when its intended outcome changes, read [skill-issue](skills/skill-issue/SKILL.md) to select a capability. Honor explicit user choices and project instructions. After selection, follow the destination's workflow and handoffs without restarting routing at each step. Handle explicit direct-answer requests directly.

| Location | Role |
| --- | --- |
| `skills/` | Task workflows and reusable methods. `type: skill` and `type: discipline` distinguish them; load the selected SKILL.md when needed. |
| `guidelines/` | Language, design, and technical references loaded by their consuming workflows; never route destinations. |
| `skills/*/templates/` | Authoring scaffolds kept beside the capability that uses them. |
| `evals/` | Objective rubrics and checker scripts for skills with meaningful script-verifiable checks; qualitative-only skills have no evaluator handoff or package. |
| `sources/` | Local research and third-party examples; exclude these copies from capability discovery. |
| `agents/` | Reserved for future agent definitions; currently empty. |
| `playbooks/` | Draft workflow outlines, including `playbooks/startup.md`. |

Skill-issue lists usable instruction files, including drafts. Empty folders and map-only entries are planned. Paths here provide navigation and do not install native host integrations; use a supported host invocation when available, otherwise read and apply the selected local instructions in context.

During an authorized stack release, [release-agent-stack](skills/release-agent-stack/SKILL.md) coordinates any required map and router refresh for capability or routing changes. Preserve manual instructions outside the markers.
<!-- END agent-stack:entry -->
