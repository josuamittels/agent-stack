# Changelog

Notable changes to Agent Stack are recorded here. Versions follow the coordinated stack revisions in [VERSIONS.md](VERSIONS.md); dates are the dates those versions were recorded.

## [0.17.2] - 2026-10-27

### Fixed

- Remove the stale Layout placeholder from the map after its scaffold was deleted.

## [0.17.1] - 2026-10-27

### Changed

- Move the Wireframes reference to `guidelines/wireframes/reference.md`.

## [0.17.0] - 2026-10-27

### Added

- Add a startup playbook outline from idea through market research, strategy, design system, and voice profile.

## [0.16.1] - 2026-10-27

### Fixed

- Mark the optional Creative Moves reference as a dotted, non-directional map link.

## [0.16.0] - 2026-10-27

### Added

- Add substantive composition, wireframe, haptics, and motion references with supporting composition diagrams.

### Changed

- Refresh the map to show the completed aesthetic references and remove the empty Interface placeholder.

## [0.15.0] - 2026-10-27

### Changed

- Require each non-empty Agent Stack commit to include its own sequential stack version increment and component inventory snapshot.

## [0.14.0] - 2026-10-27

### Added

- Add Show Me Your Work, a discipline for evidence-linked decision logs and handoffs.

### Changed

- **Breaking:** Move disciplines under `skills/<name>/` while preserving `type: discipline`, and move each authoring template beside the skill that uses it. Update references that use the former paths.
- Restructure the stack map and discovery catalog to show the new capability layout, grouped relationships, and planned resources distinctly.
- Ship now separates independently reviewable themes into ordered commits and puts shared release metadata in a final record commit.

## [0.13.0] - 2026-10-27

### Added

- Add a draft sound design guide covering hearing, emotion, musical structure, sound construction, production, and product audio.

## [0.12.0] - 2026-10-27

### Changed

- Promote `convert-colour` and `check-colour-contrast` to stable `1.0.0` disciplines after conversion and contrast results matched their verification references.

## [0.11.0] - 2026-10-27

### Added

- Add `convert-colour`, a standalone mathematical converter for HEX, RGB, HSL, HSV, CMYK, Lab, LCh, and Display P3 values.
- Add `check-colour-contrast`, a standalone RGB/HEX/HSL contrast calculator with WCAG 2.2 AA and AAA guidance for normal and large text and non-text interface components.

## [0.10.0] - 2026-10-27

### Added

- Add comprehensive colour guidance covering perception, history, language and culture, descriptive vocabulary, colour theory, formats and conversion, composition, palettes, meaning and psychology, accessibility, interface systems, data visualisation, and colour-managed production, with worked examples and troubleshooting.

## [0.9.0] - 2026-10-27

### Added

- Add comprehensive accessibility guidance covering disability and assistive technology, EU legal obligations, visual and interaction design, content and media, documents, native platforms, design systems, testing, procurement, and governance, with worked examples and all 55 WCAG 2.2 Level A and AA criteria.

## [0.8.0] - 2026-10-27

### Added

- Add comprehensive iconography guidance covering metaphors, icon and family construction, optical correction, composition, accessible application, localization, semantic systems, implementation, production, testing, and governance, with a vector construction plate and runnable web examples.

## [0.7.0] - 2026-10-27

### Added

- Add comprehensive typography guidance covering letter construction, optical correction, spacing, font families, composition, semantic systems, accessible implementation, multilingual use, and production.

## [0.6.0] - 2026-10-27

### Added

- Add a local Markdown collection of Apple Human Interface Guidelines articles, organized by topic with links between included pages.

## [0.5.0] - 2026-10-27

### Added

- Establish a root changelog that records notable changes in versioned sections.

### Changed

- Route every Ship request through Update Changelog to assess verified changes and record only notable user-facing outcomes.

## [0.4.1] - 2026-10-27

### Changed

- Expand Mind Wandering with research notes on attention, incubation, analogy, prompts, and evaluating creative work, with evidence limits made explicit.

## [0.4.0] - 2026-10-27

### Added

- Add Mind Wandering, a structured creative exploration discipline for loosening familiar approaches, trying new representations, and returning to develop useful possibilities.

## [0.3.0] - 2026-10-27

### Added

- Add Compose Voice Profile, a workflow for building reusable brand or author voice profiles from user direction and supporting evidence.

## [0.2.0] - 2026-10-26

### Added

- Provide reusable workflows for natural writing, translation, skill authoring, academic research, source inspection, and portable shipping.
- Add shared disciplines for clarification, decision-making, pre-mortems, changelog maintenance, resource-map upkeep, research-literature discovery, and objective skill checks.
- Establish English, Dutch, French, and German writing guidance, coding references, Git practices, Mermaid conventions, changelog standards, and versioning guidance.
- Add the stack map, routing catalog, reusable templates, and lifecycle inventory that help maintainers discover and coordinate the stack's capabilities.
