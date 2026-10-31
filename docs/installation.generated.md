# Generated installation reference

Generated from `src/catalog.yaml`. Commands target the eventual stable catalog; local previews use paths under `dist/preview/skills`.

```sh
npx skills add josuamittels/agent-stack --skill '*' -a codex
npx skills add josuamittels/agent-stack --skill '*' -a claude-code
```

Use `-g` for a user-wide installation. Project scope is the default.

## ask-user-question

Status: eligible stable candidate.

Prepare, deliver, and interpret any task question for the user, including direct permission gates. Use Think Harder first only when context, evidence, or a reasonable default might resolve the gap.

`npx skills add josuamittels/agent-stack --skill ask-user-question think-harder -a codex`

Bundled dependencies: think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## browse-skills

Status: blocked for public release (see skills/catalog.json).

Find and inspect related public skills for inspiration through GetEdge and original source repositories. Use when in need of comparable methods, skills, agent orchestration, conventions, or failure-handling approaches.

`npx skills add josuamittels/agent-stack --skill ask-user-question browse-skills think-harder -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## check-colour-contrast

Status: eligible stable candidate.

Calculate the WCAG contrast ratio for two opaque hex, RGB, or HSL colors and interpret the result.

`npx skills add josuamittels/agent-stack --skill ask-user-question check-colour-contrast think-harder -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## compose-voice-profile

Status: blocked for public release (see skills/catalog.json).

Compose a detailed, evidence-backed brand or author voice profile from user direction, research, guides, writing samples, visual references, and market context. Use when the user wants a reusable voice profile or tone-of-voice guide.

`npx skills add josuamittels/agent-stack --skill ask-user-question compose-voice-profile natural-writing research research-literature spawn-evals think-deeper think-harder -a codex`

Bundled dependencies: ask-user-question, natural-writing, research, research-literature, spawn-evals, think-deeper, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present; Python >=3.10; Pandoc for file exports; host-bundled LibreOffice for PDF; pypdf for PDF objective verification; web/API access for retrieval; optional OPENALEX_API_KEY.

## convert-colour

Status: eligible stable candidate.

Convert a color value between hex, RGB, HSL, HSV, CMYK, Lab, LCH, and Display P3 with the standalone script.

`npx skills add josuamittels/agent-stack --skill ask-user-question convert-colour think-harder -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## create-docs

Status: blocked for public release (see skills/catalog.json).

Create evidence-grounded documentation in root/docs for people who use a repository's product or resources. Explain its structure, components, and supported use; do not default to contributor or maintainer manuals.

`npx skills add josuamittels/agent-stack --skill ask-user-question browse-skills create-docs create-guidelines create-skill natural-writing pre-mortem spawn-evals think-deeper think-harder -a codex`

Bundled dependencies: ask-user-question, browse-skills, create-guidelines, create-skill, natural-writing, pre-mortem, spawn-evals, think-deeper, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## create-guidelines

Status: blocked for public release (see skills/catalog.json).

Create or revise reusable guideline documents. Use to define domain standards, conventions, tool usage, or best practices, or to repair a guideline defect found while evaluating a skill.

`npx skills add josuamittels/agent-stack --skill ask-user-question browse-skills create-guidelines create-skill natural-writing pre-mortem spawn-evals think-deeper think-harder -a codex`

Bundled dependencies: ask-user-question, browse-skills, create-skill, natural-writing, pre-mortem, spawn-evals, think-deeper, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## create-skill

Status: blocked for public release (see skills/catalog.json).

Create new skills and disciplines, or propose and implement approved improvements to existing ones in the agent stack. Prepare objective checks only when a skill has meaningful script-verifiable criteria.

`npx skills add josuamittels/agent-stack --skill ask-user-question browse-skills create-guidelines create-skill natural-writing pre-mortem spawn-evals think-deeper think-harder -a codex`

Bundled dependencies: ask-user-question, browse-skills, create-guidelines, natural-writing, pre-mortem, spawn-evals, think-deeper, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## mind-wandering

Status: blocked for public release (see skills/catalog.json).

Open creative possibilities through playful association, reframing, changes of representation, and deliberate return. Use to explore unfamiliar directions, escape fixation, or develop an unusual idea while preserving the task's intent.

`npx skills add josuamittels/agent-stack --skill ask-user-question mind-wandering think-deeper think-harder -a codex`

Bundled dependencies: ask-user-question, think-deeper, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## natural-writing

Status: eligible stable candidate.

Write, edit, and translate any prose people will read, including product interfaces, websites, documentation, articles, and messages. Apply when producing human-facing text, including within implementation tasks, to preserve meaning, fit the intended voice and audience, and remove formulaic AI phrasing.

`npx skills add josuamittels/agent-stack --skill ask-user-question natural-writing think-harder -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## pre-mortem

Status: blocked for public release (see skills/catalog.json).

Find concrete failure paths in an adjustable, consequential plan before commitment by imagining it has failed and working backward.

`npx skills add josuamittels/agent-stack --skill ask-user-question pre-mortem think-harder -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## quit-the-yap

Status: blocked for public release (see skills/catalog.json).

Write concise, direct in-chat answers in English Absolute style while preserving the details needed for meaning and action.

`npx skills add josuamittels/agent-stack --skill ask-user-question natural-writing quit-the-yap think-harder -a codex`

Bundled dependencies: ask-user-question, natural-writing, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## research

Status: blocked for public release (see skills/catalog.json).

Produce source-grounded research reports and literature reviews through repeatable stages, journal-filtered discovery, academic writing, deterministic citations, and Markdown, LaTeX, PDF or Word export.

`npx skills add josuamittels/agent-stack --skill ask-user-question natural-writing research research-literature spawn-evals think-deeper think-harder -a codex`

Bundled dependencies: ask-user-question, natural-writing, research-literature, spawn-evals, think-deeper, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present; Python >=3.10; Pandoc for file exports; host-bundled LibreOffice for PDF; pypdf for PDF objective verification; web/API access for retrieval; optional OPENALEX_API_KEY.

## research-literature

Status: blocked for public release (see skills/catalog.json).

Search journal-filtered scholarly databases, cross-reference work identities and citation links, and return source-linked records, abstracts, and a caller-ready search receipt.

`npx skills add josuamittels/agent-stack --skill ask-user-question natural-writing research research-literature spawn-evals think-deeper think-harder -a codex`

Bundled dependencies: ask-user-question, natural-writing, research, spawn-evals, think-deeper, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present; Python >=3.10; Pandoc for file exports; host-bundled LibreOffice for PDF; pypdf for PDF objective verification; web/API access for retrieval; optional OPENALEX_API_KEY.

## ship

Status: blocked for public release (see skills/catalog.json).

Ship a reviewed change by following the target repository's release, changelog, test, and Git workflow. Use when asked to ship, release, push, or create or update a pull request.

`npx skills add josuamittels/agent-stack --skill ask-user-question browse-skills create-docs create-guidelines create-skill natural-writing pre-mortem ship skill-issue spawn-evals think-deeper think-harder update-changelog -a codex`

Bundled dependencies: ask-user-question, browse-skills, create-docs, create-guidelines, create-skill, natural-writing, pre-mortem, release-agent-stack, skill-issue, spawn-evals, think-deeper, think-harder, update-changelog, update-map, update-router.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## show-me-your-work

Status: blocked for public release (see skills/catalog.json).

Keep an evidence-linked decision log for long-running, multi-phase, or unattended work, then audit it before handoff.

`npx skills add josuamittels/agent-stack --skill ask-user-question show-me-your-work think-harder -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## skill-issue

Status: blocked for public release (see skills/catalog.json).

Route an agent-stack request to an available skill, or a discipline for a small task or capability gap. Use at the start of a new task, when the requested outcome changes, or when deciding which stack capability fits.

`npx skills add josuamittels/agent-stack --skill ask-user-question skill-issue think-harder -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## spawn-evals

Status: blocked for public release (see skills/catalog.json).

Prepare and run deterministic, objective checks for completed skill outputs without qualitative assessment or agent delegation.

`npx skills add josuamittels/agent-stack --skill spawn-evals -a codex`

Bundled dependencies: none.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## think-deeper

Status: eligible stable candidate.

Deepen a substantive, well-scoped task with professional methods, primary inputs, suitable tools, and an independent check without enlarging its goal.

`npx skills add josuamittels/agent-stack --skill ask-user-question think-deeper think-harder -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## think-harder

Status: eligible stable candidate.

Resolve missing information and ambiguity from task context, relevant caller guidelines, evidence, and reasonable defaults.

`npx skills add josuamittels/agent-stack --skill ask-user-question think-harder -a codex`

Bundled dependencies: ask-user-question.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## translate

Status: eligible stable candidate.

Translate and localize human-facing text into a target language with fluent, culturally appropriate phrasing. Use for prose, product copy, documentation, and messages that should read naturally in their destination language while preserving the source's meaning, intent, and factual claims.

`npx skills add josuamittels/agent-stack --skill ask-user-question natural-writing think-harder translate -a codex`

Bundled dependencies: ask-user-question, natural-writing, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## update-changelog

Status: blocked for public release (see skills/catalog.json).

Create, update, or prepare a repository changelog from verified changes. Use when the user asks to record changes, maintain CHANGELOG.md, or prepare a changelog release section.

`npx skills add josuamittels/agent-stack --skill ask-user-question think-harder update-changelog -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.
