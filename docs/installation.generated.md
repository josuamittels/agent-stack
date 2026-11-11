# Generated installation reference

Generated from `src/catalog.yaml`. Commands target the experimental and stable shipping catalog; local previews use paths under `dist/preview/skills`.

```sh
npx skills add josuamittels/agent-stack --skill '*' -a codex
npx skills add josuamittels/agent-stack --skill '*' -a claude-code
```

Use `-g` for a user-wide installation. Project scope is the default.

## answer-interview

Status: eligible stable candidate.

Draft concise, evidence-backed answers to job application and interview questions from career context and a target job description, respecting exact word or character limits.

`npx skills add josuamittels/agent-stack --skill answer-interview ask-user-question compose-career-profile compose-voice-profile draft-cover-letter research research-literature spawn-evals think-deeper think-harder write -a codex`

Bundled dependencies: ask-user-question, compose-career-profile, compose-voice-profile, draft-cover-letter, research, research-literature, spawn-evals, think-deeper, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present; ReportLab, pypdf and pypdfium2 for PDF generation and QA; Python >=3.10; Pandoc for file exports; host-bundled LibreOffice for PDF; pypdf for PDF objective verification; web/API access for retrieval; optional OPENALEX_API_KEY.

## ask-user-question

Status: eligible stable candidate.

Prepare, deliver, and interpret any task question for the user, including direct permission gates. Use Think Harder first only when context, evidence, or a reasonable default might resolve the gap.

`npx skills add josuamittels/agent-stack --skill ask-user-question think-harder -a codex`

Bundled dependencies: think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## browse-skills

Status: eligible experimental candidate.

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

## compose-career-profile

Status: eligible stable candidate.

Build a detailed, evidence-grounded career profile from a person's documents and staged interview answers. Use as reusable context for applications and career materials.

`npx skills add josuamittels/agent-stack --skill ask-user-question compose-career-profile think-harder write -a codex`

Bundled dependencies: ask-user-question, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## compose-voice-profile

Status: eligible stable candidate.

Compose a detailed, evidence-backed brand or author voice profile from user direction, research, guides, writing samples, visual references, and market context. Use when the user wants a reusable voice profile or tone-of-voice guide.

`npx skills add josuamittels/agent-stack --skill ask-user-question compose-voice-profile research research-literature spawn-evals think-deeper think-harder write -a codex`

Bundled dependencies: ask-user-question, research, research-literature, spawn-evals, think-deeper, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present; Python >=3.10; Pandoc for file exports; host-bundled LibreOffice for PDF; pypdf for PDF objective verification; web/API access for retrieval; optional OPENALEX_API_KEY.

## convert-colour

Status: eligible stable candidate.

Convert a color value between hex, RGB, HSL, HSV, CMYK, Lab, LCH, and Display P3 with the standalone script.

`npx skills add josuamittels/agent-stack --skill ask-user-question convert-colour think-harder -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## create-cv

Status: eligible stable candidate.

Create evidence-backed, role-tailored CV content and a PDF in a defined EB Garamond layout from a professional career profile and target.

`npx skills add josuamittels/agent-stack --skill ask-user-question compose-career-profile create-cv spawn-evals think-harder write -a codex`

Bundled dependencies: ask-user-question, compose-career-profile, spawn-evals, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present; Python >=3.10; python-docx, Pillow, pypdf, and pypdfium2; LibreOffice or soffice for PDF export.

## create-docs

Status: eligible experimental candidate.

Create evidence-grounded documentation in root/docs for people who use a repository's product or resources. Explain its structure, components, and supported use; do not default to contributor or maintainer manuals.

`npx skills add josuamittels/agent-stack --skill ask-user-question browse-skills create-docs create-guidelines create-skill pre-mortem spawn-evals think-deeper think-harder write -a codex`

Bundled dependencies: ask-user-question, browse-skills, create-guidelines, create-skill, pre-mortem, spawn-evals, think-deeper, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## create-guidelines

Status: eligible experimental candidate.

Create or revise reusable guideline documents. Use to define domain standards, conventions, tool usage, or best practices, or to repair a guideline defect found while evaluating a skill.

`npx skills add josuamittels/agent-stack --skill ask-user-question browse-skills create-guidelines create-skill pre-mortem spawn-evals think-deeper think-harder write -a codex`

Bundled dependencies: ask-user-question, browse-skills, create-skill, pre-mortem, spawn-evals, think-deeper, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## create-skill

Status: eligible experimental candidate.

Create new skills and disciplines, or propose and implement approved improvements to existing ones in the agent stack. Prepare objective checks only when a skill has meaningful script-verifiable criteria.

`npx skills add josuamittels/agent-stack --skill ask-user-question browse-skills create-guidelines create-skill pre-mortem spawn-evals think-deeper think-harder write -a codex`

Bundled dependencies: ask-user-question, browse-skills, create-guidelines, pre-mortem, spawn-evals, think-deeper, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## draft-cover-letter

Status: eligible stable candidate.

Draft or revise a role-specific cover letter from a career profile and job details, in chat or as a designed PDF.

`npx skills add josuamittels/agent-stack --skill ask-user-question compose-career-profile compose-voice-profile draft-cover-letter research research-literature spawn-evals think-deeper think-harder write -a codex`

Bundled dependencies: ask-user-question, compose-career-profile, compose-voice-profile, research, research-literature, spawn-evals, think-deeper, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present; ReportLab, pypdf and pypdfium2 for PDF generation and QA; Python >=3.10; Pandoc for file exports; host-bundled LibreOffice for PDF; pypdf for PDF objective verification; web/API access for retrieval; optional OPENALEX_API_KEY.

## mind-wandering

Status: eligible experimental candidate.

Open creative possibilities through playful association, reframing, changes of representation, and deliberate return. Use to explore unfamiliar directions, escape fixation, or develop an unusual idea while preserving the task's intent.

`npx skills add josuamittels/agent-stack --skill ask-user-question mind-wandering think-deeper think-harder -a codex`

Bundled dependencies: ask-user-question, think-deeper, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## pre-mortem

Status: eligible experimental candidate.

Find concrete failure paths in an adjustable, consequential plan before commitment by imagining it has failed and working backward.

`npx skills add josuamittels/agent-stack --skill ask-user-question pre-mortem think-harder -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## quit-the-yap

Status: eligible experimental candidate.

Write concise, direct in-chat answers in English Absolute style while preserving the details needed for meaning and action.

`npx skills add josuamittels/agent-stack --skill ask-user-question quit-the-yap think-harder write -a codex`

Bundled dependencies: ask-user-question, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## research

Status: eligible stable candidate.

Produce source-grounded research reports and literature reviews through repeatable stages, journal-filtered discovery, academic writing, deterministic citations, and Markdown, LaTeX, PDF or Word export.

`npx skills add josuamittels/agent-stack --skill ask-user-question research research-literature spawn-evals think-deeper think-harder write -a codex`

Bundled dependencies: ask-user-question, research-literature, spawn-evals, think-deeper, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present; Python >=3.10; Pandoc for file exports; host-bundled LibreOffice for PDF; pypdf for PDF objective verification; web/API access for retrieval; optional OPENALEX_API_KEY.

## research-literature

Status: eligible stable candidate.

Search journal-filtered scholarly databases, cross-reference work identities and citation links, and return source-linked records, abstracts, and a caller-ready search receipt.

`npx skills add josuamittels/agent-stack --skill ask-user-question research research-literature spawn-evals think-deeper think-harder write -a codex`

Bundled dependencies: ask-user-question, research, spawn-evals, think-deeper, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present; Python >=3.10; Pandoc for file exports; host-bundled LibreOffice for PDF; pypdf for PDF objective verification; web/API access for retrieval; optional OPENALEX_API_KEY.

## setup-agent-stack

Status: eligible stable candidate.

Configure global Codex or Claude Code instructions to route tasks through installed Agent Stack skills. Use after installation to enable automatic routing or refresh its existing setup.

`npx skills add josuamittels/agent-stack --skill ask-user-question setup-agent-stack skill-issue spawn-evals think-harder -a codex`

Bundled dependencies: ask-user-question, skill-issue, spawn-evals, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present; Node.js >=22.20; Python >=3.10 for objective checks; Installed public skill-issue entry for the selected host; Write access to the selected host's global instruction file.

## setup-career-stack

Status: eligible stable candidate.

Initialize a project workspace for managing job applications, career context, reusable CVs, and application materials. Use when setting up a fresh career application system or organizing a new job-search project.

`npx skills add josuamittels/agent-stack --skill answer-interview ask-user-question compose-career-profile compose-voice-profile create-cv draft-cover-letter research research-literature setup-career-stack spawn-evals think-deeper think-harder write -a codex`

Bundled dependencies: answer-interview, ask-user-question, compose-career-profile, compose-voice-profile, create-cv, draft-cover-letter, research, research-literature, spawn-evals, think-deeper, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present; Python >=3.10; python-docx, Pillow, pypdf, and pypdfium2; LibreOffice or soffice for PDF export; ReportLab, pypdf and pypdfium2 for PDF generation and QA; Pandoc for file exports; host-bundled LibreOffice for PDF; pypdf for PDF objective verification; web/API access for retrieval; optional OPENALEX_API_KEY; Python >=3.10 for CV generation and PDF export; CV-generation tools and dependencies documented by Create CV.

## ship

Status: eligible experimental candidate.

Ship a reviewed change by following the target repository's release, changelog, test, and Git workflow. Use when asked to ship, release, push, or create or update a pull request.

`npx skills add josuamittels/agent-stack --skill ask-user-question browse-skills create-docs create-guidelines create-skill pre-mortem ship skill-issue spawn-evals think-deeper think-harder update-changelog write -a codex`

Bundled dependencies: ask-user-question, browse-skills, create-docs, create-guidelines, create-skill, pre-mortem, release-agent-stack, skill-issue, spawn-evals, think-deeper, think-harder, update-changelog, update-map, update-router, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## show-me-your-work

Status: eligible experimental candidate.

Keep an evidence-linked decision log for long-running, multi-phase, or unattended work, then audit it before handoff.

`npx skills add josuamittels/agent-stack --skill ask-user-question show-me-your-work think-harder -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## skill-issue

Status: eligible stable candidate.

Route an agent-stack request to an available skill, or a discipline for a small task or capability gap. Use at the start of a new task, when the requested outcome changes, or when deciding which stack capability fits.

`npx skills add josuamittels/agent-stack --skill ask-user-question skill-issue think-harder -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## spawn-evals

Status: eligible stable candidate.

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

`npx skills add josuamittels/agent-stack --skill ask-user-question think-harder translate write -a codex`

Bundled dependencies: ask-user-question, think-harder, write.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## update-changelog

Status: eligible experimental candidate.

Create, update, or prepare a repository changelog from verified changes. Use when the user asks to record changes, maintain CHANGELOG.md, or prepare a changelog release section.

`npx skills add josuamittels/agent-stack --skill ask-user-question think-harder update-changelog -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.

## write

Status: eligible stable candidate.

Write, edit, and translate any prose people will read, including product interfaces, websites, documentation, articles, and messages. Apply when producing human-facing text, including within implementation tasks, to preserve meaning, fit the intended voice and audience, and remove formulaic AI phrasing.

`npx skills add josuamittels/agent-stack --skill ask-user-question think-harder write -a codex`

Bundled dependencies: ask-user-question, think-harder.

Requirements: Node.js >=22.20 for JavaScript helpers when present; Python >=3.10 for Python helpers when present.
