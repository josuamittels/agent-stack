---
name: iconography
description: "Comprehensive iconography reference for metaphor selection, icon and family construction, optical correction, size and style variants, composition, accessible application, localization, semantic systems, vector implementation, production, testing, and governance."
version: "0.1.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Helena Zhang"
  - "Heiko Tietze"
  - "IBM Design Language"
  - "Adobe Spectrum"
  - "Apple"
  - "Microsoft Fluent"
  - "Google Material Design"
  - "World Wide Web Consortium"
  - "Aurora Harley"
  - "Kate Kaplan"
  - "Destina Gökoğlu"
  - "MDN contributors"
type: reference
status: experimental
---

# Iconography

An icon connects a visible form to an object, action, condition, or idea. Its usefulness depends on that connection surviving small size, surrounding content, unfamiliar users, different languages, and imperfect rendering. A beautiful outline can represent the wrong action. A familiar metaphor can disappear at its smallest size. A coherent family can become confusing when its members are applied inconsistently.

Design meaning, drawing, and application together. The family defines a visual language. The product defines where that language appears and what each sign means. The implementation preserves those decisions through interaction, accessibility, theming, localization, and delivery.

Use this reference to create an individual icon, build or extend a family, select a library, compose icons with content, and maintain a production system. Construction guidance concentrates on functional vector icons. Larger pictograms, app identities, dimensional artwork, signage, print, and motion have different constraints, covered where those differences change a decision.

**Requirements** protect meaning, access, technical correctness, and applicable platform contracts. **Defaults** provide a starting point. Numerical aesthetic values are examples to test with the actual family, medium, audience, and size. When extending an established family, its documented grammar takes precedence over this guide's starter values.

## Contents

1. [Define the job and scope](#1-define-the-job-and-scope)
2. [Understand the parts and measurements](#2-understand-the-parts-and-measurements)
3. [Choose meanings and metaphors](#3-choose-meanings-and-metaphors)
4. [Select, extend, or create a family](#4-select-extend-or-create-a-family)
5. [Define the visual grammar](#5-define-the-visual-grammar)
6. [Build the grid and keyshapes](#6-build-the-grid-and-keyshapes)
7. [Construct strokes, corners, and joins](#7-construct-strokes-corners-and-joins)
8. [Draw curves, silhouettes, and negative space](#8-draw-curves-silhouettes-and-negative-space)
9. [Correct geometry optically](#9-correct-geometry-optically)
10. [Control pixels and rasterization](#10-control-pixels-and-rasterization)
11. [Design sizes, weights, grades, and styles](#11-design-sizes-weights-grades-and-styles)
12. [Construct recurring icon forms](#12-construct-recurring-icon-forms)
13. [Compose modifiers and compound icons](#13-compose-modifiers-and-compound-icons)
14. [Compose icons with text and layout](#14-compose-icons-with-text-and-layout)
15. [Design interaction and state](#15-design-interaction-and-state)
16. [Apply color, hierarchy, and themes](#16-apply-color-hierarchy-and-themes)
17. [Preserve accessibility](#17-preserve-accessibility)
18. [Localize meaning and direction](#18-localize-meaning-and-direction)
19. [Adapt to platforms and media](#19-adapt-to-platforms-and-media)
20. [Animate with purpose](#20-animate-with-purpose)
21. [Build the semantic and token system](#21-build-the-semantic-and-token-system)
22. [Engineer and deliver assets](#22-engineer-and-deliver-assets)
23. [Implement accessible web icons](#23-implement-accessible-web-icons)
24. [Govern contributions and releases](#24-govern-contributions-and-releases)
25. [Proof, test, and diagnose](#25-proof-test-and-diagnose)
26. [Use the guide in a project](#26-use-the-guide-in-a-project)

For a new family, begin with the brief and metaphor inventory, then build a varied pilot set before expanding coverage. For an extension, inspect the host family's sources and difficult examples before drawing. For product application, begin with meaning, composition, state, and accessibility. Use the diagnosis table when the visible symptom does not reveal its cause.

## 1. Define the job and scope

### Write a brief that changes decisions

Specify what people must recognize or do and under which conditions. A direction such as "clean and modern" does not establish whether a symbol needs a robust silhouette, fine internal detail, persistent text, or a platform-specific metaphor.

| Decision | Information to establish |
| --- | --- |
| Function | Action, destination, object, tool, status, category, identity, instruction, or decoration |
| Audience | Domain knowledge, prior conventions, languages, cultural context, visual and motor needs |
| Environment | Screen size, viewing distance, lighting, attention, movement, resolution, print process |
| Scale | Smallest meaningful use, usual use, largest use, supported density and zoom |
| Context | Isolated glyph, labeled control, dense toolbar, list, chart, map, sign, or promotional composition |
| Voice | Specific formal qualities that should express the brand or product |
| Coverage | Concepts, confusion pairs, modifiers, states, weights, themes, localized variants |
| Delivery | Platforms, formats, component libraries, licensing, payload, ownership, maintenance |
| Success | Correct interpretation, successful selection, distinguishability, visual fit, and technical reliability |

For example, an industrial monitoring interface needs distinguishable alarm states at a glance, stable meaning across dark and light displays, and usable controls under time pressure. A cultural venue's editorial pictograms can carry more expressive contour and local character because captions and larger sizes support interpretation. These briefs should not produce the same construction or application rules.

### Separate asset roles

| Role | Primary purpose | Design consequence |
| --- | --- | --- |
| Interface icon | Support a compact command, destination, tool, or status | Prioritize simple recognition, small-size clarity, and component integration |
| Pictogram | Explain an object, category, service, or short idea | Allow a broader silhouette and more internal structure at an appropriate size |
| Spot illustration | Add narrative or expression | Compose for its placement rather than claiming interchangeability with a toolbar icon |
| App or product icon | Identify a particular product | Develop distinctive identity and platform-specific variants |
| Logo or trademark | Identify an organization, product, or owner | Follow identity, reproduction, and permitted-use rules |
| Public information or safety sign | Communicate in a physical environment | Follow the relevant symbol, sign, color, and placement standard |

A single drawing can inspire several roles, but each delivered form needs its own proof. Shrinking a detailed pictogram into a button does not make it a functional interface icon. Placing a generic library icon inside an app mask does not establish a distinctive identity.

### Decide whether an icon earns its place

Use an icon when it aids recognition, scanning, orientation, compact interaction, or a necessary visual distinction. Prefer text for a subtle instruction, an unfamiliar abstract concept, or a choice whose consequences require explanation.

Repeated decorative icons can make a list harder to scan if every row acquires an equally prominent shape. Remove them when labels already provide the useful distinctions. A blank icon slot can be better than a weak symbol invented to complete a card template.

For an unfamiliar or consequential action, default to a visible text label. A tooltip may support learning, but people should not need to inspect every glyph to discover basic navigation.

## 2. Understand the parts and measurements

### Keep the boxes distinct

| Term | Meaning | What it controls |
| --- | --- | --- |
| Canvas or artboard | The coordinate rectangle of an asset | Export dimensions and common placement frame |
| ViewBox | The SVG user-coordinate rectangle mapped into a viewport | Scaling and coordinate interpretation |
| Live area | The usual region containing visible artwork | Family scale and breathing room |
| Painted bounds | The extent of visible fills, strokes, caps, joins, and effects | Clipping and actual visual proximity |
| Keyshape | A reference circle, square, or rectangle | Starting proportions and perceived size relationships |
| Keyline | A reference line or contour | Construction alignment and recurring positions |
| Safe area | Region essential content must occupy under cropping or masking | Survival through platform transformations |
| Clear space | External separation from unrelated elements | Recognition and grouping |
| Container | A visible circle, square, tile, or other enclosing form | Hierarchy, identity, or control affordance |
| Hit target | The area that accepts pointer or touch input | Target acquisition |
| Focus indicator | Visible evidence of keyboard focus | Location of the current control |

Keep these separate in specifications. A 24-unit canvas can contain artwork about 20 units wide and sit inside a 48 CSS-pixel button. The artboard padding is neither the button padding nor its accessible name. A visible circular container need not define the exact shape of the hit target.

### Name the anatomy

A **stroke** follows a centerline with a specified width. A **contour** bounds a filled shape. A **terminal** ends a stroke. A **cap** controls how an open stroked path ends. A **join** controls a meeting between segments. A **counter** is an enclosed negative space. An **aperture** is an open entrance into a form. A **junction** is a meeting of structural parts. A **modifier** changes or qualifies a base symbol.

A cutout is genuinely transparent negative space. A white shape painted over another shape only resembles a cutout on a white background. This distinction matters in export and theming.

### Separate coordinate units from output units

SVG coordinates have no inherent physical size. A 24-unit viewBox displayed at 24 CSS pixels maps one user unit to one CSS pixel before other transforms. Displaying it at 20 CSS pixels changes that mapping. Native points, Android density-independent pixels, CSS pixels, physical pixels, and millimeters describe different measurements.

Record the coordinate system and intended output separately. Avoid instructions such as "use a 2px stroke" when the drawing uses a 256-unit grid and the intended output is 24 CSS pixels. Specify whether the number describes source geometry or delivered appearance.

## 3. Choose meanings and metaphors

### Begin with the concept inventory

List the meanings before drawing the set. Include the actual labels, locations, neighboring concepts, and likely misunderstandings. Distinguish an action from an object and an object's condition.

| Concept | Possible drawing | Collision to resolve |
| --- | --- | --- |
| Search | Magnifying glass | Zoom, inspect, investigate |
| Settings | Gear or sliders | Filters, tuning, preferences |
| Save for later | Bookmark | Favorite, rating, save file |
| Archive | Archive box | Delete, move to folder, download |
| Share | Platform convention | Export, upload, send |
| Private | Lock | Secure connection, locked editing, permission denied |
| Refresh data | Circular arrow | Reset, sync, retry, rotate |

Choose distinctions across the entire set. A gear cannot usefully mean both global settings and an unrelated automation category in the same command group without additional differentiation. Reuse a drawing for the same meaning across the product. Allow a familiar drawing to support related meanings in clearly separate contexts, with labels that resolve the difference.

### Match the kind of sign to the task

A resemblance-based sign depicts an object, such as a camera. A trace or indicator suggests a condition, such as a rising level. A conventional symbol gains meaning through learned use, such as a play triangle. Many icons combine these mechanisms.

Literal drawings are useful when the object itself matters. They become weaker when the intended action is several conceptual steps away. A rocket may resemble a rocket clearly while saying little about whether a control publishes a page, accelerates a process, opens onboarding, or upgrades a plan.

A metaphor can remain useful after its original object becomes uncommon. Judge the learned meaning with the intended audience. Historical obsolescence alone is insufficient reason to replace a familiar convention, and familiarity within a design team is insufficient evidence to retain it.

### Control semantic distance

Prefer a short connection between form and meaning. To represent invoices, a document with a recognizable monetary cue may be closer than a generic chart. To represent "reconcile transactions," a text label may be clearer than any compact composite.

Avoid picturing a pun in the source language. A flame for "burn a disc" relies on wording rather than the operation. A magic wand or sparkles should not stand for several distinct features merely because each feels helpful or automated. Label the actual action, such as "Rewrite," "Remove background," or "Generate summary."

For abstract categories, a memorable symbol can function as a learned anchor when the label remains visible. Do not claim that the drawing explains the category independently.

### Simplify around diagnostic features

Identify the few features that make the concept distinct. Preserve a key's head and teeth, a folder's tab, a bell's dome and clapper, or a lock's shackle. Remove realistic details that do not improve recognition or discrimination.

Test subtraction carefully. Removing the folder tab can turn it into a generic rectangle. Removing every camera detail can make it indistinguishable from a briefcase. The goal is the least complexity that preserves the necessary distinctions under actual conditions.

### Test resemblance and interpretation separately

Ask what people see, then what they expect the control to do. These are different questions. A person can correctly identify a cloud while expecting upload, download, weather, backup, or connection status.

Use unprompted responses before forced-choice matching. Avoid telling participants the intended metaphor or action in the task wording. Later, test selection in the real interface, with its labels and neighboring controls. A symbol that succeeds in isolation can still fail in a crowded toolbar.

Record recurrent wrong interpretations and dangerous confusions. Prefer a label, a different metaphor, or a simpler interaction when a more polished drawing does not resolve them.

## 4. Select, extend, or create a family

### Prefer a suitable maintained family

Start with an existing family when it covers the required meanings, fits the visual direction, works at the intended sizes, and permits the proposed use. Consider native symbol systems for native controls because they may supply text alignment, weight matching, localization, variants, and platform behavior.

Evaluate the actual difficult icons and the production package. A promotional sheet of easy shapes does not establish consistency across a large set.

| Criterion | What to inspect |
| --- | --- |
| Coverage | Real product concepts, rare tools, modifiers, states, and confusion pairs |
| Optical fit | Smallest size, dense icons, asymmetric icons, pairing with the actual typeface |
| Family range | Required sizes, weights, fill styles, themes, and localized forms |
| Production | Formats, imports, metadata, naming stability, accessibility integration |
| Maintenance | Ownership, updates, contribution process, deprecation policy |
| Rights | Asset license, package license, attribution, modification, redistribution, trademark restrictions |

A package's open-source code license does not automatically establish unrestricted rights to every included brand mark. Verify asset-specific restrictions when applicable.

### Extend by studying the host family

Read its construction rules and inspect editable or shipped vector sources. Compare simple, dense, curved, angular, narrow, wide, filled, and modified examples. Infer recurring treatment where documentation is incomplete, then verify the inference across several icons.

Match the host's actual scale, cap length, corner behavior, detail density, optical centering, and export conventions. A shared canvas and nominal stroke width are insufficient. Add the new icon beside its nearest conceptual and geometric neighbors throughout development.

When two libraries must coexist, assign explicit roles, such as native controls and branded editorial pictograms. Establish a boundary by function and scale. Do not mix unrelated families within one repeated toolbar or navigation group merely to fill coverage gaps.

### Create a family when the need justifies ownership

A custom family is appropriate when a distinctive visual language or specialized domain cannot be served by available assets, and the project can maintain the result. Define who will draw future additions, resolve requests, build exports, and repair failures.

Develop a pilot set before committing to hundreds of concepts. Include a circle-based form, rectangle, diagonal, organic curve, human figure, dense object, compound icon, asymmetric form, common control, and difficult domain concept. Test the grammar against these different demands. A rule that only works for home, search, and plus is incomplete.

## 5. Define the visual grammar

### Turn the direction into construction choices

A coherent family has recurring decisions about proportion, structure, and expression. Specify them in a compact style sheet with representative drawings and exceptions.

| Dimension | Decisions to record |
| --- | --- |
| Construction | Outline, solid, mixed, duotone, colored, dimensional, or a defined family of these |
| Scale | Canvas, live areas, keyshapes, optical-size masters, supported uses |
| Weight | Nominal stroke, optical corrections, fill density, heavy junction treatment |
| Endings | Butt, round, square, tapered, or custom terminals |
| Corners | Outer and inner treatment, radius families, semantic exceptions |
| Curves | Circular, elliptical, softened rectangular, organic, or another controlled character |
| Angles | Recurring diagonals and exceptions needed by the object |
| View | Front, side, plan, isometric, or controlled perspective |
| Detail | Minimum gaps, allowed internal features, visual hierarchy |
| Composition | Base/modifier relationship, slash policy, containers, badge position |
| Expression | Human proportions, irregularity, exaggeration, depth, color, and texture |

Connect these decisions to the brief. Broad open counters and restrained detail support small dense controls. Soft terminals and rounded contours can create a gentler voice, but excessive rounding can erase distinctions. Angular corners can feel precise while creating dark junctions or fragile tips that need correction.

### Choose a primary construction

| Construction | Useful qualities | Main cost to resolve |
| --- | --- | --- |
| Outline | Open texture, visible internal structure, compatibility with text | Crowded crossings and weak hairlines at small sizes |
| Solid | Strong silhouette and compact emphasis | Interior details become small counters; nearby shapes may merge |
| Mixed outline and fill | Flexibility for objects needing solid details | Exceptions can look arbitrary without a rule |
| Duotone or layered | Separate foreground, background, or components | Meaning and contrast can collapse in monochrome |
| Multicolor | Identity, category, material, or rich object distinction | Theme adaptation, contrast, and hierarchy become harder |
| Dimensional | Material, product identity, expressive depth | Lighting, projection, scaling, and asset complexity |
| Deliberately irregular | Distinctive expressive character | Small-size consistency and reproducible additions |

No construction is universally the most usable. Compare candidates in the actual task and at the actual size. Keep one primary language for equivalent roles, and define the conditions for an exception.

### Define consistency at several levels

**Structural consistency** aligns primitives and construction. **Optical consistency** aligns apparent size and weight. **Semantic consistency** aligns meanings and modifiers. **Behavioral consistency** aligns state and interaction. **Production consistency** aligns names, bounds, and formats.

A strict stroke rule can coexist with poor optical consistency. Matching colors can conceal inconsistent meanings. Review each level rather than accepting a family because its icons share rounded corners.

## 6. Build the grid and keyshapes

### Use the grid to make relationships repeatable

Choose a canvas from intended use and delivery, not from a belief that one grid defines icon quality. Common small interface systems use square canvases, but indicators, wordmarks, and specialized assets can require other proportions. Keep exceptions explicit so application code does not silently stretch them.

Define reference centers, normal live areas, keyshapes, and useful diagonal guides. Add guides only when they help construct recurring forms. Dense decorative circles do not prove that a contour is well designed.

### Calibrate keyshapes optically

A circle, square, portrait rectangle, and landscape rectangle with identical outer dimensions do not appear equally large. Start with reference shapes, compare their apparent mass, and adjust their dimensions before deriving other icons.

The following is an illustrative starter for a custom outline family at 24 CSS pixels. It is not a platform specification or a universal recipe.

| Property | Starter value | Verification |
| --- | --- | --- |
| Canvas | 24 × 24 user units | Consistent placement frame |
| Typical painted live area | About 20 × 20, centered | Room for clear contour and export padding |
| Square reference | 18 × 18 painted bounds | Does not dominate the reference circle |
| Circle reference | 20-unit painted diameter | Comparable apparent scale to the square |
| Wide reference | 20 × 16 painted bounds | Reads as wide without appearing undersized |
| Tall reference | 16 × 20 painted bounds | Comparable apparent presence to the wide form |
| Nominal stroke | 2 user units | Fits the text and leaves open internal spaces |
| Typical outer radius | 2 user units | Fits the object and related family shapes |
| Initial construction increments | Whole and half units | Useful starting coordinates, with deliberate optical exceptions |
| Smallest gap trial | Around 2 units | Remains visibly open in the actual small output |

These reference bounds describe painted artwork, including strokes. With a 2-unit centered stroke, a circle whose painted diameter is 20 has an 18-unit centerline diameter. A rectangular centerline from 3 to 21 paints approximately from 2 to 22 before corner and cap effects.

Use the keyshape that suits the object's proportions. Do not squash a person into a square or force a cloud to become a circle. Allow carefully controlled overshoot, extremities, and asymmetry where they produce a better family relationship. Keep non-negotiable clipping limits separate from soft construction guides.

### Keep export padding stable

Preserve the standard canvas even when a narrow icon leaves more internal whitespace. Tight-cropping each SVG to its painted bounds destroys shared alignment and apparent scale.

A live area can permit an antenna, arrow point, or optical overshoot to extend beyond its normal boundary. The final asset must still include all intended paint, including stroke caps and joins. Check any animation excursion separately.

### Compare the construction relationships

The plate below distinguishes reference-shape proportions, painted stroke edges, endpoint positions, and optical centering. Its enlarged diagrams explain the geometry. They do not replace proof at the intended output size.

![Four construction diagrams compare an 18-unit square with a 20-unit circle on a 24-unit canvas, a 2-unit stroke with aligned outer edges, equal-length butt and round strokes with different endpoints, and a play triangle before and after a trial optical shift.](references/iconography/construction.svg)

## 7. Construct strokes, corners, and joins

### Choose a stroke model

Use live strokes while editing when they preserve useful centerlines and reusable geometry. Export them as strokes when the target renderer and family contract support the intended scaling. Use expanded contours when custom variable thickness, stable filled geometry, or a production format requires them.

Keep editable sources before destructive expansion. Repeated expansion and simplification can introduce inconsistent corners and tiny gaps. Expanding a stroke changes its representation, not its intended appearance. Compare the result.

A nominally monoline family can need controlled corrections at dense junctions and diagonals. Apply these through documented patterns rather than arbitrary per-icon stroke overrides in application code.

### Account for cap extension

A butt cap stops at the path endpoint. A square cap extends by half the stroke width. A round cap also extends by half the width at its furthest point, with a curved end. These differences change visible length and proximity.

For a 2-unit round stroke with a required visible horizontal extent from 6 to 18, place the centerline endpoints near 7 and 17. A butt-capped line with the same visible extent uses endpoints at 6 and 18. Reusing the same endpoints produces different lengths.

Set line caps and joins explicitly in shipped assets when their values affect the family. Defaults inherited from an unrelated component should not change the drawing.

### Design corners as inner and outer relationships

Specify whether the radius describes the centerline, inner contour, or outer contour. For a simple rounded centerline corner of radius 3 with a centered stroke of width 2, the approximate outer radius is 4 and inner radius is 2. Tight radii can collapse on the inside.

A filled rounded shape with an independently drawn counter needs both contours designed. Copying the outer radius onto the inner cutout can produce inconsistent thickness. Test the visual turn, not only the numeric radius field.

Preserve semantic corners. A document fold, arrow tip, or crystalline object may need a sharper treatment than a rounded container. One radius applied to everything can make a family less coherent by weakening object structure.

### Resolve junction density

Crossings, acute angles, and merged strokes create dark knots. Open a joint, shorten an overlapping segment, taper a local contour, or separate parts where needed. Keep the identifying structure intact.

Miter joins can produce long spikes at acute angles. Control the join type and miter limit, or draw the intended contour explicitly. A rounded join removes the spike but may blunt an arrow. A bevel can introduce a visual notch. Choose deliberately.

For a plus or close symbol, inspect the center as well as the endpoints. Two translucent strokes can produce a darker overlap. A unioned shape or fully opaque stroke treatment avoids accidental overlap emphasis when appropriate.

### Reuse geometry with review

Keep shared arrows, tabs, handles, circles, and modifiers as editable components or construction primitives. Reuse speeds consistency, but the same part may need optical adjustment when placed in a dense base icon.

Document when a shared part is a fixed asset and when it is a starting construction. Otherwise, local edits either break the reusable source or create undocumented forks.

## 8. Draw curves, silhouettes, and negative space

### Establish the silhouette first

At small size, the outer contour and largest spaces carry much of an icon's identity. Begin with the overall form, proportion, and orientation. Add internal lines only when they clarify the concept or distinguish it from a neighboring icon.

Inspect a filled silhouette view of an outline icon as a structural aid, then return to its intended rendering. This test can reveal an unstable proportion, but a silhouette alone cannot validate a tool whose identity depends on internal detail.

### Draw curves with controlled points

Place curve points where they control a meaningful extremum or change in direction. At a smooth join, align the incoming and outgoing handles along a common tangent. Adjust handle lengths for curvature. A tangent match prevents a visible kink but does not guarantee an even curve.

Use the fewest points that give reliable control. Too many nodes create ripples, difficult editing, and unstable optimization. Too few can force a complex organic contour into an unsuitable geometric approximation.

Compare circular, elliptical, and softened rectangular curves in context. A camera lens may need a true circle. A cloud lobe or person's shoulder often needs a less mechanical curve. Do not claim that every attractive curve can be derived from overlapping circles.

### Design the white shapes

Treat gaps and counters as designed forms. Compare their width, area, rhythm, and openness across the icon. Small changes to an aperture can matter more than a detail on the outside.

Look for narrow wedges between diagonals, tiny holes in gears, cramped document lines, and accidental tangencies where two shapes nearly touch. Choose either a clear connection or a clear gap. Ambiguous near-contact often turns into a dark seam or broken shape when rasterized.

A constant numeric gap does not produce constant apparent openness. A diagonal channel, circular hole, and vertical slot distribute space differently. Establish a minimum-gap trial, then proof each kind at its actual smallest size.

### Balance reduction and character

Retain one or two meaningful characteristics that distinguish the family, such as a distinctive shoulder curve, proportion, terminal, or cut corner. Avoid decorating every icon with a motif that conflicts with the concept.

For organic subjects, simplify anatomy without making figures indistinguishable or stereotyped. Keep pose, head-to-body relationship, limb separation, and assistive devices readable. Use labels and inclusive variants where a single stylized figure cannot represent the intended meaning fairly.

### Construct dimensional families deliberately

Choose a shared projection before adding depth. Front and side views keep functional drawings compact. Isometric or perspective views can explain a three-dimensional object, but they need a consistent camera, orientation, depth, and treatment of hidden parts. Avoid giving adjacent icons unrelated viewpoints merely because each looks attractive in isolation.

In an isometric family, establish the axes and preserve parallel edges along each axis. In a perspective family, establish the horizon and vanishing logic. A circle on a tilted plane becomes an ellipse consistent with that plane. Reusing a front-facing circular hole on a receding face makes the object structurally inconsistent.

Define the light direction, elevation, softness, material response, and shadow behavior. Distinguish a cast shadow from shading on the object. Keep highlights subordinate to the silhouette and identifying features. A reflective metal part, matte surface, and translucent layer need different treatment, but should belong to the same environment.

At small sizes, reduce depth and shading before sacrificing recognition. Check a monochrome or flattened version to see whether lighting is carrying essential structure. Supply an intentional small variant if the rich artwork fails. For platform-generated depth and lighting, follow the host's layer model and avoid adding effects twice.

## 9. Correct geometry optically

### Compare apparent size rather than identical bounds

An open diagonal, dense square, hollow circle, and irregular figure occupy their canvases differently. Compare them together at the intended size and background. Adjust live dimensions, proportions, or detail density before using color to hide imbalance.

Curved or pointed forms may need to extend slightly beyond flat reference lines to appear equal in height. Sparse forms may need more extent than dense forms. These are optical corrections to test, not permission to expand every icon until the canvas is full.

### Center the visible mass

Geometric centering aligns a box. Optical centering aligns the perceived form. A play triangle often needs a small shift toward its point to appear centered in a circle. A download arrow over a tray may feel low because of its lower mass. Make these adjustments inside the asset or through a documented alignment mechanism.

Avoid scattered CSS nudges attached to individual screens. The same corrected asset should align predictably across uses. If a particular text relationship needs a different adjustment, keep it in the component role rather than altering the canonical icon indiscriminately.

### Correct weight locally and across the family

A diagonal can appear different in weight from a vertical stroke. A tight join appears darker than a straight run. A large filled region can dominate a more open neighbor despite identical dimensions.

Resolve the cause. Open dense joints, widen counters, adjust a diagonal contour, or revise overall scale. Do not automatically reduce every complex icon's global stroke, which can leave the sparse parts too weak.

### Use a repeatable optical comparison

Place the candidate among reference icons and its closest neighbors. Compare at actual size, in monochrome, on both light and dark backgrounds. Look first for outliers in scale, darkness, center, and complexity. Then inspect magnified contours to identify the cause.

Alternate between context and detail. Magnification finds construction defects, but it can encourage corrections that are invisible or harmful in use. Record meaningful exceptions with their reason and proof rather than describing them as accidental departures from perfection.

## 10. Control pixels and rasterization

### Understand what snapping can accomplish

Rasterization converts vector coverage into physical pixels. Aligned horizontal and vertical edges can render crisply under a known scale and translation. Curves and diagonals still need antialiasing. Fractional layout, display density, zoom, transforms, and rendering engines can change the result.

For a centered axis-aligned stroke, its two edges lie at the centerline position plus or minus half its width. To align both edges to device-pixel boundaries, consider the final device coordinates, not only the drawing coordinates.

```text
scale = displayed CSS size / viewBox size
edge_device = (center_user ± stroke_user / 2) × scale × device_pixel_ratio
              + translation_device
```

This simplified relation assumes uniform scale and an axis-aligned segment. Rotation, nonuniform transforms, browser zoom behavior, and rasterizer choices need direct proof.

At 1:1 mapping on a 1× display with no fractional translation, a 2-unit stroke centered at x = 6 has edges at 5 and 7. A 1-unit stroke centered at x = 6 has edges at 5.5 and 6.5. Centering that 1-unit stroke at x = 6.5 places its edges at 6 and 7. "Use whole coordinates" therefore does not describe every crisp stroke.

### Choose a practical snapping policy

Default to deliberate whole- or half-unit construction where it supports the intended rendering, then make optical exceptions. Favor clean axis-aligned edges in dense small icons. Preserve good curves and meaningful proportions rather than forcing every point onto integers.

A fractional stroke such as 1.5 units can be a valid family choice for its target sizes and displays. It requires proof across those conditions. An integer stroke can also blur after scaling or fractional placement. Neither the coordinate field nor an editor's pixel-preview badge establishes final quality.

Do not apply `shape-rendering="crispEdges"` as a universal repair. It is a rendering hint and can make curves or diagonals jagged. Start with ordinary vector rendering and correct geometry, scale, and placement before changing renderer hints.

### Test the actual pipeline

Render the exported asset through the production component at supported sizes, zoom levels, and display densities. Include a lower-density display when it is a target. Check whether flex/grid positioning, a transform, animation, or scaled ancestor introduces fractional placement.

Inspect PNG exports at exact intended pixel dimensions. Avoid judging a raster asset after a document editor has resampled it. Supply the required density variants when a raster format is necessary.

A screenshot enlarged by nearest-neighbor scaling can reveal pixel coverage. A normal-size view determines whether that coverage is useful. Sharper edges are not automatically better if they appear jagged or make the icon uneven.

## 11. Design sizes, weights, grades, and styles

### Choose a size strategy

Use one scalable master when it remains clear across the required range. Create optical masters when scaling causes details to close, strokes to weaken, proportions to feel wrong, or symbols to lose their distinction. Vector scalability preserves geometry, not perception.

A small master may have fewer gear teeth, wider counters, fewer document lines, more open junctions, a stronger terminal, or a different modifier relationship. A large master can support more nuance without becoming an illustration. Preserve the same identifying structure across sizes.

| Strategy | Appropriate condition | Cost |
| --- | --- | --- |
| One scalable master | Modest size range and simple robust forms | Must verify the extremes and fractional scales |
| Discrete optical masters | Dense tools, very small uses, broad size range | More drawings and explicit size selection |
| Variable symbol family | Engineered interpolation and supported runtime | Axis setup, compatibility, and instance proof |
| Separate expressive family | Larger narrative or promotional role | Role boundary and shared identity need documentation |

Specify which master serves an intermediate display size. Prefer a documented mapping over ad hoc stretching. Do not silently fall back to the most detailed asset when a small master is missing.

### Work through a small-size reduction

Consider a 24-unit document icon with a 2-unit stroke and a 2-unit internal gap, displayed at 16 CSS pixels. Pure scaling produces approximately 1.33 CSS-pixel strokes and gaps. Depending on placement and rendering, the three internal text lines may merge even when the page contour remains recognizable.

For a dedicated 16-unit master displayed at 16 CSS pixels, a trial could use a 1.5-unit stroke, fewer text lines, wider internal gaps, and a smaller fold. Compare that candidate with the simply scaled original and the family's other 16-pixel icons. These trial values do not guarantee improvement. The pass condition is clearer structure with comparable apparent weight and the same document identity.

Increasing the stroke alone would consume more of the already narrow internal space. Reduction therefore changes the composition of details as well as thickness. Record the selected master in the size mapping so the application does not choose by filename guesswork.

### Design weight as structure

Heavier icons need open counters and corrected joins, not just a larger `stroke-width`. Increasing a centered stroke expands both inward and outward. Small holes disappear, clearances shrink, and painted bounds change.

For a family of weights, compare the darkest junction, the smallest counter, the narrowest gap, and the simplest glyph. Preserve the identity of the same icon across weights while balancing the family within each weight.

Numeric weight labels are family-specific. A weight value of 400 in a symbol font does not guarantee a visual match to a text font at 400. Match perceived emphasis beside the actual text.

### Distinguish weight, grade, scale, and optical size

**Weight** changes structural thickness and may change dimensions. **Grade** offers finer darkness adjustment with relatively small size effects when a family supports it. **Scale** changes the icon's apparent size relative to its context. **Optical size** changes its drawing for a use size.

Use the axis or variant that addresses the problem. Enlarging an icon to make it darker changes spacing and hierarchy. Raising weight to recover a tiny aperture may close it further. A supported optical-size variant can solve a problem that global scaling cannot.

Do not assume every variable symbol family supplies every axis or uses the same ranges. Pin the supported font or library version and specify the instance deliberately. Test intermediate animation values if they will be visible.

### Draw outline and solid variants as related designs

A solid variant needs its own silhouette and counters. Filling every enclosed path in an outline drawing can erase identity. Adding a thick outline to a solid drawing can create an oversized blob.

For a filled folder, preserve its tab and opening relationship. For a filled bell, decide whether the clapper remains distinct. For a filled person, preserve a clear separation between head and shoulders where needed. Compare both variants within the same family and at the smallest size.

Use outline-to-fill as a state treatment only where the distinction is stable and detectable. Fill does not inherently mean selected in every context. A family that uses filled icons by default needs another selection cue.

## 12. Construct recurring icon forms

### Arrows, chevrons, and close marks

Set a shared relationship among shaft length, head width, head angle, and weight. Match the arrow's apparent direction and emphasis to its role. A navigation chevron can be lighter and more compact than a transfer arrow, but the relationship should be intentional.

A chevron often communicates disclosure or progression. A full arrow can communicate movement, direction, or a transfer. A bent arrow can represent reply, return, undo, or another convention. Inspect the actual meaning rather than treating these as interchangeable shapes.

For paired arrows, compare both directions after rendering. Pure reflection may be suitable, but asymmetric joins, optical shifts, or contextual positioning can make one feel different. A close mark should have balanced arms, open corners, and a center that does not become a dark knot.

An arrow without a source or destination is often ambiguous. A downward arrow into a tray can distinguish download from moving an item downward. Labels still resolve cases where export, download, and save are all present.

### Documents, folders, and containers

Build the base object before modifiers. Establish the page proportion, fold size, folder tab, container opening, and recurring internal-line treatment. Use sufficient spacing between text-suggestion lines so they remain distinct.

For a document pair representing copy, test overlap depth and silhouette. For a clipboard representing paste, keep its clip visible. If both become two overlapping rectangles at the target size, simplify or choose a clearer distinction.

Do not add tiny pseudo-text to imply sophistication. Use abstract lines unless specific characters carry meaning, as in text-formatting tools. Localize meaningful characters.

### Circles, clocks, and progress

Keep circular contours smooth and visibly centered. Correct the spacing of ticks, hands, or gaps. A clock needs readable hand separation and a stable center. A circular arrow needs a clear head and opening so it does not resemble an incomplete ring or loading spinner.

Separate static status from indeterminate progress. A spinner denotes ongoing work, while a circular arrow often denotes a command. Do not use one moving shape to stand for refresh, loading, success, and retry without a documented state progression.

For determinate progress, show the value in an appropriate control or accompanying text. A decorative ring should not be the sole way to know that a required operation is 90% complete.

### Gear construction as a worked example

A settings gear is a radial structure with a central counter. Design the outer diameter, root diameter between teeth, tooth width, tooth count, and hole together. At small size, too many teeth create noise and a small hole closes.

1. Choose the family view and desired painted extent. For a new 24-unit pilot, begin around a 20-unit outer extent and compare it with the reference circle.
2. Draw a root circle and one tooth. Place the tooth on the vertical axis and overlap it sufficiently for a clean union.
3. Repeat the tooth by an angle of `360° / tooth_count`. Eight teeth use 45° spacing. This is a construction example, not a preferred count for every family.
4. Union the outer parts, remove unnecessary nodes, and subtract a concentric hole. Keep the original repeated construction in the editable source.
5. Correct tooth-tip corners, root notches, and the minimum ring thickness. Ensure all teeth appear equivalent after rasterization.
6. Compare the gear beside the circle reference and other dense icons at the smallest use. Reduce teeth or enlarge spaces if it clogs.
7. Build an outline variant separately if needed. A second inner contour around every tooth can become too dense even when the solid gear works.

A rounded-star method, repeated additive shapes, or repeated cutouts can reach a useful contour. Choose the method that makes controlled revision easiest. The tool sequence does not determine the quality of the result.

### People, hands, and organic objects

Begin with a recognizable pose and proportional system. Keep limbs and fingers sufficiently separate, but avoid anatomical detail that cannot survive output. A hand gesture can have different meanings across cultures. Use it only when it fits the audience and purpose.

Do not use a standing person as a generic representation of every user ability or a gender stereotype as the default for a role. Distinguish a person, group, account, contact, and accessibility feature with explicit semantics and labels.

For animals, plants, food, and natural forms, preserve the diagnostic silhouette and a controlled curve vocabulary. A family can allow asymmetry without allowing arbitrary stroke, perspective, and detail changes.

### Tools and domain-specific symbols

Study the real object and the user's mental model before simplifying. The feature a designer finds visually interesting may not be what an expert uses to distinguish a tool. Test with people who perform the task.

Preserve established technical notation when it already carries the intended meaning. An invented drawing for a mathematical, electrical, or editing operation can be harder to learn than a conventional sign. For standardized or safety-relevant symbols, use the applicable approved source and verify permitted modifications.

## 13. Compose modifiers and compound icons

### Build a visual grammar for modification

Define a base object and a limited set of recurring qualifiers, such as add, remove, lock, warning, or synchronization. Assign consistent modifier scale, placement, visual precedence, and clearance.

Prefer one modifier on a small functional icon. If the meaning needs a document, person, lock, clock, and warning, use text or a larger composition. A compound icon should have a readable hierarchy, not several equally detailed miniatures.

| Component | Purpose | Example |
| --- | --- | --- |
| Base | Identifies the object or domain | Folder |
| Modifier | Qualifies the action or condition | Plus for create/add |
| External badge | Reports application data or state | Unread count |
| Container | Groups or frames the whole sign | Button background |

An asset modifier and a live badge have different ownership. A plus integrated into "new folder" belongs to the canonical symbol. An unread count changes with data and belongs to the application component.

### Preserve the base and modifier together

Choose an overlap that leaves the base recognizable. Simplify or open the base behind the modifier when needed. Avoid a small floating badge that appears detached or a modifier that hides the only diagnostic feature.

Use a true transparent cutout or mask for clearance when the asset must work on arbitrary backgrounds. A white halo can fail on dark or colored surfaces. If a badge intentionally has a surface-colored backing, assign that surface color through the component theme rather than baking white into the asset.

Check the union's optical center and painted bounds. A modifier can make an otherwise centered asset feel heavy in one corner. Correct the composite while preserving the family's placement contract.

### Define slashes precisely

A slash can mean off, unavailable, prohibited, hidden, muted, or disconnected. Choose its meaning by context and avoid implying that all of these are equivalent.

Set its direction, width, end treatment, clearance, and relationship to the base. Maintain a strong readable line and enough of the base to identify it. For a muted microphone, ensure the slash does not erase the microphone's key structure.

Do not apply a slash automatically as the visual equivalent of `disabled`. A disabled control is an interaction state. A slashed bell may specifically mean notifications are off. They need different accessible state and labeling.

### Keep modifiers culturally and directionally coherent

A corner placement convention is a family rule, not a universal requirement. Decide whether a modifier follows reading direction, remains tied to an object feature, or has a dedicated localized variant. Mirroring an entire compound can reverse letters, badges, or meaningful physical orientation.

Test all supported combinations. Two individually valid parts can collide, create a new misleading silhouette, or become indistinct at small size.

## 14. Compose icons with text and layout

### Match apparent scale and emphasis

Pair icons with the actual typeface, size, weight, and line height. Compare the icon's visible form with the text's x-height, capitals, and overall color. Equal CSS font size and SVG height do not guarantee balance.

Choose whether the icon supports the label or leads the composition. A routine menu icon should not dominate its text. A status symbol may need stronger emphasis when scanning conditions is the task. Preserve the hierarchy intentionally.

Use a text-integrated symbol's supported baseline and scale configuration where available. For standalone SVGs, establish a component alignment rule and apply optical correction through the asset or role. Do not convert every row to baseline alignment solely because the icon sits beside text.

### Align according to the relationship

| Context | Starting alignment | What to verify |
| --- | --- | --- |
| Single-line button or menu item | Center the icon canvas within the control's content row | Visible mass aligns with the label and control |
| Inline symbol in a sentence | Align to the text's baseline system with a measured adjustment | Line height and surrounding words remain comfortable |
| Multi-line alert | Align the icon with the first line or opening text block | It does not drift to the middle of a long message |
| Repeated list or table | Use a stable icon column and consistent content inset | Labels align despite narrow and wide symbols |
| Large pictogram and caption | Compose the visible art and caption as a group | Clear ownership and consistent vertical rhythm |

Keep the icon next to the content it qualifies. A warning at the far edge of a wide table can become detached from the value it explains. A trailing action and a status symbol should have distinct placement so people can tell which is interactive.

### Space visible shapes as well as canvases

A CSS `gap` measures between layout boxes. Internal asset padding adds to the apparent space. Compare the visible distance from artwork to text, especially when one icon is unusually narrow.

As an initial trial, a 16–24 CSS-pixel icon beside a short label might use a 4–8 CSS-pixel box gap. Adjust to the actual font, asset padding, control density, and hierarchy. Keep a token for the role after calibration. Do not patch every label with a different margin.

Use more separation between distinct control groups than within a labeled control. Repeated equal gaps can obscure grouping. Preserve text alignment when icons are missing by deciding whether the icon column remains reserved for that list role.

### Use containers for a reason

A container can signal a button, category, selected destination, identity tile, or visual grouping. Apply it consistently by role. A colored square around every decorative icon can imply interaction and add noise.

Specify the icon-to-container scale, internal padding, shape, color, state, and focus treatment. Do not stretch the icon to fill the container. An asymmetric glyph can require optical centering even when the container is perfectly centered.

If the same round shape denotes both status and an actionable button, provide enough contextual and behavioral distinction to prevent confusion. An icon's apparent clickability is a property of the whole component.

### Keep information density deliberate

In dense toolbars, group commands, preserve order, and provide labels or tooltips appropriate to familiarity. When width shrinks, move lower-priority commands into a labeled overflow rather than reducing every glyph and target.

In cards and marketing sections, vary hierarchy through the content structure before adding more icon colors, containers, and sizes. Use a small number of clearly defined roles so the page reads as a composition rather than a library specimen.

## 15. Design interaction and state

### Define the component before the glyph treatment

An icon is not a button until a control supplies role, name, interaction, target, focus, and state. Use a button for an action and a link for navigation. A noninteractive status icon should not acquire button styling or keyboard focus.

Specify default, hover where available, focus, pressed, selected, disabled, busy, success, and error behavior only where relevant to the component. These conditions are not interchangeable.

| Condition | Meaning | Suitable visual treatment |
| --- | --- | --- |
| Hover | Pointer is over an available target | Surface or emphasis change without implying selection |
| Focus | Keyboard or another focus mechanism locates the control | Visible indicator around the target |
| Pressed feedback | An activation is occurring | Brief control response |
| Toggled on | A persistent binary option is active | Fill, indicator, surface, or another consistent non-color cue |
| Current destination | User is at this page or location | Navigation indicator and appropriate current-state semantics |
| Disabled | Control cannot currently be activated | Distinct subdued treatment with correct semantics |
| Busy | An operation is in progress | Stable layout and understandable progress feedback |
| Error or warning | A condition needs attention | Shape and text that communicate the specific condition |

### Distinguish state from the next action

A speaker with a slash might show that sound is currently off or offer the action to mute sound. Choose one model and make the label, state semantics, and visual behavior agree.

For a stable toggle, use a stable label such as "Mute" and expose its pressed state. For an ordinary action button whose name changes between "Mute" and "Unmute," expose the current action and avoid redundant toggle semantics. Do not announce "Unmute, pressed" because the graphic and accessibility implementation use incompatible models.

For a show/hide password control, decide whether the label names the next action and update it consistently. Never rely on the eye drawing alone to communicate the current security or visibility condition.

### Keep selection visible beyond color

A filled variant can support selection if the difference remains clear at the target size. Pair it with a container, indicator, checkmark, label, or positional treatment where needed. Keep selected and unselected assets within the same coordinate frame so state changes do not jump.

Do not make every native control supply a custom selected icon if the platform already provides the appropriate treatment. Verify what the actual component renders before overriding its behavior.

### Handle unavailable and asynchronous actions

A busy button should preserve its name and enough context to explain what is happening. If a spinner replaces its icon, avoid changing button width or implying the operation is complete. Provide appropriate status feedback when completion matters.

A dim icon alone does not explain why an action is unavailable. Put essential constraints in accessible supporting text or the surrounding flow. Do not rely on a tooltip attached to a disabled element that cannot receive focus.

For destructive actions, use clear text and the interaction safeguards appropriate to the task. A red trash glyph does not communicate scope, permanence, or which item will be removed.

## 16. Apply color, hierarchy, and themes

### Start with semantic color roles

Default to monochrome functional icons that inherit the intended content color. Define roles such as primary, secondary, interactive, selected, success, warning, critical, disabled, and inverse. Assign roles through components and tokens.

Do not color icons individually to make a mixed family appear coherent. Fix the underlying scale and weight first. Use accent color to support hierarchy, not to compensate for weak drawing or meaning.

When an icon is paired with a label, start with comparable emphasis unless the task calls for a difference. A subdued supportive icon beside readable text can be appropriate. A high-emphasis icon should carry a corresponding informational or interactive role.

### Preserve meaning without hue

Use shape, position, label, pattern, or another visible distinction in addition to color when color carries information. A green dot and red dot cannot be the only available distinction between successful and failed jobs.

Provide a monochrome fallback for a duotone or multicolor asset when a target context removes color. If layers become indistinguishable, redesign the fallback rather than flattening them indiscriminately.

### Design both light and dark appearances

Proof the same family on light, dark, selected, and tinted surfaces. Light strokes on dark backgrounds can appear heavier or more luminous. Use supported grade, a calibrated variant, or a role adjustment when necessary, while preserving sufficient contrast.

Do not create a dark-mode asset by blindly inverting every color. Shadows, highlights, cutouts, and semantic colors may need separate treatment. A white patch pretending to be transparency will reveal itself immediately.

For layered icons, specify which layers carry meaning and which are supporting depth. A low-opacity background plane may be acceptable as decoration, while a low-opacity warning modifier may become unreadable.

### Verify the final contrast relationship

Measure against the colors actually adjacent to the meaningful shape. A glyph on a badge needs contrast against the badge, while the badge's relationship to the surrounding surface may also matter. Gradients and photographs need testing at the weakest relevant region.

Nominal contrast does not establish legibility for a very thin antialiased stroke. Use robust forms and inspect actual output. A more generous contrast target can be a useful house choice, but identify it separately from the applicable minimum.

## 17. Preserve accessibility

### Assign the accessible meaning to the right owner

| Use | Accessible treatment |
| --- | --- |
| Icon duplicates a visible button label | Hide the icon from assistive technology; let the button text name the action |
| Icon is the only visible content of a control | Give the control an accessible name expressing purpose |
| Standalone icon conveys information | Supply an equivalent text alternative or nearby associated text |
| Icon adds information to a label | Include that information without duplicating the whole label |
| Decorative icon | Exclude it from the accessibility tree |
| Complex explanatory graphic | Provide an equivalent explanation of its meaningful relationships |

Name the action or condition, not the drawing technique. Use "Download invoice," "Payment failed," or "Open navigation." "Arrow pointing down" rarely tells the user what the control does.

Avoid duplicate announcements from a button name, SVG title, and nearby text. Decide ownership once. For repeated row actions, include context such as "Delete invoice 1042" when needed to distinguish controls. Keep the visible label's text within the accessible name when a text label is present.

### Apply contrast requirements accurately

For web content targeting WCAG 2.2 AA, Success Criterion 1.4.11 requires at least 3:1 contrast against adjacent colors for visual information needed to identify user interface components and states, and for parts of graphical objects required to understand the content. Relevant exceptions include inactive components, unmodified user-agent appearances, and graphical presentations essential to the information.

The requirement does not mean every decorative layer or icon must pass independently. It also does not make low-contrast essential information acceptable because another decorative part passes. Evaluate the features required to identify the control or understand the graphic.

Visible text labels follow text contrast requirements. Do not substitute the non-text threshold for ordinary small text. A project may adopt a stricter icon contrast standard for robustness.

### Separate visible size from target size

For WCAG 2.2 AA, Success Criterion 2.5.8 generally requires a target containing a 24 × 24 CSS-pixel square, with defined exceptions for spacing, equivalent controls, inline targets, user-agent controls, and essential presentation. For the spacing exception, a 24 CSS-pixel diameter circle centered on each undersized target's bounding box must not intersect another target or the corresponding circle of another undersized target.

Treat this as a minimum with specific exceptions. Default to larger targets for frequent or touch-operated controls. A project can adopt 44–48 CSS-pixel targets as a practical starting policy while keeping native platform units and requirements separate. A 16- or 20-pixel visible icon can sit inside that larger target.

Measure the actual interactive element, not the SVG's artboard or a screenshot of its container. Avoid overlapping invisible targets. Include adequate separation between destructive and routine actions.

### Preserve interaction and adaptation

Use semantic native controls with keyboard activation and visible focus. Place focus on the control rather than its internal SVG. Preserve a logical order and ensure indicators remain visible against surrounding surfaces and overlays.

Test zoom, text enlargement, high contrast, forced colors, and screen-reader output. Do not lock the control to a height that clips enlarged labels or hide text at the breakpoint where users most need it. A scalable icon does not guarantee a scalable layout.

Respect the user's color adaptation. Avoid globally setting `forced-color-adjust: none` to preserve brand colors. Borders or outlines may be necessary when shadows disappear. Test critical SVG fills, strokes, masks, selection, and focus in the target forced-color environment.

### Make tooltips supplemental and usable

Show custom tooltips on keyboard focus as well as pointer hover where appropriate. For applicable hover/focus content, provide dismissal without moving focus, pointer access to the content, and persistence while it remains relevant, subject to the criterion's exceptions.

Keep interactive content out of a simple tooltip. Use an appropriate popover or dialog when people need to act inside it. A native `title` attribute is insufficient as the only way to discover an action, and a tooltip does not replace a control's accessible name.

Accessibility testing verifies more than a complete list of ARIA attributes. Listen to the actual accessible name, role, and state while operating the component. Confirm that its spoken meaning agrees with its visible behavior.

## 18. Localize meaning and direction

### Evaluate the metaphor in the target context

Check language-specific puns, hand gestures, mailboxes, currency, calendars, clothing, architecture, and social associations. A globe does not inherently mean language selection rather than geography or internet access. A flag identifies a country rather than a language.

Validate uncertain metaphors with the intended audience. Preserve local conventions where they improve understanding, but avoid creating unrelated variants without evidence. The aim is a consistent function across locales, even when the best drawing differs.

Meaningful letters and numerals inside icons require localization or a deliberately language-independent alternative. Text-formatting symbols may use letters from the active writing system. Replace schematic text alignment with a direction-aware variant rather than mirroring real letterforms.

### Classify direction per asset

| Direction policy | Appropriate examples | Required behavior |
| --- | --- | --- |
| Follows interface progression | Back, forward, ordered next/previous navigation | Use semantic direction and the platform's RTL behavior |
| Depicts physical direction | Move object right, compass east, map orientation | Preserve the actual direction |
| Depicts reading structure | Text alignment, list indentation, some document diagrams | Use a localized or direction-aware design |
| Fixed object or identity | Camera, logo, clock face, photograph | Preserve orientation unless there is a specific reason to adapt |
| Composite or context-dependent | Reply, send, history, progress, media controls | Follow the platform and actual task, with a tested variant policy |

Do not apply a global horizontal transform to every icon in an RTL layout. Do not mirror a clock face, a letter, a brand mark, or the geography inside a globe.

A layout can reverse icon and label positions without reversing the artwork. Treat placement, drawing orientation, semantic order, and animation direction as separate decisions.

### Test the complete localized component

Use logical layout properties for start/end spacing. Supply the relevant language and direction context. Verify that the selected asset and its accessible name describe the same action.

For mixed-direction content, preserve numbers, filenames, and technical strings correctly. Test long translated labels and scripts with different vertical metrics. An icon that aligns well with Latin capitals may need a role adjustment beside another script.

Include badges and modifiers in the review. A mirrored base may need an unmirrored badge, localized numeral, or separately positioned qualifier. Store the policy in metadata so each consuming screen does not rediscover it.

## 19. Adapt to platforms and media

### Native applications

Use the platform's symbol and control conventions where they serve the task. The same action can have a different familiar symbol on different platforms, especially sharing, overflow, navigation, and file operations. Consistent behavior and meaning can matter more than identical artwork across products.

Configure native symbols through their supported size, weight, scale, rendering mode, and semantic APIs. Do not reproduce system symbols as fixed screenshots. Check the minimum operating-system version for every required symbol and feature and supply a meaningful fallback.

For custom symbols, use the platform's current authoring templates and validation tools. A generic SVG is not automatically a valid text-integrated native symbol. Preserve baseline, layers, variant behavior, and accessibility integration expected by the host.

### App icons and product identities

Develop a recognizable core silhouette, distinctive composition, and stable identity across appearances. Test the icon beside competing apps, against varied backgrounds, and at notification or settings sizes. Evaluate recognition after masking and theme adaptation.

An app icon can support richer color and depth than an interface glyph. Keep small-size structure clear. Avoid tiny UI screenshots, nonessential words, temporary promotional badges, and details that disappear outside a large presentation.

Use current platform templates for layers, masks, safe areas, appearances, and export dimensions. These specifications change. Keep foreground/background separation or layered depth only where the platform requires or supports it, and avoid baking in system effects that the platform will apply again.

For adaptive launcher icons, design essential content to survive supported masks and motion, and supply the appropriate themed or monochrome asset. Store-listing art and launcher art can have different specifications. Verify both deliverables.

### Identity and third-party marks

Keep identity assets in a separate namespace and usage policy from generic symbols. Respect original proportions, required clear space, colors, backgrounds, and permitted variants. Do not force a trademark into the system's stroke grammar by redrawing it casually.

A library icon may prohibit trademark use, or have no uniqueness suitable for an identity. Native symbol licenses can also restrict logos and app icons. Verify permission before treating a reusable glyph as a brand.

### Pictograms and editorial compositions

Design for the actual display size, caption, narrative role, and surrounding density. A larger pictogram can have more internal hierarchy, but each added detail should support recognition or the intended idea.

Keep related pictograms consistent in visual scale and composition. A tall object, wide vehicle, and circular instrument may need different occupied bounds to feel balanced. Align their captions and reserve enough external clear space.

Use an expressive family selectively where stronger visual presence helps. Keep small functional controls visually distinct from the larger artwork. A promotional scene should not make its decorative parts look like independent buttons.

### Wayfinding and public information

Start with the destination, decision point, viewing distance, approach direction, lighting, environment, and audience. Pair signs with clear language where useful. Maintain consistent arrows and placement across the route, including reassurance after a turn and identification at the destination.

Use established public-information or safety symbols where applicable. Verify the required edition and application rules for the project. Do not restyle safety geometry, colors, or enclosures merely to match a brand. This guide does not replace a sign standard or a professional wayfinding and safety review.

Test a full-size physical proof at the intended distance and angle. A pictogram that works on a laptop may fail through glare, low light, oblique viewing, or visual competition in the environment. Specify symbol size separately from sign panel size and letter height.

### Print, engraving, embroidery, and fabrication

State minimum positive stroke, reversed stroke, gap, and feature size in physical units for the process. Obtain the producer's limits and proof the actual material. Screen pixels do not establish an embroidery or engraving specification.

Inspect ink spread, substrate color, coating, registration, stitch density, cutting radius, and negative-space closure as relevant. A fine white cutout on a dark printed field can fill in even when its positive counterpart remains visible. Produce a one-color or simplified manufacturing variant when needed.

Use vectors for compatible production pipelines and supply the requested color mode and separations. If a process needs expanded paths, retain the editable master and compare the production copy. Outline necessary embedded lettering only in production assets while preserving the source text and required language variants.

### Maps, charts, and spatial displays

Map symbols need distinguishable silhouettes, overlap behavior, clustering, legends, and selection that survives varied backgrounds. Differentiate location markers, live data, and interactive controls. Do not rely on color alone for categories or severity.

Charts need a consistent mapping between shape and variable. An icon used as a quantity must not distort comparison through inconsistent area or size. Include readable values and an accessible explanation when the graphic carries data.

For spatial interfaces, evaluate apparent angular size, distance, depth, contrast, occlusion, and input method. A fixed 24-unit drawing does not determine a usable spatial target. Test on the actual device and environment, including the platform's focus or gaze treatment.

## 20. Animate with purpose

### Give motion an informational role

Animate to acknowledge an action, explain a transition, reveal progress, or preserve continuity. Repeated decorative motion beside reading content can compete with the task. Keep most routine icons stable.

Define the trigger, changed property, duration, easing, origin, repetition, interruption, and final state. Choose the final static state before designing the transition. A successful animation should leave the same meaning clear when motion is reduced or absent.

### Preserve structure through the transition

For a toggle, a short outline-to-fill or modifier transition can reinforce change. For a refresh control, rotation can acknowledge activation, but do not imply completion until the operation actually finishes.

Morph paths only when their correspondence is engineered and the intermediate forms remain acceptable. Equal endpoint counts alone do not guarantee a readable transformation. A short crossfade or a native symbol transition can be more stable when structures differ substantially.

Keep optical centers and container sizes stable. Avoid scaling that changes the hit target or makes neighboring content jump. Test repeated activation, rapid reversal, cancellation, and loading that outlasts the expected duration.

### Support reduced motion and status access

Honor platform and web reduced-motion preferences. Use an immediate state change, restrained opacity transition, static progress indication, or text as appropriate. Preserve the information that motion was intended to convey.

Do not use indefinite motion as the only indicator of a task's status. Provide an understandable name or message for meaningful progress, completion, or failure. Avoid announcing every animation frame or repeating a live-region message continuously.

## 21. Build the semantic and token system

### Separate the drawing from its product meaning

Use a stable asset name for the depicted form or canonical family concept. Map product actions to those assets through semantic roles. Keep this distinction small enough to maintain.

```yaml
# Illustrative asset registry and product mapping, not a standard file format.
assets:
  arrow-down-tray:
    family: product-outline
    source: icons/arrow-down-tray.svg
    viewBox: [0, 0, 24, 24]
    sizes: [16, 20, 24]
    direction: fixed
    tags: [download, save, export]
    license: internal-original

roles:
  action.download-invoice:
    asset: arrow-down-tray
    labelKey: actions.downloadInvoice
    tooltipKey: actions.downloadInvoice
    component: icon-button
```

Here, `sizes` means verified output sizes, not automatically separate master files. A real registry should distinguish masters from display sizes when both exist. Search tags help discovery but do not authorize using the asset for every tagged action.

The role mapping lets a product change its metaphor without renaming a literal drawing. It also prevents a library filename such as `arrow-down-tray` from becoming the user's accessible name.

### Use predictable names and metadata

Choose a consistent naming grammar and one order for qualifiers. For example, `folder-add`, `folder-lock`, and `folder-warning` are easier to scan together than unrelated synonyms. Avoid encoding a temporary screen location such as `header-button-3` into an asset name.

Record the information necessary to select and apply the correct asset.

| Field | Purpose |
| --- | --- |
| Identifier and display name | Stable reference and readable catalog entry |
| Meaning and exclusions | Intended use and known ambiguity |
| Family and style | Visual compatibility |
| Master and supported sizes | Correct optical design and output mapping |
| Weight or axis instance | Reproducible appearance |
| Direction policy | Mirroring or localized-variant behavior |
| Variants and modifiers | Valid alternatives and combinations |
| Source and build location | Editable original and generated output |
| License and provenance | Permitted use and required attribution |
| Owner, version, status | Maintenance and deprecation |

Do not store every final accessible label inside the generic icon component. Labels depend on function, object, state model, and locale. Store reusable defaults or label keys where appropriate, while letting the consuming control provide context.

### Tokenize recurring roles

Keep source construction values separate from application tokens. A family's 2-unit stroke is a drawing convention. An application's 20 CSS-pixel navigation icon is a layout role. A button's 48 CSS-pixel target is an interaction convention.

```css
/* Illustrative calibrated roles for one product. */
:root {
	--icon-size-inline: 1em;
	--icon-size-control: 1.25rem;
	--icon-size-navigation: 1.5rem;
	--icon-label-gap: 0.375rem;
	--icon-target-min: 3rem;
	--icon-color-primary: #20242b;
	--icon-color-secondary: #505966;
	--icon-color-interactive: #174ea6;
}
```

Use the project's typography and spacing foundations to calibrate these values. Scaling relative to text can be useful for inline symbols, while stable control roles can use an explicit optical master. Avoid exposing arbitrary `strokeWidth`, rotation, and scale props to every consumer when they break family consistency.

### Document the application contract

For each icon role, specify the asset family, size/master mapping, weight, color role, alignment, gap, container, target, states, naming owner, and direction policy. A component example should show the actual contract in use.

Keep a searchable catalog with labeled examples, intended meanings, valid variants, and common misuses. Include a way to request a missing concept. A download grid without semantic guidance encourages inconsistent application.

## 22. Engineer and deliver assets

### Keep editable masters and deterministic exports

Maintain source geometry, shared primitives, construction notes, and approved variants. Generate production assets through a repeatable process where practical. Do not rely on manual edits to generated files that will disappear during the next export.

Use an asset manifest or equivalent inventory to reconcile design sources, SVGs, native resources, components, and catalog entries. Verify that the version presented to designers matches the version shipped by engineering.

### Set an SVG contract

For a monochrome interface family, a useful default contract includes the following properties.

- A deliberate, consistent `viewBox` and predictable aspect ratio.
- Complete painted bounds inside the viewport, with intentional overflow documented.
- `currentColor` for intended monochrome fill or stroke, with `fill="none"` where necessary.
- Explicit cap, join, and stroke width where they define appearance.
- Correct compound paths and fill rules for holes and overlapping contours.
- No editor backgrounds, accidental hidden shapes, external bitmap dependencies, or essential text dependent on a missing font.
- Scoped unique identifiers for masks, clip paths, gradients, and accessible titles when repeated inline.
- Removal of scripts, event handlers, and unnecessary external references from untrusted source assets through the project's approved sanitization process.

Stroke-based and expanded-contour SVGs can both be valid. Pick a contract that fits the family's scaling behavior and target renderers. Do not apply non-scaling strokes by default. Keeping a stroke fixed while geometry scales changes proportions and can close small spaces or weaken large forms.

### Optimize without changing appearance

Remove unnecessary metadata, redundant groups, invisible objects, and excessive precision only after preserving a recoverable source. Choose a precision level appropriate to the coordinate scale. A fixed decimal count is not equally safe on a 24-unit canvas and a 1024-unit canvas.

Compare before and after optimization at the smallest and largest supported sizes and on non-white backgrounds. Inspect holes, overlaps, clipping, transforms, caps, and joins. Path merging or rounding can alter appearance even when the file still parses.

Use true transparent cutouts and verify the fill rule. Nonzero winding and even-odd filling can produce different holes. Preserve the intended rule through native conversion and document export.

### Choose the delivery format

| Format or technique | Appropriate use | Risks and requirements |
| --- | --- | --- |
| Inline SVG or component | Themed interface glyphs and direct styling | Repeated IDs, DOM weight, semantic ownership, and sanitization |
| External SVG through an image element | Cacheable static asset | Internal paths do not inherit the embedding document's color; supply the correct appearance and text alternative |
| SVG sprite | Repeated symbols with shared delivery | Reference handling, accessible naming, styling, caching, and external-reference restrictions |
| Native symbol | Integrated platform controls and text | Availability, license, runtime configuration, and fallbacks |
| Native vector resource | Custom platform artwork | Supported subset, path conversion, tint behavior, and proof |
| Raster asset | Textured artwork, unsupported vector pipelines, fixed image delivery | Resolution variants, resampling, theme variants, and file size |
| Icon font | An existing font-based system with a justified delivery need | Loading failure, fallback text, accidental text semantics, axis setup, and subsetting |
| CSS mask | Simple decorative or redundant glyph using current color | Separate semantic content, forced-color testing, and mask support |

Default to SVG for custom functional web icons unless a maintained system provides a better fit. Icon fonts can be useful in an established variable-symbol workflow, but they require deliberate loading and accessible control labels. A failed font must not expose cryptic codepoints or leave the only action unidentified.

### Treat text symbols and emoji as a separate delivery choice

Use a Unicode character when it is meaningful text or established notation, with appropriate language and font support. A mathematical minus, multiplication sign, and letter x are different characters. Select the intended sign rather than a visually convenient substitute.

Do not assume a character or emoji will preserve the icon family's appearance across operating systems, fonts, and presentation modes. An emoji can become multicolor artwork, change proportions, or be announced with an unexpected name. A font fallback can change an arrow's weight or directionality behavior. Use a controlled asset for a fixed interface glyph, and give the surrounding control the appropriate meaning.

Keep meaningful textual notation available as text when selection, copying, shaping, or adaptation matters. If the visual treatment uses a custom asset, preserve the equivalent meaning programmatically. Test actual rendering and assistive output rather than assuming the character's codepoint supplies the correct product label.

### Budget delivery and failure behavior

Import only needed icons where the build supports it. Verify actual bundle output rather than assuming a package is tree-shaken. Avoid dynamic import patterns that include an entire catalog accidentally.

Cache shared assets appropriately and reserve layout space to prevent shifts. For delayed or failed assets, preserve the control's meaning through text or a tested fallback. An accessible name helps assistive technology, but a blank unlabeled visual button still fails many sighted users.

Provide the formats and color spaces required by the target. A valid web SVG does not establish a valid print PDF, native symbol template, or adaptive launcher asset. Proof each delivered format through its actual renderer.

## 23. Implement accessible web icons

### Labeled action with a decorative glyph

This complete fragment provides a visible name, a larger target, and an SVG that inherits the text color. The icon is decorative because the button text supplies the meaning.

```html
<button class="download-button" type="button">
	<svg
		class="icon"
		viewBox="0 0 24 24"
		width="24"
		height="24"
		fill="none"
		stroke="currentColor"
		stroke-width="2"
		stroke-linecap="round"
		stroke-linejoin="round"
		aria-hidden="true"
		focusable="false"
	>
		<path d="M12 3v12m-4-4 4 4 4-4M4 16v4h16v-4" />
	</svg>
	<span>Download invoice</span>
</button>

<style>
.download-button {
	display: inline-flex;
	align-items: center;
	justify-content: center;
	gap: 0.5rem;
	min-inline-size: 3rem;
	min-block-size: 3rem;
	padding: 0.625rem 0.875rem;
	border: 1px solid currentColor;
	border-radius: 0.375rem;
	background: #fff;
	color: #174ea6;
	font: inherit;
}

.download-button .icon {
	inline-size: 1.5rem;
	block-size: 1.5rem;
	flex: none;
}

.download-button:focus-visible {
	outline: 3px solid currentColor;
	outline-offset: 3px;
}

@media (forced-colors: active) {
	.download-button {
		color: ButtonText;
		background: ButtonFace;
		border-color: ButtonText;
	}
}
</style>
```

Attach the actual download behavior through the application. Use a link with a meaningful destination when the operation is navigation to a downloadable resource. This drawing is an educational example, not a prescribed family asset.

### Icon-only action

An icon-only close control can put its name directly on the button. Reuse the target and focus conventions above, provide an appropriate visual treatment, and wire it to close the intended interface.

```html
<button type="button" class="icon-button" aria-label="Close preview">
	<svg
		viewBox="0 0 24 24"
		width="24"
		height="24"
		fill="none"
		stroke="currentColor"
		stroke-width="2"
		stroke-linecap="round"
		aria-hidden="true"
		focusable="false"
	>
		<path d="m6 6 12 12M18 6 6 18" />
	</svg>
</button>
```

```css
.icon-button {
	display: inline-grid;
	place-items: center;
	min-inline-size: 3rem;
	min-block-size: 3rem;
	padding: 0.625rem;
	border: 1px solid currentColor;
	border-radius: 0.375rem;
	background: Canvas;
	color: CanvasText;
}

.icon-button:focus-visible {
	outline: 3px solid currentColor;
	outline-offset: 3px;
}
```

The SVG has no competing title and no separate tab stop. Add a supplemental tooltip if it helps the context, following the tooltip requirements. Do not use this pattern to remove necessary visible labels from unfamiliar actions.

### Toggle with stable name and explicit state

The following standalone example keeps "Mute" as the label and exposes whether it is pressed. The demonstration updates the button's UI state. Connect the same state to the actual media behavior in a product.

```html
<button id="mute" type="button" aria-pressed="false">
	<svg
		viewBox="0 0 24 24"
		width="24"
		height="24"
		fill="none"
		stroke="currentColor"
		stroke-width="2"
		stroke-linecap="round"
		stroke-linejoin="round"
		aria-hidden="true"
		focusable="false"
	>
		<path d="M4 9h4l5-4v14l-5-4H4Z" />
		<path id="mute-slash" d="m3 3 18 18" hidden />
	</svg>
	<span>Mute</span>
</button>

<style>
#mute {
	display: inline-flex;
	align-items: center;
	gap: 0.5rem;
	min-block-size: 3rem;
	padding: 0.625rem 0.875rem;
	border: 2px solid currentColor;
	border-radius: 0.375rem;
	background: Canvas;
	color: CanvasText;
	font: inherit;
}

#mute [hidden] { display: none; }
#mute[aria-pressed="true"] { border-style: double; }
#mute:focus-visible { outline: 3px solid currentColor; outline-offset: 3px; }
</style>

<script>
const muteButton = document.getElementById("mute");
const muteSlash = document.getElementById("mute-slash");

muteButton.addEventListener("click", () => {
	const nextPressed = muteButton.getAttribute("aria-pressed") !== "true";
	muteButton.setAttribute("aria-pressed", String(nextPressed));
	muteSlash.toggleAttribute("hidden", !nextPressed);
});
</script>
```

The slash supplies a non-color state difference. In a production asset, refine its clearance from the base and proof it at the target size. Use unique component identifiers or scoped references if multiple instances appear. Do not copy the fixed IDs into a repeated template unchanged.

### Informative and redundant status

If a visible status label says "Payment failed," an adjacent error symbol can be hidden from assistive technology because the text carries the information. If the icon is the only content, supply an equivalent accessible text alternative and consider whether sighted users also need a visible label.

For a standalone informative inline SVG, `role="img"` with an appropriate accessible name is a common pattern. Use either a direct label or a unique referenced title according to the component contract, then verify the actual accessibility tree. Avoid adding both an unrelated label and title that compete for ownership.

Dynamically changing a decorative SVG does not announce a meaningful status change. Use the application's appropriate status or alert mechanism for messages that need announcement, with priority and repetition suited to the event.

## 24. Govern contributions and releases

### Review the request before the drawing

A contribution request should identify the meaning, usage location, visible label, nearest existing icons, required sizes, direction policy, and why reuse or text is insufficient. Review duplicate concepts and possible aliases before adding an asset.

Approve the concept and family fit early. A polished new icon can still be an unnecessary synonym for an existing one or a semantic collision with a nearby command.

### Assign ownership

Name who owns metaphor decisions, visual construction, accessibility behavior, code generation, licensing, and release. One person may hold several roles, but none should be implicit.

Separate the canonical asset from product-specific role mapping. A new use of a lock for "editing disabled" may need semantic review even when the drawing is unchanged. A redesigned lock may affect many products even when its name is unchanged.

### Make contributions reproducible

Require an editable source, production export, metadata, at-size proof, and usage example appropriate to the change. Compare additions with the pilot/reference set and closest neighbors. Check licensing and provenance for borrowed geometry or references.

Automate mechanical checks that have clear pass conditions, such as valid SVG, expected viewBox, missing metadata, duplicate identifiers, accidental raster images, unsupported paint, or unmapped variants. Keep visual and semantic review separate. Passing a linter does not establish comprehension or family quality.

### Classify release impact

Treat identifier removal, changed semantics, changed viewBox or alignment, removed size masters, altered direction policy, and changed component API as potentially breaking changes. A visual refinement can also affect layout, recognition, or state distinction.

Document changed drawings and mappings in release notes. Publish design libraries and code packages from the same approved source or reconcile their versions explicitly. Provide before/after proof for changes that affect many consumers.

### Deprecate with a migration

Mark the old asset or role as deprecated, name its replacement, state whether meaning or appearance changes, and provide a migration period appropriate to the system. Retain aliases when safe and useful. Do not silently reuse an old identifier for a new concept.

Keep a record of deliberate exceptions, rejected metaphors, and relevant comprehension findings. A short rationale can prevent later contributors from reintroducing a known confusion. Avoid keeping obsolete alternatives prominent in the default catalog.

## 25. Proof, test, and diagnose

### Build a proof ladder

Review the result at several levels because each reveals a different kind of failure.

| Level | What to inspect | Failure it can reveal |
| --- | --- | --- |
| Source geometry | Curves, joins, counters, overlaps, coordinates, reusable parts | Kinks, spikes, accidental tangencies, unstable source |
| Family specimen | Uniform-size rows and varied neighboring forms | Apparent scale, weight, density, or style outliers |
| Small-size output | Actual-size production render, low-density where relevant | Lost detail, clogged gaps, weak strokes, phase problems |
| Component | Real text, container, target, states, and focus | Alignment, hierarchy, clipping, naming, interaction |
| Product context | Actual toolbar, navigation, data, and content | Confusion, poor findability, false affordance |
| Adaptation | Themes, forced colors, zoom, languages, RTL, reduced motion | Hidden content, wrong direction, lost state |
| Delivery | Shipped SVG, native resource, raster or physical proof | Export differences, identifier collisions, resampling, production loss |

Do not stop at the magnified source or a contact sheet. The proof that matters is the delivered icon doing its intended job.

### Use a varied specimen

Include the easiest and hardest forms in the same proof. A useful family sheet contains simple lines, circles, squares, narrow and wide objects, diagonals, organic curves, people, dense symbols, modifiers, and confusion pairs.

Show supported sizes and styles with labels. Include light and dark backgrounds, selected surfaces, meaningful color roles, and a monochrome view. Keep the sheet honest by using actual approved assets and sizes rather than manually enlarged outliers.

For a product proof, include short and long labels, repeated rows, missing icons, loading, errors, disabled actions, expanded text, and more than one instance of any asset using IDs or clipping. These are realistic conditions, not separate visual directions.

### Test the questions that remain uncertain

| Question | Appropriate method | Evidence to record |
| --- | --- | --- |
| Can people identify the depicted form? | Unlabeled recognition prompt | Unprompted descriptions and recurring confusions |
| Can people predict its function? | Interpretation prompt with limited task context | Expected actions and consequential wrong interpretations |
| Can they find it? | Realistic task in the actual layout | First selection, time, hesitation, missed location |
| Can they activate it? | Keyboard, touch, pointer, and relevant assistive technology | Misses, wrong activations, focus and naming behavior |
| Does the family fit visually? | At-size comparison and targeted preference feedback | Outliers and reasons, separate from task success |
| Did a redesign help? | Controlled comparison with stable surrounding variables | Task outcomes and uncertainty, not click rate alone |

Recruit people who represent the intended audience, including relevant domain knowledge, languages, and access needs. Avoid priming the answer through labels or task wording when testing independent interpretation. Use the labeled real interface when testing the actual product flow.

Set acceptance criteria before interpreting results, proportionate to the consequences. A confusing low-priority decorative category differs from a destructive action or emergency sign. Do not claim universal recognition from a small convenience sample or invent an acceptable percentage without a basis.

A click-rate increase can reflect curiosity or misunderstanding. Examine whether people completed the intended task and whether wrong actions increased. Preference for a drawing does not establish that its meaning is clear.

### Diagnose before adjusting

| Symptom | Likely causes to inspect | First useful correction |
| --- | --- | --- |
| One icon looks too small | Sparse silhouette, narrow proportion, inappropriate keyshape | Compare painted extent and mass with references |
| One icon looks too heavy | Dense joints, filled area, small counters, excessive detail | Open spaces or simplify before reducing all strokes |
| Icon looks low or off-center | Asymmetric visible mass, modifier weight | Apply a small documented optical shift |
| Straight strokes blur | Edge phase, fractional layout, unsupported scale | Inspect final mapping and placement |
| Curves look jagged | Forced crisp-edge hints, poor raster scale | Restore suitable antialiasing and output resolution |
| A small icon becomes a blob | Too much detail, inadequate gaps, wrong master | Simplify or use a small optical design |
| Icon and label feel unrelated | Wrong weight, scale, gap, alignment, or metaphor | Compare the whole labeled component |
| Users recognize the object but choose wrongly | Semantic distance or competing meaning | Change mapping, label, or metaphor |
| Similar commands are confused | Shared silhouette or reused metaphor | Strengthen diagnostic differences and labels |
| Dark mode exposes a white patch | Fake cutout or hardcoded surface | Use transparency or a theme-owned backing |
| Repeated icons render incorrectly | Duplicate mask, gradient, or title IDs | Scope identifiers per asset instance |
| Screen reader repeats the action | Multiple competing name sources | Assign the name to one owner |
| Screen reader reports the wrong state | Action model and toggle model conflict | Reconcile label, graphic, and state semantics |
| RTL changes meaning | Blanket mirroring or incorrect metadata | Apply per-asset semantic direction policy |
| Filled state is invisible | Both states have similar mass or selection relies on hue | Add a stronger persistent selection cue |
| Toolbar becomes cramped | Too many actions or targets reduced to glyph bounds | Regroup and overflow lower-priority commands |
| Print loses internal detail | Process gain, insufficient reversed gaps | Create and proof a production-specific variant |
| Family drifts over time | Unreviewed exceptions or source/package mismatch | Restore canonical rules and synchronized releases |

### Separate checks from claims

Record which browsers, devices, themes, sizes, locales, output formats, and assistive technologies were actually checked. Name gaps. A valid SVG does not prove a working button. A working button does not prove an understood metaphor. A successful recognition test does not prove a compliant sign installation.

## 26. Use the guide in a project

### Creating an individual icon

1. Establish the meaning, label, use size, neighbors, and audience.
2. Check for an existing asset or a clearer text treatment.
3. Inspect the host family's grammar and nearest examples.
4. Develop the silhouette and diagnostic features at the smallest use.
5. Resolve curves, counters, junctions, optical scale, and center.
6. Proof the delivered asset inside its actual component and states.
7. Add metadata, direction policy, source, and approved export.

An individual icon is complete when it communicates its intended meaning in context, fits its family, survives required output, and has a correct application contract. A clean source file alone is insufficient.

### Creating a family

Begin with an inventory of concepts and confusing neighbors. Define the visual direction and draft grammar. Build a varied pilot, prove its smallest use and hardest compositions, then revise the grammar before expanding the catalog.

Expand by related concept and construction groups so reuse remains visible. Review each addition both within its group and among the whole family. Add optical masters, weights, modifiers, or styles only when a real use requires them.

Deliver the sources, production formats, metadata, usage rules, proof, and maintenance process together. An asset folder without semantics and ownership is an incomplete system.

### Applying icons in a product

Inventory every icon role and map each one to a meaning, asset, label, component, target, state model, color, and direction policy. Remove icons that do not improve the task. Resolve repeated meanings and inconsistent metaphors before polishing alignment.

Proof representative components with real content, supported themes, text adaptation, localization, and keyboard use. Verify exported and packaged assets match the design source. Keep native behavior where the platform supplies it correctly.

### Completion criteria

A project using this guide is ready when the relevant conditions are satisfied.

- Each meaningful icon has an explicit function and a label strategy suited to its audience and consequences.
- Nearest concepts and likely confusion pairs remain distinguishable.
- The family has a coherent construction grammar and documented optical exceptions.
- Supported sizes and variants preserve identifying features, open spaces, scale, and weight.
- Composition with text, containers, and neighboring content has been checked in actual output.
- Interactive icons have correct roles, names, targets, focus, states, and keyboard behavior.
- Color, themes, reduced motion, localization, and direction preserve meaning.
- Required production formats retain intended paint, transparency, geometry, and alignment.
- Source, asset registry, component package, catalog, licenses, ownership, and release state agree.
- Verification records distinguish observed results from assumptions and untested conditions.
