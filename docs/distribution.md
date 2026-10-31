# Distribution and maintenance

## Current availability

Agent Stack is draft and unpublished. `src/catalog.yaml` declares 22 public candidates and three internal maintenance capabilities. Public eligibility requires each candidate and its bundled dependencies and versioned guidance to be stable. A stable skill with experimental question helpers is therefore blocked too.

The stack itself must be stable at version 1.0 or later before release archives can be published. Builds never promote lifecycle statuses. Preview packages are local development artifacts, not public releases.

## Source and generated files

| Location | Ownership |
| --- | --- |
| `src/skills/` | Editable `SKILL.md.tmpl` workflows, disciplines, scripts, references, and owned templates. |
| `src/guidelines/` | Shared editable guidance. |
| `src/evals/` | Editable objective packages. |
| `src/runtime/` | Portable configuration/state path helpers. |
| `src/catalog.yaml` | Explicit dependency, resource, visibility, and host declarations. |
| `scripts/` | Build, validation, and release machinery. |
| `skills/` | Committed generated stable packages and eligibility report. |
| `dist/preview/` | Ignored preview skills, plugin trees, catalogs, and archives. |
| `dist/release/` | Ignored stable release artifacts, created only after release gates pass. |

Canonical entry points use `SKILL.md.tmpl`, including the authoring scaffold. Only generated packages contain installable `SKILL.md` entries. This prevents the skills CLI’s recursive fallback from discovering unbuilt source workflows when the public catalog is empty.

Edit sources, then run `npm run build`. Commit source edits, generated stable output, generated installation documentation, and the matching version inventory together. Generated private copies are never independent component inventory entries.

## Build and check

The build requires Node.js 22.20 or later and Python 3.10 or later. Install locked dependencies with `npm ci --ignore-scripts`.

```sh
npm run build
npm run build:preview
npm run build:preview -- --skill translate
npm run check:generated
npm run check:packages
npm test
npm run package
```

`build` emits only eligible stable candidates; an empty development catalog is valid. Read `skills/catalog.json` for precise blockers. `build:preview` packages experimental candidates locally. Selecting a preview skill replaces the previous preview catalog; run the full preview build to restore all candidates.

`check:generated` computes expected output in memory without updating tracked files. `check:packages` checks current stable files against source-generated expectations and their manifests. `package` refuses a draft/experimental stack, versions below 1.0, an empty catalog, or stale stable output.

The generator stages an entire replacement tree. It refuses unowned output directories and never cleans outside its designated generated directories. Do not store personal files inside generated output.

## Declare a package

Every canonical skill needs one catalog entry. Keep its `files` list explicit, including required scripts, data, templates, and owned references. Add shared guideline files under `resources`; add an objective package slug under `evaluations` only when required by that workflow.

`required` and `conditional` dependencies are bundled transitively. Cycles are collected once; they do not authorize recursive execution. `optional` handoffs and router `routes` are discovery relationships, not installation dependencies. Repository-level `project_files` are references to files in the caller’s target project; the generator never substitutes a snapshot of this repository's release record. Declared third-party Python imports appear in `python_packages` and their consuming skill’s requirements.

Adding a new source file does not automatically publish it. Missing declarations, unresolved local links, local imports outside the selected closure, symlinks, path escapes, unsafe credential examples, and prohibited files fail the build. Templates retain their contents, with discovery-sensitive filenames changed in the distribution.

Each package has one public `SKILL.md`. Its complete instructions and dependency instructions live under `references/_stack/skills/*/instructions.md`. Scripts retain the mirrored source layout so their sibling imports and resource paths work outside this repository. Set `AGENT_STACK_ROOT` to the installed package’s absolute `references/_stack` directory before executing its command examples. Resolve helper paths from that location; the target project remains a separate location.

Required workflow instructions and guidelines are local. Research may still need live data providers, and exports may require Pandoc and a host-supplied LibreOffice. Packaging does not provide those services or executables.

## Standard installation

For an eventual stable catalog:

```sh
# One self-contained skill
npx skills add josuamittels/agent-stack --skill translate -a codex

# Selected skills and independently invocable helpers
npx skills add josuamittels/agent-stack --skill translate natural-writing ask-user-question think-harder -a codex

# Full current set for a chosen host
npx skills add josuamittels/agent-stack --skill '*' -a claude-code
```

Use `-g` for user-wide installation or omit it for project scope. Do not use `--all` when you mean all skills for one host: it also selects all agents. The standard CLI does not infer our dependency graph; individual packages already include their required snapshots. Generated dependency commands additionally expose helpers as public skills.

To inspect a local preview in a disposable project, use the absolute `dist/preview/skills` path as the source. The build itself never installs into personal agent directories.

See the [generated catalog commands](installation.generated.md) for per-candidate dependency lists and external requirements. See the [skills CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for supported commands.

## Plugins and ChatGPT

Each distribution contains `plugins/agent-stack/` and a `plugins/agent-stack-<skill>/` directory for each included skill. Every plugin includes the same self-contained skill packages, a portable root `plugin.json`, and a `.claude-plugin/plugin.json` compatibility manifest. No hooks or MCP servers are added.

Claude Code can load a local plugin with `claude --plugin-dir /absolute/path/to/plugin`. To use its generated marketplace, add the distribution directory with `claude plugin marketplace add /absolute/path/to/distribution`, then install `agent-stack@mento-agent-stack` or an individual `agent-stack-<skill>@mento-agent-stack` plugin. Validate locally with `claude plugin validate /absolute/path/to/plugin`.

The generated `.agents/plugins/marketplace.json` is for OpenAI-supported local plugin clients. Codex CLI versions exposing the plugin commands support:

```sh
codex plugin marketplace add /absolute/path/to/distribution
codex plugin add agent-stack@mento-agent-stack
# Or one skill:
codex plugin add agent-stack-translate@mento-agent-stack
```

These commands install into the host's managed cache; use them only when you intend a persistent host installation. The implementation tests use disposable project skill directories instead.

The generated marketplace Its local paths resolve from the **distribution root**, not the manifest directory. Open the distribution as a project in the supported Codex/ChatGPT desktop client, refresh or restart when required, choose its marketplace in the Plugins Directory, and install the full or individual plugin. Hosts load an installed cache copy; editing the original distribution does not necessarily update that copy.

A shell command installing a skill for Codex does not install it into every ChatGPT account or chat. ChatGPT plugin availability depends on the supported client and workspace settings. Workspace import and public directory submission are separate release operations. This build prepares artifacts without submitting or installing them.

Reference: [OpenAI packaging](https://developers.openai.com/plugins/build/plugins), [Claude Code plugin manifests](https://code.claude.com/docs/en/plugins-reference).

## User configuration and state

Never save credentials, output documents, or logs inside installed packages.

- OpenAlex reads `OPENALEX_API_KEY` from the process first. Optional saved configuration lives in `research-literature.env` under `AGENT_STACK_CONFIG_DIR`, otherwise `$XDG_CONFIG_HOME/agent-stack`, otherwise `~/.config/agent-stack`.
- Evaluation history lives under `evals/runs.jsonl` in `--state-dir`, otherwise `AGENT_STACK_STATE_DIR`, otherwise `$XDG_STATE_HOME/agent-stack`, otherwise `~/.local/state/agent-stack`.
- `python /absolute/path/to/references/_stack/runtime/paths.py --config-dir /absolute/config --state-dir /absolute/state` reports resolved paths without reading or printing keys.
- The checker’s `--root` selects resource packages; it does not select the writable state directory.

The source migration preserves any pre-existing local `.env` under `src/skills/research-literature/references/`, still ignored. It is no longer consulted by installed skills. No credential is copied to user configuration automatically. If you want to keep that configuration, move its values yourself to the external location with owner-only permissions or provide an environment variable. Do not put real values in `.env.example`.

Updates can replace complete packages while leaving user configuration and state intact.

## Updates, pinning, and removal

```sh
npx skills check
npx skills update translate
npx skills update
npx skills remove translate
```

Use the matching project/global scope options for the installed copy. Updating a skill replaces its bundled helpers together. Updating a separately installed helper does not change another skill’s pinned internal handoff.

For reproducible installation or rollback, use the full GitHub tree URL containing an existing release tag, for example `https://github.com/josuamittels/agent-stack/tree/v1.0.0/skills/translate`. The example tag must exist; none is created by this implementation. Retain the project’s skill lockfile where the CLI supports it. For another host’s plugin manager, use its supported version/update controls rather than editing its cache.

Updating installed skills does not mean installing new skills added to the catalog. To refresh the complete current set, rerun the full-set installation command. Do not install the same catalog through multiple managers at the same scope; choose one update owner.

## Stable release procedure

1. Stabilize each intended public component, its required/conditional dependencies, and versioned guidance through their own review. Confirm redistribution provenance for bundled third-party assets; preserve the CSL attribution file and embedded license. Do not automatically promote statuses to make a build pass.
2. Use the existing Ship/Release Agent Stack procedure to prepare the version, canonical inventory, changelog, map/router changes, and documentation. Every substantive planned commit retains its own stack version/inventory update. The build and packaging commands do not create commits.
3. Ship runs `npm run build` for each Agent Stack commit after its metadata, discovery, and documentation updates, then checks the rebuilt candidate before committing. It reviews and includes generated packages and installation documentation in the same commit. A failed build or required check stops delivery. This also applies to draft local commits; preview generation and artifact publication remain separate. Review `skills/catalog.json` for eligibility blockers.
4. In a separately authorized release, establish the stable version and actual release date, create the matching `v<version>` tag and GitHub release, then run the manual **Publish stable packages** workflow against that tag.
5. The workflow verifies the checked-out tag, stable release record, clean tree, generated files, tests, and checksums before attaching artifacts. It does not create tags, promote statuses, submit marketplaces, or overwrite existing assets.

skills.sh discovers repository skills through installs recorded by its CLI; creating a hosted skills.sh pack is optional. After an actual public release, verify discovery and installation telemetry through the service. See the [skills.sh FAQ](https://www.skills.sh/docs/faq).
