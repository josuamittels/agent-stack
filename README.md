# Agent Stack

Reusable agent skills for career applications, research, writing, design reviews, decisions, and development. Each skill provides a focused workflow with its required instructions, templates, and resources bundled.

[Documentation](https://agents.mittels.org) · [Installation guide](https://agents.mittels.org/installation/) · [Skill catalog](https://agents.mittels.org/capabilities/)

## Install

Agent Stack includes experimental and stable skills and guides. Drafts are excluded from shipping. Install all available skills from GitHub:

```sh
# Codex
npx skills add josuamittels/agent-stack --skill '*' -a codex

# Claude Code
npx skills add josuamittels/agent-stack --skill '*' -a claude-code
```

Run these commands from your project folder. Choose the command for Codex or Claude Code. Add `-g` for user-wide installation. See [distribution and installation](docs/distribution.md) for other hosts, plugins, updates, and external tool requirements.

After installation, use [/setup-agent-stack](src/skills/setup-agent-stack/SKILL.md.tmpl) to enable automatic routing in your global instructions. Invoke it as `$setup-agent-stack` in Codex or `/setup-agent-stack` in Claude Code, then start a new session. Your agent selects relevant skills through [/skill-issue](src/skills/skill-issue/SKILL.md.tmpl). Project installs apply where those skills are available; use `-g` to make them available across projects.

## Career

Create convincing CVs, authentic, personal cover letters, and application answers tailored to specific jobs and grounded in your actual experience. Keep your career information and application materials in one place, so each new application builds on a consistent, accurate account of what you offer.

1. **Set up your workspace**. Ask your agent to use [/setup-career-stack](src/skills/setup-career-stack/SKILL.md.tmpl) in a fresh project folder.
2. **Build your profile**. Share your career materials and target roles to establish your career profile and generate reusable CVs.
3. **Tailor each application**. Provide a job description to tailor your CV with [/create-cv](src/skills/create-cv/SKILL.md.tmpl), draft a cover letter with [/draft-cover-letter](src/skills/draft-cover-letter/SKILL.md.tmpl), and prepare application form answers with [/answer-interview](src/skills/answer-interview/SKILL.md.tmpl).

```sh
# Codex
npx skills add josuamittels/agent-stack --skill setup-career-stack compose-career-profile create-cv draft-cover-letter answer-interview -a codex

# Claude Code
npx skills add josuamittels/agent-stack --skill setup-career-stack compose-career-profile create-cv draft-cover-letter answer-interview -a claude-code
```

## Research

Get a clear, evidence-backed answer to a question, with sources you can inspect and limitations you can assess. Use the research workflow for a report or literature review, or [/research-literature](src/skills/research-literature/SKILL.md.tmpl) to find relevant scholarly sources.

1. **Frame the question**. Ask your agent to use [/research](src/skills/research/SKILL.md.tmpl), sharing your question and any starting sources.
2. **Set the scope**. Choose quick, normal, or deep research and your preferred output format.
3. **Review the evidence**. Read the synthesis alongside its sources, uncertainties, and evidence gaps.

```sh
# Codex
npx skills add josuamittels/agent-stack --skill research research-literature -a codex

# Claude Code
npx skills add josuamittels/agent-stack --skill research research-literature -a claude-code
```

## Writing

Make your writing clear, natural, and suited to its audience while preserving your meaning and voice. Develop a consistent style across your work, or adapt existing text for another language and readership.

1. **Share the context**. Provide a brief or draft, the intended audience, and the language.
2. **Choose the task**. Ask for [/write](src/skills/write/SKILL.md.tmpl), [/translate](src/skills/translate/SKILL.md.tmpl), or [/compose-voice-profile](src/skills/compose-voice-profile/SKILL.md.tmpl).
3. **Refine the result**. Give feedback on the wording and tone, or use [/quit-the-yap](src/skills/quit-the-yap/SKILL.md.tmpl) for concise chat answers.

```sh
# Codex
npx skills add josuamittels/agent-stack --skill write translate compose-voice-profile quit-the-yap -a codex

# Claude Code
npx skills add josuamittels/agent-stack --skill write translate compose-voice-profile quit-the-yap -a claude-code
```

## Thinking and decisions

Work through uncertainty, challenge assumptions, and find options you may have overlooked. These methods help you sharpen an approach or identify weaknesses in a plan before committing time and resources.

1. **Describe the decision**. Share the task or plan, its constraints, and what remains uncertain.
2. **Sharpen the approach**. Use [/think-harder](src/skills/think-harder/SKILL.md.tmpl) to resolve ambiguity or [/think-deeper](src/skills/think-deeper/SKILL.md.tmpl) to strengthen methods and evidence.
3. **Explore and challenge**. Use [/mind-wandering](src/skills/mind-wandering/SKILL.md.tmpl) for fresh angles or [/pre-mortem](src/skills/pre-mortem/SKILL.md.tmpl) to examine possible failures.

```sh
# Codex
npx skills add josuamittels/agent-stack --skill think-harder think-deeper mind-wandering pre-mortem ask-user-question -a codex

# Claude Code
npx skills add josuamittels/agent-stack --skill think-harder think-deeper mind-wandering pre-mortem ask-user-question -a claude-code
```

## Design reviews

Review a supplied design through its aesthetics, the user jobs it supports, and accessibility. Each audit preserves evidence limits and returns concrete next actions.

1. **Choose the scope.** Use [/audit-accessibility](src/skills/audit-accessibility/SKILL.md.tmpl) for access standards, [/audit-ux](src/skills/audit-ux/SKILL.md.tmpl) for user needs and task usability, or [/audit-design](src/skills/audit-design/SKILL.md.tmpl) for the coordinated review with deeper aesthetics.
2. **Share the artifact and context.** Provide the design/interface and known audience, jobs, constraints and intended character. The workflow asks about consequential missing context.
3. **Use the reports.** UX includes accessibility; Design adds its aesthetic critique. Review the linked reports and integrated action plan, with repairs, refinements and optional explorations kept distinct.

```sh
# Codex
npx skills add josuamittels/agent-stack --skill audit-design audit-ux audit-accessibility -a codex

# Claude Code
npx skills add josuamittels/agent-stack --skill audit-design audit-ux audit-accessibility -a claude-code
```

## Colour

Get colour values in the format your project needs and assess whether text has enough contrast against its background. Use the results to make informed colour choices for digital and print work.

1. **Convert a value**. Give [/convert-colour](src/skills/convert-colour/SKILL.md.tmpl) a colour value and the target format.
2. **Check a pair**. Give [/check-colour-contrast](src/skills/check-colour-contrast/SKILL.md.tmpl) foreground and background colours to assess them against accessibility thresholds.

```sh
# Codex
npx skills add josuamittels/agent-stack --skill convert-colour check-colour-contrast -a codex

# Claude Code
npx skills add josuamittels/agent-stack --skill convert-colour check-colour-contrast -a claude-code
```

## Reusable workflows

Make useful project knowledge and proven ways of working easier to share and repeat. Capture them as documentation, standards, or agent skills, with checks and decision records where they help maintain quality.

1. **Choose what to capture**. Share the repository, process, or standards you want to make reusable.
2. **Create the resource**. Ask for [/create-docs](src/skills/create-docs/SKILL.md.tmpl), [/create-guidelines](src/skills/create-guidelines/SKILL.md.tmpl), or [/create-skill](src/skills/create-skill/SKILL.md.tmpl).
3. **Support future use**. Use [/spawn-evals](src/skills/spawn-evals/SKILL.md.tmpl) for script-verifiable skill checks or [/show-me-your-work](src/skills/show-me-your-work/SKILL.md.tmpl) to keep a decision log.

```sh
# Codex
npx skills add josuamittels/agent-stack --skill create-docs create-guidelines create-skill spawn-evals show-me-your-work -a codex

# Claude Code
npx skills add josuamittels/agent-stack --skill create-docs create-guidelines create-skill spawn-evals show-me-your-work -a claude-code
```

## Discovery and delivery

Find a suitable skill for the work at hand and deliver repository changes through an established release process. Keep changes documented and follow the project's own Git and release rules.

1. **Find a capability**. Use [/skill-issue](src/skills/skill-issue/SKILL.md.tmpl) to select a stack capability or [/browse-skills](src/skills/browse-skills/SKILL.md.tmpl) to inspect public examples.
2. **Record the changes**. Use [/update-changelog](src/skills/update-changelog/SKILL.md.tmpl) to document what changed.
3. **Deliver the work**. Ask for [/ship](src/skills/ship/SKILL.md.tmpl) when ready to commit, open a pull request, or release under the repository's rules.

```sh
# Codex
npx skills add josuamittels/agent-stack --skill setup-agent-stack skill-issue browse-skills update-changelog ship -a codex

# Claude Code
npx skills add josuamittels/agent-stack --skill setup-agent-stack skill-issue browse-skills update-changelog ship -a claude-code
```

## Reference

[Documentation](https://agents.mittels.org) · [Stack map](map.mmd) · [Skill catalog](src/catalog.yaml) · [Distribution and maintenance](docs/distribution.md) · [MIT license](LICENSE)
