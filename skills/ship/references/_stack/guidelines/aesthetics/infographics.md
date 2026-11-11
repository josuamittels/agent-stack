---
name: infographics
description: "Reference for truthful visual explanation: infographic scope, representation and encoding, charts, explanatory diagrams, networks, geographic maps, metro schematics, annotation, adaptation, and production."
version: "0.1.0"
created: "2026-11-11"
updated: "2026-11-11"
author:
  - "Josua Mittelstaedt"
references:
  - "Edward R. Tufte"
  - "Andy Kirk"
  - "Dona M. Wong"
  - "Jacques Bertin"
  - "William S. Cleveland"
  - "Robert McGill"
  - "Office for National Statistics"
  - "Financial Times Visual Journalism Team"
  - "Claus O. Wilke"
  - "Transport for London"
  - "London Museum"
  - "World Wide Web Consortium"
  - "Office for Statistics Regulation"
  - "Heather Smith"
  - "Lisa Charlotte Muth"
type: reference
status: experimental
---

# Infographics

An infographic makes information understandable through visual relationships. Marks, words, numbers, and explanatory images work together so a reader can compare quantities, trace a route, follow a process, or understand a mechanism. Choose those relationships deliberately: a line can imply continuity, a larger shape can imply more, and an arrow can imply an action or cause.

## Use this reference

Use this guide to design and review visual explanations for publications, presentations, interfaces, posters, and other media. It owns the translation of established information into a representation: what marks stand for, which relationships they express, how readers decode them, and which qualifications the graphic must retain.

### Boundaries

Establish the boundary before combining this guide with another domain.

- **Infographic** is the broad communication form. It can contain charts, maps, process diagrams, technical illustrations, explanatory text, or a coordinated combination. A page of large statistics and decorative icons becomes useful when its arrangement explains a relationship.
- **Data visualisation** represents observations or derived values through an explicit mapping to visual properties. Exploratory analysis can use it to discover patterns; publication requires checking the resulting claim. A visualisation can be one component of an infographic or stand alone.
- **Diagram** represents entities and relationships, including nonquantitative information. Position and line length may be organizational rather than measured. A conceptual connection does not acquire a numerical value because it is drawn as a thick line.
- **Map** represents spatial information. Geographic maps preserve selected geographic properties; network schematics can prioritize connectivity. The intended task determines which distortions are acceptable.

This guide does not establish whether a dataset is valid, choose a statistical model, estimate causal effects, or certify a transport service. Data acquisition, cleaning, denominators, privacy decisions, and analytical inference remain with the relevant analytical or subject owner. Require those inputs before encoding them; return an unsupported claim for correction. Rendering a plausible chart cannot validate its data.

Decoration, expressive illustration, branding, and page arrangement have their own purposes. Apply this guide when their visible geometry also claims to explain facts or relationships. It does not prescribe a universal visual style, require a chart for every number, or replace specialist cartographic and technical review.

### Overlaps and ownership

Apply the shared [aesthetics framework](reference.md) for priorities and selective reading. Follow the owner for the decision at hand.

| Decision | Authority here | Neighboring authority |
| --- | --- | --- |
| Representation | Reader task, chart or diagram family, variables, encoding, scales, topology, truthful abstraction | Analytical work establishes the information and permissible inference before design. |
| Spatial arrangement | Relationships that the graphic's position, grouping, and sequence assert | [Composition](composition.md) owns grids, balance, density, page hierarchy, and layout adaptation. Preserve meaningful coordinates when applying it. |
| Text | Information needed in titles, labels, legends, annotations, and notes | [Typography](typography.md) owns type selection, numeral forms, shaping, text setting, and font delivery; [English](../languages/english.md) owns English wording. |
| Colour | Whether a variable is categorical, ordered, divergent, or cyclic; what the colour denotes | [Colour](colour.md#15-encode-data-with-colour) owns palette construction, perceptual progression, themes, and reproduction. |
| Symbols | Which entities, quantities, directions, and transfer types symbols denote | [Iconography](iconography.md) owns symbol construction, metaphor, optical correction, and family consistency. |
| Interaction and animation | Which comparisons and relationships must survive filtering, selection, and transition | [Interaction](interaction.md) owns controls, states, focus, recovery, and feedback; [Motion](motion.md) owns timing and animated transitions. |
| Access | Information and tasks that an equivalent representation must retain | [Accessibility](accessibility.md#18-make-data-and-complex-workspaces-accessible) owns access requirements, semantics, assistive technology, and verification. |
| Diagram implementation | Meaning and legibility of the chosen representation | [Mermaid](../coding/mermaid.md) owns its notation, configuration, and rendering conventions when that tool is used. |

Keep a rule with its owner. A chart's zero baseline belongs here; a palette's lightness progression belongs in Colour. A page grid must not move a data point off its measured position. Optical corrections suitable for icons must not change a quantitative mark's encoded extent.

### Reading paths

For a statistical graphic, read sections 1–8, then the relevant delivery sections. For a process or technical explanation, use 1–4 and 9. For geographic maps and metro schematics, use 10–11. Finish with 12–17 for explanation, access, adaptation, production, and review. Section 18 gives complete illustrative examples.

## Contents

1. [Use the governing rule](#1-use-the-governing-rule)
2. [Define the reader's task](#2-define-the-readers-task)
3. [Establish the information contract](#3-establish-the-information-contract)
4. [Choose a representation and encoding](#4-choose-a-representation-and-encoding)
5. [Preserve scale and geometric integrity](#5-preserve-scale-and-geometric-integrity)
6. [Make comparisons fair](#6-make-comparisons-fair)
7. [Choose and refine statistical charts](#7-choose-and-refine-statistical-charts)
8. [Show uncertainty and missingness](#8-show-uncertainty-and-missingness)
9. [Explain processes, networks, and mechanisms](#9-explain-processes-networks-and-mechanisms)
10. [Use geography when location matters](#10-use-geography-when-location-matters)
11. [Design metro and route schematics](#11-design-metro-and-route-schematics)
12. [Integrate words and graphics](#12-integrate-words-and-graphics)
13. [Direct attention without changing the evidence](#13-direct-attention-without-changing-the-evidence)
14. [Provide equivalent access](#14-provide-equivalent-access)
15. [Adapt and interact without losing meaning](#15-adapt-and-interact-without-losing-meaning)
16. [Produce and maintain the graphic](#16-produce-and-maintain-the-graphic)
17. [Review and diagnose](#17-review-and-diagnose)
18. [Work through complete examples](#18-work-through-complete-examples)

## 1. Use the governing rule

**Make the intended relationship easy to understand while preserving the evidence and limits needed to interpret it correctly.**

Apply that rule through four decisions:

1. Identify what the reader needs to understand or do.
2. Choose a representation whose visible relationships match the information.
3. Retain the context, uncertainty, and explanation required for a fair reading.
4. Check the result in its delivered form against the source and the reader's task.

Simplification reduces unnecessary decoding. It can remove ornamental frames, repeated keys, needless perspective, or an irrelevant variable. It must not erase a denominator, a meaningful exception, a route branch, or uncertainty that changes the conclusion. Adding a label, reference line, or explanation can make a graphic simpler to use even though it adds marks.

Treat beauty as a coordinated result of useful structure, legible detail, coherent expression, and careful production. A memorable image can invite attention; the explanation must still work after that first impression. When a graphic and its explanatory note give different impressions, change the graphic rather than relying on fine print to repair it.

## 2. Define the reader's task

Write the purpose as an answerable question: “Which districts have the highest incident rate?” or “Where must I change to reach the airport?” These require different information and representations. “Show the data” leaves the design undecided.

Establish these inputs before polishing:

| Input | Decision it supports |
| --- | --- |
| Audience and prior knowledge | How much notation, teaching, and subject context to supply |
| Task | Compare, rank, locate, trace, explain, estimate, monitor, or explore |
| Evidence and claim | What is established and which conclusion the display can support |
| Encounter | Passing glance, independent reading, spoken presentation, or repeated operation |
| Output conditions | Actual dimensions, distance, medium, languages, device, and interaction limits |
| Necessary detail | Values, paths, exceptions, definitions, uncertainty, and source information |
| Verification | The source reconciliation and reader task that can reveal a failure |

Choose a sentence or table when it answers the question more directly. A single value may need a clear comparator and unit rather than a pictorial chart. A table supports exact lookup across several fields; a chart reveals a pattern that would take longer to infer from rows. They can work together.

Distinguish explanation from exploration. For explanation, select an evidence-supported point and show enough context to assess it. For exploration, make dimensions and controls discoverable and allow unexpected results. An exploratory tool can start with an orientation message without prescribing a conclusion for every filter state.

## 3. Establish the information contract

Record what each item and value means. For quantities, identify the unit, period, population, denominator, geographic boundary, aggregation, and source version. For a process, identify entities, steps, decisions, dependencies, and exceptions. For a network, establish the node and edge lists and the meaning of direction, weight, and transfer.

Use real content, including difficult cases. Long place names, negative values, small samples, branching services, and missing periods can invalidate a polished sketch made with ideal examples.

Maintain a source-to-display mapping. Each plotted series, diagram assertion, and highlighted number needs a traceable origin or an explicitly identified illustrative assumption. Retain transformations and exclusions with the working material. Mark synthetic examples and conceptual reconstructions as such in the deliverable when readers could mistake them for observations.

Check derived values before drawing. Use unrounded values for calculation and consistent rounding for display. Distinguish counts from rates and relative change from percentage-point difference. A rise from 20% to 30% is 10 percentage points and a 50% relative increase. Neither description alone tells the reader how many people were measured.

If evidence is absent, do not fill the gap with an invented number, connection, cross-section, or trend. Show the gap, state the limit, or narrow the graphic's claim. Keep suppressed data suppressed in tooltips, labels, and downloads as well as the visible plot.

## 4. Choose a representation and encoding

An encoding maps information to visible properties. Identify that mapping before selecting a decorative treatment. Readers should be able to answer “What does position mean? What does size mean? What does this connection mean?”

| Reader task | Starting representation | Prerequisite or exception |
| --- | --- | --- |
| Compare or rank amounts | Aligned dot plot or horizontal bars | Retain natural order for stages, dates, or ordered responses. |
| Follow change over time | Line chart with a genuine time axis | Use columns for discrete interval totals; do not connect unrelated categories. |
| Compare two observations per item | Paired dots, dumbbells, or a slope chart | Name both endpoints; a slope does not reveal unobserved intermediate change. |
| Understand a distribution | Histogram, dot/strip plot, or distribution summary | Show sample size and explain unfamiliar summaries. |
| Relate two measured variables | Scatterplot | Separate association from causation; identify transformations. |
| Compare parts of a whole | Stacked bar or a simple pie for a few clearly different shares | Categories must form the stated whole. Use bars for fine comparison. |
| Inspect estimates against a reference | Dot-and-interval plot | Specify interval meaning and the reference. |
| Compare the same pattern across groups | Small multiples | Keep scales and encoding comparable for the claimed comparison. |
| Explain sequence or branching | Process flow or decision diagram | Edges denote named steps or conditions, not measured volumes. |
| Compare measured transfers | Width-coded flow diagram | Quantities, units, and accounting boundaries must be compatible. |
| Trace relationships | Node-link diagram, adjacency matrix, or route schematic | Choose by path tracing versus dense relationship lookup. |
| Understand an object or mechanism | Labelled illustration, section, exploded view, or sequence | Distinguish measured geometry from explanatory abstraction. |
| Locate a spatial pattern | Geographic map | Use a chart instead when geographic arrangement does not help. |

### Match the channel to the task

Default to aligned position for precise quantitative comparison. Length works well with a common baseline. Area, angle, and colour intensity can reveal broad patterns but are harder to use for close numerical judgments; add labels or another view when precision matters. These are starting preferences, not a guarantee that every positional chart outperforms every alternative.

Use shape and unordered hue to distinguish categories. Use ordered position, size, or a tested colour progression for magnitude. Do not ask an arbitrary sequence of red, yellow, and blue to communicate equal numerical intervals. Delegate the palette to Colour after defining the variable's meaning.

A visual channel should retain one meaning across a coordinated display. If line thickness denotes capacity in one panel and status in another, separate and teach the difference or choose a different encoding. Limit simultaneous encodings to those needed for the task; a third variable need not become bubble size merely because the software supports it.

## 5. Preserve scale and geometric integrity

### Baselines and domains

Magnitude bars begin at zero because their length represents the amount. Include negative values on the appropriate side of zero. Do not use a broken magnitude bar to magnify a small difference. Use labelled dots, an explicit difference plot, or a separate detail view instead. Floating ranges and waterfall contributions have different semantics: label their endpoints and references so they cannot be mistaken for zero-based totals.

Filled magnitude areas also need a meaningful zero baseline. A line or scatterplot can use a narrower domain when the task concerns variation within that range. Make its extent clear and include relevant context or a wider view when the narrow range could overstate importance. Shading a cropped line down to the plot edge creates an additional magnitude claim; avoid it.

Use regular increments on a linear axis. Position time observations according to elapsed time, including uneven intervals. Distinguish an omitted interval from an interval with no events. An axis break must be explicit and must not turn incomparable lengths into apparent quantities.

A logarithmic position scale is useful for multiplicative change or several orders of magnitude. Explain that equal distances represent equal ratios; label readable values. Ordinary logarithms do not represent zero or negative values. Do not silently add a constant to make the data fit. Prefer points or lines to bars on such axes, and state another transformation when it is required.

### Extent and dimensionality

If circles represent amounts, scale their **area**, not their radius, to the value. For nonnegative values, a positive reference value `v0` drawn at radius `r0` gives `r = r0 × sqrt(v / v0)`. Four times the amount gets twice the radius. Use a size legend, and choose another channel for negative amounts.

For similar pictograms, scaling both width and height by two makes the area four times larger. Default to repeating equal-sized units or using a plain quantitative mark. If one icon represents 1,000 people, state that unit and handle partial units consistently. Do not use different silhouettes as equal-area numerical comparators without checking their filled areas.

Avoid decorative 3D, perspective, depth, and gradients that change apparent magnitude or obscure marks. A technical illustration can require perspective; a spatial dataset can require three dimensions. State what the extra dimension means and supply a usable view or interaction for hidden information.

### Aspect and scale consistency

Choose dimensions that preserve important variation without manufacturing steepness or hiding it. There is no universal aspect ratio or required percentage of plot occupancy. Inspect plausible alternatives at delivery size. Preserve equal x/y units when angle, distance, or geometric shape is part of the claim; otherwise label their independent units.

Small multiples share domains when readers compare levels or magnitudes. Independently scaled panels can help compare within-series shape, but must visibly identify their different domains and cannot support a direct height comparison. Keep stable category assignments, baseline conventions, and symbol meanings across panels.

## 6. Make comparisons fair

Compare like populations, definitions, periods, and measurement units. Show a relevant benchmark, target, prior period, or distribution when a number otherwise lacks meaning. State whether a target is a policy choice, historical reference, or estimated threshold.

A raw count describes total burden; a rate supports comparisons adjusted for the relevant exposure. Choose by the question. If both matter, show both and name their different conclusions. Averages can conceal distributions and group differences. Ask the analytical owner for the appropriate breakdown rather than designing an unsupported subgroup story.

Keep time windows and endpoints defensible. Show a meaningful interval rather than selecting a peak or trough solely to create a dramatic change. Identify incomplete periods and changes in coverage. For monetary series, state nominal versus inflation-adjusted values and the reference year where needed.

Default away from independently scaled dual-axis overlays. Their crossings and slopes can suggest relationships chosen by the axis settings. Use aligned panels, direct annotations, or a clearly defined common index. A secondary axis that is a fixed conversion of the same quantity, such as Celsius and Fahrenheit, is a different case; verify the transformation and explain both units.

For a trained audience that routinely compares differently measured series at the same time, a dual-axis display can be justified. Make the series-to-axis mapping and units explicit, keep magnitude bars zero-based, and verify the intended reading with that audience. Do not interpret crossovers as equality or use axis tuning to imply matching growth. Retain a simpler alternative when readers cannot reliably decode the overlay.

An index of 100 at a named baseline compares relative change, not absolute size. State the baseline date and retain original levels where they affect the decision. Do not choose a different favorable baseline for each series. A zero starting value cannot support ordinary percentage-change or ratio indexing.

## 7. Choose and refine statistical charts

### Bars, dots, and ordered categories

Sort by value when ranking is the task. Preserve chronological, procedural, geographic, or ordinal order when that is meaningful. Use horizontal labels for long category names. A dot plot can save space or focus attention on position; bars make magnitude from zero explicit.

Show the full relevant set or label the selection. If grouping a long tail into “Other,” retain its definition and make it possible to inspect important members where the task requires them. Excluded categories must not silently disappear from a stated total.

### Time series and repeated observations

Use lines for continuity and columns for interval amounts when that distinction helps. Connect observations only when the relationship is legitimate. Show gaps or explicitly marked interpolation for missing observations. Do not add smooth curves that invent extrema or imply measurements between sparse observations.

Identify observed, provisional, estimated, and forecast sections with labels and distinguishable treatment. Keep comparison windows aligned. Too many overlapping lines call for a focused subset with disclosure, small multiples, or an overview plus selection. Retain context rather than fading every unselected series until it becomes unreadable.

### Distributions and relationships

A histogram's bins can change the apparent pattern. Check reasonable widths and identify the bin definition; for unequal widths, use density when area is intended to represent frequency. A boxplot needs a defined median, quartiles, and whisker rule. Show observations when small samples or unusual structure matter. A violin's smoothed shape is an estimate, not a count of observed values.

Avoid using mean bars alone when the question concerns variation. Supply an appropriate distribution or interval. For crowded scatterplots, consider smaller marks, transparency, aggregation, or faceting; explain bin counts or density when aggregating. Do not let overplotting conceal the sample size or make a rare pattern appear common. Label fitted relationships and their basis separately from observations.

### Parts, hierarchies, and cumulative values

A pie can communicate a simple, complete whole with a few clearly separated shares; avoid it for close ranking or repeated precise comparisons. Do not draw a pie from overlapping responses. A 100% stacked bar compares composition while hiding differences in total size; provide totals when relevant. Middle segments of a stack lack a shared baseline, so use separate panels for close component comparison.

Use a treemap when hierarchy and broad size relationships justify the area encoding. Give labels or a companion table for precise values. A waterfall explains additive contributions between defined start and end totals. Do not insert percentages with different denominators into the same additive bridge.

Use a table when exact values and several attributes are the main task. Align numeric fields, state units once per coherent field, and preserve header associations under adaptation. In a combined table-chart, keep the marks attached to the correct rows and values.

## 8. Show uncertainty and missingness

Distinguish variation among observations, uncertainty about an estimate, and a range of possible future outcomes. Select an encoding for the actual quantity: observations, interval, band, distribution, or explicitly bounded scenarios. Do not derive uncertainty from visual appearance.

Label an interval's type and level where relevant. A standard deviation, standard error, confidence interval, credible interval, and prediction interval answer different questions. Preserve the method's interpretation supplied by the analytical owner. Do not infer significance, equivalence, or a causal effect merely from whether two drawn intervals overlap.

Forecasts need a visible boundary from observations. Scenarios are conditional paths, not probabilities unless the source assigns probabilities. A smooth central line with an unexplained pale region can imply more certainty than the evidence supports. Name the region and show which conclusions remain uncertain.

Give zero, missing, not applicable, unavailable, and suppressed values distinct meanings. A missing region must not inherit the colour for the lowest observed value. A broken line must not imply that a measured zero occurred. Preserve these distinctions in the legend, text alternative, table, and export.

Do not rank uncertain estimates as though small differences establish an exact ordering. Show intervals, explain ties or unstable ranks, or emphasize broader groups when supported. If the uncertainty prevents the intended conclusion, revise the conclusion.

## 9. Explain processes, networks, and mechanisms

### Name the grammar

Define what nodes and edges mean before drawing them. A node can be an actor, object, state, activity, or place. An edge can mean sequence, dependency, transfer, association, communication, or cause. Avoid using one undifferentiated arrow for several relationships. Label the verb, condition, unit, or transfer type when readers need it.

Choose a process flow for actions and branches, a state diagram for lifecycle changes, a sequence diagram for messages over time, and a hierarchy for parent-child membership. Preserve established notation in specialist contexts. A diagram's reading direction does not by itself establish time or causation.

Keep decisions explicit, with labelled branches and reachable outcomes. Include important loops, exits, failures, and prerequisites. Separate concurrent work from sequential work. Number illustrated procedural steps when the order must survive a changed layout.

### Networks and measured flows

Use node-link layouts for tracing paths in a sparse network. Make node identity stable, minimize avoidable crossings, and distinguish a crossing from a junction. In a force-directed layout, proximity and central position are layout results unless explicitly encoded; do not present them as measured similarity or importance.

For dense relationship lookup, consider an adjacency matrix with a purposeful row/column order. A matrix can expose clusters but makes multistep paths harder to trace. Use the form that supports the task rather than an attractive hairball of edges.

A width-coded flow diagram needs measured, comparable flows. State units and time boundaries. Reconcile incoming and outgoing quantities, showing losses, storage changes, external inputs, or exclusions. Use a plain process diagram when there are no flow measurements. A funnel requires an ordered progression with compatible stage definitions; unrelated counts do not form an attrition process.

### Explanatory drawings

Use a section to reveal an interior, an exploded view to show assembly relationships, and a sequence to explain change. Identify cut planes, orientation, parts, and the relationship between views. Retain a stable viewpoint or provide an orientation cue when changing it.

Keep labels near their referents with unambiguous leader lines. Separate leaders from flow arrows and dimension lines. Label a magnified inset and its source region; show its different scale when dimensions matter. State “schematic” or “not to scale” when proportional accuracy is deliberately absent.

A plausible drawing can invent a mechanism. Verify parts, connections, direction of motion, and the depicted state with a qualified source. A metaphor can introduce a concept, but must not substitute for a physically or logically accurate explanation when the task depends on one.

## 10. Use geography when location matters

Use a geographic map for location, adjacency, distance, direction, or spatial patterns. Use bars or dots for ranking regions when the reader does not need their arrangement. Large territories attract attention even when they contain few people; map area does not measure population or importance.

Choose the map's extent, projection, and aggregation for the task. Every projection compromises some property; preserve the property that matters and identify material distortion. Do not use a distorted overview to support precise distance or area comparisons. Supply a suitable scale, orientation, locator, or inset when needed for use.

Default to rates, proportions, or other appropriate derived values for comparable area fills. Use proportional symbols for totals when that better answers the question. State denominators and verify boundaries and dates. A per-person rate and a per-area density describe different phenomena.

Choose and label class breaks deliberately. Quantiles, equal intervals, and domain thresholds can produce different impressions from the same values. State thresholds and units; keep breaks comparable across maps when comparing places or periods. Show missing areas separately. Do not imply a sharp real-world discontinuity simply because a classification boundary changes colour.

A cartogram can resize regions by a stated variable, but needs explanation and recognizable labels. A geographic inset that repositions an island must disclose the relocation when relative position matters. Keep address, route, and accessible-entrance information available in a usable equivalent.

## 11. Design metro and route schematics

A metro schematic can exchange geographic fidelity for clear station order, line identity, branches, and transfers. Preserve the network's topology: which stations connect, in what order, through which services, and with which permitted changes. Equal visual spacing does not establish equal travel time or walking distance.

### Establish the network before arranging it

Verify station and service identifiers, sequence, branches, termini, direction restrictions, and transfers from authoritative operator data. Distinguish a service line from the physical track it uses. Several services can share track; a schematic must still let riders follow the intended service.

Define symbols for ordinary stops, interchanges, walking links, closed sections, and other task-relevant states. A crossing without a transfer must look different from a connected junction. Different platforms, paid-area changes, or out-of-station walks may require distinct transfer descriptions. Do not collapse those distinctions to make the drawing cleaner.

### Draw a coherent route grammar

Default to a small, consistent set of directions and bend treatments. Horizontal, vertical, and diagonal segments can simplify tracing, but a fixed angle system is a design choice. Use another geometry when it better handles the actual network. Avoid unnecessary bends, acute tangles, label collisions, and ambiguous shared segments.

Expand crowded centres and compress long peripheral stretches when connectivity remains clear. Preserve useful relative orientation and recognizable geographic anchors where practical. Add geographic context selectively; a river can help orientation while an elaborate street background can obscure line tracing.

Keep line names, identifiers, and labels available alongside colour. Apply a consistent label side and offset where feasible, with deliberate exceptions at dense junctions. Show enough of a shared or branching line that the rider can follow it through the interchange without mentally jumping across unrelated strokes.

A diagram optimized for transfers is unsuitable for estimating walking distances. State its schematic character and provide geographic or travel-time information when the task needs it. Do not infer step-free access, platform accessibility, service frequency, or journey duration from a generic station symbol.

### Test routes, not only appearance

Trace representative direct, transfer, branch, reverse-direction, and disrupted journeys against the network data. Check every depicted connection and missing connection. Test whether a crossing can be mistaken for an interchange and whether a walking link looks like a train service.

Supply a structured route list or journey result preserving the required connections and transfer conditions. Verify live service and accessibility information before deployment; a visually correct network snapshot can become operationally wrong. Operator-specific symbols, dimensions, and brand rules remain with that operator.

## 12. Integrate words and graphics

Use a title to orient the reader or state a supported finding. An explanatory title can say “Waiting times rose after April” when the data establish that pattern. An exploratory title such as “Monthly waiting times by clinic” remains useful across different selections. Update a dynamic finding when its filters change.

A subtitle can define population, period, unit, and filters. Axis labels and keys decode the marks. Annotations explain consequential events, exceptions, or unusual values at their location. Notes disclose methods and limitations; the source line identifies the evidence. These roles can combine in a small graphic, but essential information must remain findable.

Prefer direct labels when they shorten the path between a mark and its meaning. Use a legend when direct labels would collide or when one key serves a coherent repeated system. Order the key to match the graphic where practical. Define unfamiliar encodings with a small worked mark or “how to read” example.

Keep labels legible at the size people receive. Use units, signs, separators, dates, and abbreviations consistently. Localize formatting and teach unfamiliar terms. Delegate typeface, numeral features, wrapping, and rendering to Typography. Resolve a crowded chart by changing content density or structure before shrinking all labels.

Keep source and material caveats with the graphic when it can circulate alone. A screenshot or social crop should retain the population, period, units, and qualification needed to prevent a false reading. A source URL can lead to full methods, but the reader should not need to open it to discover that the displayed figures are estimates.

## 13. Direct attention without changing the evidence

Create an entry point, a primary comparison, and a path to detail. Use position, annotation, and controlled emphasis to guide attention. Keep surrounding evidence readable enough to assess the highlighted claim. Emphasis must not turn excluded, uncertain, or unselected items into apparent zeroes.

Use detail where it serves inspection. A dense chart can remain clear through stable repeated structure and coherent grouping; a sparse chart can still be ambiguous. Divide complexity by question or comparison rather than by arbitrary equal-sized panels. Read Composition for the page-level arrangement.

For an explanatory sequence, orient the reader, introduce the encoding, show the comparison, then explain its consequence and limit. Keep each frame interpretable when readers revisit it. A long scrolling narrative should allow comparison without requiring people to remember a vanished chart.

Use illustrations when they explain subject matter, scale, mechanism, or context. Keep decorative artwork outside quantitative comparison fields where its shapes could be mistaken for values. Brand colour and expressive forms can remain when they preserve the encoding and access requirements.

## 14. Provide equivalent access

Define the information and operation to preserve before choosing an alternative. A chart may need a concise finding plus a structured table; a network may need an adjacency list or route instructions; a mechanism may need an ordered explanation of parts and actions. A CSV alone does not explain why an arrow denotes a transfer or how to choose a route.

Provide short identification and access to a longer structured equivalent where the visual carries complex information. Include the important pattern, values or relationships, units, scope, and qualifications. Do not replace an explanation with an inventory of colours and shapes unless those properties carry essential meaning.

Keep necessary labels and information available without distinguishing colour alone. Use the Accessibility guide for applicable contrast, semantics, input, and text-alternative requirements. Simulated colour-vision views and automated checks are useful diagnostics; they do not establish access for every reader.

For interactive work, keep equivalent information and actions synchronized with filters, selection, and data version. Make details available through appropriate keyboard and touch interaction. Choose a manageable navigation model for dense marks rather than adding thousands of unexplained tab stops. Verify the actual chart and alternate task with assistive technology where relevant.

## 15. Adapt and interact without losing meaning

Recompose for a narrow format; do not just shrink the desktop graphic. Preserve the question, scales, labels, relevant set, and comparison. Possible adaptations include horizontal bars, wrapped labels, vertically arranged small multiples, fewer simultaneous series with disclosure, or an explicitly scrollable two-dimensional region.

When a smaller view shows a subset, state that selection and retain access to required context. Do not remove inconvenient categories, error intervals, or long names to make a mobile layout fit. Keep comparison domains aligned when panels stack.

Use interaction when filtering, selecting, or inspecting changes what the reader can learn. Keep the initial state useful and show active filters, units, period, and data status. Offer a reset and distinguish no observations from zero values or an error. Preserve context when zooming or changing a domain.

Tooltips supplement interpretation; essential units and limitations cannot exist only on hover. Keep a selected mark, its details, and its place in the overview understandable. Apply Interaction for control and state behavior, and Accessibility for alternative input and equivalents.

Animation can explain a transition when object identity and scale remain stable. Provide a static comparison, pause or step control, and appropriate reduced-motion treatment when needed. Repeated autoplay is a poor substitute for side-by-side comparison. If the scale changes between frames, make the change explicit rather than morphing it into apparent data change.

## 16. Produce and maintain the graphic

Choose the production method after the information design. Use plotting tools for accurate quantitative geometry, diagram tools for structured connections, and illustration tools for authored explanatory views. Combine them when needed, retaining the source mapping. An image-generation result is a visual proposal; verify or reconstruct exact values, labels, connections, and topology before treating it as a factual graphic.

Maintain an editable master, the source snapshot or query, transformations, representation specification, and necessary export settings. Store private source material according to the project rules. If adjusting generated marks manually, preserve their encoded positions and extents and check that the next regeneration does not discard the correction.

Prefer formats that preserve sharp lines and readable text for the delivery medium. Use vector output where supported, or adequate raster dimensions for the intended physical or displayed size. There is no universal DPI for every screen graphic. Proof font substitution, glyphs, clipping, transparency, thin strokes, and colour reproduction in the exported file.

Check print at intended size and viewing distance; check screen output at supported widths and zoom. Verify a PDF's reading order and equivalents separately from its visual appearance. Test embedded charts in the actual slide, page, or application; a correct standalone export can be cropped or rescaled incorrectly by its container.

For changing information, assign an update owner and version the data and graphic together. Recheck annotations, category mappings, legends, alternate views, and exported figures after an update. Identify the publication or data date when freshness matters.

## 17. Review and diagnose

Reconcile the finished display with the source. Inspect values, labels, units, ordering, scales, intervals, category coverage, totals, connections, and notes. Recheck derived values independently of the plotting configuration. A plausible image is insufficient evidence.

Test the reader's actual question. Can someone identify the unit, make the intended comparison, explain an unfamiliar mark, or trace the route without correction from the author? Compare with a plain labelled alternative when the visual benefit is uncertain. A designer's self-review cannot establish intended-user comprehension; report that limit when no reader test is available.

| Symptom | Likely mechanism | Repair |
| --- | --- | --- |
| Large visual difference, small numerical change | Truncated magnitude baseline, area/radius error, or perspective | Correct geometry or use an explicit difference/position encoding. |
| Strong relationship appears only in an overlay | Independently tuned axes or selected time windows | Use aligned panels and defensible common periods. |
| Reader cannot tell what “more” means | Undefined size, colour, unit, or denominator | Define the encoding and comparison basis. |
| Most labels need leader lines | Too little space or too many simultaneous marks | Recompose, facet, or offer a focused view with context. |
| Every region looks extreme | Arbitrary class breaks or unsuitable colour progression | Recheck classification and apply the colour-scale owner. |
| Diagram looks precise but has no measured quantities | Decorative thickness, spacing, or gradients imply magnitude | Use uniform treatment or label the schematic semantics. |
| Rider changes at a crossing | Junction and crossing grammar is ambiguous | Correct the symbols and verify the edge list. |
| Graphic reads well only with the author present | Missing teaching, labels, context, or equivalent | Add self-contained orientation and test independent reading. |
| Export differs from the master | Substitution, clipping, scaling, or manual drift | Correct production settings and reinspect the delivered file. |

The graphic is ready for its stated conditions when the evidence supports its claims, the encoding is consistent, required relationships remain available, exports have been inspected, and material limitations are disclosed. Distinguish data checks, visual inspection, access testing, and intended-reader testing in the handoff.

## 18. Work through complete examples

The following examples are illustrative, not reported findings or live service information.

### Compare a total with a rate

Two districts report 40 incidents among 10,000 residents and 60 among 30,000 residents for the same period and definition. The second has the larger count. The first has the higher resident-based rate: 4 versus 2 incidents per 1,000 residents.

For “Where is the reported rate higher?”, use aligned dots or zero-based bars labelled “Incidents per 1,000 residents.” Show district names, period, rates, and the count/population context in an adjacent table or note. An appropriate title states that the first district's reported rate is higher. Do not claim it is more dangerous without the analytical evidence needed for that inference.

For “Where is the total workload larger?”, show counts instead. If both questions matter, use two aligned panels with distinct units. Verify both calculations, source coverage, rounding, and the text equivalent. Do not use differently sized district silhouettes as a substitute for either comparison.

### Explain a return process

The information contract says: a customer requests a return; eligibility is checked; eligible returns receive instructions; ineligible requests receive a reason and review route; received items are inspected; inspection leads to refund or a stated exception.

Use a process diagram with labelled eligibility and inspection branches. Put the customer and service actions in clear groups where that distinction helps. Show the review loop and the endpoint of each branch. Arrows mean progression under the labelled condition; their widths are equal because no volumes are supplied. Use an ordered text equivalent with the same conditions. Verify every branch against the policy, then apply the relevant diagram implementation standard.

### Draw a metro schematic

Suppose a fictional Red service runs A–B–C–D and a Blue service runs E–C–F. C allows a transfer. The drawn Red and Blue routes also cross between B and C, but there is no station at that crossing.

Make C a clear interchange and the other crossing a clear nonconnection. Label the services so colour is supplementary. A journey from A to F follows Red to C, then Blue to F; it does not change at the earlier crossing. Label the view as schematic. Do not infer the distance or walking time between E and B from their placement.

Provide the station sequences and transfer at C in text. Verify the direct A-to-D route, the A-to-F transfer, and the absence of a transfer at the crossing. Check labels in the smallest supported format and disclose any unsupported live-service information before operational use.
