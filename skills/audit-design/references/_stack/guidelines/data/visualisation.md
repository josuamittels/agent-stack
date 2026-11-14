---
name: data-visualisation
description: "Purpose-led reference for designing, selecting, explaining, and reviewing data visualisations, from data semantics and perceptual encoding to advanced charts, uncertainty, maps, multivariate views, dashboards, and accessible delivery."
version: "0.2.0"
created: "2026-10-24"
updated: "2026-11-14"
author:
  - "Josua Mittelstaedt"
references:
  - "Tamara Munzner"
  - "Andy Kirk"
  - "Claus O. Wilke"
  - "data.europa.eu"
  - "Alberto Cairo"
  - "William S. Cleveland"
  - "Robert McGill"
  - "Edward R. Tufte"
  - "Stephen Few"
  - "Financial Times Visual Journalism Team"
  - "Elizabeth Ricks"
  - "Cole Nussbaumer Knaflic"
  - "World Wide Web Consortium"
  - "Government Analysis Function"
  - "UX Magazine"
  - "Netquest"
  - "Cynthia Brewer"
  - "Mark Harrower"
  - "Alexander Lex"
  - "Nils Gehlenborg"
  - "Hendrik Strobelt"
  - "Romain Vuillemot"
  - "Hanspeter Pfister"
  - "Martin Wattenberg"
  - "Fernanda Viégas"
  - "Ian Johnson"
type: reference
status: experimental
---

# Data visualisation

A useful visualisation helps someone answer a question, understand a relationship, or make a decision with appropriate confidence. Its quality depends on the fit between purpose, evidence, representation, and use. A polished chart of the wrong quantity still answers the wrong question.

This reference supports designers, analysts, researchers, and agents working from simple comparisons through complex analytical displays. It explains how to select information, encode it, combine views, and check the result. It is a working decision reference; specialist methods still require suitable analytical expertise.

## Use this reference

Read sections 1–7 before choosing a chart. Use sections 8–16 for the relevant relationship or data structure. Sections 17–24 cover explanation, systems, interaction, access, and delivery. Sections 25–27 provide worked cases, a reusable brief, and terminology.

For a first chart, follow the brief in section 26, use the selection table in section 7, and finish with section 24. For an existing chart, first check its purpose, data contract, and scales; styling cannot repair those errors. For a complex workspace, read multivariate views, dashboards, interaction, and accessibility together.

### Relationship to other guidelines

Use the [aesthetics framework](../aesthetics/reference.md) to coordinate visual decisions. This guide develops the data-specific reasoning: what quantity matters, which comparison serves the user, what an encoding implies, and how analytical complexity remains interpretable. [Infographics](../aesthetics/infographics.md) covers the wider communication form, including process explanations, technical diagrams, and transport schematics. Apply its shared principles of truthful representation alongside this guide; a conceptual diagram and a statistical chart make different kinds of claim.

| Decision | Use this guide for | Consult the related owner for |
| --- | --- | --- |
| Colour | Variable type, comparison, reference point, encoding versus emphasis | [Colour](../aesthetics/colour.md#15-encode-data-with-colour): palette construction, perceptual ramps, themes, gamut, and reproduction |
| Shape and symbols | Category, quantity, topology, uncertainty, and direction conveyed by a mark | [Iconography](../aesthetics/iconography.md): symbol construction and family consistency |
| Spatial arrangement | Measured coordinates, comparisons, facet alignment, and analytical hierarchy | [Composition](../aesthetics/composition.md): page grids, balance, spacing, density, and reading order |
| Text | Required labels, metric definitions, annotations, and claims | [Typography](../aesthetics/typography.md): readable text and numerals; [English](../languages/english.md): wording |
| Interaction | Filter semantics, selection, comparison, and preserved context | [Interaction](../aesthetics/interaction.md): controls, feedback, state, and recovery |
| Motion | Whether change or sampled outcomes need animation | [Motion](../aesthetics/motion.md): transition behaviour and user preferences |
| Access | Equivalent analytical questions and information | [Accessibility](../aesthetics/accessibility.md#18-make-data-and-complex-workspaces-accessible): semantics, inputs, contrast, assistive technology, and verification |

Analytical work establishes data validity, transformations, statistical models, disclosure controls, and permissible inference. This guide specifies what visual design needs from that work and how to represent it faithfully. It cannot establish causality, validate a forecast, or certify a dataset. Return unresolved analytical claims to their owner before publication.

All numerical examples below are illustrative. They demonstrate design decisions, not findings about real organisations or populations.

## Contents

1. [Start with the user's purpose](#1-start-with-the-users-purpose)
2. [Establish the data contract](#2-establish-the-data-contract)
3. [Understand data types and structures](#3-understand-data-types-and-structures)
4. [Select the information and comparison](#4-select-the-information-and-comparison)
5. [Use perception and visual encoding deliberately](#5-use-perception-and-visual-encoding-deliberately)
6. [Preserve scales, coordinates, and geometry](#6-preserve-scales-coordinates-and-geometry)
7. [Choose a representation by task](#7-choose-a-representation-by-task)
8. [Compare amounts, ranks, and deviations](#8-compare-amounts-ranks-and-deviations)
9. [Show composition and overlapping sets](#9-show-composition-and-overlapping-sets)
10. [Show distributions and individual observations](#10-show-distributions-and-individual-observations)
11. [Show time, change, cycles, and cohorts](#11-show-time-change-cycles-and-cohorts)
12. [Show association and model behaviour](#12-show-association-and-model-behaviour)
13. [Show uncertainty and incomplete information](#13-show-uncertainty-and-incomplete-information)
14. [Use geography when space matters](#14-use-geography-when-space-matters)
15. [Show hierarchies, networks, and flows](#15-show-hierarchies-networks-and-flows)
16. [Handle many variables and dense data](#16-handle-many-variables-and-dense-data)
17. [Use colour, shape, and texture as a system](#17-use-colour-shape-and-texture-as-a-system)
18. [Compose, label, and explain](#18-compose-label-and-explain)
19. [Build dashboards around decisions](#19-build-dashboards-around-decisions)
20. [Design useful interaction and motion](#20-design-useful-interaction-and-motion)
21. [Provide equivalent access](#21-provide-equivalent-access)
22. [Adapt to the medium and viewing conditions](#22-adapt-to-the-medium-and-viewing-conditions)
23. [Produce, maintain, and govern](#23-produce-maintain-and-govern)
24. [Evaluate and diagnose](#24-evaluate-and-diagnose)
25. [Work through complete decisions](#25-work-through-complete-decisions)
26. [Use the design brief and handoff](#26-use-the-design-brief-and-handoff)
27. [Use terms consistently](#27-use-terms-consistently)

## 1. Start with the user's purpose

### Define the job before the display

Write a concrete purpose: “A service manager needs to decide which queue needs additional capacity this week.” Then identify what the person must see to do that. The task may require arrival volume, capacity, backlog age, and a threshold, rather than the most readily available metric, such as total completed cases.

Establish the reader's familiarity with the subject, numerical literacy, access needs, time available, and authority to act. Recover this from actual workflows, interviews, prior usage, and representative tasks. A job title alone does not establish an appropriate level of detail. An executive investigating a failure may need individual records; an analyst responding to an alert may need one clear exception.

Use a purpose statement with four parts:

> **Who** needs to **understand or decide what**, using **which evidence and comparison**, under **which conditions and consequences**?

Identify the cost of a wrong interpretation. An exploratory sketch can tolerate provisional questions; a resource allocation graphic needs visible uncertainty, comparability, and the implications of aggregation. More consequential use justifies stronger verification, not automatically more visual detail.

### Separate modes of use

| Mode | Reader needs | Design consequence |
| --- | --- | --- |
| Explore | Discover patterns and formulate questions | Preserve breadth, filtering, data access, and a record of transformations; label findings as provisional |
| Explain | Understand an established finding and its limits | Select evidence, order the argument, and annotate the relationship |
| Monitor | Notice meaningful change and decide whether to investigate | Show baseline, expected variation, freshness, thresholds, and next action |
| Diagnose | Compare competing explanations | Offer relevant breakdowns, aligned views, and source detail; do not imply diagnosis from correlation |
| Decide | Compare options and consequences | Show tradeoffs, practical thresholds, uncertainty, and affected groups |
| Look up | Retrieve a precise value or record | Prefer a table, search, or direct answer; add a chart when patterns also matter |
| Learn | Build a mental model of an unfamiliar relationship | Introduce notation progressively and demonstrate how to read an example |

A product can support several modes, but each view needs a primary one. A live operational page and a retrospective argument usually need different defaults.

### Choose whether to visualise

Use a sentence for one fact with little meaningful comparison: “The application closes on 30 June.” Use a table for exact lookup, mixed units, or a small set of options with several attributes. Use a chart when position, grouping, shape, or connection makes a relationship easier to inspect.

Do not chart unsupported data to give a claim an appearance of evidence. When the question cannot be answered, show what is known, what is missing, and what additional evidence is required.

## 2. Establish the data contract

Before drawing, document what the data means. The contract can be brief, but each material ambiguity needs a resolution or a visible qualification.

| Required input | What to establish | Common failure |
| --- | --- | --- |
| Unit of observation | One row represents a person, event, household, location, interval, or estimate | Event counts described as unique people |
| Population and coverage | Who is eligible, who is observed, geography, inclusion rules | Survey respondents described as the entire population |
| Measure and unit | Count, amount, duration, rate, index, score, or model estimate | A score of 80 presented as 80% |
| Grain | Finest valid level of detail and aggregation | Monthly values presented as daily measurements |
| Denominator | Eligible population, exposure, time at risk, or base period | Different denominators compared as equivalent rates |
| Time | Event versus recording date; timezone; period boundaries; maturity | Recent incomplete periods appearing to deteriorate |
| Provenance | Source, extraction date, revision, transformations, and owner | A polished graphic detached from its dataset |
| Comparability | Definitions, classifications, boundaries, and methods across groups | A reporting change mistaken for a real trend |
| Quality and uncertainty | Missingness, duplication, measurement error, sampling, weighting, model limits | Decimal precision implying exact knowledge |
| Disclosure | Permitted detail, suppression, aggregation, and export scope | A filter exposing a small identifiable group |

A value can be present and still be unsuitable. Check whether it measures the user's concept. Clicks can measure activity without establishing understanding. Recorded incidents can change because reporting changes. Label proxies as proxies and explain their limits where those limits affect use.

For derived measures, retain the calculation and base values. A conversion rate needs eligible exposures and conversions; an index needs its reference period; a weighted estimate needs its weighting basis. Do not average subgroup percentages unless the analytical definition justifies that operation.

Represent missing, zero, not applicable, suppressed, and not yet available as different states. A blank cell is otherwise ambiguous. Do not connect a line across an unobserved interval without making that interpolation explicit.

## 3. Understand data types and structures

### Classify by meaning

Software storage types are insufficient. A numeric identifier is a label; dates carry interval and calendar meaning; an ordinal rating is ordered without necessarily having equal steps.

| Type | Meaning and examples | Appropriate encoding | Constraint |
| --- | --- | --- | --- |
| Nominal | Unordered identity: product, route, department | Separate positions, labels, hue, shape | Do not imply numerical distance or rank |
| Ordinal | Ordered categories: low/medium/high, response levels | Ordered positions, ordered lightness, explicit labels | Equal spacing need not mean equal differences |
| Quantitative, discrete | Counts of events or units | Position, length, countable marks | Show meaningful integer resolution; negative counts need a distinct definition |
| Quantitative, continuous | Duration, mass, temperature | Position, intervals, distributions | Precision and measurement limits matter |
| Interval scale | Differences meaningful; zero arbitrary, such as Celsius | Position and difference | Ratios are not meaningful: 20°C is not twice 10°C |
| Ratio scale | Differences and ratios meaningful, such as elapsed duration | Position, proportional length or area | A true zero is meaningful; transformation must preserve the intended comparison |
| Temporal | Instants, durations, sequences, recurring phases | Timelines, lines, intervals, cycle views | Calendar order, elapsed time, and recurrence answer different questions |
| Spatial | Coordinates, regions, trajectories, fields | Maps, sections, contours, vectors | Projection, resolution, and coordinate reference matter |
| Relational | Links, membership, containment, origin–destination | Networks, matrices, trees, flow diagrams | Define whether a relation is directed, weighted, observed, or inferred |
| Text and qualitative codes | Statements, documents, categories assigned by interpretation | Tables, annotated excerpts, coded matrices | Frequency depends on coding, document length, and sampling |
| Uncertain values | Estimates, distributions, ranges, scenarios | Intervals, densities, ensembles | A distribution is richer than a single number with a decorative halo |

Discrete and continuous describe possible values; interval and ratio describe the meaning of arithmetic. These classifications overlap rather than replace each other. A month is also cyclic within a year. A demographic category can have no intrinsic order even when the display sorts groups by a measured result.

### Identify the dataset structure

A table holds items and attributes. A time series adds temporal order. A hierarchy adds containment. A network adds links that can cross levels. A field describes a value over space or time, such as temperature on a grid. A trajectory follows an entity through coordinates. A set dataset records membership, possibly in several sets at once.

Choose a representation for the structure required by the task. A network exported as an edge table still contains relationships; a table of regional totals does not require a map. A hierarchy with shared membership may need a graph rather than a tree.

Distinguish attributes from dimensions used to group observations, and distinguish both from visual dimensions. A two-dimensional page can show many attributes through position, colour, shape, panels, and text. A three-dimensional chart does not automatically support more useful analysis.

## 4. Select the information and comparison

### Give every included element a job

Include a variable, category, label, or view when it supports the primary question, a necessary secondary question, or a qualification that changes interpretation. Available data is not a reason to display it all.

Use this order when reducing material:

1. Remove decoration and repeated explanations that do not help decoding.
2. Remove irrelevant measures and duplicate views.
3. Group or facet information along a meaningful dimension.
4. Aggregate at the level of the decision, while preserving consequential variation.
5. Offer detail separately when the user can still find it and understand what was omitted.

Keep denominators, definitions, material exceptions, uncertainty, and counterevidence near the claim they qualify. A full download does not repair a misleading summary.

| Treatment | Use when | Required disclosure or safeguard |
| --- | --- | --- |
| Omit | Information does not affect the task or fair interpretation | State scope when omission could be mistaken for completeness |
| Filter | A meaningful subset answers the current question | Keep active filters and excluded population visible |
| Aggregate | Decisions concern groups or intervals | Retain aggregation rule; inspect tails and subgroups first |
| Group as “Other” | Small categories obstruct the main comparison | State membership or provide detail; preserve important small groups |
| Sample | Rendering all observations is impractical | State method and sample size; preserve rare cases where relevant |
| Clip the view | A detail view needs a smaller domain | Indicate excluded values and provide overview or overflow markers |
| Suppress | Disclosure requirements limit detail | Distinguish suppression from zero and prevent reconstruction |

### Choose the comparison that makes the quantity meaningful

A lone total rarely establishes whether something is good, unusual, sufficient, or changing. Choose the comparator from the task: previous comparable period, target, distribution of peers, expected range, counterfactual estimate, or capacity.

Prefer exposure-adjusted rates for risk or propensity, and absolute counts for workload. Often the user needs both. A group can have a lower rate and a larger total burden. Adjusting for population does not automatically remove differences in age, case mix, eligibility, or measurement.

Use consistent units and comparable periods. Distinguish stocks measured at an instant from flows measured over an interval. Do not add account balances across months as if they were revenue. Distinguish a cumulative total from the increment that changes it.

Check whether the chosen summary hides the decision. Median waiting time can conceal a severe tail. Revenue per customer can increase while the number of customers falls. An overall improvement can result from a changing mixture of groups rather than improvement within each group.

## 5. Use perception and visual encoding deliberately

### Define marks, channels, and reading tasks

A **mark** is an element such as a point, line, or region. A **channel** is a visual property that varies: position, length, size, hue, shape, orientation, or texture. An **encoding** maps a data attribute to that property. A **scale** defines the mapping from values to positions, colours, or sizes.

For example, in a scatter plot, each point might represent one store. Horizontal position shows floor area, vertical position shows weekly revenue, shape shows store format, and colour highlights a selected region. Each extra channel asks the reader to decode another rule.

Assign the most consequential comparison to the channel that makes it easiest to judge. For close numerical differences, default to position on an aligned scale. A reader can compare two neighbouring endpoints more precisely than two irregular areas. This is a useful preference for quantitative tasks, not proof that one chart is best for every purpose.

| Channel | Strong use | Limitation and design consequence |
| --- | --- | --- |
| Position on a common scale | Precise comparison, trends, association | Preserve alignment; do not shift coordinates for optical balance |
| Length | Amount from a shared baseline | Baseline defines meaning; use dots when a truncated domain is needed |
| Area | Approximate magnitude and part-to-whole | Close differences are difficult; provide values or a companion aligned view |
| Volume | Actual spatial quantities in specialist contexts | Perspective and occlusion impede comparison; prefer 2D for abstract numbers |
| Hue | Distinguishing a few categories | Does not naturally encode ordered magnitude; cultural meaning varies |
| Lightness | Ordered amount or deviation within a suitable palette | Small differences and extreme ends may be hard to distinguish |
| Chroma or saturation | Limited emphasis or a carefully tested ordering | Appearance depends on hue and background; not a universal quantitative ruler |
| Shape | A few distinct categories, redundant identity | Small or overlapping shapes become indistinguishable; no natural magnitude order |
| Orientation | Direction, angular measurements, selected distinctions | Small angular differences are hard to compare; line slope also depends on axis geometry |
| Texture or pattern | Redundant category or missing-state distinctions | Dense patterns can shimmer, merge, and interfere with labels |
| Connection | Paths, continuity, membership, dependence | A line implies a relationship; define it rather than using it ornamentally |
| Enclosure and proximity | Groups, facets, containment | Readers infer membership and similarity; spacing can make an unintended claim |
| Motion | Change, continuity of identity, sampled outcomes | Transient information burdens memory and can exclude users |

### Make grouping cues agree

Nearby items appear related. Similar marks appear to belong to the same category. Connected marks imply a path or continuity. Enclosed items imply a group. Use these cues to reduce decoding, and check that they do not contradict the data.

Rapid visual salience can draw attention to an outlier or selected series. It does not ensure comprehension. A bright mark still needs an identity and a relevant comparison. Several competing accents erase the hierarchy. See [Composition](../aesthetics/composition.md#4-use-perception-to-clarify-relationships) for grouping and attention.

### Combine channels with restraint

Use additional variables only when the task needs them simultaneously. Two positions plus category colour can work well; adding size, shape, labels, opacity, and animation can overwhelm the same plot. Prefer facets or coordinated views when an extra encoding makes identification unreliable.

Redundant encoding gives the same distinction more than one cue, such as line style plus label. It can improve access. Independent encoding assigns separate attributes to separate cues; it increases information but also decoding work. Avoid using the same property for several meanings, such as opacity for both uncertainty and selection.

## 6. Preserve scales, coordinates, and geometry

### Choose the scale for the question

| Scale | Appropriate question | Required care |
| --- | --- | --- |
| Linear | How much larger is the absolute difference? | Equal steps represent equal differences |
| Logarithmic | How many times larger; what relative growth? | Positive values only; label original units and multiplicative steps |
| Symmetric log or other signed transform | How do very small and large signed values coexist? | Explain the linear region, transform, and limits; provide readable reference ticks |
| Percentage | What fraction of a defined whole? | Give denominator; distinguish percentage-point and relative changes |
| Indexed | How did series change relative to a chosen base? | State base date/value; retain original levels when scale matters |
| Standardised | How far from a group's reference distribution? | Explain centring/scaling; do not imply equal absolute levels |
| Ordinal or band | Where does an ordered or unordered category belong? | Position is an arrangement, not a continuous measurement |
| Quantile colour bins | Which observations have similar rank? | Equal class counts do not mean equal numerical intervals |

Never replace zero with an arbitrary small positive value to make a log scale work. Use a representation that preserves zeros, separate their count, or choose an explained alternative. A logarithm changes the comparison, not merely the appearance.

### Keep extent proportional

A conventional amount bar begins at zero because its length represents the value. For small differences around a high baseline, use a dot plot with a clearly labelled restricted axis, a difference plot, or an additional detail panel. A broken bar axis does not restore truthful length comparison.

Line and scatter plots can use nonzero domains when the question concerns variation within that domain. Keep context visible, label limits, and assess whether the crop overstates practical importance. Filled area charts generally require the quantity's meaningful baseline because area itself carries magnitude.

For circles, make **area** proportional to value: `radius = k × sqrt(value)`. Doubling a value increases radius by about 1.414, not 2. For a square, side length likewise follows the square root. Scaling a pictogram's width and height directly with a value squares its area. If a true volume represents magnitude, linear dimensions follow a cube root, but readers still face perspective and occlusion.

A range bar between a start and end is an interval, not an amount from zero. Its endpoints must be labelled or explained. Keep this distinction explicit for Gantt charts, uncertainty intervals, and floating waterfall contributions.

### Control alignment and aspect ratio

Use common domains across panels when comparing levels. Independent scales can reveal within-series shape, but make their use conspicuous and state that heights are not comparable. Do not let filtering silently change a domain and make an unchanged value appear to grow.

Aspect ratio changes apparent steepness. Choose dimensions that reveal the relevant pattern without manufacturing drama. For geometric comparisons, such as predicted versus observed values against an equality line, use equal scaling of equal units when angle is meant to carry meaning.

Default to separate aligned panels rather than dual axes. Two arbitrary vertical scales can manufacture apparent agreement. A second axis can be appropriate for an exact unit conversion of the same quantity. If unrelated measures genuinely require a shared view, explain the independent scales and avoid interpreting crossings as meaningful equality.

### Use two and three dimensions deliberately

Do not add perspective to bars, pies, or ordinary dashboards. It changes apparent size, hides marks, and makes the front of the scene more prominent. A 3D scientific or spatial view can be appropriate when three-dimensional structure is the actual object of investigation. Provide orientation, scale, slice or projection views, controllable camera, and access to hidden regions. Rotation alone is an inadequate comparison method when the reader needs to remember several views.

Polar coordinates can clarify cycles or angular measurements. They also change length and area judgements; an outer ring has more area than an inner ring of equal radial thickness. Choose radial form for a relevant circular relationship, then verify the quantity readers actually perceive.

## 7. Choose a representation by task

Choose the relationship before the chart family. Then check data prerequisites, audience familiarity, required precision, available space, uncertainty, and delivery constraints. Sketch at least one straightforward alternative when considering an unfamiliar form. Keep the form that supports the task with the least unnecessary decoding while retaining necessary detail.

| Reader's question | Starting choice | Consider when needed | Avoid the common mismatch |
| --- | --- | --- | --- |
| What is the exact value? | Table or labelled number | Table with in-cell bars or sparklines | A complex graphic for one lookup |
| Which category is larger? | Sorted bar or dot plot | Grouped dots, small multiples | Pie slices for many close values |
| How far from a reference? | Diverging bar, dot with reference line | Bullet chart, difference plot | Status colour without magnitude |
| What changed between two occasions? | Paired dots or dumbbell | Slope chart, separate change ranking | Independent snapshots that require mental subtraction |
| How does a quantity change over time? | Line or columns | Step plot, small multiples, horizon plot | Lines joining unordered categories |
| What is the distribution? | Histogram or empirical cumulative distribution | Strip plot, box, violin, raincloud | A mean alone or bars of means hiding observations |
| How do two quantities relate? | Scatter plot | Hexbin, density, facets, fitted relationship | Correlation coefficient without the pattern |
| How does a whole divide? | Stacked bar or simple labelled share | Pie, treemap, stacked area | Overlapping categories presented as parts |
| Which sets overlap? | Membership matrix with counts | UpSet, simple Euler/Venn diagram | Treating all intersections as disjoint without defining them |
| Where is something happening? | Map when location changes the interpretation | Proportional symbols, choropleth, spatial field | A map for a ranking that a bar chart answers better |
| What contains what? | Indented tree or tree diagram | Treemap, icicle, sunburst | A tree when entities have several parents |
| What connects to what? | Adjacency matrix or node-link view | Ego network, directed layout | A dense hairball with no query or filtering |
| How much moves between stages? | Sankey or origin–destination matrix | Alluvial view, flow map | Widths implying measured flow from mere co-occurrence |
| Which attributes vary together? | Faceted plots or scatterplot matrix | Parallel coordinates, clustered heatmap | Encoding every attribute in one overloaded glyph |
| How uncertain is the estimate? | Point and interval | Distribution, quantile dots, ensemble, outcome samples | A point estimate that looks exact |
| Which options trade off? | Aligned attribute plots or scatter plot | Pareto frontier with assumptions | A single composite score hiding weights |

A chart name does not settle design. A histogram needs bins; a scatter plot needs a meaningful item unit; a map needs classification; a Sankey needs a conserved or explained quantity. Complete those choices in the family guidance below.

## 8. Compare amounts, ranks, and deviations

### Bars, dots, and tables

Default to horizontal bars for categories with substantial labels and one magnitude each. Sort by value for ranking, by established sequence for stages or time, and by domain order when that supports lookup. State a top-N rule and disclose ties, excluded categories, and any residual total.

Use dots when precise position matters, the domain need not include zero, or several values per category share a scale. Use grouped marks for a small number of repeated comparisons; facet when groups become hard to associate. Keep group and legend order consistent.

Direct labels help sparse plots. For large collections, use a readable axis and provide values through an accessible table or selected details. A value on every mark can defeat the pattern; no values anywhere can defeat exact use. Choose according to the task.

Tables should align numbers by decimal or place value, put units in headers, use consistent precision within a measure, and distinguish missing states. Do not sum nonadditive measures. Small bars or sparklines can add pattern without removing exact values. See [Typography](../aesthetics/typography.md) for numeral setting and [Accessibility](../aesthetics/accessibility.md#18-make-data-and-complex-workspaces-accessible) for table relationships.

### Paired change and rank

A dumbbell plot joins two measurements for the same entity. Label both endpoints and their periods; sort by change when the task is change, or by current level when the task is current priority. A slope chart gives two or a few ordered occasions; crossings matter, so reduce label collisions and teach the reading direction.

A bump chart shows rank through time, not the size of gaps between values. Pair it with actual values when moving one place could mean either a tiny or a consequential difference. Do not publish an exact league table when estimates are too uncertain to support that ordering; show intervals or meaningful performance groups.

### Targets, contributions, and deviation

Show a reference line at zero for signed differences. A diverging bar makes direction and distance visible. Define whether positive means desirable, more than target, or more than baseline; these meanings are not interchangeable.

A bullet chart combines actual value, target, and contextual ranges compactly. Explain each range and derive it from a meaningful basis. Avoid gauges when angular space and decorative frames consume room without improving the task.

Use a waterfall when additive contributions reconcile a starting amount to an ending amount. Totals are anchored; intermediate contributions float. Verify `start + contributions = end`, state units, and distinguish unexplained residuals. For multiplicative growth or percentages with different bases, first establish a valid decomposition rather than forcing a waterfall.

A Pareto display sorts contributors and adds cumulative share. The denominator must be clear, and the cumulative line needs a percentage scale. Use it to inspect concentration, not to assume a fixed “80/20” law.

## 9. Show composition and overlapping sets

### Define the whole

Part-to-whole requires mutually exclusive parts that exhaust a defined total, or a visible residual. Multi-select responses, overlapping subscriptions, and multiple diagnoses do not form ordinary slices of one whole. State whether the denominator is people, responses, events, spending, or something else.

Use a 100% stacked bar to compare proportions across groups; include sample sizes or totals when scale matters. Use ordinary stacked bars when total amount and broad composition both matter. Interior segments have moving baselines, so use separate aligned bars or facets when comparing those segments precisely.

Keep segment order stable. Put a key comparison against a shared edge when possible. Label segments that are large enough to read and provide a separate key for smaller ones; do not force illegible text inside them.

### Pies, treemaps, and unit displays

A pie or doughnut can communicate a few broad shares of one whole, especially a dominant part or simple majority. Use direct labels, a stable order, and flat geometry. Choose bars when the task requires close comparisons, several groups, or change. There is no universal slice count that guarantees clarity; actual differences, labels, size, and task determine usability.

A treemap uses nested area for hierarchical composition. It is compact and can show major contributors, but small rectangles and area comparisons limit precision. Preserve hierarchy through enclosure and labels, and provide a ranked companion when exact ordering matters. Layout changes across updates can break the reader's memory of location.

A waffle or unit chart makes proportions countable when each mark has a stated value. Explain fractional units and rounding. Icons representing people can imply individual records; make clear when marks are illustrative units rather than observed persons.

### Sets and intersections

For two or three simple sets, a labelled overlap diagram can explain membership. Areas are quantitative only when deliberately calculated; otherwise say that regions are schematic. For many intersections, use a membership matrix with bars for intersection size and set size.

Define intersection semantics. “Uses A and B” can include people who also use C, while “Uses only A and B” excludes them. These produce different totals. State filtering, empty intersections, and whether displayed intersection groups partition the population. A pairwise overlap matrix does not show all higher-order combinations.

### Survey responses

For ordered response scales, preserve the response order. A diverging stacked bar can compare negative and positive responses around a declared centre. Explain the treatment of a neutral category, refusals, and missing responses; do not conceal them by splitting or dropping them without disclosure. Show respondent counts and weighting where material. Avoid averaging ordinal answers unless the analytical convention and its assumptions support that summary.

### Multicomponent and contingency data

For three nonnegative components constrained to a fixed total, a ternary plot can show their joint composition. Each vertex represents 100% of one component. Teach how to read a point, label the three axes and total, and retain the original amounts if total size matters. The three shares are dependent: one cannot increase while the others stay fixed.

A mosaic plot can show the joint distribution of categorical variables through subdivided area. State the subdivision order, totals, and whether colour represents category or deviation from an expected model. For a specific conditional comparison, grouped bars or a labelled contingency table may be easier to read. Counts, row percentages, and column percentages answer different questions.

## 10. Show distributions and individual observations

A distribution describes how observations are spread, including concentration, skew, gaps, modes, and tails. Establish whether the user needs the centre, individual variation, the fraction above a limit, or comparison between groups.

| Form | Use for | Required choices and cautions |
| --- | --- | --- |
| Strip or dot plot | Small samples and individual observations | Show sample size; separate collisions without implying measured variation |
| Beeswarm | Observations with limited overlap | Explain that lateral displacement is layout, not another measured variable |
| Histogram | Shape and frequencies over numeric ranges | State bin boundaries and count/density; inspect several bin choices |
| Density curve | Smoothed distribution shape | State normalisation; inspect bandwidth and boundary behaviour |
| Empirical cumulative distribution | Fraction at or below any threshold | Explain direction; identify sample and weighting |
| Box plot | Compact comparison across many groups | Explain quartiles and whisker convention; it can conceal multiple modes |
| Violin | Shape comparison across groups | Make width normalisation and sample size explicit; small samples do not justify elaborate smooth shapes |
| Raincloud | Distribution, summary, and observations together | Keep layers legible and avoid repeating information without a task |
| Ridgeline | Many ordered distributions | Preserve scale and ordering; overlaps can hide tails and baselines |

### Choose bins and smoothing honestly

For a histogram, equal-width bins make height proportional to count. Unequal-width bins require frequency density, such as `count / bin width`, so **area** corresponds to frequency. Do not put raw counts into unequal-width bars. Define which bin contains a boundary value.

A useful initial bin width is a starting point, not a finding. Check whether a modest change creates or erases the pattern being claimed. Align boundaries with meaningful thresholds when appropriate, and keep shared bins across group comparisons.

Density estimation replaces discrete observations with a smoothed estimate. Too little smoothing creates apparent structure from noise; too much erases relevant variation. Check several bandwidths, avoid density extending into impossible values without explanation, and retain observations for small samples. Density height is not the probability at an exact continuous value; probability corresponds to area over a range.

Normalised curves compare shape, not the number of observations. Pair them with group sizes when workload or prevalence matters. A very small group should not appear as equally well established merely because its curve occupies the same area.

### Preserve the tail and the observation unit

Use medians and quantiles for skewed durations when relevant, but show the tail that matters to the user. A service standard such as “resolved within 48 hours” is directly answerable from a cumulative distribution or threshold share. A mean alone cannot establish it.

Do not delete outliers because they disrupt the axis. Investigate whether they are errors, valid rare cases, or a different process. If the main view clips them, show overflow counts or an additional panel and retain their contribution to summaries.

Repeated measurements from one person are not interchangeable with the same number of independent people. Indicate pairing or clustering when it changes interpretation. A box plot's observations can describe variation among people; its whiskers do not automatically describe uncertainty in the median.

## 11. Show time, change, cycles, and cohorts

### Match marks to temporal meaning

Use a line for an ordered sequence where connecting observations helps reveal change. Use columns for amounts accumulated within intervals, such as weekly orders. Use a step line when a state remains in force until a change, such as a tariff. Use interval marks for durations and event marks for discrete occurrences.

Keep real temporal spacing. Irregular observations should not be placed at equal distances unless the axis explicitly represents observation order. Show missing intervals as gaps. A connecting line is an interpolation convention, not evidence that intermediate values were observed.

Do not add a smooth curve only to soften corners. A spline can create apparent peaks, overshoot bounds, or suggest a model. State the interpolation or smoothing method when it matters. For a rolling average, identify window length, alignment, treatment of missing periods, and whether the latest window is incomplete.

### Select the time comparison

| Question | Useful view | Context to retain |
| --- | --- | --- |
| Current workload | Per-period counts or rate | Interval duration, operating days, completeness |
| Long-run movement | Time series with relevant history | Method changes, structural breaks, reference periods |
| Seasonal pattern | Seasonal overlays, cycle plots, calendar heatmap | Comparable calendar alignment and holiday effects |
| Change in growth | Period-on-period or year-on-year change | Baseline values, denominator, overlapping windows |
| Progress since a start | Indexed or elapsed-time series | Start criterion and original levels |
| Differences between groups | Shared-scale small multiples or difference series | Group definitions and aligned periods |
| Event sequence | Timeline or Gantt | Duration, dependency meaning, overlapping events |
| Retention | Cohort matrix or curves | Eligibility, cohort size, elapsed time, observation maturity |

Cumulative series mostly rise and can make stalled recent activity hard to see. Show increments when the question is current momentum. A move from 20% to 30% is an increase of 10 percentage points and a relative increase of 50%. A percentage change from a tiny or zero base needs special treatment; do not present an undefined growth rate as a large number.

For many lines, select a focus and retain quiet context, facet series, or use a heatmap. Give series stable identities across views. An end label needs sufficient space and a clear association; it should not float between two similar endpoints.

### Cohorts and survival

Separate calendar time from time since entry. A retention heatmap commonly uses entry cohort as rows and elapsed periods as columns. Show initial cohort size, define the return event, and distinguish not-yet-observable cells from genuine zero retention. Recent cohorts do not have a full history.

For time-to-event outcomes with censoring, use an analytically appropriate survival display rather than treating all incomplete observations as failures. Label the event, time origin, uncertainty, censoring convention, and numbers remaining at risk where needed. A visually falling curve does not explain why the event happened.

### Specialist temporal forms

A calendar heatmap supports recurring day or week patterns, but missing days and colour thresholds need explicit treatment. A cycle plot separates within-cycle position from change across cycles. A horizon plot folds and layers bands to compress many series; provide an annotated key and retain a conventional selected-series view. Compression trades immediate readability for density.

Candlesticks represent open, high, low, and close over a declared interval. Explain body, wick, interval, and colour direction; the candle does not reveal the full within-period path or volume. An event raster places events along aligned entity timelines and can reveal recurrence; avoid treating row order as a measured quantity unless it is defined that way.

### Forecasts and control displays

Mark the transition from observations to forecast clearly. Identify forecast horizon, update date, scenario assumptions, and uncertainty type. Do not join a model projection seamlessly to observations in a way that makes both look measured.

A run chart shows observations over time. A control chart adds method-derived limits for a defined process. Those limits differ from specification limits or management targets. Obtain the appropriate analytical method, account for changing denominators and process changes, and do not colour every ordinary fluctuation as an exception.

## 12. Show association and model behaviour

### Scatter plots and conditional comparisons

Use one mark per declared item. Label both quantities and units, and indicate any weighting. Look for nonlinear form, clusters, outliers, and unequal variation. Use group distinctions or facets when an overall relationship could conceal different subgroup patterns.

A correlation coefficient compresses a relationship. It can miss curved structure and be driven by a few influential observations. Show the relevant observations or a faithful density view before reporting a general relationship. Correlation, a fitted line, temporal order, and predictive accuracy do not establish causality.

If overlap hides observations, use smaller marks, transparency, jitter, or aggregation. Jitter changes displayed position, so restrict it to the dimension where displacement is harmless and explain it. Transparency can saturate and depends on drawing order; it is not an exact density scale.

Hexbins and two-dimensional bins show counts or summaries within cells. State the statistic, grid resolution, and treatment of empty cells. A cell showing average outcome can have high colour intensity with very few observations; provide sample size or stability information when needed.

### Fit and diagnostics

Distinguish observed points, fitted estimates, and predictions with separate visual roles. Show the range of supporting data, relevant uncertainty, and any extrapolation. A smooth fit should not conceal sparse support.

| Model question | Useful display | Interpretation to protect |
| --- | --- | --- |
| Are predictions accurate? | Predicted versus observed; error distribution | Show equality reference, units, outliers, and held-out evaluation context |
| Where does fit fail? | Residual versus fitted; residual by group or time | Structure in residuals can reveal problems; mean error alone can hide opposing errors |
| Are probabilities reliable? | Calibration plot with bin support | Calibration and discrimination differ; sparse bins need uncertainty |
| What happens at a threshold? | Confusion matrix and threshold-dependent curves | Show counts or declare row/column normalisation; prevalence and error costs matter |
| How do estimates compare? | Coefficient or forest plot | Identify effect scale, reference category, interval, adjustment, and model assumptions |
| Does a distribution fit? | Quantile–quantile plot | Explain the reference distribution and tail departures |
| Which options are efficient? | Tradeoff scatter with Pareto frontier | Explain objectives, constraints, and uncertainty; a frontier is not a recommendation |

Use a log effect scale for ratios when the analytical method calls for it, with the null at 1. For additive effects, the null is commonly 0. Do not imply significance from whether two separate intervals overlap; a comparison needs its own appropriate uncertainty calculation.

Exploring many groups, windows, or relationships increases the opportunity to find an apparently unusual result. Keep exploratory selection distinct from confirmatory analysis, retain a record of examined alternatives, and obtain appropriate analytical treatment before presenting a selected pattern as established.

Feature importance or attribution plots describe a particular model and method. They do not establish that changing a feature causes the outcome to change. State the evaluation population and distinguish global summaries from one-case explanations.

## 13. Show uncertainty and incomplete information

### Identify what varies

Separate variability among observations from uncertainty about an estimate. Standard deviation describes spread; standard error describes an estimate's sampling variability under its assumptions. A prediction interval concerns an individual future outcome; a confidence or credible interval concerns a parameter or defined estimand. These ranges are not interchangeable.

| Source of uncertainty | Useful representation | Required explanation |
| --- | --- | --- |
| Sampling or estimation | Point and interval; interval bands | Interval type, level, method, and target quantity |
| Individual outcome variation | Distribution, quantiles, prediction interval | Population and outcome being described |
| Measurement or rounding | Range, tolerance, appropriate precision | Instrument or recording limits |
| Forecast | Fan chart, ensemble, sampled paths | Forecast origin, horizon, coverage, and dependencies |
| Model choice | Alternative fits or sensitivity panels | Which assumptions vary and which remain fixed |
| Scenario | Separate conditional trajectories | Scenario conditions; no implied probability unless supplied |
| Missing coverage | Coverage panel, missing-state encoding | Who or what is unobserved and why that matters |

Explain a frequentist interval through the procedure's repeated-sampling coverage; do not casually assign a 95% probability to the fixed parameter lying in one realised interval. A credible interval has a conditional probability interpretation under the specified model and prior. Neither usually contains 95% of individual observations.

### Choose a form the audience can read

Point-and-interval plots are compact for comparing estimates. Show the estimate even when the interval is wide; do not encode only “significant/not significant.” When a decision hinges on a threshold, draw that threshold and explain what the uncertainty means for acting.

A density or quantile dot plot can communicate more than endpoints. Define whether dots represent equal probability mass, observed cases, or sampled outcomes. Frequency framing, such as “about 8 in 100,” can help when the denominator is clear and comparable.

Hypothetical outcome plots show samples of possible results. For paths or several related values, sample their joint structure rather than independently jittering points. Provide pause, replay, and a static equivalent; animation must not be the only way to understand uncertainty.

Nested bands need labelled coverage and a consistent visual order. Darker need not mean more certain unless that meaning is explicitly defined. Do not imply that an interval boundary is an absolute limit or that all values inside are equally plausible.

### Show uncertainty that changes the decision

Do not hide uncertainty merely because it weakens a clean story. Also avoid adding a meaningless generic error bar to every observation. Select the uncertainty that affects the user's interpretation and obtain the appropriate method.

For incomplete data, show the observation count, response rate, coverage, or age of data where material. Missingness can be systematic; a chart of recorded cases cannot establish the pattern among unrecorded cases. Mark imputed values or explain their role in the displayed estimate. Do not treat suppression as an ordinary uncertainty interval.

## 14. Use geography when space matters

Use a map when location, distance, adjacency, routes, or regional pattern changes the answer. If the main task is ordering regions by value, a ranked chart may work better. Pair map and ranking when readers need both location and comparison.

### Select the spatial encoding

| Data and task | Starting form | Main risk |
| --- | --- | --- |
| Regional rate or proportion | Choropleth | Large land areas dominate attention regardless of population |
| Counts at places or regions | Proportional symbols | Overlap, placement ambiguity, and area misjudgement |
| Individual locations | Point map | Privacy, overplotting, and geocoding uncertainty |
| Continuous spatial measurement | Raster, contours, or field view | Interpolation appearing as direct observation |
| Relative regional magnitude | Cartogram | Geography is distorted; identification requires support |
| Origin and destination | Flow map or matrix | Crossing lines and misleading implied routes |
| Direction and strength in a field | Arrows, streamlines, sections | Sampling density and arrow length/colour can conflict |
| Spatial distribution of people | Population-aware or equal-area approach | Uniform filling can imply people occupy uninhabited land |

Default to rates or densities for regional choropleths when comparing intensity; use counts when the task and unit justify them, with awareness of area and population effects. A rate based on a small denominator can be unstable. Provide count and denominator or a stability view when that affects interpretation.

### Declare classification and projection

Choose class boundaries to support the question: meaningful policy thresholds, equal intervals, quantiles, or an explained method. Quantiles improve distribution across classes but can exaggerate tiny numerical differences and compress large ones. Natural breaks depend on the dataset and complicate comparisons across time. Use shared boundaries and legends for compared maps.

A bivariate choropleth can encode two regional attributes, but it needs a two-dimensional key, distinguishable combinations, and a task requiring their joint spatial pattern. Prefer paired maps when readers need to retrieve each attribute independently. Do not add a second colour dimension merely to save a panel.

Identify units, period, geography, and missing/suppressed states. Include relevant small regions through insets or an alternative lookup. Quiet the basemap so roads and labels do not overpower the measured pattern. Preserve context that the task needs.

Choose a projection for the region and property that matters. Equal-area projections support area comparisons; conformal projections preserve local angles, not area everywhere. A flat map cannot preserve all geographic properties. For travel distance, use appropriate geographic or network calculations rather than measuring arbitrary screen pixels.

### Avoid spatial overclaiming

An association among regions need not hold among individuals. A regional pattern can change when boundaries or aggregation change. Examine that sensitivity before presenting a cluster as a natural boundary.

A smoothed surface estimates between observations; show measurement support and explain interpolation. A heatmap of recorded activity also reflects where observation was possible. Animated flows do not establish actual routes unless those paths were measured.

For route schematics and transport connectivity, use [Infographics](../aesthetics/infographics.md#11-design-metro-and-route-schematics); a schematic's geometry serves connectivity rather than measured geographic distance.

## 15. Show hierarchies, networks, and flows

### Hierarchies

Use an indented outline or node-link tree for parent–child structure and lookup. Use an icicle for ordered nested intervals or a treemap for hierarchical magnitude. A sunburst can make depth visible but makes label placement and outer-ring area comparisons harder.

Define whether parent values equal the sum of children or represent separate measurements. Preserve sibling ordering when it supports comparison. Show truncated branches, unknown parents, and collapsed nodes explicitly. A hierarchy assumes the declared containment structure; shared parents and cross-links need a different representation or clear duplication.

### Networks

Define a node, edge, direction, weight, and observation period before layout. A link can mean a transaction, a citation, a similarity estimate, or a conceptual association; these are different claims.

Use node-link layouts for paths, neighbourhoods, and sparse structure. Use adjacency matrices for dense connection patterns and pairwise comparison. Matrices avoid line crossings but require deliberate ordering and are less direct for tracing long paths. An ego network can answer a local question without displaying the entire graph.

Force-directed positions usually encode a layout algorithm, not measured physical distance. State this and avoid interpreting empty space as a calibrated separation. Keep node positions stable across compared states where possible. If colour shows detected communities, identify that communities are algorithm-dependent rather than established natural categories.

Provide search, selected-neighbour emphasis, edge filtering, and a legible detail view. If no relevant question can be answered without guessing at a tangled mass, change the representation. Degree, centrality, and visual prominence are distinct; a large hub is not automatically the most influential actor for the user's task.

### Flows and transitions

A Sankey encodes a declared quantity through ribbon width. Define stages, units, direction, and whether the same entities are tracked. Reconcile incoming and outgoing amounts, or show losses, gains, storage, and residuals. Do not normalise each stage independently while letting ribbons imply conserved absolute flow.

An alluvial view often shows category membership across stages or time. Explain whether ribbons track the same cases or are aggregated relationships. Reordering bands can reduce crossings but also change perceived prominence; use a stable rationale.

Use an origin–destination matrix when the task is exact pairwise magnitude or dense flows. A chord diagram can show broad exchange patterns, but ribbon identity and close comparisons are difficult; retain labels and a simpler alternative. Use arrows when direction matters, and explain whether a line follows an actual route or only joins endpoints.

A funnel is appropriate for a defined sequence of eligible stages. State whether conversion is relative to the previous stage or initial cohort. Changing eligibility, repeated entry, skipped stages, and unmatched time windows can invalidate the apparent narrowing. Prefer aligned stage counts and conversion labels when funnel geometry exaggerates loss.

## 16. Handle many variables and dense data

### Reduce complexity without losing the question

Start by separating required simultaneous comparisons from optional detail. Use aggregation for overview, filtering for a declared subset, facets for repeated structure, and coordinated views when different relationships need different encodings. Teach unfamiliar notation rather than assuming that a more advanced chart justifies itself.

| Technique | Useful when | Decision that cannot remain implicit |
| --- | --- | --- |
| Small multiples | The same relationship repeats across groups | Shared domains, category order, panel order, and missing panels |
| Heatmap | A matrix pattern matters more than exact values | What each cell means; colour scale; ordering; missing-state treatment |
| Scatterplot matrix | Pairwise associations among several numeric attributes | Variable selection, redundant half, group identity, and overplotting |
| Parallel coordinates | Users compare multivariate profiles or constraints | Scaling, axis order, direction, brush state, and crossing density |
| Radar chart | A familiar small profile comparison benefits from radial arrangement | Axis order and scales; polygon area is not a valid overall score by default |
| Dimensionality reduction | Many attributes need a provisional overview | Method, preprocessing, parameters, stability, and what geometry preserves |
| Glyphs | Local multivariate shape serves trained repeated use | Decoding cost, interference, legend, and spatial context |
| Focus plus context | Users inspect local detail while retaining an overview | Distortion or changed resolution; location of the focus |

### Heatmaps and ordering

Arrange rows and columns by meaningful sequence, declared value, or a justified clustering. Clustering can reveal structure, but both distance metric and scaling affect it. Show the ordering method where interpretation depends on it. Do not imply time or adjacency when the order was algorithmic.

Use a sequential scale for magnitude and a diverging scale for departures from a meaningful reference. Standardising each row changes the question from absolute levels to relative within-row patterns. Label that transformation; two equally dark cells may then represent very different original values.

### Parallel coordinates, radar, and projection

For parallel coordinates, different axis units can be valid because each axis has its own labelled scale. Normalisation changes apparent slopes and crossings. Keep axis orientation consistent where possible and expose the exact values for selected profiles. A crossing is a relationship between adjacent axes, not necessarily a negative correlation across the dataset.

Radar charts change polygon area when axes are reordered. Do not use filled area as an unexplained composite performance measure. For tradeoffs or exact attribute comparison, aligned dot plots usually provide clearer reading. Retain radar form only when its profile task and audience justify the cost.

Principal component views depend on scaling and linear structure; report explained variance and meaningful loadings. Nonlinear embeddings such as t-SNE can reveal neighbourhood patterns but distort other geometry. Apparent cluster size and distance between separated clusters are not automatically meaningful. Compare runs and parameters, inspect original attributes, and do not treat a pleasing projection as proof of discrete populations.

### Text, codes, and qualitative evidence

Start with the unit: words, documents, speakers, passages, or coded cases. Word frequency can reflect document length, repeated speakers, transcription choices, and stop-word rules. State tokenisation, language handling, weighting, and coverage when these affect comparison. A word cloud is an approximate prominence display; use ranked bars for close frequency comparison and excerpts for meaning in context.

A coded matrix can relate themes to cases, with counts, presence, or carefully defined intensity. Keep those encodings distinct. A missing code does not establish that a theme was absent if it was never asked about. Preserve the coding method and uncertainty, and do not turn a small qualitative sample into a population prevalence claim.

Topic and sentiment outputs are model-derived interpretations. Show representative evidence and important exceptions, not only a coloured score. A projection of document embeddings does not independently establish distinct themes. Protect confidentiality in quotations and linked case details.

### Large datasets and scientific fields

Choose level of detail from the task and display resolution. Rendering a million overlapping points does not mean the reader can see a million observations. Use aggregation, tiled resolution, density, sampling, or progressive disclosure with a visible account of the transformation.

Sampling should preserve the important structure; a uniform sample can omit rare failures. For time series, naïvely keeping every nth point can miss narrow spikes. Use a method that preserves relevant extremes or summarises ranges, and show whether the view contains observations or aggregates.

For vector or tensor fields, volumes, and simulation ensembles, define coordinates, units, resolution, and sampling support. Arrows, contours, streamlines, slices, and isosurfaces reveal different properties. A chosen isosurface threshold can hide important interior variation. Provide sections and alternative thresholds when needed; obtain specialist review for domain interpretation. See [Colour](../aesthetics/colour.md#15-encode-data-with-colour) before applying a continuous colour map to a scientific field.

## 17. Use colour, shape, and texture as a system

### Separate encoding, emphasis, and status

Decide what colour means before choosing colours. It can encode an attribute, highlight a selection, or report a status. Define these as separate roles. If blue means a department in one view, do not make the same blue mean “selected” in a neighbouring view without another clear cue.

Use the [Colour guide's data-encoding section](../aesthetics/colour.md#15-encode-data-with-colour) for palette construction and [its contrast guidance](../aesthetics/colour.md#13-provide-contrast-and-redundant-information) for usable combinations. The selection table below defines the statistical task; the colour guide owns the detailed palette method.

| Data relationship | Palette structure | Interpretation to preserve |
| --- | --- | --- |
| Unordered categories | Distinct qualitative colours with balanced prominence | Hue distinguishes identity without implying rank |
| Ordered magnitude | Sequential lightness progression, optionally with controlled hue change | A larger value follows one readable direction |
| Departures around a meaningful reference | Diverging progression with an explicit centre | Both sign and distance from the reference remain visible |
| Cyclic values | Cyclic palette with matching ends | End and start are neighbours, not extremes |
| One focus among context | Accent plus legible contextual marks | Accent means emphasis, not automatically better or larger |
| Missing or suppressed data | Dedicated state plus label, pattern, or symbol | Missing is not the low end of a measured scale |
| Uncertainty | Explicit additional encoding or separate view | It cannot be confused with magnitude or disabled state |

A diverging scale needs a meaningful midpoint, such as zero change or a target. The mean is not automatically a meaningful neutral point. Symmetric limits suit balanced signed deviations when equal distance should look equal; asymmetric domains need clear labels and a justified mapping.

### Keep colour comparisons fair

Use the same mapping for comparable views, periods, and filtered states. If the domain changes, expose the change and avoid an apparent improvement caused only by rescaling. A locally normalised heatmap supports a different task from one with a shared absolute scale.

Avoid rainbow scales for ordinary ordered magnitude. Their hue and lightness changes can introduce apparent boundaries and unequal emphasis. A cyclic hue sequence can be appropriate for genuinely cyclic measurements, but it still needs testing and an explanation.

Too many category colours force legend lookup. Reduce categories, facet, label directly, or let a user select a focus. Do not make low-priority data illegible to achieve a quiet aesthetic. A colour vision simulation can reveal a problem but does not establish accessible use; combine it with contrast measurement and task testing.

Use status colours only with a meaningful definition and another cue. “Higher” can mean more demand, more success, or more harm. Label status in words or symbols and avoid treating every decrease as negative. Check local conventions without assuming universal psychological effects.

### Shapes, borders, and patterns

Choose a small set of visually distinct silhouettes for category identity. Circles, squares, and triangles can remain distinguishable where several subtly different stars do not. Test at the smallest delivered size, including overlap and line crossings. Use [Iconography](../aesthetics/iconography.md) for construction; do not optically enlarge a quantitative symbol in a way that changes its encoded area.

Open and filled symbols can distinguish observed and estimated values, but they also differ in visual weight. State their meaning and test against the background. A thick outline changes a small symbol's apparent size; keep stroke treatment consistent for size encodings.

Line styles can reinforce series identity, especially in monochrome output. Long and short dashes must survive the exported resolution. Do not make a dashed line mean “forecast” in one panel and an unrelated category in another.

Patterns can mark suppression, uncertainty, or categories in print. Prefer sparse, distinct patterns that remain legible without overwhelming the amount. Avoid moiré, dense hatching, and texture that appears to change value as the viewer zooms. Pattern density should not accidentally create an ordered scale for unordered categories.

### Legends and visual keys

A legend is an explanation of the mapping, not a decoration. State variable, unit, domain, and any transformation. A size legend needs representative sizes with values; a continuous colour bar needs meaningful ticks. Order category keys to match the plot or the domain sequence.

Direct labels can replace a separate legend when their attachment is clear. For unfamiliar encodings, include a small annotated reading example. A key must explain all consequential distinctions, including forecast, missingness, selection, and uncertainty, without making the reader infer them from style.

For theme and print adaptation, follow [Colour](../aesthetics/colour.md#14-adapt-to-appearance-and-environment). Reversing a background does not automatically preserve ordering, contrast, or apparent prominence.

## 18. Compose, label, and explain

### Structure the comparison

Arrange the view around the user's reading sequence: question or finding, evidence, qualification, and relevant next step. Align related plot areas and scales. Put views that need direct comparison close together; separate those with different populations or units enough to prevent accidental comparison.

Use [Composition](../aesthetics/composition.md) for grids, hierarchy, spacing, and density. Measured positions constrain layout: whitespace cannot justify moving a data point, stretching a map region, or changing a bar's extent. Give long labels space rather than shrinking all text.

Allow density when the task needs it and the medium supports it. Small multiples can hold substantial information coherently. Density becomes a problem when marks, labels, or distinctions cannot be read, not simply because the page contains many numbers. Conversely, large empty KPI cards do not make a dashboard simple if users must reconstruct the relationship themselves.

### Supply the necessary words

A self-contained graphic identifies subject, measure, units, population, period, and relevant source. Place these in the title, subtitle, axes, caption, and notes according to the medium. Keep qualifications that change the headline close to that headline.

Use an assertive finding title only when the evidence supports it. “Waiting times rose after June” describes sequence; “The new system caused longer waits” requires causal evidence. A neutral exploratory view can use a question or descriptive title.

Label a ratio's denominator, an index's base, and an interval's definition. Prefer “Incidents per 1,000 eligible residents” to “Incident rate” when eligibility matters. Distinguish percent from percentage points and observed from projected values.

Annotate events, method changes, important exceptions, and practical thresholds. An annotation can identify a coincident event without claiming that it caused the change. Use a leader line or nearby text when attachment would otherwise be ambiguous.

Follow [Typography](../aesthetics/typography.md) for type, numerals, spacing, and actual-size legibility. Use consistent precision within a measure, and round according to evidence and use. “12.347%” is unhelpful if the denominator is 81 or the sampling uncertainty is several percentage points. Preserve more precision in data exports when justified, without implying that all digits are meaningful measurements.

### Build explanation without predetermining discovery

An exploratory product need not reduce a complex subject to one predetermined takeaway. Give readers a structured way to ask further questions, inspect contradictions, and understand which relationships remain unresolved. Choose a guided narrative when explanation is the task, and open exploration when users need to pursue their own questions.

An explanatory sequence can move from overview to a highlighted pattern, then a qualification and implication. Keep scales and identities stable across steps. Show enough context for the reader to assess the claim.

Do not choose the time window, subgroup, or metric solely because it produces the desired story. Check reasonable alternative views before finalising the argument. Distinguish an observation, a possible explanation, and a recommendation. A recommendation can involve values and tradeoffs beyond the data; make that step visible.

In presentations, reveal complexity in a useful order, but make the final slide or takeaway graphic independently interpretable when it will be shared. A narrated explanation does not accompany a screenshot automatically.

## 19. Build dashboards around decisions

A dashboard should answer a related set of recurring questions. Define who uses it, how often, what change prompts action, and where that action occurs. If the page serves incompatible audiences or decision cycles, create distinct views rather than one collection of every metric.

### Build the hierarchy from work

Use an overview to establish current state, a comparison to establish meaning, and detail to investigate exceptions. Place the strongest action-relevant signal where users encounter it early. Avoid equal visual weight for every metric.

A useful metric card carries the value, unit, period, comparison, and freshness needed for use. A delta needs its reference period and direction of desirability. A sparkline needs enough context to interpret its range and period. A green arrow cannot substitute for a defined target.

Show numerator and denominator for unstable rates, and distinguish missing updates from unchanged performance. A value refreshed today can describe events from last month; show both when the distinction matters.

### Make comparisons consistent

Coordinate dates, segments, units, and filters across views. If some panels use different populations or update schedules, label that scope locally. Keep category colours and names stable. Highlight which views a selection affects.

Reference thresholds should come from a target, capacity constraint, historical method, or explicit decision policy. Avoid arbitrary red/amber/green bands and false alarms driven by normal variation. Give an alert a responsible owner and a meaningful investigation path.

Do not equate a single-screen layout with success. A concise monitoring overview may fit one screen; diagnosis can need scrolling, detail, and export. Test whether users can answer the actual questions without hidden filters or repeated mental arithmetic.

### Provide a route from signal to action

Allow a user to identify an exception, inspect relevant detail, understand its definition, and reach the next authorised workflow. A chart does not need to perform the action itself, but the context should survive the handoff.

Review whether the dashboard remains useful. Remove unused measures only after checking whether they are rarely needed but consequential. Archive superseded definitions and explain revisions rather than silently changing historical meaning.

## 20. Design useful interaction and motion

Interaction is justified when users need to choose a subset, compare states, inspect detail, or explore relationships that cannot be presented well at once. It also adds hidden state, accessibility work, and maintenance. Use [Interaction](../aesthetics/interaction.md) for control behaviour and feedback.

### Define the analytical operation

| Operation | Useful outcome | Required feedback |
| --- | --- | --- |
| Filter | Restrict eligible observations | Visible scope, excluded amount where relevant, and reset |
| Highlight | Retain context while emphasising items | Persistent identity and a clear way to clear selection |
| Sort | Compare ordered values or find an item | Current sort key and direction; stable tie handling |
| Brush and link | Examine the same observations across views | Which items and views are linked; selection count |
| Zoom and pan | Inspect local structure | Visible domain and route back to overview |
| Drill down | Move to a finer meaningful grain | Breadcrumb or scope indicator; compatible totals |
| Change measure | Answer another defined question | Updated units, title, legend, and appropriate scale |
| Compare scenarios | Inspect assumptions and consequences | Explicit changed assumptions; observed data kept distinct |

A filter can change a denominator. Decide whether a selected region's percentage refers to that region or the entire population, then label it. A highlight should not silently recompute the dataset. Cross-filtering must distinguish “subset of the total” from “total within the subset.”

### Keep state discoverable and recoverable

Use sensible initial conditions that answer a common question. Expose active filters, chosen time range, selected measure, and any nondefault scale. Provide reset and preserve state in a shareable link or explicit export description when sharing matters.

Do not hide the only definition or essential qualification in a tooltip. Tooltips can supply exact values and secondary metadata. Make equivalent details available through keyboard and touch, and avoid covering the selected point or its comparison. See [Accessibility](../aesthetics/accessibility.md#14-specify-component-behavior) for hover and focus behaviour.

Show loading, empty, missing, error, and stale states distinctly. “No matching records” differs from “The source did not load.” When a request fails, do not leave old values under a new filter label.

### Use motion for continuity, not evidence

Animate when a transition helps users track the same entities or understand a process. Avoid movement that makes stable values look active or creates emotional urgency unsupported by the data. Motion can show a change, but close comparisons often need simultaneous static positions.

For animated time series or maps, retain time labels, controls, pause, and a static summary or small multiples. Do not require users to remember an entire sequence to identify a difference. Use [Motion](../aesthetics/motion.md) and [Accessibility](../aesthetics/accessibility.md#16-control-motion-time-and-interruption) for preferences, timing, and interruption.

## 21. Provide equivalent access

Plan access with the representation. A chart with good colours can still be inaccessible if its meaning exists only in pixels or its interaction requires a mouse. Follow the [Accessibility guide](../aesthetics/accessibility.md), especially [data and complex workspaces](../aesthetics/accessibility.md#18-make-data-and-complex-workspaces-accessible).

### Preserve the question as well as the values

Provide a short identification of the graphic and an accessible explanation or data representation with the information necessary for its purpose. A detailed alternative may need trends, relationships, exceptions, uncertainty, and relevant geometry. A table of all values does not automatically explain an unfamiliar network or spatial pattern.

For a static chart, a useful short description might identify “Weekly backlog by service, January to June; summary and data follow.” The visible summary can state the main pattern and material limitation. The structured table supplies values, units, periods, and missing states. Avoid repeating a long description in several assistive-technology paths.

For an interactive view, preserve the same analytical task through suitable controls, a data view, or an equivalent workflow. Ensure filter state, selected item, and updates are available programmatically. Do not make every point in a huge plot a separate tab stop; design a manageable navigation model.

Sonification can provide another way to inspect temporal or spatial patterns when its mapping is learnable and controllable. It is a complement or task-specific alternative, not an automatic replacement for text and data access. Follow [Sound](../aesthetics/sound.md) for audio behaviour and retain a non-audio route.

### Test perception and operation separately

Use labels, shapes, line styles, or patterns so critical distinctions survive a loss of hue. Meet applicable text contrast and non-text contrast requirements with the scope defined in [Colour](../aesthetics/colour.md#13-provide-contrast-and-redundant-information). Meaningful graphical parts generally need 3:1 against adjacent colours under the applicable criterion; this is not a requirement that every palette swatch contrasts 3:1 with every other swatch.

Inspect actual thin lines and small marks as well as nominal colour values. Test keyboard operation, focus visibility, touch, magnification, reflow, relevant screen-reader reading, and reduced motion. A chart can have an accessible name yet no usable analytical alternative.

Do not depend on instructions such as “see the red area” alone. Identify the category or meaning in words. Keep essential notes legible; accessibility is not achieved by making the main chart attractive and moving qualifications into tiny text.

## 22. Adapt to the medium and viewing conditions

Choose the delivered dimensions and encounter conditions early. A printed page, projected slide, mobile screen, and analytical workstation support different reading distances, density, and interaction.

| Medium | Adaptation | Meaning that must survive |
| --- | --- | --- |
| Small screen | Reflow panels, shorten tick density, use selection or detail views | Population, scale, identity, and essential qualification |
| Large screen | Use coherent panels and overview/detail | Reading order and direct comparison rather than unused space |
| Presentation | Increase readable marks and labels; sequence explanation | Final claim, baseline, and limitations when shared |
| Report or paper | Make figures self-contained and captions precise | Units, methods, uncertainty, and cross-panel references |
| Print | Test monochrome, final size, and paper conditions | Distinctions formerly carried by colour or interaction |
| Screenshot or social image | Include essential context within the captured frame | Subject, measure, date, source, and bounded claim |
| Wall display | Prioritise a few legible monitoring signals | Freshness and actionable status without hover |

Recompose rather than merely shrinking. A wide line chart might become stacked panels; a dense comparison might become a searchable table with a selected series. Do not remove uncertainty or small groups to make a narrow layout fit.

Changing aspect ratio changes the impression of slope. Keep axis labels and context sufficient for interpretation. Preserve semantic order when panels wrap. If a two-dimensional graphic genuinely needs horizontal scrolling, retain orientation and offer another route to the same information.

Use vector formats for appropriate static linework and text where supported; use suitable raster resolution for images and dense fields. Test fonts, clipping, patterns, transparency, and legend placement in the actual export. A correct source canvas does not establish a correct PDF, image, or embedded chart.

## 23. Produce, maintain, and govern

### Separate data from presentation

Maintain a reproducible path from source to displayed values. Keep derived measures, filters, weighting, rounding, and suppression explicit. Prefer a chart specification or repeatable script over manual redrawing for recurring work. Manual refinement can improve presentation, but it must not sever the geometry from its data.

A declarative chart separates data, transformations, marks, encodings, scales, guides, layers, facets, and interactions. Review each independently. A library can infer an aggregation, drop missing values, or assign independent scales without making that choice appropriate. Inspect the rendered output and the effective specification, not just the input table.

Choose tools by task, data size, update cadence, export requirements, access, collaboration, and maintainability. A bespoke visual needs a clear benefit over a supported standard form. Avoid baking transient plugin availability, prices, or API defaults into a long-lived design standard; verify those during implementation.

### Establish a visualisation contract

Record the metric definition, source version, transformation, domains, category ordering, palette roles, missing states, thresholds, update schedule, and accessible equivalent. For a recurring product, make these shared specifications rather than choices each chart author reinvents.

Retain source and retrieval information in the delivered work at a useful level of detail. Keep complete query or calculation lineage in accompanying project records. Provide downloads that match the visible filter state, with definitions and appropriate disclosure controls.

### Protect people and honest interpretation

Evaluate what the display enables a reader to infer about people, especially in small groups or linked views. Suppressed cells can sometimes be reconstructed from totals or repeated filters. Apply the source owner's disclosure rules throughout interactions and exports.

Consider who is absent, whose categories were assigned, and whether a proxy measures the claimed concept. A ranking can reinforce measurement bias; a map can stigmatise an area without explaining coverage or uncertainty. Use respectful labels and retain meaningful subgroup differences where a summary would hide unequal outcomes.

Avoid visual certainty unsupported by evidence, cherry-picked baselines, dramatic perspective, selective truncation, unexplained composite scores, and inaccessible qualification. State when the design involves a value judgement, such as prioritising total burden over rate.

### Maintain after delivery

Assign an owner and update cadence. Distinguish data refresh from definition changes. Show stale data clearly; do not let a successful page load imply that a source refresh succeeded.

Check changes in schema, categories, denominators, and units before reusing an old mapping. New categories need deliberate colours and labels. Revised history may change a finding; retain a revision note and date when that affects previous use. Retire views that no longer support a valid question.

## 24. Evaluate and diagnose

### Check four kinds of correctness

Evaluate the purpose, abstraction, representation, and implementation separately. A fast, attractive interface can still solve the wrong problem. A good representation can still display a wrong aggregation.

| Layer | Question | Appropriate evidence |
| --- | --- | --- |
| Purpose | Does this help the intended person do their actual work? | Observed workflow, representative tasks, user feedback |
| Data and abstraction | Are the measure, unit, population, and comparison appropriate? | Source reconciliation and analytical/domain review |
| Representation and access | Can people decode the intended relationship and its limits? | Task-based reading, alternatives, access checks |
| Implementation and delivery | Are values and mappings correct in every important state? | Recomputed examples, rendered inspection, interaction and export checks |

Before polishing, ask a representative reader to explain what a mark represents, identify the denominator, answer the main question, and state a limitation. Observe errors and hesitation. Asking whether a chart “looks clear” is weaker evidence than seeing whether it supports the intended task.

### Use a practical review sequence

1. Recompute displayed totals, rates, changes, interval endpoints, and selected examples from the approved data.
2. Reconcile the chart's inclusion rules with the population and active filters.
3. Check baselines, scale type, domains, proportional area, and alignment.
4. Check whether smoothing, binning, ordering, or aggregation changes the claimed pattern.
5. Inspect contrary cases, subgroup differences, tails, missingness, and uncertainty.
6. Read title, annotations, and alternatives against the evidence and inference limits.
7. Exercise important states: empty data, one category, negative values, extreme values, long labels, stale data, and changing filters where applicable.
8. Inspect the delivered size, theme, device, print/export, and accessible route.
9. Ask whether the reader can complete the intended interpretation or action; revise from the earliest failed layer.

Use checks appropriate to the actual artifact. A one-off static comparison does not need a software test suite; a repeatedly refreshed product needs repeatable validation of calculations, states, and data changes.

### Diagnose the mechanism

| Observed problem | Likely cause to inspect | First useful repair |
| --- | --- | --- |
| “I understand it, but it does not help” | Wrong question or measure | Return to the decision and required evidence |
| Users compare incompatible groups | Hidden denominators, units, or coverage | Align definitions or separate and qualify views |
| The important difference is hard to see | Poor channel or moving baseline | Use aligned positions or an explicit difference view |
| A minor change looks dramatic | Cropped scale, aspect ratio, or selective window | Restore context or show absolute and relative views |
| It is a colourful puzzle | Too many encodings or weak keys | Reduce channels, label, facet, or teach a reading example |
| A chart shows an implausible pattern | Data or transformation error | Reconcile source rows before changing styling |
| Overall progress hides deterioration | Aggregation or shifting composition | Show meaningful subgroups and their weights |
| The dashboard is tiring | Competing signals, hidden state, or missing comparison | Prioritise questions and make state explicit |
| A screenshot misleads | Context or qualifiers outside the export | Include essentials in the captured view |
| It passes visual inspection but excludes users | Missing semantic or operational equivalent | Test the actual task with assistive and alternative input |

Record material limitations and unresolved questions. Mechanical checks establish those checks, not scientific validity or universal usability.

## 25. Work through complete decisions

The following cases use invented values. Each starts from the user's job and keeps data selection, representation, and interpretation connected.

### Allocate inspection capacity: count and rate answer different questions

**Purpose.** A manager must choose where to add inspection capacity. District A recorded 40 incidents among 10,000 eligible residents; District B recorded 60 among 30,000.

**Choose the evidence.** The incident rates are 4 and 2 per 1,000 residents. B has the larger recorded workload; A has the higher rate. Establish comparable recording, exposure, period, and case severity before interpreting either as priority.

**Choose the view.** Use two aligned panels with the same district order: counts for workload and rates for intensity. Label units independently. Add relevant capacity or severity when it changes the allocation decision. A map adds value only if travel, adjacency, or location affects the work.

**Leave out.** Decorative district silhouettes and unrelated demographic variables. Keep denominators visible because they change the apparent ranking.

**Bound the conclusion.** The counts and rates support different priorities. They do not independently establish cause, preventability, or expected benefit from another inspector.

### Find long waits: a centre alone misses the decision

**Purpose.** A service owner needs to know whether cases meet a 48-hour resolution standard. Eight durations are 8, 10, 12, 12, 14, 16, 50, and 118 hours.

**Choose the evidence.** The median is 13 hours and the mean is 30 hours. Six of eight cases, or 75%, meet the standard. The centre looks comfortable while two cases exceed the limit substantially.

**Choose the view.** For this small sample, use a strip plot with one mark per case and a labelled 48-hour line. Supply the exact values and threshold count in a table. For many cases, use an empirical cumulative distribution with the same threshold and a suitable tail view.

**Leave out.** A smooth violin suggesting a richly measured population from eight cases, or a green median-only card. Keep sample size and time window visible.

**Bound the conclusion.** This describes the eight observed cases. If they exclude unresolved work, the apparent performance can be biased. Include or separately account for unresolved cases using an appropriate analytical definition.

### Explain overall improvement without hiding subgroup deterioration

**Purpose.** A team wants to know whether completion improved within both simple and complex cases.

| Period | Simple completed / eligible | Simple rate | Complex completed / eligible | Complex rate | Overall rate |
| --- | --- | --- | --- | --- | --- |
| Earlier | 9 / 10 | 90% | 40 / 100 | 40% | 49 / 110 = 44.5% |
| Later | 80 / 100 | 80% | 3 / 10 | 30% | 83 / 110 = 75.5% |

**Choose the evidence.** Overall completion increased because the mix shifted towards simple cases. Both subgroup rates fell. An aggregate arrow alone would suggest an improvement that did not occur within either group.

**Choose the view.** Use paired dots for the two subgroup rates, plus a separate composition view or eligible counts explaining the mix. Show the overall rate as an additional summary with its meaning clearly qualified.

**Leave out.** A causal explanation for the decline unless supported by further evidence. Do not omit complex cases because they form a small later subgroup.

**Bound the conclusion.** Changes in composition explain this arithmetic reversal. They do not explain why either group's outcome changed. A standardised comparison would require an agreed reference weighting.

### Monitor conversion without overstating a small group's result

**Purpose.** A product owner needs to compare two channels and decide whether to investigate their conversion performance. Channel A records 20 conversions from 100 eligible visits; B records 3 from 10.

**Choose the evidence.** The displayed rates are 20% and 30%. B has the higher observed rate and much less evidence. A supplies more conversions. Confirm that visits are the intended observation unit and repeated visitors are handled appropriately.

**Choose the view.** Use dots on a common percentage scale with labelled counts and analytically supplied intervals. If the immediate task is workload, add conversion counts separately. To inspect uncertainty in the difference, obtain the appropriate comparison estimate; separate intervals alone do not settle the decision.

**Leave out.** A “B wins” badge, unsupported significance, or a fabricated interval chosen by the designer. Keep eligibility and observation period.

**Bound the conclusion.** The sample rates differ. These observations alone do not establish a stable advantage or the effect of changing channel allocation.

### Understand migration between stages without inventing flow

**Purpose.** An operations team needs to understand where 100 entering cases go. Sixty reach review, 30 are withdrawn, and 10 remain pending. Of the 60 reviewed cases, 45 are approved and 15 rejected.

**Choose the evidence.** Each case belongs to one state at each declared stage. The balances reconcile: `100 = 60 + 30 + 10` and `60 = 45 + 15`. Approval is 75% of reviewed cases and 45% of all entering cases; both statements need their denominators.

**Choose the view.** A Sankey can show volume through review and final outcomes, with pending and withdrawal as explicit branches. For a more direct stage comparison, use aligned labelled counts and conversion ratios. State the cohort entry period and observation cutoff so pending cases are not treated as final failures.

**Leave out.** Loops or flows inferred from separate stage totals if individual transitions were not tracked. Keep pending cases because they account for unresolved mass.

**Bound the conclusion.** The view describes this cohort at the cutoff. It does not predict final approvals among pending cases.

### Design a dense multivariate investigation

**Purpose.** An analyst must identify facilities with unusual energy use after accounting for size and operating pattern.

**Choose the evidence.** Obtain facility-level energy use, floor area, operating hours, observation period, data completeness, and relevant context. Keep total consumption and intensity separate; a single intensity ratio may not represent the relationship adequately.

**Choose the view.** Begin with a scatter plot of energy use against size, then facet or filter by an analytically justified operating category. Link a selected facility to its time series and a table of measurements. A model-adjusted residual view can be added after an appropriate model is established. It should retain original units or explain the residual scale.

**Choose encodings.** Use position for the two primary quantities, a small category palette for operating type, and a labelled selection cue for the current facility. Avoid also encoding every metadata field in size, opacity, and shape. Use [Colour](../aesthetics/colour.md) and [Interaction](../aesthetics/interaction.md) to construct and operate those roles.

**Leave out.** An embedding whose attractive clusters do not answer the energy question, and a single composite “efficiency” score with undisclosed weights. Provide metadata through detail views rather than deleting it.

**Bound the conclusion.** An unusual facility is an investigation candidate. Measurement problems, schedules, weather, or facility purpose may explain it. The chart does not independently establish waste or fault.

## 26. Use the design brief and handoff

Use this brief before implementation. Keep it proportionate to the work: a single comparison may need a few sentences; a recurring analytical product needs a fuller specification.

| Decision | Record |
| --- | --- |
| User and situation | Who uses the result, where, how often, and with what prior knowledge? |
| Purpose | What question, interpretation, decision, or action should the display support? |
| Success | What should a representative user be able to determine correctly? |
| Evidence | Source, population, observation unit, grain, coverage, period, and freshness |
| Measures | Definitions, units, denominator, weighting, transformations, and uncertainty |
| Relationships | Magnitude, difference, distribution, time, association, composition, location, connection, or another declared structure |
| Scope | Included, excluded, aggregated, sampled, suppressed, and accessible detail |
| Comparison | Baseline, target, peer, threshold, or alternative and why it is relevant |
| Representation | Selected form, a plausible alternative, and the reason for the choice |
| Encoding | What each position, length, area, colour, shape, line, and enclosure means |
| Scale | Domain, transform, zero/reference, binning, normalisation, and cross-view resolution |
| Explanation | Title, labels, key, annotation, qualification, source, and permitted claim |
| Access and medium | Delivered dimensions, equivalents, input routes, themes, export, and print |
| Interaction | Initial state, filter semantics, linking, detail, reset, and sharing |
| Production | Reproducible pipeline, update cadence, owner, and failure states |
| Verification | Arithmetic reconciliation, analytical review, reading tasks, rendered inspection, and access checks |
| Limits | Questions the display cannot answer and assumptions still unresolved |

Before handoff, make the intended interpretation and its limits readable without the design conversation. Include the specification, data or retrieval route, relevant definitions, visual and accessible output, and maintenance information appropriate to the project. Keep exploratory findings distinct from approved explanatory claims.

## 27. Use terms consistently

| Term | Meaning in this guide |
| --- | --- |
| Attribute / variable | A property recorded or derived for an observation |
| Baseline | A reference from which position, extent, or change is interpreted |
| Channel | A visual property used to carry information |
| Cohort | A group defined by a shared entry event or condition and followed under a declared rule |
| Denominator | The eligible total or exposure against which a quantity is expressed |
| Dimension | A grouping attribute, geometric axis, or independent measurement; specify which meaning applies |
| Distribution | How observations or probability mass are spread across possible values |
| Domain | Input values mapped by a scale; distinguish it from the subject domain |
| Encoding | A declared mapping from information to visual properties |
| Estimand | The precisely defined quantity an analysis aims to estimate |
| Facet / small multiple | A repeated view for subsets, usually with coordinated structure |
| Grain | The level of detail at which observations or displayed summaries are defined |
| Mark | A point, line, region, or other visible element representing information |
| Normalisation | Rescaling relative to a declared reference, total, range, or distribution |
| Overplotting | Marks overlapping so that observations or distinctions become hidden |
| Range | Output extent of a mapping, or a numerical interval; clarify the context |
| Rate | A quantity relative to exposure, eligible population, or time, as explicitly defined |
| Scale | The mapping between data values and a visual channel |
| Selection | A set of items emphasised or used to control a view; state whether it filters data |
| Uncertainty | Limits in knowledge about a value, estimate, model, or outcome |
| Variability | Differences among observations or outcomes, which may exist even when well measured |
