---
name: typography
description: "Comprehensive typography reference for letter construction, optical correction, spacing, family design, composition, font selection, semantic systems, accessible implementation, multilingual use, and production."
version: "0.1.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Karen Cheng"
  - "World Wide Web Consortium"
  - "Unicode Consortium"
  - "Microsoft Typography"
  - "Rainer Erich Scheichelbauer"
  - "Apple"
  - "IBM Carbon Design System"
  - "MDN contributors"
  - "Katie Hempenius"
  - "Barry Pollard"
  - "Matthew Butterick"
  - "Aileen Xin"
  - "Ilya Greben"
  - "Kenneth Wang"
type: reference
status: experimental
---

# Typography

Typography gives language a visible structure. Its smallest decisions concern the shape of a stroke and the white space beside it. Its largest decisions concern how a publication, product, or identity speaks, organizes information, and accommodates its readers. Make those decisions together. A well-drawn alphabet can fail through poor spacing, a good text face can fail in an unsuitable role, and a coherent scale can fail when content or user settings change.

Use this reference to design letterforms, evaluate fonts, compose text, and build systems for print and digital use. The detailed construction guidance concerns Latin type. The principles of testing in context transfer widely, but Latin anatomy, proportions, case, spacing, and hierarchy do not describe every writing system.

**Requirements** protect meaning, access, correct encoding, and delivery. **Defaults** provide a workable starting point. Numerical aesthetic ranges are hypotheses to test with the actual font, content, output, language, and audience. A deliberate exception needs a purpose and a proof, rather than an appeal to a universal rule.

## Contents

1. [Start with the reading task](#1-start-with-the-reading-task)
2. [Understand the units and anatomy](#2-understand-the-units-and-anatomy)
3. [Read history and character in forms](#3-read-history-and-character-in-forms)
4. [Define the construction system](#4-define-the-construction-system)
5. [Correct geometry optically](#5-correct-geometry-optically)
6. [Construct Latin capitals](#6-construct-latin-capitals)
7. [Construct Latin lowercase](#7-construct-latin-lowercase)
8. [Design numerals and mathematical signs](#8-design-numerals-and-mathematical-signs)
9. [Design punctuation and symbols](#9-design-punctuation-and-symbols)
10. [Design diacritics and language coverage](#10-design-diacritics-and-language-coverage)
11. [Space and kern the font](#11-space-and-kern-the-font)
12. [Build weights, styles, and optical sizes](#12-build-weights-styles-and-optical-sizes)
13. [Engineer and release a usable font](#13-engineer-and-release-a-usable-font)
14. [Select and combine typefaces](#14-select-and-combine-typefaces)
15. [Compose readable paragraphs](#15-compose-readable-paragraphs)
16. [Build hierarchy and page rhythm](#16-build-hierarchy-and-page-rhythm)
17. [Apply typography to the medium](#17-apply-typography-to-the-medium)
18. [Build a typography system](#18-build-a-typography-system)
19. [Implement web typography](#19-implement-web-typography)
20. [Load fonts and design fallbacks](#20-load-fonts-and-design-fallbacks)
21. [Preserve accessibility](#21-preserve-accessibility)
22. [Compose across languages and scripts](#22-compose-across-languages-and-scripts)
23. [Proof and diagnose](#23-proof-and-diagnose)
24. [Use the guide in a project](#24-use-the-guide-in-a-project)

For a font project, begin with sections 1 and 4, then use the construction, spacing, family, and engineering sections as a loop. For a publication, begin with sections 1 and 14, establish the body paragraph, and develop the page around it. For a product, begin with the reading tasks and real components, then specify roles, implementation, and accessibility. Use the diagnosis table when something looks wrong but its cause is unclear.

## 1. Start with the reading task

### Write a brief that changes decisions

Define the reader, content, conditions, and intended voice before choosing a family or drawing a letter. Record the following information.

| Decision | Questions the brief must answer |
| --- | --- |
| Function | Is this continuous reading, scanning, wayfinding, comparison, identification, display, or a combination? |
| Content | Which actual words, names, numbers, symbols, and extremes must work? How much text is typical? |
| Reader | What languages, reading experience, visual needs, and familiarity with the subject matter apply? |
| Conditions | At what size, distance, lighting, resolution, material, and duration will people read? |
| Voice | Which qualities should be visible, and which associations should be avoided? |
| Coverage | Which scripts, localized forms, figures, punctuation, weights, italics, and features are required? |
| Delivery | Which platforms, publishing formats, loading budgets, licenses, and production constraints apply? |
| Success | What must a reader recognize, find, understand, or do? What proof would reveal failure? |

A useful direction connects tone to visible properties. For example, a public information service might need an open, unhurried voice expressed through moderate proportions, clear apertures, robust strokes, plain labels, and room for translation. An experimental music poster might use extreme width contrast and a dense title while giving time, venue, and access details a quieter, immediately readable treatment.

A list such as "elegant, premium, modern" is incomplete. Decide whether elegance means fine contrast, broad spacing, restrained hierarchy, fluid calligraphic forms, or something else. Those choices produce different results and have different costs.

### Separate kinds of success

**Legibility** concerns distinguishing characters and signs. **Readability** concerns sustained reading in a particular arrangement. **Hierarchy** helps people understand relationships and find a path. **Expression** gives the text a voice. **Fitness** includes language coverage, behavior, economy, licensing, and production.

Evaluate each separately. An unmistakable display letter may make a poor paragraph. An economical body face may look too quiet for a title. A family can have strong brand associations and insufficient currency or language support. No classification guarantees success across these tasks.

### Choose the appropriate kind of type work

- Use an existing family when its design, coverage, and behavior meet the brief.
- Commission or create a typeface when a recurring need justifies a reusable character system and its maintenance.
- Draw lettering when a fixed word or phrase needs composition-specific forms. A successful logo does not imply a usable alphabet.
- Make a revival when historical material provides a meaningful starting point. Define the source, intended fidelity, target size, and permitted modernization.
- Use an exploratory or modular alphabet when its constraints support the work. Distinctive construction still needs an explicit readability boundary.

A revival requires interpretation. Compare original drawings, proofs, printed specimens, sizes, and later revisions. Ink spread, worn sorts, scanning, and reproduction can change the apparent design. Record which source governs each disputed feature. Correcting a technical artifact and erasing an intentional characteristic are different decisions.

## 2. Understand the units and anatomy

### Distinguish the design, file, character, and glyph

A **typeface** is the designed system of forms. A **family** groups related styles. A **font** is a usable implementation of a design, commonly a file. A static font usually represents one style. A variable font can represent a range of styles through axes.

A **character** is an abstract textual unit. A **glyph** is a visible form used to represent text. One character can have several glyphs, and several characters can form one glyph. Keep the underlying characters intact when selecting ligatures, alternates, or localized forms. Visual substitution must not corrupt search, copy, pronunciation, or reading order.

### Measure the coordinate system correctly

| Term | Meaning and consequence |
| --- | --- |
| Em | A scale unit tied to the selected font size. In a font source, units per em define its coordinate grid. The em is not the outline width of M. |
| Point | In common digital publishing, 1/72 inch. A 12-point font describes a body scale, not a 12-point visible capital. |
| CSS pixel | A reference unit. It is not necessarily one device pixel or a fixed physical measurement on screen. |
| Font size | Scale applied to the font's em. Equal sizes in different families can have very different apparent sizes. |
| Baseline | Reference line on which most Latin letters appear to sit. Rounded forms can extend below it. |
| x-height | Height of the lowercase body, conventionally measured with x. It strongly affects perceived size and texture. |
| Cap height | Height of flat-topped capitals. It need not equal ascender height. |
| Ascender / descender | Portions extending above the lowercase body or below the baseline. They provide differentiation and require vertical space. |
| Advance width | Distance by which text advances after a glyph. It includes spacing, rather than only the inked outline. |
| Sidebearings | Space between the outline and its advance boundaries. They can be asymmetric or negative. |
| Bounding box | The extent of the visible outline. It differs from the advance and the line box. |
| Line height / baseline distance | Distance between successive lines in ordinary horizontal composition. It is not simply the visible gap between letters. |
| Leading | Traditionally, extra spacing between type bodies. Modern software often uses the term for total baseline distance. Check the application's meaning. |

For a 1,000-unit em, an x-height of 500 units becomes half the selected font size before other adjustments. That example explains scaling, not an ideal proportion. A font with 2,048 units per em can represent the same visible design.

Read size/leading notation carefully. A setting written as `12/15` commonly means 12-point type on a 15-point baseline distance. It does not mean a 15-point visible gap. CSS defines 1 point as 4/3 CSS pixels, but physical screen appearance still depends on display and viewing conditions.

In CSS, `rem` relates to the root font size, `em` to the relevant element's font size, and `ch` to the advance of the zero glyph. A width of `65ch` does not guarantee 65 average characters in a proportional face. Measure representative lines as well.

### Learn anatomy through relationships

A **stem** is a main stroke. A **bowl** encloses or partly encloses a space. A **counter** is the white space within a form. An **aperture** is an opening into that space. A **crossbar** connects strokes. An **arm** projects without joining another main stroke at one end. A **shoulder** is an arch, as in n. A **spine** is the changing curve of S. A **terminal** ends a stroke. A **serif** is an added finishing element. A **bracket** joins a serif to a stroke. A **spur**, **ear**, **link**, **loop**, and **tail** describe distinctive small structures.

Use these terms to identify a problem precisely. "The e is weak" might mean its eye is too small, its crossbar is too heavy, its aperture closes, or its width disrupts the paragraph. Each needs a different correction.

## 3. Read history and character in forms

### Use history to explain constraints

The following is a broad account of Latin printing traditions. Periods overlap, revivals reinterpret their sources, and classification names vary. These categories help describe forms. They do not rank quality or encompass the history of world typography.

Capitals and lowercase have different histories. Inscriptional capitals informed monumental forms, while faster manuscript hands developed other structures over centuries. Humanist scribes and printers drew on manuscript traditions, including Carolingian minuscule, in forming the lowercase used in early roman printing types. This helps explain why lowercase letters are not miniature capitals and why their proportions need a separate design logic.

| Tradition | Structural clues | Useful context and cautions |
| --- | --- | --- |
| Inscriptional capitals | Varied widths, clear stroke construction, carefully balanced monumental forms | Stone and brush traditions inform classical cap proportions. They do not supply one compulsory grid for a digital family. |
| Humanist / Venetian serif | Strong pen-derived construction, oblique stress, often a sloping e bar and small x-height | Early Italian printing translated manuscript forms into repeatable type. Contemporary versions vary considerably. |
| Garalde / oldstyle serif | Oblique stress, modulated strokes, bracketed serifs, differentiated widths | Often supports a literary or historical voice. Specific cuts differ in size, darkness, and economy. |
| Transitional serif | More vertical stress, increased contrast, more regular construction | Often combines pen-derived detail with a more deliberate drawn structure. "Transitional" does not mean unfinished. |
| Didone / modern serif | Vertical stress, strong thick-thin contrast, fine unbracketed serifs | Can carry a formal, dramatic voice. Delicate display cuts can lose their hairlines in small or rough reproduction. |
| Slab serif | Substantial serifs, often low contrast, bracketed or unbracketed construction | Grew with commercial display needs. Later humanist and text slabs extend far beyond that origin. |
| Grotesque sans | Low contrast with historically varied proportions, terminals, and details | Can provide a direct or industrial voice. Irregularity can be part of its coherence. |
| Neo-grotesque sans | More systematic construction and repeated cuts, often compact apertures | Can support an even, restrained texture. "Neutral" describes a use or association, not absence of character. |
| Geometric sans | Circular or geometric skeletons, repeated simple forms | Can feel constructed or emphatic. Successful examples still contain optical corrections and exceptions. |
| Humanist sans | Pen-related proportions, differentiated structures, often open apertures | Frequently useful for information and signage, subject to actual recognition tests. |
| Script, blackletter, incised, decorative, and experimental forms | Distinct construction traditions or deliberate departures | Use specific descriptions and cultural context. These are substantial fields, not a leftover category of novelty fonts. |
| Monospaced designs | Equal advances across the supported set | A spacing constraint rather than one historical style. Proportions and punctuation must adapt to that constraint. |

Metal type encouraged size-specific cutting and imposed physical spacing limits. Phototypesetting enabled close overlaps and new display treatments. Digital outlines made scalable reuse easy, sometimes at the expense of optical size distinctions. Variable fonts restore fine control over multiple design dimensions, but only when those dimensions are actually designed and implemented.

For a rough chronology, Venetian printing types developed in the fifteenth century, with influential French oldstyle designs following in the sixteenth. Transitional and Didone traditions developed across the eighteenth century and into the nineteenth. Slabs and early commercial sans serifs expanded the display vocabulary in the nineteenth. Twentieth-century modernist, humanist, photographic, and digital approaches multiplied the available models. These are overlapping developments in Latin type, rather than a single progression toward a superior form.

### Describe emotional character as a hypothesis

Associations come from form, language, cultural memory, repeated use, content, and composition. A Didone can suggest fashion in one context and an official announcement in another. Rounded terminals can feel welcoming, childish, mechanical, or clinical depending on the rest of the work.

Translate a desired impression into observable choices, then test it with representative content.

| Desired tendency | Properties worth exploring | Failure to watch for |
| --- | --- | --- |
| Quiet, sustained reading | Moderate contrast, steady spacing, clear differentiation, restrained emphasis | Excessively pale or undifferentiated text |
| Formal authority | Disciplined proportions, stable rhythm, deliberate cap treatment | Stiffness, small text, or reliance on an unfamiliar historic association |
| Warmth | Humanist movement, softened joins, generous but connected spacing | Sentimentality or indistinct shapes |
| Technical precision | Clear numerals, dependable punctuation, regular alignment, controlled widths | Monospace used for long prose solely to signal technology |
| Energy | Condensed scale, angular gesture, decisive contrast or rhythm | Aggression, collision, or constant emphasis |
| Luxury or delicacy | Fine detail, ample space, controlled contrast, precise production | Hairline loss and unreadable functional information |
| Play | Unexpected proportions, animated terminals, selected alternates | Every glyph competing for attention |

Avoid gender, personality, or cultural stereotypes as design rules. Validate tone with the intended readers when the association matters. Do not claim that a stylistic choice proves trustworthiness, comprehension, or conversion.

## 4. Define the construction system

### Set a floor plan before polishing details

Establish the relationships among cap height, x-height, ascenders, descenders, width, weight, contrast, and spacing. Choose the intended optical size and output. Keep these relationships adjustable while the first words develop.

Distinguish three different dimensions.

- **Stress** describes where curved strokes carry their weight.
- **Contrast** describes variation between thick and thin strokes.
- **Posture** describes whether the overall form stands upright or leans.

An upright letter can have oblique stress. An italic is not defined only by a diagonal axis inside its bowls. Reverse contrast moves emphasis toward strokes that are thin in more conventional models.

### Establish a stroke logic

A broad nib held at a stable angle produces contrast through its direction of movement. A flexible pointed nib produces changing width through pressure. Constructed forms can instead follow a geometric, modular, or deliberately invented logic. Study the relevant tool movement even when drawing directly in software.

The term **ductus** describes the movement that makes a form, including stroke sequence, direction, and manner. Use it to explain why related letters distribute weight differently. If measuring contrast, state the convention. A thin-to-thick ratio decreases as contrast increases, while a thick-to-thin ratio increases. An unexplained percentage can reverse the intended comparison.

Record how this logic governs bowls, branches, serifs, terminals, joins, and endings. Related elements need a shared behavior, not identical outlines. The same tool meets a diagonal and a vertical at different angles. Copying one terminal everywhere can destroy the logic that initially made it coherent.

### Develop serifs, terminals, and endings

A serif system includes shape, length, thickness, angle, bracketing, and its transition into the main stroke. Wedge, slab, hairline, rounded, and cupped forms create different rhythms and reproduction demands. A bracket can soften a join and redistribute weight. A large bracket can also reduce the counter space beside it.

Distinguish finishing details by their position. A foot serif stabilizes a stem and occupies horizontal space. A beak on an open curve influences its aperture and balance. A ball or teardrop terminal adds local mass. That mass can help balance an open r or c, but can also close it at small size.

Check inner and outer serifs separately on diagonals. Their junction angles differ, and the outer serif can obstruct neighboring letters. Shortening an inner serif can relieve a congested m, while shortening an outer one can improve the fit of A or V. Preserve the family's character while making those corrections.

Sans serif endings still need a system. Horizontal cuts, vertical cuts, perpendicular cuts, rounded ends, flares, and tool-shaped terminals affect both aperture and gesture. Perpendicular cuts on a diagonal can extend past an alignment line and make the letter appear unusually tall. Rounded ends can look heavier than flat cuts. Test the endings across c, s, a, r, f, t, and the diagonals rather than selecting them independently.

### Start with revealing control characters

For a Latin text design, start with a small combination such as `n o h d a e s i`. It reveals straight strokes, curves, stem-bowl joins, branch behavior, ascender height, apertures, and character. Add capitals such as `H O E` early enough to compare cases.

For a cap-led display design, `H O E` establishes stems, curves, horizontal weights, width relationships, and endings. Add a complex letter such as R or S to test whether the proposed language can extend beyond simple forms.

A productive sequence is control shapes, short words, related groups, mixed-case text, then increasingly complete proofs. Do not finish the alphabet before asking whether the first letters work together. A striking a or g cannot compensate for a weak n/o rhythm.

### Balance consistency and individuality

Define which properties are structural constants and which can vary. A family might share curve tension, contrast, endings, and spacing while allowing unusually expressive Q and R tails in alternates. Another might use rigid modules as its central concept.

Test a signature feature in ordinary words. If each appearance creates a dark interruption or demands attention, decide whether the feature belongs in display use, an alternate, or the main text design. Avoid preserving a favorite letter at the expense of the system.

## 5. Correct geometry optically

### Judge the visible result at its intended size

Geometric equality is useful for constructing a starting point. Optical equality is the result to pursue when the brief calls for even text. Make corrections while comparing neighboring forms, then inspect both enlarged outlines and actual-size text.

| Optical problem | Likely correction | Important limit |
| --- | --- | --- |
| Round letters look short beside flat letters | Extend curves beyond alignment lines with overshoot | Amount depends on curvature, weight, size, and renderer. |
| A sharp point looks short | Extend the apex or vertex further than a blunt form needs | A broad flat point can need little extension. |
| Horizontal stroke looks heavy | Thin it relative to a corresponding vertical | Intended contrast can override this relationship. |
| Bowl looks weak beside a straight stem | Increase its maximum thickness while controlling the rest of the curve | Matching one measured location does not match total color. |
| Curve looks heavy at its thinnest point | Reduce the minimum and refine transition | Prevent a fragile hairline at output size. |
| Stacked lobes look top-heavy | Reduce the upper lobe and strengthen the lower | Expression can intentionally change this balance. |
| Central bar looks low | Move it toward the optical center | A's bar and some stylistic constructions follow different needs. |
| A thin diagonal seems discontinuous behind a thick stroke | Offset the segments enough to appear continuous | Need varies with contrast and crossing angle. |
| Straight-to-round joins look pinched or swollen | Ease curvature and redistribute the transition | Mere tangent alignment does not guarantee smooth-looking curvature. |
| A junction becomes a dark clot | Taper strokes, open the relief, or add a controlled trap | A large visible notch changes the style. |

### Control black and white together

**Typographic color** is the apparent darkness and texture of text, independent of its actual ink or screen color. A glyph's contribution depends on stroke area, counter shape, width, and surrounding space. Equal stem widths across every character rarely produce equal color.

When a form looks too dark, consider widening its counter, thinning a crowded region, changing a join, or altering width. Increasing sidebearings alone can create a dark letter surrounded by a pale hole. When it looks too light, removing space within the form can be more effective than tightening its neighbors.

A high x-height gives lowercase forms more area, but also reduces the relative distinction of ascenders and descenders. A very low x-height can require wider letters or a larger size. Choose the relationship for the reading task, rather than maximizing one measurement.

### Draw curves as systems

Draw the inner and outer contours independently enough to control their visible relationship. A counter is not necessarily an inset copy of the outside. An obliquely stressed O is not an upright ellipse rotated as one object.

Use as few points as the intended curvature needs. Place extrema where appropriate for the outline format and production process. Keep handles aligned at smooth joins, and inspect transitions for flat spots, bumps, or abrupt curvature changes. Balanced handles can be a useful starting point, but equal handle lengths are not a universal requirement.

Squared bowls can look pinched through their middle when straight sides meet rounded ends abruptly. Ease the transition or introduce a subtle curve to the apparently straight side. Do not assume that joining a rectangle to two semicircles produces a convincing O.

### Use optical correction deliberately

An experimental alphabet may intentionally preserve mathematical symmetry or uneven color. State where that effect belongs. Prove that readers can still identify the required content. The exception should serve a visible concept rather than excuse an unresolved drawing.

## 6. Construct Latin capitals

### Choose a proportional approach

Classical capitals often contrast broad round forms with distinctly narrow E, F, L, or S forms. More uniform systems adjust widths toward an even texture. Both approaches require optical correction. Historical square and rectangle constructions can explain a model without prescribing every width in a contemporary font.

Set O and H together. Compare the white area of the round and square structures, the weight of their curves and stems, and their rhythm in words. Establish E next if its width, arm lengths, or endings reveal more of the design's character. Avoid assigning every letter the width of a geometric box merely because it belongs to the same group.

### Develop groups with distinct corrections

| Group | Construction decisions | Proof and repair |
| --- | --- | --- |
| O | Set curve tension, stress, contrast, width, overshoot, and counter behavior | Compare `HOHO`. Check an apparently circular O for horizontal heaviness and an oval O for pinched sides. |
| C, G, Q | Derive curve behavior from O, then redraw for openness, added strokes, and tails | A sliced O can leave C too light. G can become dark through its throat. Q's tail can obstruct its counter or collide below. |
| E, F, H, I, L, T | Share stem and horizontal logic, with independent widths, arm lengths, and bar positions | Removing an E arm can leave F/L too pale. A broad T pushes adjacent letters away. I may need bars where recognition matters. |
| D, B, P, R | Coordinate straight stems with bowls and internal joins | D is usually redrawn rather than made from half an O. B's two bowls need independent size and weight. P/R bowls are not automatic copies of B. |
| S | Balance upper/lower lobes around a continuous reversing spine | Avoid a straight central diagonal, lumps where curves reverse, and apertures that turn it into B or 8. |
| J, U | Coordinate descending or bottom curves with the family's stems and endings | J's tail affects spacing and line clearance. A symmetrical heavy-stem U can need more width than a calligraphic U. |
| A, V | Set diagonal contrast, apex/vertex shape, taper, and overshoot | A's crossbar crowds its counter. V's counter and external wedges make its fit different from O. |
| W, M | Combine diagonals while managing multiple counters and width | Two unchanged Vs make W too wide. M's center can become a dark wedge. Inspect the inner spaces rather than only the outer silhouette. |
| X, Y | Balance crossing or branching diagonals | X can need staggered thin strokes. Y's branch point must balance a top-heavy fork against a cramped upper counter. |
| N, K, Z | Resolve hybrid structures, joins, and diagonal distribution | Thin N stems may need reinforcement. K's junction can clog. Z needs stable upper/lower balance and a deliberate thick-stroke direction. |

### Treat complex forms individually

**S.** Begin with the movement of the spine. Two unequal oval constructions can help establish a skeleton, but their junction needs redrawing into a continuous change of curvature. Establish the widest points, lobe sizes, terminals, and minimum strokes together. A lower lobe commonly needs more visual mass for stability. Test `SOS`, `HSH`, and words with repeated S forms. A beautiful isolated S may still be too narrow or too dark in text.

**B, P, and R.** B's upper bowl is commonly smaller and lighter than its lower bowl. Open its waist without creating an accidental notch. P has a large open lower area, so its bowl needs a different balance. R's leg fills that area but introduces a new diagonal gesture and difficult neighboring spaces. Decide whether the leg is straight, bowed, joined, or separated. Compare it with K and the tail of Q without forcing identical gestures.

**G.** Its internal stroke must distinguish it from C without closing it toward O. Adjust bowl width, throat height, spur, and stroke weight as a group. Proof G with following stems, as in `GI`, `GN`, and `Gl`, since a projecting bar can disturb fit.

**A and V.** Evaluate the dark junction and the shape of the counter. Taper the inner diagonals where necessary. A's bar often sits below the mathematical middle to open its upper counter and stabilize the letter. The outer serif lengths can differ from inner ones to permit better spacing. A rotated V is a construction aid, not a finished A.

**W and M.** Joined, overlapping, and cropped constructions create different counter rhythms. Removing an inner serif or changing the diagonal angle can improve color without losing the main idea. Keep the several triangular spaces related, while allowing unequal sizes. A central point need not extend as far as an exposed outside point.

**X and K.** Inspect continuity at the intersection and density at the join. K can have a single junction, a double junction, a bridge, or an open gap. The structure must work in the narrowest and heaviest intended style. A solution that survives only in a light master is incomplete.

### Compare capitals in use

Use repeated controls, varied words, punctuation, and mixed case. Include wide and narrow words, initials, abbreviations, and target-language capital patterns. German prose, for example, exposes capitals more often than many English text specimens. Track all-cap words separately from sentence-case fit. They need not have the same ideal spacing.

## 7. Construct Latin lowercase

### Establish rhythm before exceptions

The lowercase forms most of the texture in ordinary Latin prose. Set n and o together at the intended size. Use l to examine the ascender, but do not judge its weight alone. A single stem has a different visual contribution from a bowl or branch.

The o should share the capital O's curve behavior while accommodating a smaller body. It can need different width, contrast, and overshoot. A narrow capital O does not justify an equally narrow lowercase o if the counter then closes. Set uppercase and lowercase together throughout development.

### Work through related forms

| Group | Construction decisions | Failure to inspect |
| --- | --- | --- |
| o, l, n | Establish bowl, stem, branch, counter, and vertical proportions | O/o mismatch, excessively dark lowercase, or weak stem rhythm |
| b, d, p, q | Coordinate bowl/stem joins, reliefs, ascender/descender details, and stress | Mechanical reflection moves weight into the wrong places or erases intended differences |
| e, c | Redraw width and bowl weight around open sides, eye, bar, and terminals | e eye closes, c becomes pale, or `cl` resembles d |
| n, h, m, u | Share branch logic with changes for height, counter count, and orientation | m too wide or dark, u too pale, or branch joins forming spots |
| r | Balance the branch, terminal, stem, and white space underneath | `rn` resembles m, or the branch leaves a conspicuous hole |
| s | Redraw the S principle for the smaller body | A scaled cap becomes too dark or its spine develops a kink |
| a | Resolve bowl, upper arch, aperture, stem, terminal, and foot | Tiny lower counter, weak upper arch, unstable lean, or crowded foot relief |
| g | Coordinate bowl, link, loop, ear, and total depth | Dark upper bowl, pinched link, crowded lower loop, or projecting ear |
| i, j | Set tittle size, shape, height, and optical alignment | Dots disappear, collide with accents, or disconnect visually from stems |
| f, t | Shape hooks, bars, height, tails, and overhangs | Collisions with dots/ascenders and difficult spacing after f |
| v, w, y | Redraw diagonals at x-height and develop tail behavior | Congested joins, weak w rhythm, or y colliding below |
| k, x, z | Reconcile diagonal angles, counters, and junctions at reduced height | Dense k center, broken x diagonal, or disproportionate z |

### Avoid mechanical reflection

Letters such as b, d, p, and q may share components, but they arise through different stroke sequences. Reflection can put their stress, reliefs, and endings in inconsistent positions. Rotation can be a more useful starting point in some constructions, followed by individual correction.

The same applies to n and u. A rotated n can establish a skeleton, but the new lower curve, upper endings, and distribution of white require adjustment. Treat component reuse as a maintenance tool that remains subordinate to visible quality.

### Resolve the branch and relief

The n's shoulder determines much of the family's movement. Placing weight higher in the arch gives a different gesture from carrying it into a more vertical right stroke. The branch usually needs to thin as it leaves the left stem. Preserve enough white above the join for the intended output.

The m commonly needs narrower arches or reduced internal details. The h shares the n's branch but must relate to the ascenders. The r's branch ends early, so it needs its own curve and terminal balance. Do not assign all these letters identical widths, joins, or sidebearings.

Reliefs are the open notches around joins such as those in b and n. Increase their clarity through a steeper connection, reduced local thickness, a small change in stem shape, or a carefully designed trap. A deep trap can be functional at small size and conspicuous at display size. Prove both before using one outline for both jobs.

### Give a and g enough development time

A double-storey a combines two different spaces and a complex arch. Coordinate the shape of its lower bowl with the upper curve. An arch that implies a round construction and a bowl that implies an unrelated square construction can feel unresolved. Check the terminal and foot against c, r, and d. Watch for a stem that appears to lean even when its coordinates are vertical.

A two-storey g needs its small upper bowl to remain open while sharing color with larger letters. The link must connect clearly without forming a dark knot. The lower loop can be open or closed and often needs asymmetric shaping. The ear can connect the design to r or a terminals, but should not unnecessarily push the following letter away or force taller line spacing.

Single-storey a and g offer other rhythms and associations. Their suitability depends on distinctiveness, reader familiarity, size, spacing, and the brief. Include both as alternates when they solve real uses. Do not declare one structure universally more readable.

### Design f and its neighbors together

A generous f hook can collide with i, j, l, accented letters, and punctuation. Options include a narrower hook, contextual alternates, and standard ligatures. The ligature should look like a deliberate solution, preserve text meaning, and avoid an unexpected change in word spacing.

Draw t at its own intermediate height. Its bar and terminal relate to f but need not match. A high x-height leaves less room for both the f hook and the t's distinguishing upper section. Test these constraints before locking the family's vertical metrics.

## 8. Design numerals and mathematical signs

### Specify figure style and width separately

| Style | Use | Check |
| --- | --- | --- |
| Proportional oldstyle | Figures embedded in lowercase prose where their texture suits the publication | Ascenders/descenders, punctuation alignment, and ambiguity with letters |
| Proportional lining | Titles, general interface numbers, and mixed numeric text | Relationship to capitals and body size |
| Tabular lining | Tables, timers, counters, and changing measurements | Equal advances, stable alignment, decimals, signs, and currency |
| Tabular oldstyle | Tables whose editorial voice benefits from oldstyle forms | Availability, alignment, and whether varying heights aid or distract from comparison |

Lining versus oldstyle describes vertical form. Tabular versus proportional describes advances. Neither distinction implies the other. Tabular digits do not make every punctuation mark or currency sign share their width.

### Design the set as a set

- Distinguish 0 from O/o through proportion, height, contrast, or a designed alternate. A slashed or dotted zero can help identifiers, but should remain an alternate glyph for the digit zero, not a replacement character such as Ø or ∅.
- Distinguish 1 from I/l through a flag, foot, bar, or other structural cue. Prove actual identifiers rather than one isolated trio.
- Give 2, 3, 5, and 7 enough weight to balance their open sides. Their terminals, bowls, and cuts should relate to letters without becoming forced copies.
- Keep 4's triangular counter and multi-stroke junction clear. An open structure can help, but must remain recognizable to the audience.
- Test 6 and 9 independently. Rotating one can establish a starting point but does not guarantee matching balance.
- Coordinate 8's upper/lower counters, waist, and spine. The most complex figure often needs local thinning to match the others.

Tabular forms must be optically centered within equal advances. A narrow 1 often needs a different drawing from the proportional version. Verify the actual exported set, including all styles used in the product.

### Include the numeric ecosystem

Design or select decimal marks, grouping separators, colon, percent, per mille, plus, minus, equal, multiplication, division, fractions, currencies, superior/inferior figures, and scientific notation as required. A mathematical minus aligns with the operator axis and differs from a text hyphen. Check its relationship to plus and equal.

Use locale-aware number formatting. Decimal separators, grouping, signs, currencies, and spaces vary. Test negative values, zero, long values, percentages, dates, time, unit labels, and mixed scripts. Financial columns may need decimal alignment as well as tabular digits.

For extensive equations, use a math-capable font and layout engine. A general text font's scattered mathematical symbols do not establish complete mathematical typesetting support.

## 9. Design punctuation and symbols

### Make small marks visible and distinct

Punctuation contributes both structure and voice. Periods must survive small output. Commas need a tail distinguishable from a period. Colons, semicolons, quotes, and apostrophes need optical weight and placement appropriate to their context. Their resemblance to i dots or terminals can establish a relationship, but exact copying can make them too heavy or too weak.

| Marks | Construction and application decisions |
| --- | --- |
| Period, comma, colon, semicolon | Coordinate mass, tails, spacing, and vertical placement. Inspect decimal and time use as well as prose. |
| Quotes and apostrophe | Distinguish opening/closing direction where the language uses it. Test contractions, nested quotes, capitals, and accented neighbors. |
| Question and exclamation | Balance upper structure and dot, preserve the gap at small size, and match surrounding color. Include inverted forms for languages that need them. |
| Hyphen, en dash, em dash, minus | Give each its intended function, width, weight, and alignment. Do not assume the measured dash width always equals its historical name. |
| Parentheses, brackets, braces | Enclose the relevant vertical range. Provide or select case-sensitive forms when available. Test equations, all-caps, lowercase, and nested use. |
| Ellipsis | Test the designed glyph against the publication's required treatment. It should not become an accidental word space or a dark bar. |
| @ | Control the density of the enclosed letter and ring. Small forms often need lighter strokes or a larger body. |
| # | Preserve clear intersections and a counter large enough for reproduction. Match its intended text or number context. |
| Ampersand | Connect its gesture to the family while allowing distinctive construction. Confirm recognizability in names and short phrases. |
| Bullets and list markers | Match apparent weight and alignment to text. A mathematically centered dot may appear misplaced beside the lowercase body. |

### Preserve the intended character

Use actual prime marks for measurements when appropriate, rather than quotation marks. Do not substitute an acute accent for an apostrophe. Do not replace a minus with a hyphen simply because it is easier to type.

Choose quotation conventions, dash spacing, ellipsis treatment, and nonbreaking spaces through the language and publication style. In code, data, commands, identifiers, and literal strings, preserve required straight quotes and exact characters. Automatic typographic substitution must not alter executable or machine-readable content.

## 10. Design diacritics and language coverage

### Treat coverage as a design requirement

A list of Unicode code points is insufficient. Readers need correctly shaped and positioned forms, appropriate localized behavior, working combining sequences, and adequate line clearance. Define supported languages and scripts explicitly. Review with knowledgeable readers, especially when the designer does not use the language.

Design accents with the family. Do not finish an English-only alphabet, then squeeze all additional marks into the remaining space. Tall capitals, high x-heights, deep descenders, and stacked accents are interacting constraints.

### Give marks their own optical treatment

- Shape acute and grave for the language, weight, posture, and available space. Their placement is optical, not automatically centered by bounding box.
- Draw circumflex and caron as related but distinct marks when needed. Some letters use a side form of the caron that resembles a small apostrophe but has its own spacing.
- Adjust diaeresis dot size and separation to the parent letter. A narrow Ï and a broad Ö need not use the same dot spacing.
- Keep the tilde recognizable as a small changing curve rather than an indistinct bar.
- Distinguish cedilla, comma below, and ogonek. Romanian Ș/Ț use comma below. Turkish Ş uses cedilla. Similar appearance does not make the characters interchangeable.
- Test cap and lowercase marks separately. Capitals may need different accent drawings, but flattening every accent to avoid clipping is a poor substitute for adequate metrics.
- Preserve dotless and dotted forms correctly. Turkish and Azerbaijani casing, for example, cannot be handled by English assumptions about i/I.

Design ß and ẞ as letters in their own right, with clear distinction from B and Greek beta. Use language-appropriate casing and content rules rather than substituting by appearance.

### Test sequences, not only precomposed letters

Include precomposed and decomposed text, such as `é` and `e` followed by a combining acute. Test mark-to-base and mark-to-mark attachment, multiple accents, italic marks, and the extremes of weight and width. A font can contain all required components and still position them incorrectly.

Use anchors and reusable components to maintain relationships, then inspect exceptional letters. Language-specific forms may require dedicated glyphs and substitution rules. Validate actual word shapes, including Vietnamese stacked marks and other coverage beyond a basic Western European set when required by the brief.

## 11. Space and kern the font

### Establish spacing while drawing

The reader sees the interaction between outlines and surrounding white. Design sidebearings as part of each glyph's form. Base spacing should produce a convincing rhythm before pair-specific kerning begins.

1. Space n and o at the intended text size. Compare `nnnn`, `oooo`, `non`, and `noononno`.
2. Space H and O in repeated and mixed patterns.
3. Compare capitals with lowercase in strings such as `nHn`, `nOn`, and sentence-case words.
4. Extend the principles to related sides, then inspect open forms, diagonals, and single stems individually.
5. Add word space and punctuation. Proof paragraphs before refining only glamorous pairs.
6. Kern the remaining contextual exceptions after base fit is stable.

Round sides commonly need smaller measured sidebearings than flat sides because the open corners already contribute white. The right side of n may need a different bearing from its left. These are optical relationships, not fixed fractions to apply to every font.

### Judge area, rhythm, and grouping

Compare the white between letters with the white inside them, while preserving clear boundaries. Equal minimum gaps can look unequal because a wedge, an open bowl, and a rectangle distribute space differently.

Do not turn "spacing relates to counters" into an equation. Very light, very heavy, condensed, or expanded designs require separate judgement. State whether a change refers to absolute sidebearing values, space relative to a counter, or overall word density. These can move in different directions.

A repeated dark spot beside a single-stem letter can indicate poor sidebearings. A persistently dark glyph in every context usually needs an outline correction. A pale triangular hole around A/V/T can require both shape and fit changes. A fixed word space should separate words without breaking a paragraph into disconnected islands.

### Reconcile all-caps and mixed case

Capitals have larger internal spaces, but most running text uses them beside lowercase letters. Their base fit often favors mixed case. All-caps headings can therefore need additional tracking. Test rather than assuming that all uppercase text needs the same positive value.

Small caps are designed forms with weight and proportions suited to a smaller body. Reduced full-size capitals usually look too light. Their spacing and surrounding punctuation also need attention.

### Kern residual problems

Kerning adjusts particular contexts that sidebearings cannot resolve. Include pairs such as `AV`, `To`, `Ty`, `Wa`, `Yo`, `Ta`, and punctuation neighbors, but build the test set from the actual glyph inventory and languages.

Create directional classes for genuinely similar sides. The left and right class memberships of a letter can differ. Include accented letters and alternates when their profiles match, then add justified exceptions. Check interactions rather than only class membership counts.

Excessive pair exceptions can signal a bad class model, unstable spacing, or an unresolved outline. Automatic kerning can provide a starting point. It does not replace proofing.

In composition software, default to the font's metrics kerning. Use an optical algorithm when a specific font or mixed-font run benefits from it, and compare the result. Do not globally override a well-made kerning system because "optical" sounds more precise.

### Proof spacing at several scales

Use control strings to isolate relationships, real words to expose repetition, and paragraphs to judge texture. Include difficult pairs, repeated verticals, capitals, punctuation, digits, and mixed-language content. An all-pairs test helps reveal holes but does not replace natural text.

Inspect at intended size first. Large zoom often encourages excessively tight spacing. Use distance, inversion, or blur briefly to inspect abstract rhythm, then return to normal reading. Never approve a readable text face solely from abstract texture.

## 12. Build weights, styles, and optical sizes

### Plan a family around real roles

Choose the styles the work requires before generating a large matrix. A reading family might need regular, italic, semibold, and their optical adaptations. A headline family might prioritize width and extreme weight. A multilingual interface might need reliable medium/bold emphasis and broad language support more urgently than a thin display style.

Weight names and numbers are relative within a family. Two fonts labeled 400 can have different darkness. Match weight through specimens and actual content. Do not assume equal numeric steps create equal-looking differences.

### Redesign weight rather than outlining it

A heavier style needs more than adding thickness to every contour. Preserve counters, apertures, joins, and spacing as mass increases. Adjust width, contrast, terminals, dot size, and local reliefs where necessary. A light style needs coherent grouping and details robust enough for its intended use.

Select perceptually useful intermediate weights. A mathematical progression can seed the design, but the family should expose meaningful roles. Compare regular/bold pairs in running text, not only a graduated word specimen.

Distinguish **weight** from **grade**. Weight changes commonly affect widths and copyfit. A grade axis is intended to adjust darkness with little or no change to advances, depending on the design. Verify the actual family before using grade to preserve alignment or compensate for output conditions.

### Draw width as a design dimension

Condensing through a horizontal transform deforms curves, changes contrast, narrows counters, and alters terminal angles. Design condensed forms with corrected bowls, joins, proportions, and fit. Expanded forms also need deliberate management of internal white and stroke mass.

A designed width axis can solve limited spaces while retaining family character. It must not become an automatic shrink-to-fit mechanism for arbitrary content. Confirm recognition and minimum usable width, and allow layout changes when content needs them.

### Treat italic as a related voice

A true italic may change construction, proportions, spacing, joins, and individual letterforms. Slanting the upright can produce distorted curves and crowded joins. An oblique design can legitimately preserve more of the upright structure, but it still needs correction.

Proof italic beside upright text, in sustained passages when required, and with punctuation, capitals, accents, and ligatures. Long swashes or overhangs can break narrow columns. Bold italic should be designed or supplied when the content uses simultaneous emphasis.

### Design for optical size

Text designs often need more robust fine strokes, clearer counters, more open details, and spacing suited to small reproduction. Display designs can support finer contrast and more delicate detail. The exact direction and amount of change depend on the design and medium.

A display cut enlarged or reduced is still the same outline. A true optical design changes the outline and often spacing. An `opsz` axis can interpolate these decisions. It cannot invent them in a font without optical-size design data.

Test the smallest actual use, normal reading use, and the largest display use. A text cut can look coarse at headline size, while a beautiful display cut can become brittle in captions. Select a role-specific cut rather than repairing a fundamental mismatch with tracking alone.

### Inspect the whole interpolation space

Compatible masters need corresponding contour structures, nodes, start points, directions, and components for the chosen production method. Compatibility allows interpolation, but does not establish attractive intermediates.

Check named instances, midpoints, and combinations near axis extremes. Look for collapsed counters, wandering joins, mismatched marks, unstable spacing, curve kinks, and sudden substitutions. Multi-axis combinations can fail even when each axis looks good in isolation. Add intermediate control where needed and proof the exported font, not only the editor preview.

## 13. Engineer and release a usable font

### Separate drawing completion from font completion

A font is software as well as artwork. Before calling it usable, verify its encoding, names, metrics, shaping, features, style relationships, export, and delivery. Keep editable sources, build settings, proof materials, version history, and the distributed binaries identifiable.

| Layer | Required decisions and checks |
| --- | --- |
| Character map | Correct Unicode mapping and appropriate handling of alternates and unencoded glyphs. Avoid assigning unrelated characters to convenient slots. |
| Outlines | Clean contours, intended winding, closed paths, no stray points, correct overlap handling for the output format, and robust curves. |
| Components | Reliable dependencies, placement, and transforms. Ensure exported results preserve the intended forms. |
| Horizontal metrics | Advances, sidebearings, kerning, and equal-width sets where promised. |
| Vertical metrics | Ascender, descender, and line-gap behavior across target applications. Include accents, stacked marks, and script extents in clipping tests. |
| Naming and family metadata | Consistent family/subfamily identity, version, style links, and variable instance presentation. Confirm actual application menus. |
| Substitution and positioning | Working ligatures, alternates, localized forms, mark attachment, kerning, and script shaping as promised. |
| Rendering | Output-specific rasterization, hinting where useful, small-size consistency, and printer behavior. |
| Formats | Appropriate desktop, web, application, or document distribution formats. Verify the actual exported files. |
| Rights and delivery | License, attribution/notices, allowed uses, modification/subsetting permissions, and responsible maintenance. |

OpenType can contain different outline technologies. Do not treat "OpenType" and "TrueType" as mutually exclusive design-quality categories. File extensions alone do not establish feature coverage or rendering quality.

### Set metrics for real content

A visible capital is not the whole line. Test the highest marks and deepest descenders the supported scripts require. Confirm whether target applications derive default line spacing or clipping from different font metrics.

Keep family metrics coordinated so style changes do not unexpectedly move surrounding lines. Do not force a compact metric box by cutting off legitimate forms. A font's metrics and an application's line-height policy must work together.

### Build features conservatively

Keep required shaping active. Make discretionary decoration opt-in. Use substitutions that preserve logical characters. Localized glyphs need correct script/language registration and application support. Test feature combinations, not only each switch separately.

Provide the correct set of numeric and small-cap features when promised. Test selection, copying, search, accessibility, and PDF extraction. A glyph visible in a font editor's grid is not evidence that users can access it through normal text.

### Validate release artifacts

Install a uniquely identifiable test build to avoid confusing it with an older cached version. Test representative desktop and browser applications. Compare font menus, styles, punctuation, accents, layout, and export. Check for missing glyphs and incorrect fallback in real text.

Automated validators can catch malformed tables, naming defects, coverage problems, and other repeatable issues. Read their findings and confirm the relevant output. A validator cannot decide whether curves are beautiful, spacing is coherent, or language forms are culturally appropriate.

For a commission, deliver the agreed files, source ownership arrangements, documentation, coverage list, supported axes/features, and known limitations. Avoid promising unsupported languages simply because a general character range exists.

## 14. Select and combine typefaces

### Start with the hardest recurring reading task

For a publication, establish the body face first. For a data product, begin with representative labels, values, tables, and identifiers. For a poster, establish the headline and functional information together. Select display treatments only after the recurring content has a viable home.

Evaluate candidates with the same text, equivalent apparent size, comparable darkness, and intended output. Comparing family names at identical nominal point sizes can reward a large x-height rather than better design.

### Inspect more than a promotional specimen

Check the following before choosing a family.

- The actual cuts and files available, including italic, bold, width, and optical variants.
- Required scripts, localized forms, accents, symbols, punctuation, and numeric features.
- Recognition of confusable forms such as `Il1`, `O0o`, `rn/m`, and `cl/d` in the target context.
- Text color, spacing, word shapes, and the density of repeated characters.
- Real rendering on the intended devices or material.
- Fallback behavior, loading cost, document embedding, and application compatibility.
- License fit, provenance, version, distribution source, and maintenance expectations.

A historically named family may have many unrelated or differently interpreted digital versions. Record the foundry, exact cut, version, and source. "Use Garamond" is not a complete production specification.

### Choose a pairing strategy

Default to one capable family until a second family has a defined job. Add contrast through scale, weight, posture, width, and composition before assuming another family is necessary.

| Strategy | When it helps | What to control |
| --- | --- | --- |
| Single family | Coherent interfaces, restrained publications, flexible identities | Enough functional variation without invented styles |
| Superfamily | Related serif/sans/mono voices across a larger system | Match actual optical size and color, not just family branding |
| Contrasting display and text faces | A distinctive title voice alongside sustained reading | Shared visual balance with a clear role boundary |
| Editorial serif plus utility sans | Reading content with captions, navigation, labels, or data | Apparent size, punctuation, numerals, and baseline relationships |
| Specialized mono or numeric face | Code, identifiers, technical readouts, or aligned measurements | Use only where its equal advances or specialized glyphs help |
| Deliberately dissonant pairing | Expressive editorial or cultural work | A dominant voice, controlled repetition, and readable supporting information |

When pairing, compare x-height, cap height, width, contrast, curve behavior, stress, and terminals. Harmony can come from compatible proportions or deliberate contrast. There is no requirement to match every trait.

Avoid two nearly identical faces that create an unexplained discrepancy. Conversely, two very different faces need some compositional relationship, such as consistent alignment, shared rhythm, or a clear distribution of roles. An unusual pair can work when its tension is intentional and tested.

### Evaluate the system with actual language

Set the real headline, longest title, ordinary paragraph, short label, error message, dense table, and representative names. Include the languages and symbols the product will actually display. Compare alternatives in the same layouts rather than selecting solely from a row of family names.

Select for the intended lifespan. A highly fashionable display voice can be appropriate for a short campaign and expensive to maintain in a durable utility product. Familiarity can support recognition without making a face compulsory. A free font can be excellent, and a commercial font can be unsuitable. Judge the specific implementation.

## 15. Compose readable paragraphs

### Tune the paragraph as one unit

Family, apparent size, weight, measure, line height, tracking, word spacing, and paragraph separation interact. Adjust them together. Begin with real prose containing typical punctuation, emphasis, numbers, and words of varied length.

The following ranges are practical starting points for ordinary Latin text, not accessibility thresholds or universal optima.

| Variable | Starting point | Adjust when |
| --- | --- | --- |
| Web body size | About `1rem` for general UI text and `1.125rem` for a reading surface, respecting user defaults | The chosen font looks small, distance increases, content is dense, or user needs differ. |
| Print body size | Roughly 10–12 pt for ordinary close reading | Format, x-height, paper, audience, and print quality require a different size. |
| Prose measure | Roughly 45–75 characters per line, including spaces | Narrow screens, columns, captions, scripts, and content change the useful range. |
| Web prose line height | Roughly 1.45–1.65 times font size | Measure, x-height, marks, weight, and paragraph length affect how easily readers follow successive lines. |
| Print prose baseline distance | Roughly 1.2–1.45 times font size | Output, face, language, and page design call for more or less room. |
| Multi-line heading line height | Roughly 1.05–1.25 for uncomplicated Latin display text | Accents, descenders, italics, fallback, or script extents need more room. |
| Tracking | Start with the font's designed spacing | Particular sizes, all-caps use, poor fit, or expressive aims justify a change. |
| Paragraph separation | Begin with a clear gap of around half to one line, or a modest first-line indent | Genre and reading rhythm call for another convention. |

A font that needs a very different size is not necessarily defective. Its intended scale may differ. Avoid shrinking text to force a column to match a reference layout.

### Read measure and leading together

Long lines require a dependable return to the next line. More leading can help, but excessive leading separates the paragraph into stripes. Short lines need enough content to establish a reading rhythm without constant jumps.

If a paragraph feels tiring, inspect line length, contrast, size, and density before adding leading. A narrow mobile viewport should reduce measure naturally rather than trigger horizontal scrolling. A fixed maximum reading width can coexist with a wider page grid.

Use ragged alignment at the start edge as a robust default for ordinary web prose. Justified text needs a capable composition engine, language-aware hyphenation, and sufficient measure. Inspect rivers, stretched word spaces, repeated hyphens, and weak last lines. Do not justify a narrow column merely to make its edges square.

### Keep paragraph grouping unambiguous

Use either a consistent first-line indent or a gap as the primary signal in ordinary continuous prose. A publication can deliberately combine them, but two strong signals often waste space and weaken rhythm. The first paragraph after a heading commonly omits the indent.

Keep a heading closer to the paragraph it introduces than to the previous section. Related captions, notes, and list items need local grouping. Test spacing visually at the full page scale, rather than deriving every relationship from one multiplier.

### Manage line endings without damaging text

Use language-aware hyphenation where it improves the setting. Inspect proper names, technical terms, repeated hyphenation, and breaks across pages. Hyphenate through the composition system where possible, rather than inserting permanent hyphens into source content.

Watch for a final word stranded on a very short last line, a heading isolated from its text, and a paragraph line stranded across a page or column boundary. Publishing terms for widows and orphans vary. Define the specific failure rather than relying on the name alone.

For fixed editorial layouts, repair awkward endings through column width, modest spacing changes, paragraph editing with permission, or the composition settings. For responsive text, prefer robust wrapping. Hard line breaks and nonbreaking spaces can create new failures at another width or in another language.

### Track with restraint

Tracking is a uniform spacing adjustment across a run. Kerning concerns particular pairs. Tracking cannot fix a single bad pair without changing all the good ones.

Small all-caps labels may benefit from modest positive tracking. Large Latin display text may benefit from modest tightening. Values such as `0.04em` or `-0.02em` are trials to inspect, not defaults to paste globally. Preserve recognizable word grouping and check accented capitals.

Do not apply Latin tracking conventions to connected scripts. Even within Latin, a narrow face, a wide face, a text cut, and a display cut have different designed fit. Begin with zero added tracking and let the actual result justify changes.

### Use emphasis with a clear hierarchy

Use italics for local changes of voice or conventional emphasis and bold for stronger emphasis or scanning where the genre supports it. Avoid emphasizing so many words that a paragraph becomes a field of competing signals. Small caps can suit abbreviations or editorial distinctions when real small caps exist.

Underlining has an interaction meaning on the web. Keep inline links visibly distinguishable and check their underline against descenders and text weight. Do not use color alone to carry a necessary distinction. A publication's quotation, capitalization, dash, and numeral policies should remain consistent across the composition.

## 16. Build hierarchy and page rhythm

### Give each level a job

Hierarchy should express the content's relationships and reading sequence. Establish a small number of distinct roles, then use them consistently. More levels are justified when the content actually needs them, not because software provides six heading tags.

A primary title, section heading, local heading, body paragraph, caption, and label can differ through several properties. Choose the minimum effective combination. Size, weight, position, space, width, posture, and color can reinforce one another, but changing all of them at every level makes the system noisy.

Keep visual style separate from document semantics. A small section heading remains a heading. A large price or statistic does not become a heading merely because it uses a display style. Use an intelligible heading structure and source order.

### Establish rhythm across the page

Start with the paragraph's baseline distance and reading width, then derive margins, columns, gutters, heading spacing, lists, notes, and captions. A spacing scale can help maintain relationships. Do not force every line height onto a grid if the rounding makes text cramped or detached.

A baseline grid is particularly useful for aligned editorial columns and facing pages. It is a tool for coordination, not a reason to distort a quotation, table, equation, or script with different vertical needs. Use local exceptions deliberately and preserve clear hierarchy.

Inspect a page at three distances. Close inspection reveals spacing and punctuation. Normal reading distance reveals legibility and flow. A reduced overview reveals hierarchy, density, and balance. None replaces the others.

### Align visible forms as well as boxes

Glyph boxes contain unequal sidebearings and vertical whitespace. A heading aligned mathematically with a text block can appear indented because its first letter has an open side. A quote mark can make an otherwise aligned paragraph look displaced.

Use optical margin alignment or hanging punctuation in controlled editorial layouts where it improves the edge. For interfaces, favor robust component alignment over numerous manual offsets. Recheck any optical adjustment when font, size, language, or content changes.

### Compose display text for meaning

Let line breaks support phrasing and emphasis. Consider the shape of each line, the relationship between short and long lines, repeated words, punctuation, and negative space. An even rectangle is not the only successful title shape.

Large scale magnifies small spacing errors. Check individual pairs and endings after setting overall tracking. Tight display leading must still clear accents, descenders, and alternate forms. A title designed in English may need different breaks or even a different scale in another language.

Expressive treatments such as distortion, rotation, overlap, outline, texture, or animated variation can serve a specific phrase. Keep essential information readable and provide a suitable accessible text representation. Do not make every line a competing graphic event.

## 17. Apply typography to the medium

### Editorial print and books

Design a representative spread before completing the style sheet. Include ordinary prose, the longest heading, a note, a caption, a quotation, and any tables or illustrations. Choose trim, margins, binding allowance, column width, and type together. A perfect paragraph can still sit badly on a spread.

Proof at physical size on representative stock. Ink spread can close counters and fill reliefs. Fine strokes can break, especially in small reversed text or on rough material. Use a text or grade variation where appropriate. A desktop print can reveal scale and rhythm but does not reproduce every press condition.

Control headings at page bottoms, isolated lines, running furniture, folios, contents entries, footnotes, and cross-references. Notes can be smaller than body text but must remain readable and clearly associated with their references. Do not solve excessive content by progressively shrinking everything.

Keep text live in working documents and accessible exports. Embed fonts when permitted and required. Verify substitution, character mapping, copy extraction, reading order, and final pagination. Outline a separate production copy only when the agreed workflow requires it, preserving an editable source. Outlined text sacrifices normal text behavior.

### Interfaces and forms

Prioritize recognition, scanning, and action. Use stable styles for labels, values, helper text, errors, navigation, and status. Distinguish them through position and wording as well as appearance.

Keep essential labels visible. Placeholder text does not replace a label. Allow error messages and translated labels to wrap. Prefer flexible component height and padding to a fixed box calibrated for one line. A readable text size and a sufficient interaction target are separate decisions.

Do not use small, faint text as the default way to make a screen look refined. Remove redundant content, improve grouping, or simplify the hierarchy before reducing the visibility of useful information.

### Tables, dashboards, and data

Use tabular figures for values that update or align vertically. Choose alignment by the meaning of the data: prose labels normally align at the start, comparable numbers often at the end or decimal point. Keep units, precision, signs, and missing-value conventions consistent.

Differentiate values from labels and explanation. Avoid turning every metric into a large headline. A stable number column can matter more than a dramatic display face. Verify the typography with zero, a negative number, the largest expected value, and empty or unavailable states.

Use a real minus and enough contrast for negatives and secondary values. Do not rely solely on red/green, weight, or arrow shape. Keep essential precision visible and make truncated values recoverable.

### Code and identifiers

Choose clear punctuation and confusable-character differentiation. Test `Il1`, `O0`, `{}[]()`, `:;`, `.,`, `-_`, `=`, and operator sequences. Monospacing supports alignment but does not automatically improve every kind of reading.

Disable discretionary programming ligatures by default when readers need to inspect exact symbols, unless the product explicitly supports them as a preference. Keep underlying text unchanged. Preserve indentation, code direction, selection, and copy behavior. For mixed-script identifiers or security-sensitive strings, visual similarity may require product safeguards beyond typography.

### Native applications

Map product roles to platform text styles and user scaling behavior. On Apple platforms, prefer semantic system text APIs and support Dynamic Type where available. Custom fonts need explicit scaling and appropriate treatment of accessibility settings such as Bold Text. Do not replace platform behavior with one set of fixed point sizes.

On Android, use platform-scaled text sizing and test the largest supported settings. Nonlinear scaling means a hand-written global multiplier is not a reliable replacement for platform APIs. Keep text and line-height behavior coordinated.

Platform parity means the same information remains clear and usable. It does not require identical numbers, font files, or line breaks. Use the current platform's conventions and verify on devices.

### Signage, presentations, and spatial text

Size for viewing distance, angle, lighting, duration, and movement. A slide readable on a laptop can fail at the back of a room. A sign viewed while walking needs fast differentiation and a clear hierarchy. Condensation can save space but can also reduce recognition.

Proof in the intended conditions or a defensible physical simulation. Avoid thin weights, delicate contrast, ambiguous characters, and long continuous passages where glance reading is required. In spatial environments, keep essential text stable, comfortably oriented, and readable against changing backgrounds. Surface dimensions alone do not define perceived size.

### E-books, email, and constrained outputs

Allow reflow and reader preferences. Do not use a fixed-layout book image as a substitute for ordinary text in an otherwise reflowable product. Test font embedding, supported features, fallback, line breaks, and user font changes in the actual reader.

Email clients, office software, embedded web views, and presentation systems can support different features from a browser. Establish an acceptable fallback early. A sophisticated type system is incomplete if its everyday export loses the hierarchy.

### Identity, logos, and motion

Treat a wordmark as a fixed composition with its own optical spacing. Custom modifications can be justified there without changing the product's reading font. Test the mark at small size, reversed, in one color, and in the required reproduction processes. Preserve a readable brand name in surrounding text and accessible naming.

Animated type needs a purpose, adequate reading time, stable essential information, and a reduced-motion alternative. Weight and width animation can change layout. Keep it out of tasks where movement interrupts reading or comparison. Avoid making an animation the only way to obtain a message.

## 18. Build a typography system

### Inventory tasks before generating a scale

List recurring text uses and the differences users need to perceive. Consolidate visually similar uses that share a function. Keep genuinely distinct tasks separate even when their initial numbers happen to match.

A practical system often needs display, page title, section heading, component title, body, label, caption, code, and data roles. A small product may need fewer. Do not create a size-weight-role matrix full of unused combinations.

### Separate values, roles, and application

Use the smallest architecture that keeps decisions understandable.

1. **Primitive values** define available families, sizes, weights, and spacing values.
2. **Semantic roles** bind those values to a purpose, such as `type.body.reading` or `type.label.control`.
3. **Consuming styles or components** apply the role and the correct content semantics.

A larger system can add component aliases or brand/platform modes where they have real responsibilities. Avoid multiple alias layers that merely rename the same values. Conversely, do not scatter literal numbers through components when a shared role exists.

Name by purpose. `type.body.default` survives a change in size better than `text-16-regular`. A style name such as `heading.small` describes presentation; it does not decide which HTML heading level the content needs.

### Specify a complete role contract

For each role, document the following properties or policies.

| Contract area | Required information |
| --- | --- |
| Purpose | Intended content, typical length, and prohibited uses |
| Font | Exact family/cut, fallback stack, required styles, and coverage |
| Shape | Size, weight, posture, optical-size policy, and any width/grade setting |
| Spacing | Line height, tracking, paragraph relationship, and measure where relevant |
| Features | Numeric style, ligatures, small caps, localized or stylistic settings |
| Behavior | Wrapping, truncation/recovery, responsive changes, and user scaling |
| Context | Brand/platform/language variants and applicable constraints |
| Semantics | How authors choose structural tags or native accessibility roles |
| Evidence | Representative proof content and tested conditions |
| Ownership | Who changes the role, how exceptions are recorded, and how updates migrate |

Text color normally belongs to a separate semantic color system so the same type role can support default, secondary, inverse, or status contexts. Link the policies without duplicating every typography token for every color.

### Use scales as a scaffold

A modular scale multiplies a base by a ratio: `size(n) = base × ratio^n`. It is a useful way to propose relationships. It does not establish that each generated value is necessary, legible, or harmonious in the chosen font.

Smaller ratios can support subtle differences in dense products. Larger ratios can produce pronounced editorial contrast. A deliberate stepped scale is also valid. Round, skip, or revise values when the actual hierarchy needs it, while keeping the final set coherent and documented.

Establish the body and recurring controls before finalizing the display range. Choose line heights independently enough to suit multi-line behavior. A geometric size scale does not imply one fixed ratio for line height, margin, or tracking.

### Example role set

This is an illustrative Latin web system for a moderately spacious information product. Values are starting points for a chosen font with a substantial x-height. It is not a ready-made brand system. Sizes use the user's root font setting. Colors and component spacing are defined separately.

| Role | Family | Size | Weight | Line height | Tracking | Use |
| --- | --- | --- | --- | --- | --- | --- |
| `display.hero` | Selected display cut | 2.5–4.5rem | 600 | 1.1 | Trial -0.02em | Short campaign title, adjusted for marks |
| `heading.page` | UI family | 2–2.5rem | 650 if supplied | 1.2 | 0 | Main page title |
| `heading.section` | UI family | 1.5rem | 600 | 1.3 | 0 | Major content division |
| `heading.component` | UI family | 1.125rem | 600 | 1.4 | 0 | Card, panel, or local group title |
| `body.default` | UI family | 1rem | 400 | 1.5 | 0 | Descriptions and ordinary interface prose |
| `body.reading` | Selected text cut | 1.125rem | 400 | 1.6 | 0 | Extended reading, bounded measure |
| `label.control` | UI family | 0.9375rem | 600 | 1.4 | 0 | Controls and fields, wrapping permitted |
| `caption.default` | UI family | 0.875rem | 400 | 1.45 | 0 | Supporting information, never essential prose hidden by size |
| `data.default` | UI family | 1rem | 400 | 1.5 | 0 | Comparable values with tabular lining figures |
| `code.default` | Mono family | 0.9375rem | 400 | 1.55 | 0 | Code and precise identifiers |

A static family without a 650 cut must map that role to a supplied weight or choose another family. Do not rely on accidental browser synthesis. Prove the scale in a real page, a dense screen, and the smallest supported layout.

### Define responsive and density behavior

Keep roles stable while their values change. A page title can have bounded fluid sizing or step at content-driven breakpoints. Body text can remain stable while the layout changes. Not every role needs to grow with viewport width.

Density variants should primarily change layout, grouping, and available space. Do not obtain a "compact" mode by making all useful text tiny. Keep a documented lower bound for each role based on actual testing.

At larger user settings, let rows grow, alignments stack, and columns reduce. Preserving the relative information order is more important than preserving the exact default geometry. Font scaling and responsive viewport scaling solve different needs.

### Govern changes as layout changes

Changing a font can alter every line break, control width, table, and page count. Version the font source and system mapping. Review representative screens and documents, identify affected roles, and supply migration guidance when values or names change.

Maintain one authoritative specification and generate platform styles where practical. Compare design-tool values with shipped code. Require a reason and proof for new styles or exceptions. Retire unused roles instead of accumulating near-duplicates.

For multiple brands, vary identity-bearing choices through explicit modes while retaining understandable role semantics. For multiple languages, allow script-specific fonts, sizes, and line heights under the same functional role. A shared role should preserve purpose rather than enforce identical glyph dimensions.

## 19. Implement web typography

### Map font data accurately

Declare the actual weight and style supplied by each file. A static bold file is one weight. A variable file can expose a supported range. Do not declare a broad range for a static file or promise styles the font does not contain.

CSS weight values can run from 1 to 1000. `normal` maps to 400 and `bold` to 700. The selected family determines which values are available and how they look.

Prefer high-level properties for ordinary weight, width, style, and optical sizing. Use `font-variation-settings` for additional axes or carefully justified low-level control. A later declaration can replace the entire variation-settings list, so coordinate these settings through the role system.

| Axis | Meaning | Application rule |
| --- | --- | --- |
| `wght` | Weight | Use `font-weight` for normal role selection. |
| `wdth` | Width | Use the supported high-level CSS width/stretch property. Confirm the font's range. |
| `opsz` | Optical size | Start with `font-optical-sizing: auto` when the font supplies it. |
| `slnt` | Slant | Use supported oblique styling and declare the actual slant range. |
| `ital` | Italic selection | Choose through `font-style` where supported by the font organization. |
| Custom axes | Foundry-defined behavior, such as grade or specialized shaping | Inspect documentation and valid values. Do not infer behavior from an unfamiliar tag. |

A variable font can include several axes without replacing every family file. Italics and different script resources may still be separate. Test the exact files, browser, and CSS mapping.

### Example implementation

The following example is illustrative. The two `Example Sans` files must be supplied by the project, licensed for web use, and genuinely support the declared weight range. It provides complete basic styles without requiring advanced wrapping support. It does not define a finished visual identity.

```html
<article class="article" lang="en">
	<h1 class="page-title">A guide to the collection</h1>
	<p class="lede">Find the records that explain how the collection developed.</p>
	<h2 class="section-title">Reading the records</h2>
	<p>Each entry includes a date, a description, and its source.</p>
	<p><strong>Check the date</strong> before comparing two entries.</p>
	<p><em>Updated descriptions</em> retain a link to the earlier version.</p>
	<p class="data-value">1,204 records</p>
</article>
```

```css
@font-face {
	font-family: "Example Sans";
	src: url("/fonts/example-sans-upright.woff2") format("woff2");
	font-style: normal;
	font-weight: 400 700;
	font-display: swap;
}

@font-face {
	font-family: "Example Sans";
	src: url("/fonts/example-sans-italic.woff2") format("woff2");
	font-style: italic;
	font-weight: 400 700;
	font-display: swap;
}

:root {
	--font-ui: "Example Sans", system-ui, sans-serif;
	--size-body: 1rem;
	--size-reading: 1.125rem;
	--size-section: 1.5rem;
	--size-title: 2.5rem;
	--weight-regular: 400;
	--weight-emphasis: 600;
	--weight-strong: 700;
	--leading-body: 1.6;
	--measure-reading: 65ch;
}

html {
	font-size: 100%;
}

body {
	font-family: var(--font-ui);
	font-size: var(--size-body);
	font-weight: var(--weight-regular);
	line-height: 1.5;
	font-optical-sizing: auto;
}

.article {
	max-inline-size: var(--measure-reading);
	margin-inline: auto;
	padding-inline: 1rem;
	font-size: var(--size-reading);
	line-height: var(--leading-body);
	overflow-wrap: break-word;
}

.article > * {
	margin-block: 0;
}

.article > * + * {
	margin-block-start: 1em;
}

.page-title {
	font-size: var(--size-title);
	font-weight: var(--weight-emphasis);
	line-height: 1.2;
}

.section-title {
	font-size: var(--size-section);
	font-weight: var(--weight-emphasis);
	line-height: 1.3;
}

.article > .section-title {
	margin-block-start: 2em;
}

.section-title + p {
	margin-block-start: 0.5em;
}

.lede {
	font-size: 1.125em;
}

strong {
	font-weight: var(--weight-strong);
}

em {
	font-style: italic;
}

.data-value {
	font-variant-numeric: lining-nums tabular-nums;
}

@supports (text-wrap: balance) {
	.page-title {
		text-wrap: balance;
	}
}
```

The article's computed font determines the `ch` measure. The root remains at the user's preferred size. Unitless line heights scale with each element's font size. All headings can wrap. The example deliberately uses a fixed `rem` title size to keep the base specimen straightforward. Select responsive display behavior separately and test it.

### Use fluid sizes with a scaling test

A bounded fluid title might use `clamp(2rem, 1.5rem + 2vw, 4rem)`. The minimum, preferred value, and maximum need a content-based reason. Adding a relative minimum helps but does not prove that the text can reach the required enlargement. Viewport terms can counteract page zoom as the effective viewport shrinks.

Test at the smallest supported layout, with enlarged default text, and with browser zoom. If the title cannot achieve sufficient enlargement or causes loss, revise the expression or use discrete relative sizes. A stable body size with a changing layout is often sufficient.

### Use features only when supplied

Prefer properties such as `font-variant-numeric` and `font-variant-caps` for their defined purposes. Keep low-level `font-feature-settings` for cases that need them. Do not assume a CSS declaration adds missing glyphs or that every application applies the same feature set.

Use standard ligatures where they improve the text and preserve correct shaping. Avoid globally disabling required script features. Enable discretionary ligatures or stylistic sets only in roles where their effect is wanted.

Provide real bold and italic styles. If using `font-synthesis: none`, first verify that necessary emphasis remains visible across primary and fallback fonts. Blanket suppression can leave unsupported language runs without a meaningful bold distinction.

### Handle wrapping at the correct layer

Use `text-wrap: balance` selectively for short titles when supported. Consider `pretty` for text where its implementation and layout cost are acceptable. Keep normal wrapping as the functional baseline.

Allow flex and grid children containing text to shrink where needed, often through `min-inline-size: 0`. Use emergency wrapping for long identifiers or URLs where appropriate. Do not apply `word-break: break-all` globally to prose.

Use truncation only for a defined reason and provide access to the complete value. A pointer-only tooltip is insufficient for touch and keyboard users. Layout must accommodate the essential message before decorative symmetry.

Avoid global font-smoothing overrides as an aesthetic shortcut. They are platform-specific, can change perceived weight, and do not repair an inappropriate font or insufficient contrast.

## 20. Load fonts and design fallbacks

### Treat fallback as a real state

Choose a fallback that supports the required languages and has a plausible apparent size, width, and line behavior. Test the page with the custom fonts unavailable. It should remain readable, navigable, and complete.

A system stack can be the primary choice when native behavior and low delivery cost suit the product. It will vary across platforms. A generic `sans-serif` or `serif` ending provides a final fallback but does not guarantee one appearance or comprehensive coverage.

Plan both whole-font fallback and per-glyph fallback. One unsupported symbol can come from another family with a different baseline, weight, or width. Inspect mixed-script and symbol-heavy text for these seams.

### Choose the loading strategy deliberately

`font-display: swap` prioritizes early fallback text and permits later replacement. It can cause layout movement. `optional` permits fallback to remain when the font is not ready within its brief opportunity. `fallback` allows a limited swap period. Browser timing is not an exact author-controlled millisecond contract.

Select the strategy for the role. A delayed decorative face and a critical reading font can need different policies. Avoid hiding essential text for a prolonged loading period. Verify the first visit with a cold cache and an unreliable network.

### Match metrics when it helps

Use a measured fallback adjustment when the unadjusted swap causes meaningful movement. `size-adjust` scales outlines and metrics. Ascender, descender, and line-gap overrides can coordinate line layout. They do not make two typefaces identical.

Calculate and test values for the actual primary/fallback pair and styles. Do not copy percentages from another project's font pair. Matching x-height alone can leave widths and line breaks different. Confirm that accents and fallback script extents remain visible.

### Budget actual font delivery

Default to WOFF2 for modern web delivery. Load the styles and coverage the page needs. A variable file can be efficient when many instances are used, but a large multi-axis file can cost more than a small static subset. Compare actual transfer sizes, request counts, text visibility, and layout stability.

Preload only critical files whose early arrival improves the first view. Keep the preload URL identical to the eventual request and use the appropriate font type and cross-origin mode. Preloading every style competes with other important resources.

Subset only within the license and the actual language/content requirements. Preserve necessary marks, substitutions, positioning, and glyph dependencies. `unicode-range` describes applicability and download selection. It does not remove data from an unchanged font file.

Use safe asset versioning and caching so a font update reaches users predictably. Check font request failures, CORS, content-security restrictions, missing weights, and duplicate downloads. Font delivery belongs in production verification, not only design review.

## 21. Preserve accessibility

### Apply the relevant requirements accurately

For web work targeting WCAG 2.2 AA, check text contrast, resizing, reflow, spacing adaptability, semantics, and access to the complete content. These checks are necessary parts of a broader accessibility review. Typography alone cannot establish whole-product conformance.

| Area | Check |
| --- | --- |
| Contrast | Ordinary text generally needs at least 4.5:1. Large text generally needs 3:1. Large means at least 18 pt, approximately 24 CSS px, or 14 pt bold, approximately 18.67 CSS px. Apply the criterion's actual exceptions where relevant. |
| Enlargement | Text can reach 200% without loss of content or function, subject to the criterion's scope. Check controls and labels too. |
| Reflow | Ordinary vertically scrolling content works at a width equivalent to 320 CSS px without two-dimensional scrolling or loss. For horizontally scrolling content, test the corresponding 256 CSS-pixel height. Necessary two-dimensional content has scoped exceptions. |
| Spacing overrides | For applicable markup and scripts, simultaneously set line height to 1.5 times font size, paragraph spacing to 2 times, letter spacing to 0.12 times, and word spacing to 0.16 times. Content and function remain available. These are override test values, not mandatory default styling. |
| Meaning | Structure, order, labels, and distinctions remain available beyond visual size, weight, position, or color. |

Do not round a failing contrast ratio upward. Test text against its actual background, including overlays, images, hover/focus content, and variable surfaces. Thin strokes can remain weak even when nominal foreground/background colors pass. Make the text more robust rather than treating the ratio as a complete readability verdict.

### Preserve adaptation

Allow text containers and controls to grow. Test fixed-height rows, badges, buttons, tabs, error regions, and navigation, since these often fail before ordinary paragraphs. Keep essential information recoverable if a constrained component truncates.

Avoid viewport settings that disable zoom. Do not force all users into one size, tracking value, or reading width. Respect native scaling and user styles. Test large text independently from a narrow viewport because the failure modes differ.

No single family guarantees accessibility or solves dyslexia for every reader. Provide clear forms, suitable size and spacing, robust contrast, sensible line length, and choice where useful. Test with representative readers when the product's audience or stakes warrant it.

### Keep meaningful text as text

Use real text for content people must read, search, select, translate, or access with assistive technology. A screenshot or outlined vector can reproduce appearance while losing normal text capabilities. Where an image of text is necessary, provide the appropriate accessible equivalent and retain an editable source.

Keep reading order consistent with meaning. Do not use visual reordering or one-element-per-letter markup that scrambles the message for assistive technology. Decorative duplicates and animated copies must not produce repeated announcements.

### Keep color and weight in proportion

Secondary information can be quieter without becoming faint. Light gray, small size, thin weight, and dense spacing compound. Do not apply all four to the same useful text.

Dark mode requires its own proof. Bright text can appear heavier against a dark field, but automatically thinning it can damage legibility. Adjust actual colors and, when justified, a suitable grade or weight. Preserve hierarchy and contrast in both modes. Pure black and white are valid options when they fit the conditions; there is no universal requirement to soften them.

## 22. Compose across languages and scripts

### Set language and direction correctly

Use actual language metadata so shaping, hyphenation, pronunciation, and localized forms can operate correctly. Set the document's base direction where appropriate. Isolate unknown-direction inline content with supported markup such as `<bdi>` or an appropriate `dir` policy. Do not reverse strings manually to simulate right-to-left text.

Language and script are different dimensions. One language can use more than one script, and a script can serve many languages with different forms or conventions. A broad label such as "Arabic support" or "CJK" does not specify every reader's needs.

### Localize the role rather than forcing the outline

Match visual balance across scripts through apparent size, density, line rhythm, and role. Equal nominal size or Latin x-height does not guarantee equal readability. Allow script-specific line heights, fallback stacks, and emphasis treatments.

Avoid scaling a script unnaturally to match Latin capitals. Preserve its own proportions and essential marks. A multilingual family is useful when its individual script designs are sound. Shared branding does not prove equal quality across all scripts.

### Respect script-specific composition

| Context | Required attention |
| --- | --- |
| Arabic and related writing | Contextual joining, ligatures, mark positioning, direction, and adequate vertical room. Do not imitate Latin tracking by inserting spaces between joined letters. |
| Indic and other complex scripts | Correct shaping of clusters, reordering, conjuncts, and marks. Do not split grapheme clusters for animation or truncation. |
| Chinese and Japanese | Appropriate regional glyph forms, punctuation placement, line-start/end restrictions, and mixed Latin treatment. Latin word-count and measure rules are insufficient. |
| Korean | Hangul syllable composition, word spacing, and line-breaking conventions appropriate to the language and content. |
| Vertical composition | Writing mode, punctuation, orientation of Latin/numeric runs, and script-specific layout conventions. Rotation of a horizontal block is not a complete solution. |
| Greek and Cyrillic | Native proportions and localized forms, including italic behavior. Superficial resemblance to Latin letters is not a construction method. |
| Mixed-direction text | Numbers, punctuation, links, filenames, and embedded names must remain in logical order and be isolated appropriately. |

Use a script-aware shaping engine. Test in the final application because correct font data can still be mishandled by composition software. Subsetting, custom canvas rendering, or splitting text into many styled spans can break shaping.

### Proof localization realistically

Include actual translated screens or pages, names, dates, currencies, plural forms, quotes, and the longest plausible content. Do not approve localization through English text with a few accented letters added.

Allow expansion and contraction. A translated button or heading may need another line or layout. Do not compensate automatically by reducing its font size. Test fallback and missing glyphs on a device without the development machine's font collection.

Obtain native-reader review for culturally specific forms, emphasis, punctuation, and line breaking. For a new script extension, involve type designers who understand that writing system before declaring support complete.

## 23. Proof and diagnose

### Build a proof ladder

Inspect each level because a failure can emerge only when forms combine.

1. **Outline.** Check curve quality, joins, overshoot, and intended construction.
2. **Control pattern.** Compare repeated stems, rounds, diagonals, and their spaces.
3. **Word.** Test rhythm, confusable combinations, punctuation, and repeated letters.
4. **Mixed text.** Compare case, figures, italic, emphasis, marks, and languages.
5. **Paragraph.** Judge apparent size, color, measure, leading, rag, and sustained reading.
6. **Component or page.** Check hierarchy, grouping, reading order, fit, and alignment.
7. **Delivery.** Test real font files, loading/fallback, scaling, export, material, and viewing conditions.

Keep the relevant proof content and output settings reproducible. When comparing alternatives, change one principal variable at a time so the cause remains visible. After the local repair, recheck the containing word, paragraph, and page.

### Use a varied specimen

The following original diagnostic set is a starting point for Latin work. Extend it to the actual glyph set, language, and content. It is not a language-coverage certification.

```text
Controls
HHHH OOOO HOHO HOOH
nnnn oooo non noononno
nHn nOn HnH HoH

Distinctions and fit
Il1 I1l lI1 O0o 0Oo
rn m cl d vv w
AVATAR WAVE TYPE To Ty Wa Yo
minimum milliner rhythm civic evening
SASS BASIS SENSE SOS
BPR DOP RARE QUIET

Mixed content
A narrow path opens beside the old library.
Three entries changed: 07, 18, and 204.
Ilona reviewed record O01 at 11:10.
Regular text, real italic, bold text, and bold italic.

Numbers and signs
0123456789 111111 888888 000000
1,204.50 9.75 −42.00 +6.25 0.00
12:08 23:59 100% 5 × 7 = 35
$12.50 €12,50 £12.50 ¥1200
() [] {} @ # & ? ! : ; . , - – — −

Coverage samples to extend
À É Î Ö Ü Ç Ñ Ā Ł Œ ẞ
à é î ö ü ç ñ ā ł œ ß
Ångström Straße œuvre São Łódź
```

Use actual styled runs for the emphasis line. The words "real italic" do not exercise an italic font unless it is selected. Compare precomposed and decomposed sequences deliberately in a separate coverage test. Add domain-specific symbols, abbreviations, and native-script passages.

### Diagnose before adjusting

| Visible symptom | Likely causes | First useful action |
| --- | --- | --- |
| O looks short beside H | Missing or insufficient optical overshoot | Compare outlines and actual-size `HOHO`. |
| Curve looks pinched | Abrupt straight-to-curve transition or weak counter shaping | Inspect both contours and redistribute curvature. |
| One glyph is dark in every word | Crowded structure, inappropriate weight, or insufficient counter space | Redraw the glyph before widening all surrounding spaces. |
| Repeated verticals form spots | Sidebearings too tight or inconsistent stem weight | Compare n/o controls and single-stem combinations. |
| Word looks like disconnected pieces | Loose fit, weak strokes, or incompatible proportions | Inspect at reading size and compare inner/outer white. |
| `rn` reads as m | Spacing, branch shape, or narrow word context | Repair the specific interaction, then retest r/n elsewhere. |
| Caps look detached from lowercase | Independently spaced cases or mismatched color | Proof mixed-case controls and rebalance case fit. |
| Font works large but fails small | Wrong optical cut, delicate details, closed apertures, or weak rendering | Test a text cut and the actual output before changing layout. |
| Paragraph is gray but tiring | Small apparent size, excessive measure, weak contrast, or unsuitable leading | Read real prose and adjust the paragraph variables together. |
| Justified text has rivers | Narrow measure, poor hyphenation, or stretched word spaces | Improve composition settings or use ragged alignment. |
| Heading looks detached | Too much space after it or too little before it | Repair proximity before increasing weight. |
| Every section appears equally important | Too many competing styles or insufficient role contrast | Reduce the active hierarchy and clarify reading order. |
| Numbers shift during updates | Proportional digits or unstable separators/layout | Verify tabular figures and the whole formatted value. |
| Font swap moves the page | Different metrics, widths, or late discovery | Measure fallback, loading strategy, and actual requests. |
| Italic looks mechanically skewed | Missing style or incorrect mapping | Inspect the rendered font and supply the intended italic. |
| Accents clip | Tight line boxes, restrictive containers, or incorrect font metrics | Inspect actual bounds and line layout at all required sizes. |
| New script has a different voice | Per-glyph fallback or unsuitable cross-script mapping | Identify rendered fonts and proof script-specific roles. |
| Large text breaks controls | Fixed dimensions, no wrapping, or hidden overflow | Allow growth, stacking, and access to full content. |
| System drifts over time | Raw values, duplicate roles, undocumented exceptions | Reconcile real use with the authoritative role specification. |

### Verify the final conditions

For a font, inspect all promised glyphs, styles, features, axis combinations, and target applications. For a web system, check the smallest supported layout, normal and large text, zoom/reflow, spacing overrides, keyboard access to truncated content, slow loading, failed loading, and both color modes when provided. For print, inspect the final exported file and representative physical output.

Record actual results and limitations. A screenshot establishes one captured rendering. A parser establishes syntax. A font validator establishes the conditions it tests. None alone certifies typographic quality. Visual and reader testing remain necessary for the decisions they can expose.

## 24. Use the guide in a project

### When designing a typeface

Produce a brief, construction model, representative control set, spaced words, mixed-case paragraphs, and a coverage plan before expanding into a large family. Refine outlines and spacing together. Build styles from proven controls, then validate the exported font and its promised behavior.

A useful handoff includes the intended roles and size range, language coverage, source and binary versions, supported features/axes, proof specimens, required notices, and known limitations. Explain where the font should not be used.

### When composing a publication

Choose the actual font cuts and figure policy, establish a readable paragraph, and build a representative spread. Define hierarchy, paragraph signals, captions, notes, and production behavior. Review complete pages after changes to font, size, measure, or content. Deliver the editable source and verified final output required by the project.

### When building a product system

Inventory reading tasks, prove the hardest content, define the smallest sufficient role set, and map it to each platform. Implement font delivery and fallbacks alongside the visual styles. Test user adaptation and localization before freezing component geometry. Keep examples, ownership, and migration rules with the specification.

### Completion criteria

The work is ready for its agreed use when the following statements are supported by actual proofs.

- Readers can distinguish the required characters and understand the intended content under the target conditions.
- Letterforms, fit, paragraph rhythm, and hierarchy work together without unresolved distracting defects.
- All required languages, styles, numbers, punctuation, and features behave correctly in the delivered implementation.
- The system survives realistic content, fallback, size changes, and the relevant accessibility settings.
- The chosen output preserves meaning, text access, and required production behavior.
- The delivered specification identifies exact assets, roles, exceptions, ownership, and known limitations clearly enough for another person to apply it.
