---
name: "wireframes"
description: "Reference for creating, comparing, presenting, and exporting rough grayscale interface wireframes at a declared screen size. Use for early interface variants and structural design exploration."
version: "0.1.0"
created: "2026-10-27"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Mike Angeles"
  - "Billy Carlson"
  - "Yale Usability & Digital Accessibility"
type: "reference"
status: "experimental"
---

# Wireframes

Wireframes communicate an interface's structure and direction through rough skeleton blocks. They make placement, hierarchy, contrast, density, and the main action visible while leaving final styling and content open. Aim for a minimalist, aesthetic composition that remains quick to change.

Use this reference for individual screens, interface variants, and short flows on mobile, tablet, desktop, or another declared rectangular format. The consuming skill owns the brief, number of alternatives, selection process, and later implementation. Use [Composition](../aesthetics/composition.md) for broader spatial principles and [Accessibility](../aesthetics/accessibility.md) for access requirements.

**Include a detail when it helps someone understand or compare the concept. Abstract it when it only specifies the final design.** Grayscale alone does not make a detailed mockup low fidelity.

## Establish the minimum brief

Recover these inputs from the request and available context:

| Input | What is needed |
| --- | --- |
| Purpose | What the person should understand or accomplish on this screen |
| Essential content | The regions, controls, and information needed to communicate that purpose |
| Format | Logical width × height, orientation, platform if known, and viewport or full-page scope |
| Exploration | What is fixed and which structural decisions may vary |

Do not require final copy, brand assets, exact data, or a complete product specification. Infer reversible details and record consequential assumptions briefly outside the screen. Ask only when a missing decision prevents a useful comparison. If dimensions are unspecified, choose a plausible format for the stated platform and disclose the exact dimensions; do not silently mix sizes.

For example: “Compare search-first and category-first product discovery at 390 × 844. Preserve search, categories, results, and basket access. Product names and counts are illustrative.” This is enough to begin.

## Set the detail level

Show major regions, their relative size and placement, reading order, grouping, navigation, primary action, and any component that defines the idea. Include representative supporting detail so the screen has believable density.

| Element | Default representation | Add detail when |
| --- | --- | --- |
| Heading | One or two thicker bars | A short heading is needed to identify the task |
| Supporting copy | A small group of thinner bars with plausible line lengths | Meaning changes the layout decision |
| Navigation or action | Recognizable control with a short functional label | Its destination or consequence would otherwise be unclear |
| Image or illustration | Flat rectangle, circle, or simple silhouette at the intended proportion | The graphic's structure is central to the concept |
| Chart | A few lines, bars, or segments | Comparison, scale, or chart reading is being evaluated |
| Repeated content | Enough representative rows or cards to reveal rhythm and density | A longer list or edge case changes the structure |

Use semantic labels such as “Search,” “Filters,” and “Continue” where they resolve ambiguity. Use bars for subordinate prose. Avoid lorem ipsum paragraphs and invented final marketing copy. Bar lengths should suggest plausible content rather than form an ornamental pattern.

Keep numbers and chart shapes illustrative unless supplied by the brief. Do not imply verified business results. If exact copy or data is necessary to judge the concept, include it locally and explain why that region has more detail.

Stop when a reviewer can identify the screen's purpose, dominant region, main action, and distinguishing idea without a long explanation. Do not add complete settings, exhaustive states, detailed illustrations, or production behavior to make the wireframe feel finished.

## Use a restrained visual vocabulary

Default to white and neutral grays, flat fills, simple geometry, and one plain sans-serif font for necessary labels. Use relative darkness, scale, and placement to establish emphasis. Avoid gradients, brand styling, decorative shadows, detailed icons, and stock images.

A practical starting palette is white for the screen, `#f2f2f2` for supporting surfaces, `#dedede` for placeholder regions, `#aaa` for supporting marks, and `#555` for emphasis. These are adjustable house defaults, not required values or proof of accessible contrast. Use a sufficiently dark tone for readable labels; do not treat visible text like a pale placeholder bar.

Keep tone meanings consistent across a comparison. Reserve the strongest emphasis for the main action or concept-defining region. Distinguish selection with an outline, marker, or shape change as well as tone. Dark-interface explorations may reverse the tonal hierarchy while remaining grayscale and clearly identified.

Align related edges and use a small, consistent spacing rhythm. Make gaps within groups smaller than gaps between groups. Use whitespace to organize before adding borders. A sparse screen may need generous open space; a dense workspace needs enough visible content to show its actual character. Minimalism does not justify removing task-essential information.

Use simple, consistent corners and strokes. Device chrome is optional: a light frame usually communicates the viewport sufficiently. Add safe areas or platform chrome when they affect available space, and use the same treatment across comparable variants.

## Make components recognizable

Preserve the minimum anatomy that distinguishes each component:

- **Button:** bounded action area with a short label when the action matters; distinguish primary and secondary emphasis.
- **Field:** input boundary or surface, label if needed, and a value or placeholder cue. A bare rectangle must not be mistaken for an image.
- **Selection:** visible options and a recognizable selected marker. Preserve the difference between a single choice, multiple choices, and a range.
- **List or table:** repeated rows, shared alignment, and enough columns or metadata to reveal the scanning pattern.
- **Card:** content grouping and any relevant action. Do not put every region in a card by default.
- **Tabs or navigation:** distinct destinations and an active item when relevant. Avoid inventing navigation depth that the concept does not need.
- **Media or visualization:** plausible occupied area and only the internal structure needed to explain its role.

For a selectable plan, a name, price placeholder, two supporting bars, and a selected marker can be sufficient. A blank card cannot communicate the same decision. Conversely, a photo region usually needs only its shape and proportion.

## Preserve the target format

Declare each screen's logical dimensions in pixels. Lay out the screen at those dimensions independently of the surrounding comparison board. Treat the declared rectangle as the viewport unless the brief specifies another kind of canvas.

Keep the viewport fixed when the board becomes narrower. Wrap frames, permit board scrolling, or scale a frame uniformly; do not let the board's columns reflow the interface or distort its aspect ratio. Logical size, display scale, and export pixel scale are separate settings.

Show the initial viewport and its fold honestly. Content below it may be explained with a short outside note or an additional full-content view. Label full-content views explicitly. Do not squeeze a long page into one screen or accidentally clip essential content to obtain a cleaner composition.

Indicate sticky actions, internal scrolling, overlays, and keyboard occupation only when they affect the proposal. A static annotation or separate state is usually enough. If multiple screen sizes are requested, compose an intentional adaptation for each and label it; a smaller screenshot of the desktop layout is not a mobile variant.

## Compare meaningful variants

Hold the task, essential content, target dimensions, and abstraction level constant within a comparison. Keep common elements consistent enough that the structural differences are visible.

Vary decisions such as content order, navigation model, dominant region, grouping, density, action placement, or progressive disclosure. Changing corner radii or gray shades does not establish a new interface direction. If an alternative deliberately hides information behind an action, identify where it moves rather than silently deleting it.

Give each variant a stable ID and a short name describing its idea. Add one sentence outside the frame explaining the structural change and its relevant tradeoff. For example: “B · Search first — Prioritizes direct lookup; category browsing starts below the initial viewport.”

Separate alternative concepts from flow steps. Order steps consistently, identify branches and destinations where necessary, and label additional states. Keep comparable flow stages aligned across alternatives when practical. Avoid generating an entire product flow when one representative screen can answer the design question.

## Present the work clearly

Use a quiet neutral board with consistent gutters, aligned frame tops, and uniform display scale for screens of the same size. Keep captions, assumptions, dimensions, and flow annotations outside the interface. Use a small shared legend only when a convention is not self-evident.

The board should let a reviewer scan the alternatives and inspect each at a useful size. Provide a way to view individual screens when a large overview would make them too small. Divide large sets into labeled groups rather than delivering a single unreadable image.

Identify the work as exploratory wireframes. State the design question and invite feedback on structure, priority, or task clarity. A short caption should orient the reviewer; it should not compensate for an unintelligible screen. Describe proposed behavior as proposed, and do not imply that a static screen is a working prototype.

## Produce editable source and exports

Default to a self-contained HTML comparison board using CSS and inline SVG where useful. Keep assets local or inline, use a system font stack, and avoid external dependencies or a build step. Static rendering is sufficient; add interaction only when needed to evaluate the concept. If interaction is included, use appropriate semantic controls, keyboard operation, and visible focus.

An established vector design workflow may retain its native editable source instead. Keep one authoritative source and derive exports from it; do not maintain independently redrawn versions. Raster-only generation is a poor default for repeatable geometric wireframes because precise revision and sizing become harder.

| Deliverable | Convention |
| --- | --- |
| Editable source | HTML board by default, or the established native source with a usable review preview |
| Comparison view | Labeled overview at consistent scale; the HTML board may fulfill this role |
| Individual screens | PNG viewport exports, defaulting to 2× logical dimensions |
| Optional exports | PDF review packet, vector-native SVG, or explicitly labeled full-content PNG when useful or requested |

For a 390 × 844 viewport, a 2× PNG is 780 × 1688 pixels. Export the viewport region without board captions, gutters, or decorative outer device framing. Preserve in-viewport chrome and safe areas that formed part of the layout. Capture the declared state consistently and use an opaque background by default.

Use predictable names such as `search-v02-390x844.png` and `search-wireframes.html`. Add a state suffix when needed, such as `search-v02-filters-open-390x844.png`. Label full-content exports separately and report their actual dimensions. Include logical dimensions and raster scale in the board or delivery note; filenames alone need not encode every property.

Wait for the document and any included assets to finish rendering before capture. Inspect actual exports for missing blocks, changed dimensions, clipped controls, illegible labels, and incorrect states. For PDF, preserve grayscale backgrounds and keep each intended screen or comparison group intact; inspect the rendered pages for unwanted pagination.

If a requested export cannot be generated, provide the usable source and report the missing format explicitly. Do not describe an ungenerated or uninspected file as complete. Avoid producing optional formats merely to fill an output checklist.

## Review and hand off

Before delivery, check the source at its declared size and inspect the rendered board and required exports:

- The purpose, dominant region, main action, and distinct idea are understandable.
- Placeholders preserve plausible hierarchy and density; essential controls remain recognizable.
- Alternatives differ structurally while retaining comparable content and fidelity.
- Dimensions, safe areas, fold, overflow, and state match the declared format.
- Grayscale emphasis is consistent, necessary labels are readable, and decoration has not overtaken exploration.
- IDs and captions map unambiguously to the source and exports; the files open as delivered.

Remove details that do not support the design decision. Add only the labels or structural cues needed to fix ambiguity. Deliver links to the source and requested exports with a brief account of the explored directions, assumptions, and known limitations. A selected wireframe establishes a direction for further design; final content, responsive behavior, accessibility, and usability still require validation at the appropriate stage.
