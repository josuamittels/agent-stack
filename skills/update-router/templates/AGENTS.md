# [Repository name]

<!-- Copy this template to the repository root as AGENTS.md. Links below resolve from that destination. -->

[Project instructions maintained by the repository owner belong outside the managed section. Preserve them when refreshing routing. This is an AGENTS template, distinct from the standalone router template.]

<!-- BEGIN agent-stack:entry -->
## Agent stack guide

[Describe the repository in one sentence.] See [the stack map](map.mmd) for organization and dependencies. Check actual instruction files before treating a mapped resource as available.

At the start of a new task, or when its intended outcome changes, read [skill-issue](skills/skill-issue/SKILL.md) to select a capability. Keep explicit user choices and project instructions authoritative. Once selected, follow the destination's workflow and handoffs without restarting routing at each step. A direct-answer request can be handled directly.

| Location | Role |
| --- | --- |
| `skills/` | Workflows and reusable methods, differentiated by `type: skill` or `type: discipline`; read the chosen SKILL.md when using it. |
| `guidelines/` | Supporting standards and references selected by workflows; never routing destinations. |
| `skills/*/templates/` | Authoring scaffolds kept beside the capability that uses them. |
| `evals/` | Evaluation packages for capabilities that use them; fixtures are not available skills. |
| `sources/` | Research and third-party examples; exclude them from capability discovery. |
| `agents/`, `playbooks/` | [Describe actual contents or state that these directories are reserved and empty.] |

The router catalog exposes usable instructions, including drafts. Empty folders and map-only entries are planned. Repository paths provide navigation; native host discovery requires separate installation or configuration. Use the host's supported invocation when available, otherwise read and apply the local instructions in context.

During an authorized stack release, [release-agent-stack](skills/release-agent-stack/SKILL.md) coordinates any required map and router refresh for capability or routing changes. Keep manual instructions outside the markers.
<!-- END agent-stack:entry -->
