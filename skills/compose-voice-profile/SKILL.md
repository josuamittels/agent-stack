---
name: "compose-voice-profile"
description: "Compose a detailed, evidence-backed brand or author voice profile from user direction, research, guides, writing samples, visual references, and market context. Use when the user wants a reusable voice profile or tone-of-voice guide."
version: "0.1.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Affaan Mustafa"
  - "Lauren Pope"
  - "Ankit Vora"
  - "Anthropic"
  - "Samber"
  - "WoopSocial"
  - "UK Home Office"
  - "UK Department for Business, Innovation, Science and Trade"
type: "skill"
status: "experimental"
---

# Compose Voice Profile

Compose a detailed, reusable voice profile that fits the brand, its audience, product, market, language, and intended use. Base it on the inputs and sources available for the task, then return it in the structure of [`templates/voice-profile.md`](templates/voice-profile.md).

## Scope

Use when the user wants to create or substantially redefine a brand's or author's writing voice, tone, or style guide from a brief and related evidence. The user may provide audience research, product or positioning information, market context, audience preferences, geography, language, topics, existing brand guides, visuals, writing samples, examples, or direct instructions. Use the available inputs together; do not require every input category.

This skill composes the profile. It does not write a campaign, publish copy, run a full market research project, or replace a visual identity guide. For a separately requested source-grounded research report, use [Research](../research/SKILL.md) and then continue with its findings. Do not treat that report workflow as a substitute for broad market research. For requested copy, use the writing or content skill that owns that deliverable and pass the completed profile along.

### Boundaries

- Do not invent product facts, audience preferences, market conditions, cultural norms, brand values, or examples.
- Distinguish what the brand currently does from the voice the user wants it to adopt.
- Treat visual references as context, not direct evidence of verbal style or audience demographics. Label interpretations and seek corroboration in the brief, brand guide, or audience evidence.
- Do not adopt ECC defaults, another brand's distinctive traits, or a general style framework as this brand's voice without support from the user or evidence.
- Preserve legal, safety, accessibility, and product-claim limits supplied by the user or authoritative brand materials. Flag conflicts; do not quietly remove a constraint.
- Read the template as input. Never overwrite `templates/voice-profile.md` when producing a profile.

## Inputs

Use the user's stated goal and any available details about:

- **Brand or author:** identity, purpose, values, positioning, personality, and existing brand guidance.
- **Product and topic:** offer, differentiators, claims, use cases, and subject matter to cover.
- **Audience:** user research, audience preferences, needs, expertise, objections, and feedback.
- **Market:** category conventions, competitors, alternatives, and credible research about points of difference.
- **Place and language:** country or region, target language, locale, cultural context, spelling, terminology, and market variants.
- **Expression:** channels, visual identity or references, current writing samples, admired examples, and explicit do/don't instructions.
- **Deliverable:** profile purpose, intended users, output language, requested depth, and file destination if specified.

These inputs are optional. Use materials the user supplies or clearly identifies as relevant. Do not scan unrelated private files, collect more examples by default, or conduct broad market research unless the user asks for it. When a referenced source is unavailable, record that limit and proceed with the remaining evidence when possible.

Read [`templates/voice-profile.md`](templates/voice-profile.md) before drafting; it supplies the required headings, tables, fields, and front matter. If local copies of ECC’s brand-voice skill and voice-profile schema are available in `sources/ECC/`, use their evidence-led extraction and conflict-reporting methods when analyzing writing samples or current voice. Those source copies may be absent; in that case, apply the evidence inventory, sample analysis, and conflict checks in this skill directly. Do not claim to have consulted unavailable materials, and do not import ECC-specific defaults or hard bans as universal rules.

Before composing the profile, read the language guideline for the requested output language when available. Start with [English](../../guidelines/languages/english.md), [Dutch](../../guidelines/languages/dutch.md), [German](../../guidelines/languages/german.md), or [French](../../guidelines/languages/french.md). Keep the template's section headings in their original order and fill its content in the requested language unless the user asks to localize the headings too. When no matching guideline exists, use English guidance for transferable writing principles and preserve the requested language.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Establish the profile contract

Identify the brand or author, what the profile should enable, its audience, requested language and locale, desired direction (current, aspirational, or both), and output destination. Recover details from the request and supplied materials first.

Ask a concise question only when a missing decision could materially change the profile or make it misleading. Otherwise proceed with a clearly labeled assumption, set confidence appropriately, and record the gap under **Evidence and Open Questions**.

### 2. Read the template and inventory evidence

Read the current [`templates/voice-profile.md`](templates/voice-profile.md). Preserve its complete heading order, front matter, and table structure in the completed profile. Use **Profile Details** to record the profile's purpose, product or offer, market, geography, language/locale, channels, source set, and confidence when those details apply.

Create a working source inventory. For each relevant input, note its type, origin, date or freshness, market/language/channel, and what it can establish. Classify evidence as:

1. Direct user instruction or preference.
2. Current approved brand or product guidance.
3. Observed writing from the brand or author.
4. Audience research, feedback, or preference evidence.
5. Market, category, competitor, or performance evidence.
6. Visual reference or design cue.
7. External voice framework or example.

Use source material in the workspace only when the user supplied it or clearly identified it as relevant. Read linked pages the user named when browsing is available. Verify current or decision-relevant market claims with suitable sources when the user requests fresh research; otherwise use provided research and identify its date and limits.

### 3. Analyze the inputs without conflating them

For real writing samples, identify patterns that recur across representative examples. Examine rhythm, compression, capitalization, parentheticals, questions, claims, transitions, vocabulary, preferred moves, and patterns to avoid, using ECC’s workflow when its local source is available. Note sample date, channel, authorship, and whether it represents the voice the user wants.

For strategy and research inputs, identify the product promise, audience needs, preferred language, market conventions, and meaningful points of distinction. Treat audience preferences as evidence only for the population and context actually studied. Treat performance metrics as signals; do not claim a writing choice caused results without evidence.

For visuals, describe observable elements such as color, typography, imagery, composition, and overall energy. Translate them into verbal direction only as a labeled interpretation, and corroborate that direction with explicit positioning, user intent, or audience evidence. Do not infer demographics, values, or personality solely from visual style.

Separate **observed current voice** from **intended voice direction**. If an approved guide conflicts with current examples, describe the guide as intended policy and examples as observed practice. Follow the user's stated goal for the profile, make the difference explicit, and preserve unresolved conflicts in the template.

### 4. Synthesize with Think Deeper

Invoke [Think Deeper](../think-deeper/SKILL.md) before drafting. Pass:

- The requested outcome and exact template path.
- The source inventory and provenance labels.
- The user's direct instructions and priority constraints.
- Product, audience, market, location, language, and channel facts.
- Writing-pattern observations and visual cues, with uncertainty labels.
- Conflicts, missing evidence, and current-versus-intended voice distinction.

Ask Think Deeper to reconcile authenticity, audience fit, distinctiveness, readability, product promise, market context, and language/locale needs. Request concrete writing behaviors, situation-specific tone shifts, evidence links, assumptions, conflicts, and unresolved questions. Carry those findings into the profile; do not treat the handoff as a second deliverable or claim it ran if it was unavailable.

### 5. Compose the profile in the template

Fill every section in the current template. Replace metadata placeholders with supported details; use `Not supplied`, `Not in scope`, or an empty list where the template requires a value that the sources cannot establish. Do not leave instructional square-bracket prompts in the completed profile.

Make the profile specific enough to guide a writer:

- Define personality as stable traits grounded in purpose, user direction, or recurring evidence.
- Describe tone as a response to context, audience, or purpose; state what to turn up or down.
- Explain rhythm, structure, compression, vocabulary, terminology, claims, mechanics, and calls to action as observable choices.
- Give channel guidance only for channels supported by the brief or sources.
- Translate traits into practical do/avoid rules and examples. Identify constructed examples as such; never present them as source quotations.
- Cite or name the source behind important observations in the profile. Keep user instructions, observations, research findings, and inferences distinguishable.
- For multiple audiences, countries, or languages, document material differences separately instead of forcing them into one average voice.

Keep the requested depth high through evidence and useful distinctions, not repetition. Do not fill a section with generic advice just to make it look complete.

### 6. Review and return

Review the draft against the template and the original request:

- Every template section and table appears in the same order, unless the user explicitly requested a different format.
- The profile distinguishes stable voice from changing tone and current practice from intended direction.
- Key recommendations are concrete, relevant to the audience and product, and traceable to a source or explicitly marked as proposals.
- No unsupported claims, stereotypes, fabricated preferences, or visual-to-verbal leaps remain.
- Uncertainty, conflicts, source limitations, and open questions are visible.
- The requested language and locale are respected.
- No template prompts or unresolved placeholders remain.

Apply [Natural Writing](../natural-writing/SKILL.md) to the profile's prose while keeping this skill responsible for the analysis and template structure. For the objective evaluator, include the complete output and the absolute path to the template in `evidence.template_path`. If the profile is returned only in the conversation, write a temporary UTF-8 copy for the evaluator and remove that temporary file after the check.

Return the completed Markdown in the conversation unless the user requested a file. If they specify a path, create the completed profile there without modifying the source template. Summarize the source basis and any material limits briefly outside the profile.

### 7. Validate implementation

When invoked as a helper, return to the owning workflow without separate evaluation. For a skill with meaningful, deterministic, task-specific checks, invoke [Spawn Evals](../spawn-evals/SKILL.md) once with a structured invocation record containing the original request, resolved constraints and their source, complete UTF-8 outputs, and machine-readable evidence. Its objective package in `evals/compose-voice-profile/` defines only those checks. Report PASS, FAIL, or NOT PASSED — UNVERIFIED with the failing or unavailable verification steps. Do not use model judges, sub-agents, qualitative assessments, weighted scores, or synthetic scenarios. If no package exists for an objectively checkable skill, report NOT PASSED — UNVERIFIED; do not create one during an ordinary skill invocation. If no meaningful objective check is possible for this skill, omit this entire validation section and all Spawn Evals references from the skill.

## Output

Return a completed Markdown voice profile based on [`templates/voice-profile.md`](templates/voice-profile.md), with its template sections filled, metadata resolved, source evidence identified, and unknowns or conflicts labeled. Use the requested output path when supplied; otherwise provide the complete profile in the response. Include a short note on the sources used, the current-versus-intended voice basis, and material confidence limits. Do not return only analysis, a list of adjectives, or an empty scaffold.

## References

- Optional local reference: ECC’s brand-voice skill and voice-profile schema under `sources/ECC/`, when present in the working repository.
- Lauren Pope, [“The anatomy of a brilliant brand voice”](https://la-pope.medium.com/the-anatomy-of-a-brilliant-brand-voice-31cfd1d9b835): personality, tone, rhythm, vocabulary, audience fit, and readable guidance.
- Ankit Vora, [“Brand Voice: What It Is and How to Define It (+ Template)”](https://www.semrush.com/blog/brand-voice/): audience research, current-asset review, and actionable voice charts.
- UK Home Office, [“Voice and tone”](https://design.homeoffice.gov.uk/design-and-content/content/voice-and-tone): stable voice and context-specific tone expressed as practical behavior.
- Department for Business, Innovation, Science and Trade, [“Creating your business brand”](https://www.business.gov.uk/support/ideas-planning-strategy/creating-business-brand/): customer, competition, location, behavior, language, and visual identity as brand context.
