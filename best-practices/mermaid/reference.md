---
name: "mermaid-best-practices"
description: "Reference for Mermaid diagram conventions, with a required color-coded flowchart standard and syntax examples."
version: "0.1.0"
updated: "2026-10-24"
author:
  - "Josua Mittelstaedt"
references:
  - "Yashodhara Keerthisena"
  - "International Organization for Standardization"
  - "Mermaid"
type: "reference"
status: "draft"
---

# Mermaid Diagrams – Best Practices

This guide defines the house standard for Mermaid diagrams. Use flowcharts by default for process maps: they show steps, choices, and the order in which work proceeds. Use another diagram family when the subject is better described as messages, states, relationships, or measurements.

The examples in this guide show the required visual language and how to express it in Mermaid. The rules apply to diagrams written for technical and nontechnical readers. A diagram should communicate its subject, path, and outcome without requiring its author to narrate it.

## Contents

- [Purpose and scope](#purpose-and-scope)
- [Required flowchart appearance](#required-flowchart-appearance)
- [Mermaid construction rules](#mermaid-construction-rules)
- [Flowchart symbol catalog](#flowchart-symbol-catalog)
- [Choosing and combining symbols](#choosing-and-combining-symbols)
- [Complex flows, connectors, and loops](#complex-flows-connectors-and-loops)
- [Readability and accessibility](#readability-and-accessibility)
- [Diagram-family variations](#diagram-family-variations)
- [Examples](#examples)
- [Final review checklist](#final-review-checklist)

## Purpose and scope

A process flowchart describes how work moves from an entry point through actions and decisions to one or more outcomes. Use a flowchart for straightforward workflows, decision-making, step-by-step instructions, process explanation, and process improvement.

This house style defines the default colors, familiar flowchart shapes, labels, direction, branches, and connectors. Apply these conventions consistently so diagrams are easy to interpret across teams and subject areas.

Mermaid turns text declarations into rendered diagrams. The code has two audiences: the renderer reads node identifiers and syntax, while people read visible labels and follow the layout. Keep both clear. Mermaid 10.9.5 has a core set of flowchart shapes; this guide uses that syntax throughout. When a symbol has no dedicated core shape, use a supported shape with an explicit label rather than relying on newer shape declarations.

## Required flowchart appearance

Use the palette below for default process flowcharts. Each color has one stable role. The values are chosen to match the supplied reference image.

| Element | Fill | Text and outline | Meaning |
| --- | --- | --- | --- |
| Start terminator | Pale green `#DFF7A5` | Deep navy `#002B3D` | Process entry |
| End terminator | Pale coral `#F5C9C5` | Deep navy `#002B3D` | Process completion or stop |
| Decision | Pale lavender `#C9CEF4` | Deep navy `#002B3D` | Question or condition that branches the flow |
| Process / task | Pale yellow `#FFE99A` | Deep navy `#002B3D` | Action, operation, or task |
| Flowline | No fill; line `#002B3D` | Label `#002B3D` | Direction and sequence between steps |
| Canvas | Light cool gray `#EFF4FA` | — | Diagram background when the renderer permits it |

Keep node outlines and flowlines deep navy. Use solid arrowed lines for the main flow. Use a dotted line only for an optional, alternate, exception, or other specially defined relationship, and identify its meaning with a label or legend. Put branch labels on their flowlines. Never rely on color alone to distinguish a symbol's role.

The standard silhouettes are as important as their colors: use a stadium or oval for start and end, a diamond for decisions, and a rectangle for process steps. Color the start and end separately. Other symbols retain their conventional shapes; use role colors on them only when this preserves their meaning.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"background": "#EFF4FA", "primaryTextColor": "#002B3D", "lineColor": "#002B3D", "fontFamily": "Arial, sans-serif"}}}%%
flowchart LR
    start([Start]) --> check{Decision}
    check -->|Yes| action[Process]
    check -->|No| alternate[Process]
    action --> finish([End])
    alternate --> finish

    classDef start fill:#DFF7A5,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef decision fill:#C9CEF4,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef process fill:#FFE99A,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef finish fill:#F5C9C5,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    class start start;
    class check decision;
    class action,alternate process;
    class finish finish;
    linkStyle default stroke:#002B3D,stroke-width:2px,color:#002B3D;
```

`classDef` establishes reusable node styles; `class` assigns a style to one or more node identifiers; `linkStyle default` gives flowlines the standard navy treatment. The initialization directive sets the background and text defaults where supported. If the renderer ignores that directive, the node styles still carry the main role colors, but the background may differ.

## Mermaid construction rules

### Declare direction

Declare a reading direction at the beginning of each flowchart:

- `LR`: left to right; use for short, linear processes and the default image's orientation.
- `TB` or `TD`: top to bottom; use when a process has several stages or branches.
- `RL` or `BT`: right to left or bottom to top; use only when the process or surrounding page gives a clear reason.

Keep the primary sequence moving in one direction. Use a return arrow only when the work genuinely repeats or returns for rework.

### Separate identifiers from labels

Use short, stable identifiers for code, such as `start`, `validate_order`, and `payment_decision`. Give each node a visible label written for the reader. The identifier need not be visible in the diagram.

Quote labels that contain punctuation, reserved words, or text Mermaid could interpret as syntax. Avoid the all-lowercase visible label `end`, which can conflict with flowchart syntax; write `End`, `END`, or a specific phrase such as `Order complete`.

### Write useful labels

Use concise labels that state an action, question, data item, or outcome. Begin process labels with action verbs and keep the grammatical form consistent (`Review request`, `Send receipt`). Write decisions as clear questions or conditions. State outcomes on the outgoing flowlines (`Yes`, `No`, `Approved`, `Needs revision`).

Break compound actions into separate steps when the reader needs to understand their order. A label should explain the step without becoming a paragraph inside the shape.

### Use flowlines consistently

Use arrow-headed flowlines to communicate sequence and direction. In Mermaid, `A --> B` is a solid directed edge and `A -.-> B` is a dotted directed edge. A line without an arrowhead does not establish process direction and should not represent a process transition.

Keep routes orderly and avoid crossing lines. If a chart is becoming hard to follow, simplify its scope, use connectors, or split detailed work into a separate process map.

## Flowchart symbol catalog

Use the symbol whose meaning matches the operation. The first four symbols below form a practical baseline. Advanced symbols add detail only when the distinction matters to the reader.

| Symbol | Meaning | Mermaid representation | Use and limits |
| --- | --- | --- | --- |
| **Terminator** | Beginning or end of a process; usually an oval or stadium shape. | `A([Start])`, `Z([End])` | Place entry near the beginning of the reading direction and completion near its end. State what begins or concludes when the context is not obvious. Keep start green and end coral. Avoid extra endpoints unless the real process has distinct entries or exits. |
| **Flowline / arrow** | Direction and order of work from one step to another. | `A --> B`; labeled branch: `A -->|Yes| B` | Keep the main direction consistent. Avoid crossings and clutter. A dotted arrow may identify an optional or alternate route, but define its meaning. |
| **Process / action** | A work step, operation, action, or task. | `A[Review request]` | Use a rectangle and an action label. Include enough detail to identify the work; split a crowded or compound action into smaller steps. Do not omit necessary work. |
| **Decision** | A condition that chooses which route to follow, often yes/no or true/false. | `A{Is the request complete?}` | Use a diamond containing a precise question. Label every outgoing branch. Each answer should lead to a distinct, logical next step or a valid endpoint. Avoid vague results, accidental dead ends, and too many outcomes in one decision; chain decisions when appropriate. |
| **Input / output** | Data received by a process or produced by it. | Parallelogram: `A[/Enter customer details/]` | Name the data. Represent input and output in separate shapes when both occur; combining them can hide the direction of information. Include inputs and outputs needed to understand the process. |
| **Predefined process / subroutine** | A reusable or separately detailed process invoked from the current flow. | `A[[Verify identity]]` | Name the subprocess and provide a clear path to its detail. Use it when the work merits its own breakdown. Without a reference, the node hides important logic; overuse makes the whole process opaque. |
| **Document** | A physical or digital document used in a process. | `A[Document: Signed agreement]` | Name the document and state the relevant action, such as review, signature, filing, or delivery. Connect it to the flow so its role and movement are clear. This labeled rectangle is an approximation. |
| **Multiple documents** | A packet or group of documents or files. | `A[Document set: Application packet]` | Use when the group matters as a unit. Identify its contents or purpose where needed. This labeled rectangle is an approximation. |
| **Manual input** | Data entered by a person instead of being captured automatically. | `A[/Manual input: Enter payment details/]` | Identify the required information. Do not label automated collection as manual input. Repeated manual input may indicate avoidable effort or a bottleneck. The visible label supplies the manual meaning. |
| **Manual operation** | A task performed by a person or through physical effort. | `A[/Inspect package manually\]` | Describe the human action and place it at the point where it happens. Avoid using it for automated tasks. An underspecified manual step can cause delays or errors. |
| **Preparation** | Setup or initialization that prepares for later steps. | `A{{Initialize session}}` | Place it immediately before the work it enables. State what is prepared and why; an unexplained setup label leaves the effect unclear. |
| **Display** | Information presented to a person, such as a screen result or report. | `A[Display: Show confirmation]` | Describe what appears. A generic label such as `Display` does not identify the information. The labeled rectangle is an approximation. |
| **Delay** | An intentional wait before the next process step. | `A[Delay: Wait up to 24 hours]` | Include duration when known and explain the cause or condition. Use only when the pause affects the process or timeline; routine gaps do not need a delay shape. The labeled rectangle is an approximation. |
| **Database** | Structured data storage from which information is retrieved or to which it is written; often cylindrical. | `A[(Customer database)]` | Name the stored information and show the related interaction. Do not use an unlabeled cylinder for every data step. |
| **Stored data / storage** | Saved information such as files, archives, or records. | `A[Stored data: Archived records]` | Say what is stored, retrieved, or updated. Group similar storage interactions when separate nodes add no clarity. The labeled rectangle is an approximation. |
| **Direct-access storage** | Information on a medium that can be accessed directly, such as a disk. | `A[Direct-access storage: Customer records]` | Name the medium or information. Do not imply direct access when retrieval actually depends on reading a sequence. The labeled rectangle is an approximation. |
| **Internal storage** | A specific internal data-storage type, commonly used in programming diagrams. | `A[Internal storage: Session state]` | Name the storage role. The label must explain what is stored because Mermaid 10.9.5 has no dedicated core shape for it. |
| **Sequential-access storage** | Information stored in an order that must be read sequentially, such as magnetic tape. | Use a named storage node; a paper-tape symbol is not automatically equivalent. | State that access is sequential and identify the medium when relevant. Show the data movement. |
| **On-page connector** | A same-diagram jump that links separated flow segments without a long crossing line. | Matching circles: `A((C1))` … `B((C1))` | Use the same unique identifier at both points. Place connectors where they reduce clutter. Too many or mismatched connectors make the flow harder to trace. |
| **Off-page connector / reference** | A continuation in another diagram or on another page, often drawn as a pentagon. | Use a named reference node, e.g. `A[Continue: Fulfillment diagram]`. | Include the destination identifier and break at a natural process boundary. A reference without a correct destination is misleading. A single Mermaid flowchart does not paginate itself. |
| **OR symbol** | A choice among multiple possible routes where one route is selected; commonly depicted as an ellipse with a vertical cross. | Use a labeled decision diamond to approximate it; name the alternatives explicitly. | Make alternatives distinct and understandable. Use the decision diamond for ordinary questions; reserve a special OR symbol for a process where that specific choice meaning matters. |
| **Merge symbol** | An upside-down triangle where multiple branches converge into one subsequent flow. | Connect all incoming edges to one shared next node. | Merge only paths that can logically continue together. Label branches when their origins are unclear. Too many unrelated inputs obscure the process. A visible triangle is not required when shared convergence is already clear. |
| **Summation junction** | A circle marked with a cross where several paths converge, reducing the need to follow parallel lines. | `A((Join))` as a labeled circle approximation. | Identify incoming routes and use the shape consistently. Do not combine incompatible paths. Use a normal shared next step when it communicates the convergence more clearly. |
| **Annotation** | Explanatory information that does not alter the process path. | `note[Note: Only for verified requests]` with a dotted association from the relevant step. A `%%` comment is hidden from readers. | Keep a visible note separate from operational steps and make its relationship to the relevant node clear. Code comments do not replace reader-facing notes. |

Some specialized symbols have no dedicated shape in Mermaid 10.9.5. A labeled node or converging-edge pattern can be a useful approximation, but the label must preserve the intended meaning. Do not use a similar-looking shape if it represents a different operation. If a distinction is essential and Mermaid cannot express it clearly, choose a diagram type or authoring method that can.

## Choosing and combining symbols

Select a symbol by asking what the step does:

1. Is it where the process begins or ends? Use a terminator.
2. Is work performed? Use a process rectangle.
3. Does a condition route the flow? Use a decision diamond and label every result.
4. Does data enter or leave? Use an input/output parallelogram.
5. Does a special distinction help the reader? Add a document, manual operation, subprocess, delay, or storage symbol only when needed.

Simple processes usually need only terminators, processes, decisions, and flowlines. Add advanced symbols as the detail requires. Use a consistent shape for each role and keep spacing and alignment steady. When the chart becomes too complicated, reduce its scope, remove unnecessary decisions, group similar data interactions, or split it into smaller related diagrams.

### Combining branches

Label each decision route at its point of departure. Keep the route labels short and mutually clear. If two routes later rejoin, direct both arrows to the same next step when their distinction no longer matters. Add a visible merge or junction only when the convergence itself needs to be emphasized.

## Complex flows, connectors, and loops

Use a decision and a return flowline to show repetition. One branch returns to the step that repeats; the other leaves the loop. Label both the continue condition and the exit condition. For nested loops, use a separate decision for each loop and label each condition so the reader can tell which iteration it controls. Add spacing or connectors to keep return paths distinct.

Use matching on-page connectors where a direct line would cross other routes or stretch across the diagram. For work that continues in another diagram, use a named off-page reference and keep the destination label identical at both ends. Put the transition at a natural boundary, not at an arbitrary point.

Use a predefined process when a step contains enough work to deserve a separate detailed flowchart. Give the subprocess a clear name and an explicit reference. Do not use a subprocess symbol to conceal a step that readers need in order to follow the current diagram.

When a process includes an exception or optional path, keep the main sequence solid and visually primary. A dotted line may distinguish the alternative, but add a legend or direct label to define it. Dotted lines can indicate different things in different diagrams, so never leave their meaning to guesswork.

```mermaid
flowchart TB
    begin([Start review]) --> inspect[Inspect item]
    inspect --> retry{More items to review?}
    retry -->|Yes| inspect
    retry -->|No| done([Review complete])

    classDef start fill:#DFF7A5,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef decision fill:#C9CEF4,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef process fill:#FFE99A,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef finish fill:#F5C9C5,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    class begin start;
    class retry decision;
    class inspect process;
    class done finish;
    linkStyle default stroke:#002B3D,stroke-width:2px,color:#002B3D;
```

## Readability and accessibility

Before sharing a diagram, trace every route from each entry through its decisions to a valid next step or end. Confirm that the order is correct, the flowlines point in the intended direction, and every branch is explicit.

Avoid common flowchart problems:

- **Overloaded symbols:** shorten labels or split compound work into ordered steps.
- **Missing steps:** include all actions and information needed to understand or perform the process.
- **Unclear endpoints:** name the entry and outcome; explain multiple endpoints when the real process requires them.
- **Weak decisions:** write a precise condition and label all possible results.
- **Inconsistent formatting:** maintain one direction, one symbol meaning per shape, and consistent spacing and style.
- **Crossed or excessive lines:** reroute the process, use connectors, or divide it into smaller diagrams.
- **Unexplained custom shapes:** use familiar shapes by default and explain any special symbol in a legend.
- **Excessive decision points:** simplify the scope or separate a large process into focused views.
- **Unclear data handling:** name data stored or retrieved and show its direction to or from storage.

Keep text concise and large enough to read at the intended display size. Use strong text/background contrast. Color reinforces the shape and label; it never carries meaning by itself. Walk through the rendered diagram at normal viewing size to check that paths, labels, and symbols remain clear.

## Diagram-family variations

Flowcharts are the default for ordinary process maps. Other diagram families have different jobs and visual grammars. Choose the family that best expresses the relationship being explained.

| Diagram family | Use it to represent | Preserve this family’s conventions |
| --- | --- | --- |
| Flowchart | Process actions, decisions, and sequence | This guide's shapes, color roles, direction, and labeled flowlines |
| State diagram | States and transitions in a system or lifecycle | Name states and show the events or conditions that cause transitions |
| Sequence diagram | Messages exchanged between participants over time | Identify participants and show messages in chronological order |
| Class diagram | Classes, attributes, operations, and software relationships | Use class and relationship notation; do not turn classes into process steps |
| Entity relationship diagram | Data entities and their relationships | Name entities and make relationship cardinality clear |
| Gantt chart or timeline | Tasks and events positioned in time | Show dates, durations, ordering, and dependencies as appropriate |
| Quantitative chart | Measured or counted data | Label measures and units; use a chart form suited to the data |
| UML model | Software structure, object behavior, and system design | Use the relevant UML diagram type when its defined relationships are needed |
| BPMN process model | Complex business processes, events, gateways, and automation | Use BPMN when detailed business rules and process orchestration matter |

Do not carry flowchart colors or shapes into another family when they conflict with that family's meaning. Styling may be adapted where it improves legibility, but the diagram's notation must remain accurate. The main process-modeling options differ in purpose and complexity:

| Aspect | Flowchart | UML | BPMN |
| --- | --- | --- | --- |
| Purpose | Visualize straightforward processes and workflows | Model software structure, object behavior, and relationships | Model detailed business processes and workflow orchestration |
| Common elements | Start/end, process, decision, arrows | Classes, objects, use cases, activities | Events, tasks, gateways, sequence flows |
| Typical use | Step-by-step procedures, decisions, quick mapping, and brainstorming | Software engineering, application development, and system design | Business-process automation, rule-heavy workflows, and enterprise optimization |
| Complexity | Simple to moderate | Moderate to high | High |

Choose the simplest family that can express the subject faithfully. A basic flowchart is easier to scan for a straightforward process; use a richer model when the subject depends on relationships or rules that a flowchart would hide.

### Common use cases

| Area | Typical flowchart content |
| --- | --- |
| Manufacturing | Production stages such as assembly, inspection, and packaging; quality decisions for approval or rework; handoffs between procurement, production, and logistics. |
| Healthcare | Patient admission, records and test results, diagnosis decisions, emergency response, and treatment paths. |
| Software development | Function execution, system operations, conditional logic, debugging paths, and reusable subprocesses. |
| Business and finance | Sales, customer support, financial approvals, payroll subprocesses, transaction storage, and loan or invoice decisions. |

These are examples of how the same basic symbol system applies in different fields. Domain-specific shapes may be added when they have a clear meaning and are explained for the intended audience.

## Examples

### Canonical request flow

```mermaid
%%{init: {"theme": "base", "themeVariables": {"background": "#EFF4FA", "primaryTextColor": "#002B3D", "lineColor": "#002B3D"}}}%%
flowchart LR
    start([Request received]) --> complete{Complete?}
    complete -->|Yes| process[Process request]
    complete -->|No| ask[Request missing details]
    ask --> process
    process --> finish([Request completed])

    classDef start fill:#DFF7A5,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef decision fill:#C9CEF4,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef process fill:#FFE99A,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef finish fill:#F5C9C5,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    class start start;
    class complete decision;
    class process,ask process;
    class finish finish;
    linkStyle default stroke:#002B3D,stroke-width:2px,color:#002B3D;
```

This example has one entry and one completion point, an action-led process label, a question in the decision, explicit outcomes, and a left-to-right sequence. The missing-details route returns to processing only after those details are obtained; when that work is part of the process being documented, show it as a separate step.

### Data input, storage, and output

```mermaid
flowchart TB
    start([Start]) --> input[/Enter customer information/]
    input --> validate{Information valid?}
    validate -->|Yes| save[Save customer record]
    save --> database[(Customer database)]
    database --> output[/Display confirmation/]
    output --> finish([End])
    validate -->|No| correct[Correct missing fields]
    correct --> input

    classDef start fill:#DFF7A5,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef decision fill:#C9CEF4,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef process fill:#FFE99A,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef finish fill:#F5C9C5,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    class start start;
    class validate decision;
    class save,correct process;
    class finish finish;
    linkStyle default stroke:#002B3D,stroke-width:2px,color:#002B3D;
```

This example distinguishes user input, validation, process work, data storage, and displayed output. The invalid-data path returns to an explicit correction step. If the stored information or retrieval direction matters, label that interaction as well.

### Optional exception path

```mermaid
flowchart LR
    start([Start]) --> main[Main process]
    main -.-> exception[Optional exception review]
    main --> finish([End])
    exception --> finish

    classDef start fill:#DFF7A5,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef process fill:#FFE99A,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef finish fill:#F5C9C5,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    class start start;
    class main,exception process;
    class finish finish;
    linkStyle default stroke:#002B3D,stroke-width:2px,color:#002B3D;
```

In a rendered diagram, add a legend stating that the dotted arrow marks an optional exception path. Apply that meaning consistently to every dotted path in the same diagram.

### Advanced symbol examples

The following example uses only core Mermaid 10.9.5 flowchart syntax. Where that version has no dedicated shape for a symbol, the visible label states the symbol's role.

```mermaid
flowchart LR
    start([Start payment]) --> input[/Manual input: Enter payment details/]
    input --> prepare{{Prepare payment}}
    prepare --> verify[[Verify account]]
    verify --> document[Document: Payment receipt]
    document --> wait[Delay: Wait for settlement]
    wait --> display[Display: Show payment status]
    display --> finish([Payment complete])

    classDef start fill:#DFF7A5,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef process fill:#FFE99A,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    classDef finish fill:#F5C9C5,stroke:#002B3D,color:#002B3D,stroke-width:2px;
    class start start;
    class prepare,verify,document,wait,display process;
    class finish finish;
    linkStyle default stroke:#002B3D,stroke-width:2px,color:#002B3D;
```

The parallelogram shows input, the hexagon preparation, and the double-sided rectangle a reusable subprocess. Document, delay, and display are labeled rectangle approximations because Mermaid 10.9.5 has no dedicated core shapes for those roles.

## Final review checklist

Before sharing a Mermaid diagram, confirm each item that applies:

- The diagram family matches the question being explained.
- A process flowchart declares one clear reading direction.
- Start, decision, process, and end use the required shapes and colors.
- Every node has a concise, reader-facing label and a distinct code identifier.
- Each decision is a clear condition, and every outgoing branch is labeled.
- Flowlines show direction, avoid unnecessary crossings, and have a defined meaning.
- Optional, alternate, or exception paths are identified in labels or a legend.
- Inputs, outputs, documents, subprocesses, delays, and storage are named precisely when used.
- Connectors match and point to a valid destination.
- Every path leads to a valid next step or endpoint; loops return to the right step and have a clear exit.
- The diagram contains all information needed to follow the process without narration.
- Text is readable at display size, colors have sufficient contrast, and no meaning depends on color alone.
- Every shape uses Mermaid 10.9.5 syntax; any unsupported symbol is represented by a clearly labeled approximation.
