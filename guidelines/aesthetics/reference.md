---
name: aesthetics-framework
description: "Shared design-reference framework: domain ownership, selective reading paths, decision priorities, and evidence for AI-assisted design across interfaces and other media."
version: "0.1.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references: []
type: reference
status: experimental
---

# Aesthetics framework

Use these references to make informed design decisions. Each guide owns one domain; together they explain how behavior, form, perception, and delivery support an experience. They provide judgment and constraints rather than a mandatory visual style or a workflow for executing every project.

## Choose the reference by the decision

| Reference | Owns | Consult when |
| --- | --- | --- |
| [Interaction](interaction.md) | Task and object models, control choice, state transitions, focus lifecycle, navigation, commitment, recovery, and feedback events | Deciding what a person can do and what the system promises in response. |
| [Composition](composition.md) | Spatial hierarchy, grouping, balance, negative space, density, grids, layout adaptation, and spatial stability | Deciding where things belong and how their relationships survive different formats. |
| [Typography](typography.md) | Letterforms, font selection and engineering, text composition, typographic roles, shaping, and font delivery | Deciding how language looks, reads, wraps, and renders. |
| [Colour](colour.md) | Colour perception, vocabulary, spaces, mixing, palettes, themes, data scales, colour calculation, and reproduction | Deciding how colour relationships communicate and survive delivery. |
| [Iconography](iconography.md) | Symbol meaning, metaphor, family grammar, vector construction, optical correction, variants, and asset delivery | Selecting, drawing, extending, or applying symbols. |
| [Motion](motion.md) | Temporal composition, timing, easing, springs, trajectories, choreography, animated transitions, and animation lifecycle | Deciding how a change develops through time. |
| [Sound](sound.md) | Auditory perception, acoustic character, musical structure, synthesis, mixing, sonic vocabulary, and playback | Designing an audible experience or deciding whether sound contributes enough to use. |
| [Haptics](haptics.md) | Tactile perception, contact, materials, force, vibration, tactile vocabulary, and physical delivery | Designing actual touch or feedback on supported hardware. |
| [Accessibility](accessibility.md) | Access requirements, conformance and legal scoping, semantics, assistive technology, equivalent access, and accessibility evaluation | Establishing constraints and verifying that the whole task remains available. |

The owner contains the explanation, conditions, exceptions, and detailed examples. Another guide links to it at the relevant decision. Domain-specific consequences stay with their domain: typography explains why glyphs collide; composition explains why a container clips; accessibility defines the adaptation requirement. This division prevents competing versions of the same rule.

## Read selectively and follow dependencies

Start with the task, medium, existing system, and unresolved decisions. Read the selected guide's **Use this reference** section, then the relevant sections. When a passage delegates a decision to another guide, read that destination before making the decision. A link identifies a dependency; it does not mean the dependency has been applied. Follow dependencies for the current decision and reuse already loaded guidance. Load additional material when the work exposes a need, rather than loading the entire collection by default.

For UI work:

- Establish behavior and access constraints with Interaction and the applicable Accessibility sections. Use Composition to arrange the task.
- Consult Typography, Colour, and Iconography for the visual decisions the interface actually needs. Applying an existing system usually needs its role and application guidance, not instructions for creating a font or icon library.
- Consult Motion for authored animation. Consult Sound and Haptics only when those channels serve the experience and the delivery platform supports them. Additional sensory effects are optional design choices.
- Return to the relevant implementation, handoff, and verification sections before claiming the result is ready.

For a publication, identity, soundtrack, physical object, or spatial experience, follow the medium-specific paths within the guides. Their specialist depth remains available without becoming a prerequisite for an ordinary UI. The nested [Apple platform references](references/apple-human-interface-guidelines/fundamentals/design-principles.md) supplement these guides for Apple work; inspect the relevant platform and verify changing SDK or platform specifications before relying on them.

## Resolve decisions in context

Establish what people need to understand, feel, compare, or accomplish. Identify real content, recurring use, difficult states, supported languages, devices, environments, and delivery limits. Reuse this context across domains; extend it with domain-specific questions rather than producing a separate generic brief for every guide.

Meet applicable requirements and preserve truthful information, task integrity, and informed choice. Within those constraints, preserve the established product, brand, and platform conventions unless the brief authorizes a change. Choose expressive properties that support the intended experience. Use a guide's defaults where the context leaves a decision open; adjust them when a concrete condition makes another choice better.

**Requirements** are obligations within their stated scope. Accessibility identifies standards and legal obligations separately from stronger product conventions. **Defaults** are preferred starting points with room for a justified alternative. Numerical aesthetic ranges and examples are trials, not universal thresholds. An example's units, script, hardware, output conditions, and prerequisites are part of its meaning.

Translate an aesthetic intention into observable choices. “Precise” might mean aligned comparison fields, restrained scale differences, compact spacing, stable symbols, and immediate feedback. “Playful” might mean an unusual silhouette, an expressive type role, or one elastic transition. Choose a few coordinated mechanisms, explain their purpose, and compare them in the actual task. Adjectives alone do not specify a design, and using every available mechanism weakens emphasis.

When domains compete, name the conflict and change the smallest relevant decision. A brand accent that cannot support a label can remain in non-text roles while a functional colour serves the label. A motion concept that obscures a state needs a different transition. A layout that cannot accommodate the required language needs recomposition. Do not resolve a conflict by quietly dropping information, access, or the intended character.

## Coordinate domains without duplicating their rules

Interaction defines the event, state, consequence, and recovery. Composition allocates space. The visual and sensory guides define how that event is expressed. Accessibility constrains and verifies the resulting routes to information and action. For example, a save contract determines when “saved” is true; an animation, chime, or tactile cue expresses that event without redefining it.

Use a small shared vocabulary of values, semantic roles, and component applications where it helps the product. Keep each domain's meaningful parameters and exceptions in its guide. A feature specification references those contracts and records only its additions or differences. Do not create token layers, variants, or sensory vocabularies that have no recurring use.

## Match evidence to the claim

Inspect the result in the form people receive: a working interface, rendered type, exported asset, decoded audio, physical sample, or actual haptic device. Compare the candidate with a simpler alternative when the benefit is uncertain. Use the domain's diagnostic guidance to identify the mechanism before changing arbitrary values.

Distinguish what was proposed, implemented, rendered, measured, perceived, and tested with intended users. Code inspection does not establish usability; a screenshot does not establish interaction; a waveform does not establish a sound's emotional effect; an API call does not establish a tactile experience. Report unavailable evidence and remaining uncertainty without claiming it was verified.

Review complete tasks and relevant failure conditions alongside aesthetic character. Keep domain-specific checks in the owning guide and combine the results in one project review. Readiness means the agreed design works under its stated conditions, with a clear account of what still needs validation.
