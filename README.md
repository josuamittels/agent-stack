<div align="center">

# Agent Stack

### Serious leverage for people building things with limited AI capacity.

Focused skills for the work around a venture: research, decisions, product and design quality, writing, delivery, and the systems that make good work repeatable.

[![skills.sh installs](https://skills.sh/b/josuamittels/agent-stack)](https://skills.sh/josuamittels/agent-stack)
![Release status: draft](https://img.shields.io/badge/release-draft-orange)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[Explore the skills](#whats-in-the-stack) · [Install a preview](#install) · [How the stack is organized](#how-its-organized) · [Why we made it](#why-we-made-it)

</div>

---

You have a product to shape, a market to understand, customers to reach, and a business to build. Your AI budget is finite. Finding a trustworthy skill for each job takes time, and long instructions can spend your context before the real work starts.

**Agent Stack is a curated set of practical agent skills for that reality.** Each one gives an agent the process, judgment, and supporting material needed for a specific kind of work, without asking it to load an entire operating manual first.

The aim is simple: **higher-quality work per unit of attention, time, and tokens.**

> Agent Stack is in draft and has not been published. The skills.sh badge is included for the eventual public listing; public installs are not available yet. You can build and install local previews today.

## What’s in the stack

There are **22 public-catalog candidates** today. They cover reusable ways to think, research, write, create, and ship. The catalog is broad, but it is not a finished set of turnkey startup playbooks: the skills are focused building blocks you can use on their own or combine into a longer workflow.

### Find the signal and make better decisions

| Skill | Use it to |
| --- | --- |
| [Research](src/skills/research/SKILL.md.tmpl) | Produce source-grounded research reports and literature reviews, with staged workflows, citations, and export options. |
| [Research Literature](src/skills/research-literature/SKILL.md.tmpl) | Search scholarly sources, verify work identities, and return records and abstracts with a search receipt. |
| [Think Harder](src/skills/think-harder/SKILL.md.tmpl) | Resolve uncertainty from context and evidence before asking you to decide. |
| [Think Deeper](src/skills/think-deeper/SKILL.md.tmpl) | Strengthen the methods, evidence, and checks behind a settled task. |
| [Pre-mortem](src/skills/pre-mortem/SKILL.md.tmpl) | Find plausible ways a consequential plan could fail before you commit to it. |
| [Ask User Question](src/skills/ask-user-question/SKILL.md.tmpl) | Prepare a focused question when a decision depends on information only you can provide. |
| [Mind Wandering](src/skills/mind-wandering/SKILL.md.tmpl) | Explore fresh angles when the obvious approaches are not enough. |

### Make the work clear, distinctive, and well crafted

| Skill | Use it to |
| --- | --- |
| [Write](src/skills/write/SKILL.md.tmpl) | Write or edit clear human-facing prose while preserving intent and voice. |
| [Translate](src/skills/translate/SKILL.md.tmpl) | Translate or localize supplied text with attention to natural phrasing and audience. |
| [Compose Voice Profile](src/skills/compose-voice-profile/SKILL.md.tmpl) | Turn writing samples, research, and direction into an evidence-backed voice profile. |
| [Convert Colour](src/skills/convert-colour/SKILL.md.tmpl) | Convert color values across common digital and print color spaces. |
| [Check Colour Contrast](src/skills/check-colour-contrast/SKILL.md.tmpl) | Calculate contrast for two colors and interpret the result against accessibility thresholds. |

Visual quality matters across the whole product, not just in a final polish pass. The source tree also contains developing guidance for accessibility, composition, color, typography, iconography, interaction, motion, sound, haptics, and wireframes. These design references are not all part of installable packages yet; see [release status](#availability-and-release-status).

### Build repeatable ways of working

| Skill | Use it to |
| --- | --- |
| [Create Docs](src/skills/create-docs/SKILL.md.tmpl) | Create evidence-grounded product and repository documentation. |
| [Create Guidelines](src/skills/create-guidelines/SKILL.md.tmpl) | Define or repair reusable standards and working conventions. |
| [Create Skill](src/skills/create-skill/SKILL.md.tmpl) | Turn a proven workflow into a reusable skill, with objective checks when they fit. |
| [Spawn Evals](src/skills/spawn-evals/SKILL.md.tmpl) | Prepare and run deterministic checks for outputs with criteria a script can verify. |
| [Show Me Your Work](src/skills/show-me-your-work/SKILL.md.tmpl) | Keep an evidence-linked decision log for long or multi-stage work. |

### Find, route, and deliver the work

| Skill | Use it to |
| --- | --- |
| [Browse Skills](src/skills/browse-skills/SKILL.md.tmpl) | Inspect comparable public skills for methods and inspiration. |
| [Skill Issue](src/skills/skill-issue/SKILL.md.tmpl) | Route a request to a suitable stack capability. |
| [Ship](src/skills/ship/SKILL.md.tmpl) | Carry a reviewed change through the target repository’s release and Git workflow. |
| [Update Changelog](src/skills/update-changelog/SKILL.md.tmpl) | Record a release’s changes in its changelog. |
| [Quit the Yap](src/skills/quit-the-yap/SKILL.md.tmpl) | Make an in-chat answer concise without losing details needed to act. |

Some skills are small disciplines that support many workflows; others own a larger task from intake through delivery. Required dependencies are bundled with each package, so you do not need to install a separate helper set for every skill.

## Install

### Install a local preview

The public catalog is not released yet. To try a skill, build a preview and install it into a disposable project. This requires Node.js 22.20 or later and Python 3.10 or later.

```sh
npm ci --ignore-scripts
npm run build:preview
npx skills add /absolute/path/to/agent-stack/dist/preview/skills --skill research -a codex
```

Replace `research` with a candidate name from the tables above. The preview build packages the selected skill’s required instructions and resources together. To install the complete preview set, use `--skill '*'`:

```sh
npx skills add /absolute/path/to/agent-stack/dist/preview/skills --skill '*' -a codex
```

The examples use Codex. The generated preview distribution also includes plugin packages for supported local plugin clients. See [distribution details](docs/distribution.md) for Claude Code, ChatGPT, updates, and package behavior.

### Install from the public catalog

Once Agent Stack and the selected skills pass their release gates, install a single skill or the full catalog with the standard skills CLI:

```sh
# One skill
npx skills add josuamittels/agent-stack --skill research -a codex

# The current complete public set
npx skills add josuamittels/agent-stack --skill '*' -a codex
```

These are future commands, not currently available installs. Omit `-g` for project installation; add it for user-wide installation. The public catalog will include only stable skills with stable dependency closures.

## Why we made it

We wanted strong agent workflows without needing a large model budget or a dedicated AI team. The best individual skills are hard to find, hard to compare, and often buried inside stacks with very different assumptions. Meanwhile, a long generic prompt can consume the very context needed to do the task well.

We studied agent stacks including gstack, ECC, pstack, LifeOS, and other skill libraries. We looked at how they organize skills, route work, handle dependencies, and guide an agent through a task. Agent Stack brings those lessons together as **condensed, usable expertise**: enough instruction to do the work carefully, with deeper references and helper procedures available when the task calls for them.

That matters for entrepreneurs because the work rarely stays in one lane. One day you need to test an idea; the next you need to understand a market, shape an experience, write for a specific audience, or turn a repeated process into a system. A focused skill gives the agent a better starting point and keeps you in charge of the decisions that are yours to make.

The direction is a connected set of playbooks that can support the journey from zero to one, then help turn proven work into repeatable operations. The current catalog lays the groundwork with research, judgment, communication, craft, and delivery capabilities; it will grow as complete venture workflows are designed and proven.

## Why this approach works

- **The task gets the context it needs.** A focused workflow avoids loading unrelated material into every request.
- **Quality is part of the method.** Research skills keep claims connected to sources; design guidance treats accessibility and craft as product requirements; writing guidance accounts for voice, audience, and language.
- **You can start small and combine workflows.** Install one capability for a specific job, or build a larger sequence around your project.
- **Repeatable work becomes reusable.** Skills, templates, scripts, and references can encode a process so you do not have to rediscover it each time.
- **The package brings its dependencies.** Required helper instructions and guidance travel with the skill, reducing setup and version drift.
- **You stay in control.** Skills guide the agent’s process; they do not replace your judgment, approve decisions, or silently change your project setup.

## How it’s organized

Agent Stack has a small, explicit source of truth and generated packages for installation.

| Location | What it contains |
| --- | --- |
| [`src/skills/`](src/skills/) | Canonical skill and discipline instructions, scripts, references, and templates. |
| [`src/guidelines/`](src/guidelines/) | Shared standards, including language, design, coding, and documentation guidance. |
| [`src/catalog.yaml`](src/catalog.yaml) | The public candidates, their dependencies, required files, resources, and supported hosts. |
| [`skills/`](skills/) | Generated stable packages. Do not edit these directly. |
| [`dist/preview/`](dist/preview/) | Local preview packages generated for development. This directory is ignored by Git. |
| [`docs/`](docs/) | Distribution, installation, lifecycle, and maintainer documentation. |

Each capability has one primary instruction file. A **skill** owns a substantial workflow; a **discipline** provides a focused method that other workflows can call. The catalog declares which instructions and resources belong in each package. The build follows those dependencies and bundles the needed material into a self-contained install.

To change a capability, edit its source under `src/`, update its catalog entry if the package contents change, then rebuild. Generated `skills/` output is for released packages, not authoring.

## Availability and release status

Agent Stack is currently **experimental, version 0.37.0, and unpublished**. Although 22 skills are public-catalog candidates, the stack-wide release gate has not been met. The build does not promote draft skills to stable, and the source repository is not the public skills catalog.

Local previews are available now. Public skills.sh installs and download counts will become meaningful after publication. Some candidate skills are themselves still experimental and may be excluded from the first stable release. Check the generated [candidate catalog](docs/installation.generated.md) and [version inventory](VERSIONS.md) for current component status.

## License

Agent Stack is licensed under the [MIT License](LICENSE).
