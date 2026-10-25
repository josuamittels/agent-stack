# Agent Stack

## …

<!-- BEGIN agent-stack:entry -->
## Agent stack guide

This repository contains Mento's reusable agent capabilities and supporting resources. See [the stack map](map.mmd) for organization and dependencies; actual instruction files establish availability.

At the start of a new task, or when its intended outcome changes, read [skill-issue](skills/skill-issue/SKILL.md) to select a capability. Honor explicit user choices and project instructions. After selection, follow the destination's workflow and handoffs without restarting routing at each step. Handle explicit direct-answer requests directly.

| Location | Role |
| --- | --- |
| `skills/` | Task workflows and the skill-issue router. Load the selected SKILL.md when needed. |
| `disciplines/` | Reusable methods supporting skills. Direct use can fit a small task or a gap without a matching skill. |
| `guidelines/` | Language, design, and technical references loaded by their consuming workflows; never route destinations. |
| `templates/` | Authoring scaffolds for skills, references, standalone routers, and AGENTS instructions. |
| `evals/` | Evaluation packages and checks for capabilities that use them. Fixtures do not expose executable capabilities. |
| `sources/` | Local research and third-party examples; exclude these copies from capability discovery. |
| `agents/`, `playbooks/` | Reserved directories, currently empty. |

Skill-issue lists usable instruction files, including drafts. Empty folders and map-only entries are planned. Paths here provide navigation and do not install native host integrations; use a supported host invocation when available, otherwise read and apply the selected local instructions in context.

After capability or routing changes, [update-router](disciplines/update-router/SKILL.md) refreshes this section and skill-issue's managed catalog. Preserve manual instructions outside the markers.
<!-- END agent-stack:entry -->
