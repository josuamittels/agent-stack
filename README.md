# Agent Stack

Mento’s reusable agent workflows, disciplines, and reference guidance.

## Release status

The stack is **draft** and has not been published. Public packages require a stable stack at version 1.0 or later and stable skills with stable dependency closures. A skill being a public candidate does not make it installable yet. No statuses are promoted by the build.

## Develop and preview

```sh
npm ci --ignore-scripts
npm run build:preview -- --skill translate
npm test
```

Edit canonical instructions in `src/skills/`, shared references in `src/guidelines/`, and objective packages in `src/evals/`. `src/catalog.yaml` declares public candidates and their packaging dependencies. Never edit generated root `skills/` files.

For a disposable project, install a locally generated preview with the standard CLI:

```sh
npx skills add /absolute/path/to/agent-stack/dist/preview/skills --skill translate -a codex
```

Preview builds remain local and unpublished. The same package contains the required helper instructions and language guidelines; no sibling install or online fetch is needed.

## Eventual stable installation

These commands are for a future stable catalog, not the current draft:

```sh
# One skill, including private dependency snapshots
npx skills add josuamittels/agent-stack --skill translate -a codex

# Also make its helpers independently invocable
npx skills add josuamittels/agent-stack --skill translate natural-writing ask-user-question think-harder -a codex

# Complete public set for Claude Code
npx skills add josuamittels/agent-stack --skill '*' -a claude-code
```

Project installation is the default; use `-g` for user-wide installation. Host-specific plugins and archives are generated from these same packages.

- [Distribution, configuration, updates, and maintenance](docs/distribution.md)
- [Generated candidate install commands and dependencies](docs/installation.generated.md)
- [Versions and lifecycle](VERSIONS.md)
- [Maintainer resource map](map.mmd)

Installing capabilities does not edit a consumer project’s `AGENTS.md`. The repository’s own `AGENTS.md` routes maintainers to editable sources.
