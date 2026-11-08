# Global instruction targets

Read before selecting a host or file. These rules describe local Codex and Claude Code sessions, not hosted accounts or organization policy.

| Host | Global target | Verify loading |
| --- | --- | --- |
| Codex | `AGENTS.md` under `CODEX_HOME`, otherwise `~/.codex`. Use a nonempty `AGENTS.override.md` instead when present, because it shadows the base file. | Start a new session and ask which instruction sources it loaded. |
| Claude Code | `CLAUDE.md` under `CLAUDE_CONFIG_DIR`, otherwise `~/.claude`. For a custom profile, verify its loaded sources. | Start a new session and inspect `/memory`. |

Use the current host unless the user selects another one. Configuring both means running the workflow separately for each requested host. Never infer both from finding both configuration directories. For an unfamiliar host or unverified custom loading arrangement, identify the supported target before editing.

The host's installed catalog establishes public skill availability. Verify that the `skill-issue/SKILL.md` entry in the selected installation root is readable. Current Codex commonly uses project `.agents/skills` or user `~/.agents/skills`; older clients and plugins may expose other locations. Claude Code commonly uses project `.claude/skills` or user `~/.claude/skills`, with plugin namespacing where applicable. Use the paths actually exposed by the host. Skill-directory symlinks are normal; do not treat an instruction-file symlink as permission to modify its target.

The routing block intentionally contains no machine-specific skill paths. A global rule can therefore work with project-scoped installations without redirecting future projects to one checkout. If the router entry is missing, report the missing prerequisite before changing global instructions. Installing skills remains separate. For use across projects, offer these commands without running them unless installation is requested:

```sh
# Codex
npx skills add josuamittels/agent-stack --skill '*' -a codex -g

# Claude Code
npx skills add josuamittels/agent-stack --skill '*' -a claude-code -g
```

Official references, checked 2026-11-08: [Codex instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code memory](https://code.claude.com/docs/en/memory), [Claude Code settings](https://code.claude.com/docs/en/settings), and [Claude Code skills](https://code.claude.com/docs/en/skills).
