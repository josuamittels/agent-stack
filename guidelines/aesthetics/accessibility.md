---
name: accessibility-best-practices
description: "Comprehensive accessibility reference for inclusive product decisions, EU legal scoping, WCAG requirements, visual and interaction design, content, implementation, assistive technology, design systems, evaluation, and ongoing operations."
version: "0.1.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "World Wide Web Consortium"
  - "European Parliament and Council of the European Union"
  - "European Commission"
  - "European Telecommunications Standards Institute"
  - "European Committee for Standardization"
  - "European Committee for Electrotechnical Standardization"
  - "United Nations"
  - "Apple"
  - "Google"
  - "Government Digital Service"
  - "Harvard University Information Technology"
  - "The A11Y Collective"
  - "Figma"
  - "Emily Stevens"
  - "Soumitra Mishra"
type: reference
status: experimental
---

# Accessibility – Best Practices

Accessibility lets people with disabilities perceive information, understand choices, operate controls, and complete tasks with the independence and privacy available to other people. It belongs to the whole service: its interface, content, technology, documents, communications, support, and connected providers.

Use this reference when planning, designing, building, buying, reviewing, or maintaining digital products. It is written for designers, engineers, content authors, researchers, testers, and accountable product owners. Web applications provide the main implementation examples. Native software, documents, media, terminals, and spatial experiences need their own platform checks as described below.

The default product target is **WCAG 2.2 Level AA, plus the stronger product conventions in this guide**. That target does not by itself establish legal compliance or meet every person's needs. Apply the actual legal and contractual requirements to the product and jurisdiction. The legal and standards snapshot in this document was checked on **27 October 2026**; recheck it before a compliance decision.

## Contents

1. [Understand the purpose and boundaries](#1-understand-the-purpose-and-boundaries)
2. [Design around functional needs](#2-design-around-functional-needs)
3. [Choose standards and conformance targets](#3-choose-standards-and-conformance-targets)
4. [Scope European legal obligations](#4-scope-european-legal-obligations)
5. [Write an accessibility brief](#5-write-an-accessibility-brief)
6. [Create readable visual systems](#6-create-readable-visual-systems)
7. [Preserve scaling, reflow, and user preferences](#7-preserve-scaling-reflow-and-user-preferences)
8. [Make structure and meaning programmatic](#8-make-structure-and-meaning-programmatic)
9. [Support keyboard, focus, and alternative input](#9-support-keyboard-focus-and-alternative-input)
10. [Make navigation predictable](#10-make-navigation-predictable)
11. [Build forms that support completion](#11-build-forms-that-support-completion)
12. [Make authentication and transactions accessible](#12-make-authentication-and-transactions-accessible)
13. [Handle dynamic content and application state](#13-handle-dynamic-content-and-application-state)
14. [Specify component behavior](#14-specify-component-behavior)
15. [Support cognition, language, and emotional safety](#15-support-cognition-language-and-emotional-safety)
16. [Control motion, time, and interruption](#16-control-motion-time-and-interruption)
17. [Provide image, audio, and video equivalents](#17-provide-image-audio-and-video-equivalents)
18. [Make data and complex workspaces accessible](#18-make-data-and-complex-workspaces-accessible)
19. [Deliver accessible documents and communications](#19-deliver-accessible-documents-and-communications)
20. [Apply the principles across platforms](#20-apply-the-principles-across-platforms)
21. [Encode accessibility in the design system](#21-encode-accessibility-in-the-design-system)
22. [Evaluate with complementary methods](#22-evaluate-with-complementary-methods)
23. [Resolve defects and verify repairs](#23-resolve-defects-and-verify-repairs)
24. [Assign ownership and sustain access](#24-assign-ownership-and-sustain-access)
25. [Work through a complete service example](#25-work-through-a-complete-service-example)
26. [Use the WCAG 2.2 A/AA coverage index](#26-use-the-wcag-22-aaa-coverage-index)
27. [Check delivery readiness](#27-check-delivery-readiness)

For a new product, start with sections 1–5 and the critical journeys. For a component, use sections 8–14 and 21. For an existing product, establish the scope in section 22, then remediate through section 23. The coverage index is a lookup aid, not a replacement for the full criteria and their definitions.

## 1. Understand the purpose and boundaries

### Begin with equal participation

An inaccessible service can prevent someone from obtaining work, education, healthcare, public information, money, transport, or ordinary social participation. A barrier may also force a person to reveal private information to someone helping them. Being able to complete a task personally matters even when someone else could do it on their behalf.

Treat accessibility as a product quality and civil-rights concern. Its value does not depend on demonstrating a conversion increase. Commercial reasons still matter: accessible products can serve more people, satisfy procurement requirements, reduce avoidable support and rework, and remain usable across more devices and settings. Measure those effects where useful; do not promise a universal financial return.

Designing a labeled, keyboard-operable control often helps people using touch, voice, switches, or automation. Captions help deaf people and can also help someone in a noisy room. These wider benefits strengthen the work without displacing disabled people as its central users.

### Distinguish related concepts

| Concept | What it asks | Consequence for a team |
| --- | --- | --- |
| Accessibility | Can people with disabilities access and use this content and functionality? | Identify barriers, meet applicable requirements, and verify supported ways to complete tasks. |
| Usability | Can the intended users achieve their goals effectively, efficiently, and satisfactorily in context? | Evaluate comprehension, effort, errors, and task success. Accessible products can still be hard to use. |
| Inclusive design | Whose experiences and constraints shape the decisions, and who is excluded? | Include diverse people in research and decision-making; examine exclusion beyond disability alone. |
| Universal design | How broadly can the same design serve people without specialized adaptation? | Build flexible defaults; recognize where personal settings and alternatives remain necessary. |
| Accommodation | What adjustment does this person need in this situation? | Provide an effective individual route when needed, while continuing to repair systemic barriers. |
| Conformance | Does a defined artifact meet a specified standard and level under stated conditions? | Keep scope, version, evidence, exceptions, and claims precise. |

A compliant component can become inaccessible through poor composition, missing content, or a broken provider. A usable prototype can still lack the semantics needed in production. Examine both the measurable requirements and the actual experience.

### Keep aesthetics accountable to function

An accessible product can be distinctive, expressive, dense, quiet, or playful. Preserve the design's character through composition, imagery, language, shape, and meaningful motion. Essential text, state, focus, and controls need dependable treatment in every direction.

When a brand color cannot support a text role, change the role or the pairing. Use a darker functional shade and retain the original color in decoration. When a cinematic effect causes discomfort or hides content, provide a stable presentation with the same information and actions. An accommodation should preserve the task, rather than remove the feature's useful capability.

## 2. Design around functional needs

### Understand disability in context

Barriers arise through the interaction of a person's abilities, the task, the environment, and the design. A diagnosis does not predict a single interaction pattern. People may have several disabilities, use several technologies, or change methods during one task. Some needs are permanent, some temporary, some fluctuating. Fatigue, pain, medication, stress, glare, noise, and unreliable connectivity can change an experience.

Do not use temporary or situational examples to imply that living with a disability is equivalent to a brief inconvenience. Do use them to identify fragile assumptions in a design.

| Functional need | Common barriers | Design responses and useful checks |
| --- | --- | --- |
| Access without vision | Unlabeled controls, visual-only state, meaningless reading order, inaccessible diagrams | Semantic structure, text alternatives, meaningful names, announced state; test screen readers and relevant braille workflows. |
| Access with low vision | Faint text, clipped enlargement, scattered controls, overlays covering magnified content | Robust contrast, reflow, scalable text, proximity, visible focus; test zoom and magnification. |
| Access without reliable color discrimination | Status or series encoded only by hue | Text, shape, pattern, line style, and explicit state in addition to color. |
| Access without hearing | Uncaptioned speech, audio-only alerts or support | Accurate captions, transcripts, visible alerts, text contact options; include relevant non-speech sounds. |
| Access with combined hearing and vision loss | Audio descriptions alone, fast announcements, text inaccessible to braille | Structured persistent text, flexible pacing and compatible output; investigate the person's actual equipment. |
| Access with limited dexterity, strength, reach, or movement | Tiny controls, dragging, long gestures, repeated activation, inaccessible keyboard paths | Generous hit areas, alternatives, keyboard/switch support, cancellation, efficient navigation and rest. |
| Access without speech | Voice-only interaction, mandatory phone calls, speech-based identity verification | Keyboard/text routes and equivalent support or verification alternatives. |
| Access with memory, language, learning, attention, or executive-function differences | Hidden rules, ambiguous labels, complex recovery, timed tasks, dense instructions | Familiar patterns, explicit steps, persistent instructions, reuse of information, save/resume and clear feedback. |
| Access with vestibular or sensory sensitivities | Parallax, moving backgrounds, flashing, unexpected sound, excessive stimulation | Stable alternatives, motion preferences, user-controlled media and predictable transitions. |
| Access with pain, fatigue, or fluctuating energy | Repeated data entry, long sessions, needless navigation, forced restarts | Shorter necessary paths, preserved progress, flexible timing and multiple input methods. |

These rows overlap. A high-contrast presentation may help one reader while causing discomfort for another. Use sufficient default contrast and support user-selected presentation rather than choosing an unreadable compromise.

### Understand the technology chain

Assistive technology includes screen readers, refreshable braille displays, magnifiers, alternative keyboards, switches, eye-gaze systems, speech input, hearing technologies, and reading or communication aids. Built-in browser and operating-system features also provide access: zoom, text size, forced colors, captions, reduced motion, sticky keys, and keyboard navigation.

A screen reader uses the platform's accessibility information, not merely the visible pixels. It may let the user navigate by headings, links, controls, landmarks, or tables; speech and braille can expose different practical issues. A switch user may rely on sequential scanning. Voice users often refer to visible control labels. A magnifier user sees a small region and may miss a message far from the active control.

Support the chain from authored content through browser or native toolkit, accessibility API, assistive technology, and user. Test representative combinations and document limitations. No single browser, simulator, screen reader, or input device represents the whole chain.

## 3. Choose standards and conformance targets

### Establish the baseline explicitly

Use WCAG 2.2 AA for new web work unless a stronger legal or contractual target applies. Level AA requires every applicable Level A and Level AA success criterion. It is not an average score. A criterion that does not apply needs a defensible reason, such as no prerecorded video in the evaluated scope.

Select useful AAA improvements where they serve the audience, such as stronger focus indicators, larger targets, reduced interaction animation, or enhanced contrast. Do not claim whole-product AAA because those improvements exist. Some AAA requirements cannot be met for all kinds of content.

| Instrument | Role | How to use it |
| --- | --- | --- |
| WCAG success criteria and conformance requirements | Normative web accessibility requirements | Specify version, level, scope, and supported technologies. Apply the actual wording and definitions for edge cases. |
| Understanding documents and techniques | Explanations, examples and ways to meet requirements | Use to interpret intent and check exceptions. A listed technique is not the only permitted implementation. |
| WAI-ARIA | Semantics for roles, states, properties and relationships | Use where native semantics are insufficient; implement the associated behavior. |
| ARIA Authoring Practices Guide (APG) | Informative interaction patterns | Choose an appropriate pattern, adapt carefully and test the result. Examples do not certify production support. |
| Cognitive accessibility guidance | Needs and patterns beyond the conformance baseline | Add task simplification, recovery, reminders and personalization where relevant. |
| EN 301 549 | Accessibility requirements for ICT products and services | Select the applicable edition, clauses and legislative mapping; include software, documents, support or hardware as relevant. |
| ATAG | Accessibility of authoring tools and their support for accessible output | Apply when building editors, CMS tools, document generators and publishing systems. |
| Platform accessibility guidance | Native conventions, APIs and accommodations | Apply the host platform's semantics, settings, controls and testing tools. |

Authoring Tool Accessibility Guidelines (ATAG) address the editing interface and the output it helps authors produce.

WCAG 3 remains an evolving Working Draft in this document's October 2026 snapshot. It does not replace the WCAG 2 target for production conformance decisions. APCA or another supplementary contrast model may inform design research; use the WCAG 2 contrast method for a WCAG 2 claim.

### Use the four principles as diagnostic questions

The four organizing principles are often abbreviated **POUR**. Use them to discover barriers and explain the reason for a requirement. They do not replace criterion-level evaluation.

| Principle | Question | Design consequence |
| --- | --- | --- |
| Perceivable | Can the person obtain the information through an available sense and representation? | Offer meaningful equivalents and adaptable presentation; keep content distinguishable. |
| Operable | Can the person control the interface and navigate the task with their available input and time? | Support keyboard and alternative input, clear focus, manageable targets and user control. |
| Understandable | Can the person understand the content, choices and consequences? | Use coherent language, predictable behavior, instructions, feedback and recovery. |
| Robust | Can the content work through supported browsers, platforms and assistive technology? | Expose dependable semantics, relationships, values and changes; verify interoperability. |

Apply all four to the same task. A visible error can be perceivable while remaining incomprehensible, and a correctly named control can still be impossible to operate. Accessibility depends on the complete chain.

### Define the unit of conformance

Evaluate complete pages and complete processes. A purchase includes choosing a product, entering details, authentication, payment, verification, errors and confirmation. A provider-controlled step can still block the process. Include authenticated, permission-dependent, empty, loading, error and success states.

Rely on accessibility-supported uses of technology. Where a conforming alternative version is considered, verify that it meets the standard's conditions, stays current, provides equivalent information and functionality, and is reachable accessibly. A phone number, separate PDF, or reduced feature set is not automatically a conforming alternative.

Content that is not relied on for conformance must still satisfy the non-interference requirements. A flashing advertisement or keyboard trap cannot become acceptable by labeling it optional.

### Use requirements language consistently

In this guide, **requirement** identifies a standards obligation within its stated scope or an applicable legal duty. **Default** identifies a product convention that can be adjusted with a documented reason and equivalent access. **Enhancement** identifies a stronger accommodation. A product default can be stricter than AA without being an AA requirement.

When sources appear to conflict, resolve the applicable law and standard first, then the target platform and user need. A native point size does not redefine a CSS-pixel threshold. A legal exception does not prove that the content is usable.

## 4. Scope European legal obligations

### Build a legal applicability record

European accessibility law contains several overlapping instruments. The UN Convention on the Rights of Persons with Disabilities establishes a rights framework that includes access to information and communication technology. Specific EU directives and national laws turn parts of that framework into concrete duties. Public procurement, employment, equality, sector-specific and national accessibility rules can also apply.

Before a compliance decision, identify the legal entity, role, countries served, public/private status, product or service category, consumer audience, dates, delivery channels, contracts and connected providers. Record the national implementing law, regulator or enforcement body, applicable technical requirements, documentation duties and any claimed exception. Obtain jurisdiction-specific legal review when coverage or an exemption is consequential. This reference cannot decide a particular organization's liability.

### Distinguish the two main digital-accessibility directives

| Instrument | Main scope | Practical implications |
| --- | --- | --- |
| Web Accessibility Directive, Directive (EU) 2016/2102 (WAD) | Websites and mobile applications of public sector bodies, subject to defined exclusions | Technical accessibility, an accessibility statement, a feedback mechanism and national enforcement/monitoring. Do not assume every publicly funded organization has the same status. |
| European Accessibility Act, Directive (EU) 2019/882 (EAA) | Listed products and specified services, including substantial private-sector consumer activity | Assess the relevant product/service requirements, sector-specific provisions, conformity information, economic-operator responsibilities and national implementation. It does not cover every private website merely because it is online in the EU. |

The WAD's phased application dates were 23 September 2019 for newer websites, 23 September 2020 for other covered websites, and 23 June 2021 for mobile applications. These dates are historical obligations, not upcoming deadlines.

The EAA's main application date is **28 June 2025**, with scope and transition conditions. Examples of covered services include consumer banking, e-commerce, e-books and dedicated software, electronic communications, services providing access to audiovisual media, and defined elements of passenger transport. Urban, suburban and regional transport have a narrower specified scope. Answering communications to 112 has distinct provisions and national timing options.

Examples of covered products include consumer general-purpose computers and operating systems, payment terminals, specified self-service terminals, e-readers, and specified consumer terminal equipment for electronic communications or access to audiovisual media. Classify the actual offering against the law; a list of examples cannot settle borderline cases.

For a covered e-commerce journey, assess identification, security, electronic signatures and payment as well as browsing. Consumer banking has additional requirements, including an information-complexity provision tied to the Common European Framework of Reference for Languages (CEFR) B2 level. That provision does not turn B2 into a universal requirement for all EU websites. E-book requirements address navigation, assistive technology, presentation flexibility, accessibility metadata and digital rights management.

### Include procurement and workplace access

Public procurement can introduce duties beyond the WAD's website/app scope. Article 42(1) of Directive 2014/24/EU requires technical specifications for procurement intended for use by people to take accessibility or design for all into account, except in duly justified cases. Staff-facing systems can therefore matter as well as public services. Resolve the applicable procurement instrument and mandatory requirements before writing a tender; include measurable criteria, evidence and acceptance testing in the contract.

Employment access is also broader than a consumer website target. Article 5 of Directive 2000/78/EC addresses reasonable accommodation for disabled people in employment, subject to its conditions. Recruitment portals, internal tools and training can create workplace barriers even where the EAA's consumer-service scope is absent. A generally accessible design and an individual's reasonable accommodation are related responsibilities, not interchangeable legal tests.

A service offered from outside the EU can still fall within applicable EU-market obligations. A strictly business-to-business offering may have a different EAA analysis from a consumer service, but can still face procurement, workplace, national or contractual requirements. Record the actual audience and transaction instead of using a “B2B” or “international” label as an exemption.

### Treat exclusions and transitions narrowly

The EAA exempts **microenterprises providing services** from its accessibility requirements and related compliance obligations. Its definition uses fewer than 10 employees and annual turnover **or** annual balance-sheet total not exceeding €2 million. Check how the relevant enterprise is assessed; do not infer eligibility from one department's headcount. Microenterprises dealing with products do not receive the same blanket exemption. Other laws and contracts can still apply.

Both directives have defined content exclusions. Their scope and dates differ. Examples include some older media or office files, qualifying archives, certain maps, and third-party content outside the operator's funding, development and control. The WAD also has specific organizational and content exclusions. Evaluate the actual provision before excluding anything; purchasing a widget or outsourcing a checkout does not make it uncontrolled third-party content by default. An old document needed for an active public administrative process may still need to be accessible.

For EAA transitions, distinguish services using qualifying pre-existing products, contracts agreed before 28 June 2025 that may continue unaltered within the permitted period, and national options for qualifying existing self-service terminals. The directive includes a transition ending on 28 June 2030 and a possible terminal-use limit tied to economic life, capped at 20 years after entry into use. **There is no blanket rule that existing websites have until 2030.** Record the precise provision and national implementation relied on.

### Document exceptional claims

Under the WAD, disproportionate burden requires an assessment; it is not established by inconvenience or a preference to spend elsewhere. Explain relevant inaccessible content and available alternatives in the required statement.

Under the EAA, fundamental alteration and disproportionate burden have defined conditions. Use the prescribed assessment criteria, documentation, retention, renewal and notification duties as applicable. External funding specifically for accessibility affects reliance on the burden exception. Separate what is genuinely excepted from the requirements that remain achievable.

Assign an accountable owner, capture the evidence and alternatives considered, and set a review trigger. Do not let an exception become a permanent unexamined waiver for an entire product.

### Separate technical publication from legal citation

As checked on 27 October 2026:

- **EN 301 549 V3.2.1 (2021-03)** is the established harmonized reference identified by the Commission for the WAD. Its web provisions use WCAG 2.1, with additional applicable requirements elsewhere in the standard.
- **EN 301 549 V4.1.1 (2026-09)** has been published. It updates the WCAG baseline to 2.2, adds relevant requirements including user-preference provisions, and includes mapping for the EAA. The official publication guidance inspected for this snapshot reports that this edition has not yet become the cited legal reference; confirm its current Official Journal status before reliance.
- A standard's publication, a label saying “harmonised European standard,” or delivery to the Commission does not establish citation in the Official Journal under a particular directive. A citation under the WAD does not automatically create an EAA presumption of conformity.

Before relying on presumption of conformity, verify the **specific directive, edition, citation, limitations, applicable clauses and any transition or withdrawal date** in the current official record. The presumption covers only the requirements mapped by that reference. Do not state an expected future citation date as an enacted obligation. Continue meeting applicable legal requirements while standards work proceeds.

For planning, build toward WCAG 2.2 AA and the relevant new EN provisions. For an assessment, retain the edition required by law or contract until it changes, while separately checking additional binding requirements. WCAG 2.2 removed the obsolete 4.1.1 Parsing criterion; a legacy checklist based on another instrument may still list it. Record this version difference instead of silently mixing checklists. Valid structure and dependable semantics remain necessary.

### Maintain the right public and internal information

A covered public-sector website or app needs a current accessibility statement using the applicable national model, with an accurate accessibility status, limitations, alternatives, feedback route and enforcement route. Review it when the product or evidence changes and at the required intervals.

For EAA services, prepare the required accessible information explaining the service and how it meets the applicable requirements, together with procedures for ongoing conformity and corrective action. Product responsibilities can include technical documentation, conformity assessment, an EU declaration of conformity and CE marking. A normal website does not gain an EAA compliance badge through CE marking.

Keep audit scope and dates, evidence, supplier records, applicable requirements and exception assessments. Name the national authority for the actual jurisdiction; penalties, complaint procedures and deadlines are not uniform across the EU. A voluntary accessibility page does not replace a legally required statement, service information or product documentation.

## 5. Write an accessibility brief

Capture the decisions that affect access before committing to layouts or architecture.

| Brief field | What to record |
| --- | --- |
| People and context | Intended audiences, known access needs, languages, devices, environments, and whose experience is missing. |
| Tasks | Critical journeys, consequences of failure, private or sensitive actions, and required providers. |
| Baseline | Standards, editions, level, law/contract applicability, supported platforms and explicitly selected enhancements. |
| Content | Media, documents, charts, generated content, user content and editorial responsibilities. |
| Interaction | Input methods, focus model, gestures, time limits, notifications, authentication and recovery. |
| Adaptation | Zoom, large text, contrast modes, reduced motion, orientation, localization and personalization. |
| Verification | Manual and automated methods, representative combinations, user participation, release evidence and owners. |
| Operations | Feedback/support routes, monitoring, procurement conditions, remediation and review triggers. |

Write acceptance criteria as observable outcomes. “Accessible checkout” is too broad to verify. Use: “A keyboard user can choose delivery, correct an invalid address, pay through the provider, and reach a persistent order confirmation. Focus remains visible and follows the task; a screen reader receives field errors and payment outcomes.”

Include people with disabilities during discovery and prototypes, then again in realistic implementation. Recruit for relevant functional needs and technology experience; compensate participants and provide accessible recruitment, consent and session materials. Ask about accommodations without demanding unnecessary diagnostic details. Simulations and internal tests can reveal defects, but cannot substitute for lived experience.

## 6. Create readable visual systems

### Measure the actual color relationship

Use semantic roles such as text, muted text, border, focus, selected, warning and disabled. Verify foreground/background **pairs**, including light/dark themes, component states, nested surfaces, overlays, images, gradients and transparency. A color value has no independent accessibility rating.

| Visual information | WCAG 2.2 requirement | Application |
| --- | --- | --- |
| Ordinary text and images of text | 1.4.3, AA: at least 4.5:1 | Includes labels, placeholders, help, errors and active button text. |
| Large text and images of large text | 1.4.3, AA: at least 3:1 | Large means at least 18 pt, equivalent to 24 CSS px, or 14 pt bold, approximately 18.67 CSS px. Bold alone is insufficient. |
| Identifying information for controls/states and necessary graphical parts | 1.4.11, AA: at least 3:1 against adjacent colors | Evaluate the visual parts needed to identify the control or understand the graphic. Every decorative boundary need not pass. |
| Enhanced text contrast | 1.4.6, AAA: at least 7:1 ordinary and 4.5:1 large | Useful for demanding reading contexts; a selected enhancement is not whole-product AAA. |

Apply actual exceptions: inactive controls, incidental/decorative text and logotypes have relevant text-contrast exceptions; unmodified user-agent controls and essential graphical presentations have scoped non-text exceptions. Do not classify a useful instruction as decoration. Disabled controls can be exempt from contrast criteria while still needing an understandable explanation of availability.

The WCAG 2 ratio compares relative luminance: `(lighter + 0.05) / (darker + 0.05)`. Use an implementation of the specified color conversion and calculation. Do not substitute an HSL lightness difference, grayscale impression or APCA score. Do not round 4.49:1 up to a pass. Resolve compositing before measuring translucent content. For images and gradients, verify the least favorable relevant background; add a stable backing where the image cannot guarantee contrast.

Nominal contrast does not establish full readability. Tiny or thin lettering, anti-aliasing, glare and display quality can weaken an otherwise passing design. Increase robustness where necessary. Test both light and dark appearances; automatic inversion is not a complete theme.

### Use multiple cues for meaning

Combine color with words, shape, position, pattern or line style. A required field needs an understandable indicator and programmatic requirement. An error needs text and association. A selected option needs an exposed selected state, with a visible cue that survives loss of color.

Default to underlined inline links. If links are distinguished from surrounding text through color, verify the relevant sufficient technique and an additional visible cue on interaction; an underline avoids relying on subtle color differences. In charts, use direct labels or keys with distinguishable patterns and line styles. “Red means overdue” is insufficient when overdue status matters.

### Make controls and text legible

Keep useful text as text. Use clear letterforms, realistic sizes and weights, adequate spacing and distinguishable characters. Prefer sentence case for labels and ordinary prose. Avoid long all-capital or italic passages and fully justified narrow columns. These are readability defaults, not universal WCAG prohibitions.

For ordinary web body text, start near `1rem`, then judge the font's actual size, script, density, audience and device. WCAG does not mandate a universal 16 px minimum. Labels, navigation, hints and errors need their own proof. See the [typography reference](typography.md) for font selection, composition and implementation details.

Do not trade clear affordances for a sparse screenshot. Inputs need recognizable boundaries or another sufficient identifying treatment. Icon-only actions need meaningful names and discoverability; unfamiliar or consequential actions usually benefit from visible words. Keep content grouping and feedback near the task so they remain understandable under magnification.

## 7. Preserve scaling, reflow, and user preferences

### Test resizing and reflow independently

For 1.4.4, AA, text can be resized up to 200% without loss of content or function, except captions and images of text. For 1.4.10, AA, ordinary vertically scrolling content reflows at a width equivalent to **320 CSS px**, without two-dimensional scrolling or loss. Horizontally scrolling content uses the corresponding **256 CSS-pixel height** condition.

A 1280 CSS-pixel-wide desktop viewport at 400% browser zoom is one way to test the vertical-content reflow condition. It does not mean every device must offer a particular zoom control, nor that a mobile screenshot tests desktop zoom. Test text-only enlargement separately where available. Check the actual responsive state produced by zoom.

Parts that require two-dimensional layout for use or meaning, such as a map, a complex table or a diagram, can have scoped reflow exceptions. Let that region scroll or provide a usable alternate view while the surrounding page reflows. A whole dashboard does not become exempt because it contains one table.

Use fluid containers, wrapping, minimums that fit the viewport and layouts that grow with content. Test sticky headers, sidebars, cookie banners, chat widgets, dialogs, fixed toolbars, long words and long translations. They often fail before the main paragraph. Essential controls cannot disappear behind an on-screen keyboard or a cropped region.

### Allow text-spacing overrides

For applicable markup and scripts, test all of the following together without other style changes:

| Property | Override value |
| --- | --- |
| Line height | At least 1.5 times the font size |
| Space after paragraphs | At least 2 times the font size |
| Letter spacing | At least 0.12 times the font size |
| Word spacing | At least 0.16 times the font size |

Under 1.4.12, AA, content and function must survive this override. These are **test values**, not mandatory default styles. Apply only properties used by the language/script. Avoid fixed-height text containers, clipped badges and absolute positioning that presumes one line. Truncation needs a dependable way to retrieve the full information for every supported input method.

### Respect user-controlled presentation

Do not disable browser zoom with viewport restrictions. Prefer relative sizing where it supports scaling, but verify behavior: using `rem` or `clamp()` does not prove that content scales adequately. Avoid a root font size or fixed cap that defeats the user's choice.

Support relevant system settings and modes: large text, reduced motion, high contrast/forced colors, captions and platform contrast/transparency preferences. Test custom icons, selected states, checkboxes and focus in forced colors; backgrounds, shadows and images can disappear. Preserve meaningful borders using system colors where appropriate. Restrict `forced-color-adjust: none` to justified, tested cases.

Offer product preferences when the task needs them, such as data density, theme or reduced stimulation. Start from the system preference where available, allow a deliberate override, and retain it appropriately. Do not require users to discover an “accessibility mode” to gain basic keyboard or screen-reader access. A custom toolbar must not interfere with browser or assistive-technology settings.

Support portrait and landscape unless a specific orientation is essential, as required by 1.3.4, AA. A layout preference or a desire to resemble a printed page is not an essential-orientation justification.

## 8. Make structure and meaning programmatic

### Build the semantic foundation

Use elements that represent their function: headings for headings, lists for lists, links for navigation, buttons for actions, inputs for entry, and tables for tabular relationships. Visual weight alone does not communicate a heading to assistive technology. CSS flex/grid does not communicate a data table.

Use a descriptive page title, a clear primary heading and a meaningful heading hierarchy. A single primary `h1` is a useful default, not a universal WCAG counting rule. Nest levels to reflect content structure; do not choose heading levels to get a font size. Mark major regions with native landmarks and give repeated landmarks distinct names where needed.

Keep the document order meaningful. CSS reordering must not create confusing reading, focus or magnified-view sequences. Preserve meaning with styles disabled or transformed by user preferences. Set the page language and mark meaningful changes of language; use the proper script direction and isolate mixed-direction content. Do not reverse text strings to mimic right-to-left layout.

### Treat ARIA as an interface contract

Prefer native HTML or native toolkit controls. They carry semantics and much expected behavior, though author changes can still break them. Add ARIA to expose information that native structure cannot express; avoid redundant or conflicting roles.

A role does not implement keyboard interaction, focus, selection, validation, visual state or event handling. A `div` with `role="button"` still needs a full button implementation. Use a `<button>` unless the task genuinely requires a different construct. Avoid `role="application"` for ordinary pages; it changes interaction expectations and can disrupt screen-reader navigation.

For each control, expose:

- **Name:** what the control acts on or does, such as “Remove delivery address.”
- **Role:** the type of control, such as button or checkbox.
- **Value and state:** current value, checked/selected/expanded/pressed status, validity, availability or progress as relevant.
- **Relationships:** its label, instructions, error, controlled region or group.

Use visible labels as the naming source where possible. The accessible name of a text-labeled control contains the visible text under 2.5.3, A; start with that text by default. Avoid showing “Save” while naming it “Submit record.” Do not manually add “button” or “link” to a name when the role already supplies it.

Use `aria-labelledby` for an existing naming relationship, `aria-describedby` for supplementary instructions, and `aria-label` for a name when no suitable visible text exists. These mechanisms have different precedence and support characteristics. Inspect the computed name rather than assuming attributes concatenate. `title` is not a dependable sole label or instruction.

### Hide only the right things

Decorative or duplicate graphics should not create repeated announcements. Use `alt=""` for decorative HTML images. Hide decorative inline SVG from assistive technology when its enclosing control already has a name. Meaningful CSS background imagery needs an equivalent elsewhere.

Do not put `aria-hidden="true"` on an active control or an ancestor of focusable content. It hides accessibility information without preventing keyboard focus. Use the appropriate mechanism for the intended behavior: removal or `hidden` for absent content, `inert` for an inactive subtree, and a carefully tested visually hidden pattern for text that remains available to assistive technology. A visually hidden label does not help someone who needs a visible instruction.

Meaningful custom canvas/WebGL interfaces need an accessible information and interaction model. A hidden paragraph saying “interactive visualization” does not expose the same task. Keep real interactive controls in the DOM or native accessibility tree, with an equivalent model of the content.

## 9. Support keyboard, focus, and alternative input

### Preserve keyboard conventions

All functionality needs a keyboard route under 2.1.1, A, except operations whose underlying function genuinely depends on a movement path. Freehand drawing has different constraints from moving a card between columns. No keyboard trap is permitted; if leaving a component requires an unusual method, provide instructions.

Use `Tab` and `Shift+Tab` between ordinary controls. Use the chosen pattern's arrow keys, Home/End, Enter, Space and Escape within composites. A standard button activates through Enter and Space; a link conventionally activates through Enter. Preserve text-editing, browser, operating-system and assistive-technology keys.

Do not make every child of a composite a separate tab stop. A tablist or menu can use roving `tabindex` or another appropriate pattern to expose its internal focus model. Ordinary reading content does not need `tabindex="0"` merely to be read. Avoid positive `tabindex`; repair the document and component order.

Disable, remap, or restrict single-character shortcuts to focus on the relevant control as required by 2.1.4, A. A global “s” shortcut can interfere with speech input and screen readers. Document discoverable shortcuts and provide ordinary controls for the same actions.

### Make focus a visible, meaningful state

Keyboard focus marks the current interaction point. Selection marks an option's current state. They can differ. Keep both discernible, including when an unfocused control remains selected.

Under 2.4.7, AA, visible focus is required. Under 2.4.11, AA, author-created content must not entirely hide the newly focused control, subject to the criterion's conditions. The product default is stronger: **keep the focused control and its indicator fully visible** where practical. Fix sticky overlays and scroll behavior; do not settle for a one-pixel glimpse.

Default to a clear external outline, at least 2 CSS px thick, offset from the component, using a color or two-color treatment that remains visible on the relevant surfaces. Verify contrast and clipping in context. This implementation choice alone does not prove 2.4.13, AAA: that criterion tests an indicator area equivalent to a 2 CSS-pixel perimeter and a 3:1 contrast change between the same pixels in focused and unfocused states, with its own exceptions. Also assess applicable non-text contrast. Do not describe the AAA area rule as an AA mandate.

Define `--focus-ring` as a verified focus color for the supported surfaces before using this example. A multi-surface design may need a two-color indicator.

```css
/* Scoped starting point. Verify actual surfaces, clipping and forced colors. */
:focus-visible {
	outline: 3px solid var(--focus-ring);
	outline-offset: 3px;
}

@media (forced-colors: active) {
	:focus-visible {
		outline-color: Highlight;
	}
}
```

Keep a dependable browser indicator if custom styles cannot supply one. Do not remove `outline` globally. `:focus-visible` normally accommodates keyboard focus without requiring a ring after every pointer action; verify custom and programmatic focus paths too.

### Support pointer, touch, speech, and switches

For 2.5.8, AA, pointer targets are at least **24 × 24 CSS px**, unless an actual exception applies. Under the spacing exception, a 24 CSS-pixel-diameter circle centered on each undersized target's bounding box must not intersect another target or the corresponding circle of another undersized target. “24 pixels between icons” is not the rule. Other exceptions concern equivalent controls on the same page, inline targets, unmodified user-agent controls and essential presentation.

Default to **44 × 44 CSS px or larger** for standalone web controls, with separation appropriate to the task. This is a product convention; WCAG 2.5.5's 44 × 44 target is AAA and has its own exceptions. Dense desktop tools can use a justified smaller design while meeting AA and verifying accuracy, focus and input support. The visible icon may be smaller than the hit area, but enlarged hit areas cannot overlap or capture adjacent actions. Native points and Android dp are different platform units.

Provide simple pointer alternatives for multipoint and path-based gestures. Give dragging a single-pointer alternative that needs no dragging, such as selecting an item then selecting a destination, or using Move up/Move down buttons. A keyboard-only alternative does not by itself meet 2.5.7, AA.

Activate ordinary pointer actions on release, allowing cancellation by moving away before release. If activation occurs on the down event, satisfy the criterion's cancellation/undo or essential conditions. Avoid custom gesture handling that prevents ordinary scrolling, zooming or text selection. Provide alternatives to device motion and let users disable motion actuation unless its exception applies. Do not force touch users to use a separate, reduced-function interface when they connect a keyboard or switch methods.

## 10. Make navigation predictable

Provide a way to bypass repeated content, usually a visible-on-focus skip link to the main region. Verify that it moves the interaction point as intended, including keyboard focus where necessary. The destination must remain visible below sticky headers.

Keep repeated navigation and identification consistent. Give pages unique, useful titles, mark the current location, and make link purpose clear in its programmatically available context. “Read more” repeated across unrelated cards creates avoidable ambiguity; use meaningful linked text or an appropriate accessible name that retains the visible wording.

For a set of pages, provide more than one way to find a page where 2.4.5, AA, applies, such as navigation plus search or a site map. The criterion has process-step/result exceptions. A search box is useful only if its input, results, filters, no-results state and navigation are accessible.

Opening a new page, submitting a form or switching context must not happen merely because a control receives focus. Changing a field should not cause an unexpected context change without prior notice. Prefer explicit Apply or Continue actions for changes that would disrupt reading or data entry. Update browser history and Back behavior appropriately in applications.

Use a disclosure pattern for ordinary expanding navigation. Application-style `menu` roles bring specialized keyboard expectations and usually do not fit a list of website links. On small screens, keep the menu's trigger, expanded state, focus behavior and dismissal coherent. Treat it as modal only when it actually blocks interaction outside.

Repeated help mechanisms maintain the same relative order across pages under 3.2.6, A, unless the user initiates the change. The criterion does not require adding help to every page. As a product default, make support easy to find where failure is consequential and offer a channel that does not require speech.

## 11. Build forms that support completion

### Explain before asking

Ask only for necessary information. Give each field a persistent visible label linked programmatically to the input. Group related choices with `fieldset`/`legend` or an equivalent supported structure. Explain format constraints, limits and required/optional status before users encounter an error. A placeholder is not a label; it disappears during entry and may be too faint.

Use appropriate native types and input-purpose metadata. For personal information covered by 1.3.5, AA, programmatically identify the purpose, usually with valid `autocomplete` tokens. Choose `inputmode` to offer a suitable mobile keyboard without rejecting legitimate characters. A telephone number is not a numerical quantity; leading zeros and plus signs matter. Keep culturally flexible names, addresses, dates and identifier formats.

Make a field's label clickable where native behavior supports it. This expands the usable target without adding competing controls. Keep hint and error text associated with the field, and keep visual instructions close enough to use under magnification.

```html
<!-- Invalid state after validation; use a unique ID set per field instance. -->
<label for="contact-email">Email address</label>
<p id="email-hint">We send your booking confirmation here.</p>
<input
	id="contact-email"
	name="email"
	type="email"
	autocomplete="email"
	required
	aria-invalid="true"
	aria-describedby="email-hint email-error"
>
<p id="email-error">Enter an email address in the format name@example.com.</p>
```

Remove the invalid state and stale error association when corrected. Keep a useful hint. This snippet demonstrates one field state; a production form also needs validation behavior, submission handling and form-level feedback.

### Validate without disrupting entry

Validate at a useful moment: on submission, or after leaving a field when early feedback helps. Avoid announcing errors on every keystroke. Tell the person what needs correction and how to correct it without exposing security-sensitive information. “Invalid” alone is insufficient.

After a failed submission, preserve entered data, show an error summary and identify affected fields in text. Default to focusing the summary when the form has several errors, with links that reach each field. A focused summary need not also be an interruptive alert. For one local error, deliberate field focus may be more appropriate. Test the chosen behavior with the actual screen reader and layout.

Separate validation errors from service failures. If the address service is unavailable, do not imply that the address is wrong. Offer manual entry or a recoverable alternative. If the network fails, preserve a draft where safe and make retry understandable. Do not force a complete restart after one mistake.

### Reduce repetition and preserve progress

Under 3.3.7, A, information already entered or supplied in the same process is populated or available to select when required again, except where re-entry is essential, required for security, or the information is no longer valid. A checkbox for “Use billing address as delivery address” can reduce effort. Do not silently reuse sensitive information in a different context.

Break long tasks into meaningful steps when that improves comprehension. State progress and requirements, support Back without data loss, and provide review before submission. Avoid unnecessary steps that turn a short task into a navigation burden. Let people save and resume where interruption is likely; explain retention and session expiry.

Disabled submission can hide the reason a form cannot proceed. Default to an available submit action with clear validation, or provide explicit, accessible instructions and state when disabling is necessary. `aria-disabled` announces unavailability but does not stop events; native `disabled` changes keyboard and form behavior. Choose deliberately.

## 12. Make authentication and transactions accessible

### Remove avoidable cognitive tests

For 3.3.8, AA, authentication cannot require a cognitive-function test without an applicable alternative or assistance mechanism, subject to the criterion's object-recognition and personal-content exceptions. Passwords are not categorically prohibited. An implementation that supports password managers and copy/paste can provide assistance. The stronger AAA criterion removes those recognition exceptions.

Allow paste, autofill, password managers and accessible show/hide-password controls. Do not force users to transcribe a code manually if it can be copied or filled. A single code input is often easier than separately managed digit boxes; if boxes are used, preserve whole-code paste, editing and announcements. Explain expiry and resend without resetting the person's other work unnecessarily.

Offer appropriate authentication options, such as supported passkeys or an accessible alternative, without assuming every user owns a particular phone or can perform a biometric action. A magic-link workflow must work across email, browser, device switching and return to the task. Recovery and multifactor enrollment need the same attention as sign-in.

Do not rely on a visual CAPTCHA, audio challenge or object-recognition exception as the entire accessibility strategy. Each can exclude users. Prefer abuse prevention that avoids a user puzzle; if a challenge is necessary, provide effective, verified alternatives. Non-text CAPTCHA also has separate text-alternative requirements. Test the actual vendor integration.

### Preserve safety and privacy

Make account creation, verification, consent, identity checks, recovery and support usable without seeing, hearing, speaking, or making precise gestures where the task permits alternatives. Camera-only or timed liveness checks require careful provider assessment and a workable alternative. Never solve an inaccessible flow by requiring a user to disclose their password or hand control to a helper.

Under 3.3.4, AA, covered legal, financial and stored-user-data submissions need the relevant reversibility, checking or confirmation safeguard. Provide a clear review of amount, recipient, consequences and editable details. Prefer undo for easily reversible actions; use confirmation for consequential actions that cannot be easily undone. Avoid repeated low-value confirmation dialogs that train automatic acceptance.

Explain sensitive session timeouts, preserve appropriate data, and let people extend where required. Coordinate with security on genuine exceptions; “security” is not a universal reason to block paste, remove accommodation or erase progress. State what has and has not happened after an interrupted transaction so the person can avoid duplicate payments.

## 13. Handle dynamic content and application state

### Decide whether to move focus or announce

A content update and a context change need different treatment. Avoid sending focus to every update; avoid leaving focus on an element that has disappeared. Define the behavior in the component or journey contract.

| Event | Default behavior | Verify |
| --- | --- | --- |
| New application route representing a new page | Update the document title and place focus at the main heading or a suitable start point | User learns the new context; Back/Forward and restored state remain coherent. |
| Inline disclosure opens | Keep focus on the trigger; expose expanded state | New content follows meaningfully and is reachable. |
| Search or filter results update | Keep focus on the control; announce a concise result summary when useful | Avoid reading the entire result set or announcing on every keystroke. |
| Modal dialog opens | Move focus inside and make the background inactive | Reading and keyboard navigation remain within the active task. |
| An item is deleted | Move focus to a logical surviving item, action or heading | Announce the outcome and provide undo where supported. |
| Background save completes | Keep focus; expose a short status message | Confirmation is available without interrupting typing. |
| Submission fails | Follow the form's error-summary or field-focus pattern | Errors are understandable, persistent and connected to correction. |
| Async operation fails | Keep task context; expose the failure and retry/help | Failure is distinguishable from ongoing progress and no data is silently lost. |

These are defaults. A route that only changes a filter may not need the same focus movement as a new page. A browser's restored navigation state may be more useful than resetting focus. Document the intended outcome and verify it with the real framework and browser.

### Use announcements sparingly

Under 4.1.3, AA, qualifying status messages need programmatically determinable roles or properties so assistive technology can present them without focus. Use a polite status region for ordinary completion and result counts. Reserve alerts or assertive announcements for genuinely urgent information. Most interface updates are not emergencies.

Create the relevant region before updating its text when required for reliable support. Keep messages concise, group related changes and prevent duplicate output from both focus movement and a live region. Do not make an entire application, table or streaming response a live region. Test how busy/atomic settings interact with the chosen technology rather than adding attributes indiscriminately.

Keep significant messages visible and recoverable. A transient toast should not be the only record of a failed payment, expiring booking or completed export. An announcement cannot replace a visible message for a deaf or hard-of-hearing screen-reader user, someone using magnification, or someone who missed the output.

```html
<!-- Mount this before the operation. Update its text after the save result. -->
<p id="save-status" role="status"></p>
```

For a completed save, set the text to a short confirmation such as “Changes saved.” For a failure, provide a persistent explanation and a working retry action; changing this message alone is not a recovery design.

### Preserve a stable interaction model

Mark loading regions appropriately, provide understandable progress and prevent accidental duplicate actions. Keep stable element identities so routine renders do not reset focus, cursor position or screen-reader location. Skeletons should not be exposed as dozens of meaningless elements. Remove busy state when loading ends, including on failure.

For uploads or long jobs, expose name, value, limits or indeterminate state as appropriate, plus textual status, cancellation and retry. Do not announce every percentage point. For lazy loading and infinite lists, preserve position and provide predictable access to more content and the footer. Pagination or a Load more action often produces a more controllable experience.

For chat and AI-generated output, keep reading position stable, offer a stop control, and announce meaningful chunks or completion without token-by-token speech. Make citations, code, tables and actions accessible. Automated alt text, captions, descriptions or summaries need review appropriate to their consequences; fluent output is not evidence of accuracy or completeness.

## 14. Specify component behavior

Every component needs a semantic and interaction contract, including its failure states. Choose a maintained implementation that matches the required pattern before inventing a custom one.

| Component | Required design decisions and behaviors | Common failure |
| --- | --- | --- |
| Button, link, icon action | Correct role; meaningful name; keyboard activation; visible focus; availability and feedback | Clickable non-semantic container; nested interactive controls; icon exposed without a name. |
| Toggle button, checkbox, switch | Clear label; exposed state; distinguish persistent on/off state from a one-time command | Color-only state; label changes that make a pressed state ambiguous. |
| Disclosure/accordion | Button trigger; expanded state; relationship to content; heading structure; predictable focus | Hiding content while focus remains inside; making every accordion a modal. |
| Tabs | Tablist/tab/tabpanel relationships; selected state; one appropriate tab stop; arrow-key navigation | Tab semantics on links to independent pages; automatic activation that waits on a network request. |
| Dialog | Accessible name; suitable initial focus; active/inert regions; contained tab sequence for modal use; dismissal and return focus | `aria-modal` applied while users can still interact with the background. |
| Menu button | Clear trigger and expanded state; appropriate menu semantics; arrows/Enter/Escape and return | Using application-menu roles for ordinary website navigation without the expected keyboard model. |
| Combobox/autocomplete | Label; editable/select-only choice; popup role; expanded state; active option; selection/cancel behavior | Treating typed text as a selected result without confirmation; breaking native text-editing keys. |
| Tooltip | Trigger accessible by keyboard; description relationship; dismissal, hoverability and persistence as applicable | Essential instructions on hover only; interactive links inside a tooltip. |
| Slider/range | Name, value, range, understandable units and keyboard adjustment; precise-entry alternative where useful | Drag-only interaction; exposing “40” without its meaning. |
| Date picker | Label and format; usable keyboard calendar if present; direct entry where appropriate; error and locale handling | Requiring repeated month navigation for a date decades in the past. |
| Table/grid | Choose reading table versus interactive grid; header relationships; focus and editing model if interactive | Adding `role="grid"` to a static table without implementing grid navigation. |
| File upload | Operable file input or equivalent; type/size instructions; status; correction, cancellation and removal | Drag-and-drop-only input or unlabeled progress. |
| Alert/banner/toast | Severity, persistence, announcement behavior, action access and dismissal | Auto-dismissed critical information or an assertive announcement for every routine message. |

### Dialogs and layered interfaces

Default to a native dialog or a well-tested library implementation where suitable. A native element still needs a name, sensible content, initial focus, close behavior and verified platform support. Opening an element with `showModal()` has different behavior from merely adding an `open` attribute.

On open, move focus to the first useful element. For long or structured content, the title or an introductory static element with programmatic focus can preserve reading order better than a distant button. For irreversible actions, initial focus on the least destructive choice is often appropriate. Do not make the entire dialog one long description when its structure should be navigated.

While modal, contain Tab/Shift+Tab and make background content inert to interaction and accessibility navigation. Provide an obvious close/cancel action and Escape dismissal by default. If a critical process cannot safely dismiss, explain the available path and verify that the user can finish or leave it; modality cannot become an indefinite trap. Restore focus to the trigger or a logical successor if the trigger no longer exists.

Test stacking, scrolling, viewport changes and the mobile keyboard. A modal that fits an initial screenshot may become unusable with large text or validation messages. Non-modal popovers need an appropriate exit and focus policy without trapping users unnecessarily.

### Tooltips, hover content, and touch

Under 1.4.13, AA, applicable additional content appearing on hover/focus must be dismissible, hoverable and persistent under the criterion's conditions. Escape is a useful dismissal mechanism when a tooltip obscures content. Keep it visible while the pointer moves onto it, until focus/hover is removed, the user dismisses it or its information becomes invalid.

Tooltips are supplementary. Put essential instructions in persistent text. Touch users need equivalent access without hover. If a popup contains interactive controls, use an appropriate popover/dialog pattern rather than pretending it is a tooltip.

### Composite controls

For tabs, activate automatically on focus only when the panel appears without noticeable delay; otherwise use manual activation so arrow navigation remains efficient. For comboboxes, expose open state and active option, preserve standard text editing, allow deliberate selection and cancellation, and distinguish “no results” from no input. Do not conflate DOM focus, the active descendant and committed selection.

For virtualized lists and grids, communicate position/count where necessary and ensure the focused or active item is not removed unexpectedly. Test actual content retrieval, editing, sorting and return from details. If a complex pattern is not necessary, use a simpler native control or list.

## 15. Support cognition, language, and emotional safety

### Reduce the mental work of the task

Make the goal, current state and next action explicit. Use familiar words and patterns, explain technical terms when needed, and present instructions in the order people act. Put the key action before qualifications that do not affect the immediate choice. Preserve qualifications that do affect consent, eligibility, cost or risk.

Use descriptive headings, short coherent sections and lists for genuinely sequential or parallel information. Avoid unexplained symbols, vague labels and references such as “click the green option on the right.” Provide enough context to identify an option without relying on sight, hearing, location or memory alone.

Prefer recognition over recall: show the choices, retain previously supplied information, summarize the current selection and offer review. Keep instructions available during the task. If a process needs external documents, explain that before the user begins.

Progressive disclosure can reduce clutter, but hidden information must remain findable and appropriately announced. Do not hide costs, requirements or essential help behind an unlabeled icon. A simplified mode should retain the useful task and make its limitations clear.

### Support understanding and recovery

Different readers may need plain language, Easy Read material, symbols paired with words, sign language, translation, audio or personal assistance. These are different accommodations. An automated reading-grade score or a specialist font does not establish comprehension. Test important instructions with the intended audience and qualified reviewers.

Do not claim plain language, a particular reading grade or a dyslexia font is a universal WCAG AA requirement. Some language and reading requirements are AAA; other legal instruments can impose additional obligations. Preserve technical precision while reducing unnecessary complexity.

Make mistakes recoverable. Retain input, provide Back and Undo where useful, avoid unexpected defaults, and explain changed conditions. Use a calm, specific error such as “Your session expired. Sign in again to continue from your saved delivery details,” only when that recovery really exists. Do not blame the user for a system failure.

### Respect attention, autonomy, and distress

Give users control over interruptions, animation and nonessential sound. Avoid false urgency, repeated nagging, hidden cancellation and manipulative consent. A person may need more time to decide without being pushed into an action.

For sensitive services, consider whether reminders, on-screen messages or shared-device notifications could reveal private information. Let people choose safe contact methods and provide a private way to leave or resume when relevant. Do not infer a person's disability, diagnosis or competence from their behavior or accessibility settings.

Accessibility and privacy can reinforce each other: an independently usable form reduces the need for a helper to handle private data. Collect accommodation information only when needed, explain its use and limit retention. Make the feedback mechanism accessible without requiring medical proof.

## 16. Control motion, time, and interruption

### Make motion purposeful and optional

Use motion to explain a transition or state when it helps. Avoid parallax, automatic camera travel, large zooming effects, repeated bouncing and moving backgrounds that compete with reading. Direct manipulation can still cause discomfort. Short duration alone does not make motion safe.

Respect `prefers-reduced-motion` and the platform's equivalent. Provide a static or reduced-motion rendering with the same information and actions. Prefer starting with a stable experience and enabling nonessential motion only when preferences permit it. If the product offers a motion preference, make it usable before the effect and preserve it.

```css
/* Animation is optional; all information is visible in the base state. */
.result {
	opacity: 1;
	transform: none;
}

@media (prefers-reduced-motion: no-preference) {
	.result--new {
		animation: result-arrive 140ms ease-out;
	}
}

@keyframes result-arrive {
	from { opacity: 0; }
	to { opacity: 1; }
}
```

This example does not address media playback or JavaScript-driven movement. Check every motion source. Do not rely on animation events to expose content or finish a transaction; the static path must work. Reduced motion does not necessarily mean zero fades, and some people prefer no transitions at all. Make choices appropriate to the audience.

Under 2.3.3, AAA, nonessential motion animation triggered by interaction can be disabled. Adopt this as a product convention even when the formal target is AA. It is separate from the A requirements for automatic movement and flashing.

### Provide control over automatic content

Under 2.2.2, A, automatically starting moving, blinking or scrolling content that lasts more than five seconds and appears alongside other content needs a pause, stop or hide mechanism unless essential. Automatically updating information alongside other content also needs control, or control of update frequency, unless essential; it has **no five-second allowance**.

Default to static carousels with explicit controls. If automatic rotation is justified, supply a discoverable pause action, stop appropriately during interaction, and do not resume against the user's choice. Reduced motion does not replace playback or rotation controls. Scroll-driven storytelling must preserve ordinary reading, navigation, keyboard use, and a meaningful stable alternative.

Audio that starts automatically for more than three seconds needs the specified pause/stop or independent volume control under 1.4.2, A. Default to user-initiated playback. Do not use audio, haptics or motion as the sole confirmation of an important event.

### Avoid flashes and dangerous stimuli

Default to no flashing. Under 2.3.1, A, content cannot flash more than three times in any one-second period unless below the defined general and red-flash thresholds. Those thresholds involve more than a frequency count. Use appropriate analysis when flashing material is unavoidable; do not judge safety by eye or through a warning alone. A pause button cannot undo exposure that occurs before someone reaches it.

Consider videos, ads, GIFs, loading effects and user-supplied media as well as authored animations. Large alternating patterns, motion and bright transitions can cause discomfort even when a flash criterion passes. Provide control and lower-stimulation alternatives.

### Give people enough time

Under 2.2.1, A, content-set limits need an applicable turn-off, adjustment or extension route unless a defined exception applies. The adjustment route permits at least ten times the default. The extension route warns at least 20 seconds before expiry, offers a simple extension action and allows at least ten extensions. Real-time, essential and limits longer than 20 hours have specific exceptions.

Default to avoiding unnecessary time limits. For reservations or security-sensitive sessions, explain the time condition early and provide the permitted extension/recovery behavior. Do not treat every business deadline as an essential technical exception. Preserve work after reauthentication where safe; that is also a useful stronger accommodation beyond the baseline timing rule.

Keep important messages until dismissed or available in a persistent location. A toast that vanishes after five seconds may be missed by someone reading with a magnifier, using switches or processing slowly. Timing must be evaluated as part of the task, not just as an animation setting.

## 17. Provide image, audio, and video equivalents

### Choose image alternatives by purpose

An alternative communicates the image's contribution in its context. It need not list every visible object.

| Image purpose | Treatment | Example |
| --- | --- | --- |
| Pure decoration or redundant visual treatment | Empty alt for an HTML image, or appropriate hiding for a decorative graphic | A flourish beside an already named heading uses `alt=""`. |
| Information | Concise text equivalent of the relevant meaning | A product photo describes a distinguishing handle or opening when it affects the choice. |
| Action or destination | Name the function of the enclosing control | A standalone linked logo names the destination or organization, rather than its colors and geometry. |
| Complex chart/diagram | Concise identification plus nearby structured explanation or equivalent data | A route diagram has a readable route list and necessary connections. |
| Meaningful text in an image | Provide the words or an equivalent, and prefer real text where possible | A promotional graphic's date and booking instructions also appear as text. |

Avoid filenames, automatic “image of” prefixes that add no meaning, SEO keyword lists, and guessing a person's identity or feelings. Context can justify more detail, such as an art collection, product specification or evidence image. Keep alternatives current when images change. Review generated descriptions against the actual asset and task.

For complex graphics, a long alt attribute is usually less usable than a short identification and structured nearby equivalent. An SVG needs appropriate naming and role where meaningful; test how the delivered markup is exposed. Decorative copies must not cause duplicate reading. Images of text have limited exceptions under 1.4.5, AA; a desire to preserve a chosen font is usually insufficient.

### Plan media alternatives before production

Captions convey spoken content and relevant non-speech audio in synchrony with the media. Dialogue-only subtitles or an automatic transcript may omit speaker identification, sound cues and meaningful timing. Audio descriptions convey important visual information through audio. A descriptive transcript can combine speech, relevant sounds and visual information in structured text.

| Media | WCAG 2.2 A/AA provision | Production decision |
| --- | --- | --- |
| Prerecorded audio only | 1.2.1, A: an equivalent alternative for time-based media, subject to the labeled media-alternative exception | Provide an accurate transcript with speakers and meaningful sound. |
| Prerecorded silent video | 1.2.1, A: equivalent time-based alternative or audio track, subject to the same exception | Describe the meaningful sequence and actions. |
| Prerecorded synchronized video/audio | 1.2.2, A: captions; 1.2.3, A: audio description or a media alternative, with stated exceptions | Plan both audible and visual equivalents. |
| Prerecorded synchronized video at AA | 1.2.5, AA: audio description | A transcript alone does not replace this AA requirement. If the existing audio already conveys all necessary visuals, an additional track may be unnecessary. |
| Live synchronized video/audio | 1.2.4, AA: live captions | Plan a real captioning service and operating procedure. |

Sign-language interpretation, extended description and other media alternatives may be needed by the audience or a stronger requirement, even when not mandated at AA. A sign language is a language with its own users and regional variation. A text transcript does not meet every deaf person's language needs. Deafblind users may need persistent structured text rather than either audio or rapidly changing captions.

Review captions for accuracy, timing, speakers, punctuation and meaningful sounds. Check that captions do not cover essential visuals and remain legible when enlarged. Preserve equations, names and specialized terms accurately. Treat automatic output as a draft requiring appropriate quality control.

### Make the player usable

Provide labeled, keyboard-operable play/pause, volume, captions, description and full-screen controls as applicable. Expose state and progress without flooding announcements. Ensure focus remains visible, sliders are usable, controls are reachable at zoom, and a person can leave the player. Do not trap keyboard or screen-reader navigation in an embedded frame.

Allow users to find transcripts and accessible versions near the media. Preserve alternatives in downloads, embedded variants and published recordings. If a live event is recorded, evaluate the recording as prerecorded content for its later publication rather than assuming live provision settles it.

## 18. Make data and complex workspaces accessible

### Preserve relationships in tables

Use native tables for data relationships, with a useful caption and correctly associated header cells. `scope` can express straightforward row/column headers; complex relationships may need explicit `headers`/`id` associations. Simplify a table before creating an elaborate association structure. Avoid merged cells that make the relationships unnecessarily hard to follow.

Put a sorting button in the appropriate header and expose sort state on the relevant header. State the column, direction and result as needed without reannouncing the whole table. Give row actions meaningful context, such as “Edit annual plan,” while retaining their visible labels.

At narrow widths, preserve the associations. A horizontally scrollable region can be appropriate for a truly two-dimensional table; it needs discoverability, keyboard access where required and a visible focus treatment. A card transformation needs explicit labels and a reading order that retains the data's meaning. Do not merely hide columns needed for the task.

### Provide the same analytical task

For a chart, include a meaningful title, unit, period, important trends and an appropriate data equivalent. A summary supports orientation; a table or other navigable representation supports detailed comparison. Choose the equivalent around what users must do: compare values, find outliers, filter periods, inspect uncertainty or act on an item.

A download is useful but may add an inaccessible tool dependency or omit live interactions. Provide an in-product equivalent for important tasks. Keep filters, data versions and units synchronized across views. Distinguish absent, suppressed, estimated and zero values in both visual and textual representations.

Make information that appears on hover available on keyboard focus or deliberate activation. Avoid a tab stop on every one of thousands of marks; use a documented navigation model or a structured alternate view. Do not present a table as equivalent when a visual user can also select a point and take an action that the table cannot perform.

Use line styles, markers, direct labels and text alongside color. Evaluate meaningful boundaries and marks against adjacent colors, without demanding that every decorative gridline carry equal contrast. Test what remains understandable when patterns or colors change in forced-color settings.

### Make spatial work manageable

Maps need searchable places, textual addresses, meaningful controls and an alternate way to obtain the location or route information required by the task. Provide non-drag panning/zooming and keyboard routes as applicable. A static “map” label is not equivalent to finding an accessible entrance.

For editors, whiteboards, timelines, node graphs and drag-based workspaces, define an accessible object model: items, names, properties, hierarchy, relationships, selection and actions. Provide ways to create, find, move, connect, edit and delete objects without relying on precise spatial manipulation. Offer coordinates or relative ordering where meaningful, with feedback and undo. Verify that a hidden list view supports the same useful operations.

Dense tools can require training and specialized keyboard models. Make those models discoverable and consistent, and provide task-level testing with intended users. Complexity is a reason for careful design and expert review, not a general accessibility exception.

## 19. Deliver accessible documents and communications

### Choose the format around the task

Default to accessible HTML for ordinary online information and forms. Offer downloads where people need offline use, printing, stable pagination or editing. A PDF can be accessible, but export settings alone do not establish access. Fix the structured source and verify the delivered file.

| Artifact | Author and verify |
| --- | --- |
| PDF | Tagged structure, meaningful reading order, headings, language/title, real text, image alternatives, table headers, labeled links and form controls, keyboard order and appropriate security settings. Verify extraction, navigation and assistive-technology output. |
| Word or similar document | Real heading/list styles, language, descriptive links, alt text, meaningful tables, readable layout and accessible forms. Avoid using floating text boxes to create a visually ordered but semantically scrambled page. |
| Presentation | Slide titles, reading order, sufficient type/contrast, meaningful descriptions, accessible charts and captioned media. Present verbal descriptions of meaningful visuals. Provide material and alternatives participants can use independently. |
| Spreadsheet | Clear named sheets, meaningful table organization and headers, explanatory text, accessible charts, predictable input cells and understandable errors. Avoid merged-cell layouts that obscure data relationships. |
| EPUB/e-book | Navigable structure, text resizing and reflow where appropriate, language, alternatives, accessible navigation and metadata; rights-management settings that preserve accessibility. |
| Email/message | Live text, meaningful headings and links, logical reading order, image alternatives, understandable actions and usable light/dark rendering. Test actual mail clients and image-blocked output. |

Use optical character recognition (OCR) for scanned documents when necessary, then correct recognition and restore structure. OCR alone cannot reconstruct headings, tables, reading order or meaningful alternatives reliably. A tagged file can still contain wrong tags and a poor reading sequence. Formal PDF/UA or EPUB accessibility targets can strengthen a delivery contract; verify the applicable edition and validator rather than equating a format label with universal usability.

For generated exports, treat the template and data mapping as production code. Test long content, multipage tables, missing values, charts and user-supplied images. Maintain equivalents when the source changes. Label links with file type and size where that helps users decide how to access them.

### Keep the service accessible beyond the screen

A confirmation email, invoice, calendar invitation, support attachment, consent form or downloadable statement can be the only persistent record of an action. Include these outputs in the journey acceptance criteria. Plain-text email is useful but does not excuse inaccessible essential content in the main message.

Provide contact options that do not all depend on speech, hearing, a specific device, or the broken interface. State expected response times honestly. A support agent can provide interim assistance, but assistance should preserve privacy and be tracked alongside the permanent repair.

## 20. Apply the principles across platforms

### Native applications

Use platform controls and accessibility APIs rather than treating a native screen as a web page with renamed attributes. Supply meaningful labels, traits/roles, values, state, grouping, actions and traversal order. Keep content discoverable without requiring users to know hidden custom gestures.

Support native text scaling, contrast and motion settings. On Apple platforms, test VoiceOver, relevant Dynamic Type sizes, Voice Control, keyboard access and switch navigation. On Android, test TalkBack, font/display scaling, relevant switch/voice input and target behavior. On desktop, include keyboard operation, platform accessibility APIs, magnification and screen readers used by the audience. Select the actual platform versions in the product's support matrix.

Use platform units and conventions. A common touch default is 44 × 44 pt on iOS and 48 × 48 dp on Android; these are platform design targets, not conversions of WCAG's CSS pixels. Desktop and spatial controls need their own platform-specific sizing and testing. Verify current official platform guidance before implementation; do not use the smallest published size as the default for every context.

Custom drawing and games need explicit accessibility representations. Group information that forms one meaningful item, while preserving independently actionable children. Test navigation order, rotor or heading navigation where supported, custom actions, announcements, and return after overlays. Do not manually append a role to every label or make a whole complex screen one inaccessible element.

### Hybrid applications and embedded views

Test the boundary between web and native content. Focus, language, announcements, keyboard handling and back navigation can change at the boundary. Verify dialogs inside web views, authentication redirects, downloads, external browsers, deep links and returning to the originating task. A web test and a native test performed separately cannot prove the transition works.

### Kiosks and self-service terminals

Closed-functionality products cannot assume users will install their own assistive technology. Assess nonvisual operation, tactile controls, speech output, private audio, hearing compatibility, reach, force, time limits and physical access as relevant. Payment and identity steps need privacy as well as operability.

Apply the relevant EN clauses and product rules with hardware and accessibility specialists. An accessible website on an unreachable touchscreen does not make a terminal accessible. This guide supplies digital design principles, not a complete hardware or built-environment specification.

### Spatial, immersive, and game experiences

Provide alternatives to precise hand, gaze, head, speech or whole-body movement. Keep essential controls comfortably reachable and allow seated or stationary use where the task permits. Support recentering, adjustable interaction ranges, meaningful descriptions, captions and stable ways to locate information.

Avoid compulsory camera motion and sustained peripheral movement. Offer a stable frame of reference, lower-motion locomotion or equivalent navigation, pause and comfort settings before exposure. Depth, stereo sound and haptics can supplement information but cannot be the only representation where users need alternatives.

Offer appropriate control remapping, adjustable difficulty, timing and assistance in games without assuming one accommodation fits all players. Evaluate the actual platform and user task with specialists. Do not claim WCAG AA alone certifies immersive comfort or physical safety.

## 21. Encode accessibility in the design system

### Specify valid combinations and behavior

Tokens and components should make the dependable path easy to use. Store semantic colors, supported foreground/background pairs, focus treatment, typography roles, target sizing, motion behavior and layering rules. A palette of individually attractive values is not a contrast contract.

```yaml
# Illustrative contract fields, not a universal token schema.
component: booking-submit
semantics: native-button
name-source: visible-text
label: Confirm booking
states:
  - default
  - hover
  - focus-visible
  - submitting
  - unavailable
  - failed
focus:
  appearance: system-focus-ring
  during-submit: retained
  on-success: confirmation-heading
feedback:
  submitting: persistent-status
  failure: persistent-message-with-retry
adaptation:
  - text-at-200-percent
  - reflow-at-320-css-pixels
  - spacing-overrides
  - forced-colors
  - reduced-motion
```

For each reusable component, document anatomy, semantic role, naming requirements, keyboard model, focus entry/exit, exposed states, announcements, alternatives, responsive behavior, content limits, and known support constraints. Include the responsibility left to consumers. A button can enforce its role; it cannot decide whether “OK” describes a consequential action adequately.

### Design and test the full state matrix

Include default, hover, focus, active, selected/checked, expanded, disabled, read-only, loading, success, warning, error and empty states as applicable. Distinguish disabled from read-only, pressed from selected, and focused from active. Include combined states: a selected item can have focus, and a submitting form can fail.

Add realistic long labels, translation expansion, right-to-left language, large text, narrow widths, high contrast, reduced motion, absent images and asynchronous failure. Use the actual rendered component rather than relying only on design-tool contrast plugins. A prototype cannot establish production semantics or keyboard support unless it genuinely implements them.

### Govern composition and change

Provide simple native patterns before complex custom widgets. Review dependencies for accessibility behavior, maintenance and escape hatches. A library's reputation or an “accessible” marketing claim does not settle the implementation in this product.

Test both the base component and its composition in real pages. Enforce safe naming APIs, unique IDs, supported token pairings and necessary prop relationships where practical. Avoid APIs that let every consumer replace a semantic button with an arbitrary container. Keep a deliberate escape route for real exceptions, with review and evidence.

When changing a shared token or component, identify affected states, themes and consumers; a focus or label regression can spread throughout the product. Version behavior changes, document migration, retest critical journeys and retire broken variants. Keep accessible examples as the default documentation, rather than as a special appendix.

For CMS and authoring tools, support accessible creation: semantic headings, alt/decorative decisions, table headers, captions, link text and sensible templates. Preserve this structure on export. The authoring interface must also work for authors with disabilities. Avoid requiring meaningless alt text merely to satisfy a nonempty field.

## 22. Evaluate with complementary methods

### Define scope and evidence before testing

Record the build/version, pages and states, complete journeys, standards/editions, browsers, operating systems, assistive technology, settings, languages, roles, third parties and documents. Use production-like data and a safe environment for consequential actions. Explain omissions and what they prevent you from claiming.

For a substantial site, use a structured conformance-evaluation method: define scope, explore the product, select a representative sample, evaluate and report. Include shared templates, unique page types, unusual components, authenticated and error states, full processes and suitable additional sampling. A sample supports bounded conclusions and defect discovery; it does not prove that every page was tested.

### Combine methods for different questions

| Method | What it can establish | What it cannot establish alone |
| --- | --- | --- |
| Automated rules in rendered states | Detect specified issues such as missing names, certain semantic defects and calculable contrast conditions | Meaningful alt text, logical focus, complete task access, comprehension or legal compliance. |
| Design/source review | Identify intended behavior, content omissions, architecture risks and implementation defects | Actual browser/AT behavior or the delivered rendering. |
| Manual keyboard/pointer checks | Operability, focus order, visibility, dismissal, cancellation and alternatives in tested states | The full nonvisual experience or all disability needs. |
| Screen-reader/braille evaluation | Exposed names, roles, relationships, reading, announcements and task access in tested combinations | Every screen reader, every user strategy, or visual usability. |
| Zoom, text, contrast and motion checks | Layout resilience and accommodation behavior in tested conditions | Whether the text and workflow are understandable to all audiences. |
| Research with disabled users | Real strategies, effort, misunderstandings and barriers in realistic tasks | Exhaustive criterion coverage or universal representation. |
| Expert conformance assessment | Structured interpretation and evidence against the stated target | A permanent guarantee across later changes or untested scope. |

Automated scans and accessibility-tree snapshots are useful inputs. A high score or zero detected violations is not a conformance certificate. Tools find different issues; a percentage of machine-tested rules is not a percentage of accessible user experience. Here, AT means assistive technology. Screenshot inspection cannot reveal all semantics, and a semantic snapshot cannot reveal every clipped control.

### Use a representative support matrix

Select combinations based on audience, platform support and product risk. A practical starting set for a web service can include keyboard-only testing; a Windows screen reader with a supported mainstream browser; VoiceOver with Safari on an Apple platform; and mobile screen-reader testing on relevant iOS/Android devices. Add braille, switch, voice input or specialist combinations where needs and risk justify them. Do not claim this starting set is universally sufficient.

Use trained evaluators for unfamiliar assistive technology. Learn basic navigation and distinguish an implementation failure from a tester's unfamiliarity, a platform setting, or a known technology defect. Record actual versions and settings, reproduce the failure, and investigate inconsistent results. One passing combination does not cancel a failure in another supported combination.

### Run repeatable manual checks

The following sequence is a baseline for a changed journey. Expand it for media, complex tools, documents or legal requirements.

1. **Orient.** Check title, language, headings, landmarks, page purpose and initial reading order. Confirm the task is understandable before starting.
2. **Use the keyboard.** Start from a known point. Reach all functionality, bypass repetition, move through composites, open and close layers, and reverse direction. Confirm focus remains visible, logically placed and recoverable.
3. **Use a screen reader.** Read in sequence and by structure, list links/controls where supported, complete forms, trigger errors and observe dynamic updates. Verify name, role, value, state and relationships rather than expecting one exact spoken phrase.
4. **Enlarge and reflow.** Test 200% text resizing, the 320 CSS-pixel-equivalent reflow condition, meaningful narrow layouts and large-text settings separately. Check sticky content and on-screen keyboards.
5. **Override presentation.** Apply simultaneous text-spacing values, forced colors/high contrast and reduced motion. Check text and meaningful graphics against actual backgrounds in all supported themes and states.
6. **Use alternative input.** Verify targets, cancellation, hover/focus behavior, non-drag and simple-pointer alternatives. Test speech/switch methods selected in the support matrix.
7. **Exercise failure and recovery.** Trigger validation, network/provider failure, timeout, empty results and interrupted authentication. Correct, retry, go back, resume and cancel without losing essential context or duplicating actions.
8. **Inspect outputs.** Open confirmation messages, documents, exports and support paths. Test media alternatives and their player where present.
9. **Record evidence.** Capture the build, environment, steps, expected/actual behavior and remaining limits. Reconcile with the criterion inventory and critical task acceptance criteria.

Use real implementations for interaction claims. Design annotations can specify expected behavior; they do not demonstrate it. The illustrative snippets in this guide need integration and runtime verification before production use.

### Include users without turning them into a checklist

Give participants realistic tasks, accessible materials and the accommodations they request. Let them use familiar technology when feasible. Observe strategies and ask about breakdowns without coaching away the barrier. Distinguish a participant's preference, an individual access need and a broader implementation defect.

A person who uses a screen reader does not represent all blind people; a successful test by one person does not eliminate every criterion failure. Combine participation with standards-based evaluation. Keep personal disability information out of ordinary defect reports unless necessary and consented to.

## 23. Resolve defects and verify repairs

### Write a reproducible barrier report

Capture a user task, affected scope, environment, steps, expected behavior, actual barrier, impact, relevant criterion or convention, evidence, owner and retest condition. Describe what the person cannot do, not just the attribute that is missing.

```text
Task: Correct a delivery address after submission.
Environment: Tested build, browser, OS and screen-reader versions.
Steps: Submit with an empty postcode; navigate to the reported error.
Expected: The error identifies the postcode and provides a route to correction.
Actual: The summary says only 'Invalid'; the input has no associated error.
Impact: A nonvisual user cannot identify the problem or required correction.
Requirement: WCAG 3.3.1 and 3.3.2; assess 3.3.3 for a known correction.
Repair direction: Specific summary link plus persistent associated field error.
Retest: Repeat the failed submission, correction, resubmission and return path.
```

Use a screenshot, recording or accessibility-tree evidence when it helps, but include text steps. Attach no unnecessary personal, financial or authentication data.

### Prioritize by user impact and propagation

| Priority | Decision basis | Typical response |
| --- | --- | --- |
| Critical | Unsafe exposure, privacy loss, or complete blockage of an essential task without a usable alternative | Stop the affected release or operation as appropriate; provide effective assistance and fix urgently. |
| High | Significant task failure or severe effort for an affected group; widespread shared-component defect | Treat as a release blocker for the affected scope unless a formally accountable decision and effective interim route exist. |
| Medium | A task remains possible but has substantial confusion, avoidable effort or unreliable access | Schedule a near-term repair and prevent recurrence. |
| Low | Limited friction or a stronger convention beyond the baseline | Improve through planned refinement, while checking whether repeated instances compound. |

Priority is a product triage convention, not a legal severity scale or WCAG level. A Level A failure is not automatically more severe than every AA failure. Consider consequence, available alternatives, frequency, duration and propagation; a low-frequency barrier to a critical right can still be critical. Do not reduce priority because an affected group is small.

### Repair the cause and retest the task

Fix shared components, templates, content models or tokens when they cause repeated barriers. Then inspect affected consumers. A component-level patch can leave an incorrect accessible name or broken focus behavior in an assembled page.

Retest the original reproduction and the complete affected journey, including relevant neighboring states and support combinations. Check that the repair does not break pointer use, touch, other assistive technology or another theme. Add focused regression protection for behavior likely to recur, using automation where it can meaningfully detect the issue.

Keep “fixed,” “retested” and “verified in release” distinct. A code merge is not evidence that the deployed provider, document or content now works. Update user-facing limitations and internal records when the actual state changes.

Use an interim accessible route when a permanent repair cannot be immediate. It needs equivalent practical access, truthful availability, privacy and an owner; a callback next week may not substitute for today's deadline. Record and repair the underlying defect. An overlay or accessibility widget does not establish that the underlying service meets requirements.

## 24. Assign ownership and sustain access

### Give responsibilities to the people making decisions

| Role | Responsibility |
| --- | --- |
| Product/service owner | Scope, resources, acceptance criteria, release decisions, legal applicability coordination and remediation accountability. |
| Design | Task structure, visual requirements, interaction/focus contracts, adaptation and accessible design annotations. |
| Engineering | Semantics, input behavior, platform integration, state, automation and dependable implementation. |
| Content/media authors | Understandable information, structural authoring, alternatives, captions and maintained accessible outputs. |
| Research | Inclusive recruitment, accessible sessions and evidence about real task use. |
| QA/accessibility specialists | Test scope, criterion interpretation, assistive-technology evaluation, defect evidence and retesting. |
| Procurement/vendor owner | Contracted requirements, evidence, provider testing, remediation commitments and replacement options. |
| Support/operations | Accessible contact, timely accommodation, incident escalation, feedback and ongoing service monitoring. |
| Legal/compliance | Jurisdiction-specific interpretation, exemptions, statements, conformity documentation and regulator obligations. |

One person may hold several roles. An accessibility lead coordinates and advises; they cannot personally guarantee every design, content and code decision. Give each blocker an owner with authority to repair it.

### Buy and integrate with evidence

Before selecting a vendor, request evidence against the relevant standard, version, product version and configuration. An Accessibility Conformance Report, including one created with a Voluntary Product Accessibility Template (VPAT), is a disclosure, not an automatic independent certification. Read the exceptions, test dates, methods and actual scope.

Test a realistic proof of the provider's critical task before committing where possible. Include embedded frames, redirects, errors, mobile use, identity verification, authentication, payment, exported documents and support. Contract for accessible updates, remediation times, incident reporting, access to necessary evidence and an exit route if the provider cannot meet essential requirements.

Do not promise to repair a cross-origin widget through host-page ARIA. Identify what the team controls and what the supplier must change. Keep effective alternatives while escalating defects. Vendor ownership does not remove responsibility for the user's end-to-end service experience or settle legal exemptions.

### Sustain access through change

Include accessibility in discovery, design reviews, implementation, content publishing, release checks and production feedback. Retest after changes to shared controls, styling, routing, authentication, content templates, media pipelines or vendors. Review the support matrix as platform usage and behavior change.

Track meaningful evidence: unresolved blockers in critical journeys, defect age and recurrence, verified task coverage, supplier risks, user feedback resolution and completion of planned expert/user reviews. Use coverage denominators that name the scope. Avoid a single accessibility score that hides an untested login or a blocked payment.

Maintain an accessible feedback route outside likely failure points. Acknowledge reports, provide a usable route where possible, assign ownership and verify the resolution. Publish accurate accessibility information and review legal/standards assumptions at material changes. A statement is a living disclosure, not a promise that the product will remain unchanged.

## 25. Work through a complete service example

The following fictional booking journey illustrates how the requirements work together. It is a design and acceptance model, not a report of a tested application.

### Define the task and evidence

A consumer chooses a timed visit, enters contact details, pays through a provider and receives a ticket. Availability can change during payment. The journey needs a bounded reservation timer and must work on mobile and desktop. The organization separately assesses whether the EAA and relevant national rules apply.

Product acceptance covers discovery, selection, errors, timing, payment, return, confirmation, ticket and cancellation. The team selects WCAG 2.2 AA, generous target sizes, fully visible focus, reduced motion and persistent critical status as its baseline conventions. Its support matrix includes keyboard, representative desktop/mobile screen readers, zoom/large text and reduced-motion/forced-color checks.

### Specify the interactions

| Stage | Concrete design | Evidence required |
| --- | --- | --- |
| Find a visit | Descriptive title and heading, simple navigation, skip link, accessible search/filter form | Users can orient, bypass repetition and find a result without pointer hover. |
| Choose a time | Native radio choices labeled with date, time, price and availability; visible/programmatic selected state | Keyboard and nonvisual selection work; unavailable options explain their state; controls survive enlargement. |
| Enter details | Persistent labels, appropriate autocomplete, clear required status, reusable information and a helpful error summary | Users can submit invalid data, identify and correct each problem, and proceed without re-entering correct fields. |
| Reserve | Clear timer conditions and an appropriate warning/extension or documented applicable exception | The warning is perceived in time; an extension works through supported input methods; expiry preserves a usable recovery path. |
| Pay | Accessible provider integration with explicit outcome and return route | The whole provider process works; cancellation, declines, additional verification and network failures are tested. |
| Return | A persistent booking state distinguishes confirmed, pending, failed and expired | The system does not announce success before confirmation or invite a duplicate payment while uncertain. |
| Receive ticket | Accessible in-page record and email; accessible downloadable format if offered | Ticket reference, date, entry conditions and cancellation/support are independently usable. |
| Change/cancel | Clear consequences, review where appropriate and persistent outcome | Users can complete the later task with the same supported methods. |

A chart-like time grid can retain an expressive visual layout while presenting native radio groups in a meaningful sequence. For a large availability calendar, choose a documented calendar pattern or provide a simpler equivalent list. The fallback must preserve available times and the ability to book them.

### Walk through a failure

The user submits an incomplete address. The form retains all correct data, focuses a summary titled “There is a problem,” and lists a link reading “Enter your postcode.” Activating it reaches the named field. The field is marked invalid and describes the actual problem. After correction, stale error state is removed.

During payment, the provider times out. The service displays a persistent “Checking your payment” state while it reconciles the result. The person can leave and return through a safe route; they are not told to pay again until the system knows a second payment is appropriate. When the outcome is confirmed, the page title, heading and persistent message identify the booking. Focus and announcements follow the agreed route behavior without reading the whole ticket unexpectedly.

Testing this journey requires the actual provider states and outputs. A passing radio-group test and an accessible-looking confirmation screen cannot establish end-to-end access.

## 26. Use the WCAG 2.2 A/AA coverage index

This index contains all **55 Level A and AA criteria in WCAG 2.2**, organized for review. The summaries are working prompts; apply the full criterion, definitions, exceptions and conformance requirements to decide a pass. “Not applicable” needs evidence about the evaluated scope. The index excludes AAA and the obsolete 4.1.1 Parsing criterion.

### Perceivable

| Criterion | Level | Review prompt |
| --- | --- | --- |
| 1.1.1 Non-text Content | A | Does non-text information have an equivalent serving its purpose, with the correct treatment of decoration, controls, sensory content, tests and CAPTCHA? |
| 1.2.1 Audio-only and Video-only (Prerecorded) | A | Is the required equivalent available for prerecorded audio-only and video-only content, considering the labeled media-alternative exception? |
| 1.2.2 Captions (Prerecorded) | A | Are captions available for prerecorded audio in synchronized media, subject to the specified exception? |
| 1.2.3 Audio Description or Media Alternative (Prerecorded) | A | Is the required description or time-based-media alternative available for prerecorded synchronized video? |
| 1.2.4 Captions (Live) | AA | Are captions provided for live audio in synchronized media? |
| 1.2.5 Audio Description (Prerecorded) | AA | Is meaningful visual information in prerecorded synchronized video available through audio description? |
| 1.3.1 Info and Relationships | A | Are structure and relationships available programmatically or in text, including headings, labels, groups and tables? |
| 1.3.2 Meaningful Sequence | A | Is a sequence that affects meaning programmatically determinable? |
| 1.3.3 Sensory Characteristics | A | Can instructions be understood without relying only on shape, color, size, location, orientation or sound? |
| 1.3.4 Orientation | AA | Does content work in both orientations unless a particular orientation is essential? |
| 1.3.5 Identify Input Purpose | AA | Are covered personal-information input purposes programmatically identified in supported technologies? |
| 1.4.1 Use of Color | A | Is color supplemented when it conveys information, actions, responses or distinctions? |
| 1.4.2 Audio Control | A | Is automatically playing audio over three seconds stoppable/pausable or independently volume-controlled as required? |
| 1.4.3 Contrast (Minimum) | AA | Does text meet 4.5:1, or 3:1 for large text, with only applicable exceptions? |
| 1.4.4 Resize Text | AA | Can text reach 200% without loss, within the criterion's scope? |
| 1.4.5 Images of Text | AA | Is real text used when the presentation can be achieved with the technologies used, except where customizable or essential? |
| 1.4.10 Reflow | AA | Does content work at the specified 320 CSS-pixel width or 256 CSS-pixel height condition, with only scoped two-dimensional exceptions? |
| 1.4.11 Non-text Contrast | AA | Do the necessary identifying control/state visuals and meaningful graphic parts meet 3:1 against adjacent colors, subject to exceptions? |
| 1.4.12 Text Spacing | AA | Do the simultaneous applicable spacing overrides preserve content and functionality? |
| 1.4.13 Content on Hover or Focus | AA | Is applicable additional content dismissible, hoverable and persistent? |

### Operable

| Criterion | Level | Review prompt |
| --- | --- | --- |
| 2.1.1 Keyboard | A | Can functionality be operated through a keyboard interface without specific timing, except genuinely path-dependent underlying functions? |
| 2.1.2 No Keyboard Trap | A | Can users leave every keyboard-focusable region, with instructions where the method is nonstandard? |
| 2.1.4 Character Key Shortcuts | A | Can character-only shortcuts be turned off/remapped, or are they active only while the relevant component has focus? |
| 2.2.1 Timing Adjustable | A | Can content-set time limits be disabled, adjusted or extended under the prescribed conditions, unless an exception applies? |
| 2.2.2 Pause, Stop, Hide | A | Can applicable automatic movement and updates be controlled, with the separate timing conditions applied correctly? |
| 2.3.1 Three Flashes or Below Threshold | A | Is flashing absent, no more than three times per second, or below both applicable thresholds? |
| 2.4.1 Bypass Blocks | A | Is there a mechanism to bypass repeated blocks of content? |
| 2.4.2 Page Titled | A | Does the page title describe its topic or purpose? |
| 2.4.3 Focus Order | A | Does sequential focus preserve meaning and operability? |
| 2.4.4 Link Purpose (In Context) | A | Is each link's purpose determinable from its text and programmatically determined context, except genuine ambiguity to all users? |
| 2.4.5 Multiple Ways | AA | Are pages locatable through more than one method where required, except process steps/results? |
| 2.4.6 Headings and Labels | AA | Do headings and labels describe their topic or purpose? |
| 2.4.7 Focus Visible | AA | Does a keyboard-operable interface provide a mode with visible focus? |
| 2.4.11 Focus Not Obscured (Minimum) | AA | Is the newly focused component not entirely hidden by author-created content, under the criterion's conditions? |
| 2.5.1 Pointer Gestures | A | Do multipoint/path-based operations have a single-pointer alternative without a path requirement, unless essential? |
| 2.5.2 Pointer Cancellation | A | Do single-pointer functions satisfy the down-event, abort/undo, up-reversal or essential conditions? |
| 2.5.3 Label in Name | A | Does a text-labeled control's accessible name contain its visible label? |
| 2.5.4 Motion Actuation | A | Is device/user-motion functionality also operable through controls, and can motion response be disabled, except where permitted? |
| 2.5.7 Dragging Movements | AA | Is a single-pointer non-drag route available unless dragging is essential or the relevant unmodified user-agent exception applies? |
| 2.5.8 Target Size (Minimum) | AA | Are targets at least 24 × 24 CSS px or covered by the actual spacing/equivalent/inline/user-agent/essential exceptions? |

### Understandable

| Criterion | Level | Review prompt |
| --- | --- | --- |
| 3.1.1 Language of Page | A | Is the page's default human language programmatically determinable? |
| 3.1.2 Language of Parts | AA | Are passages/phrases in another language identified, subject to the stated exceptions for names, technical terms and similar cases? |
| 3.2.1 On Focus | A | Does receiving focus avoid causing a change of context? |
| 3.2.2 On Input | A | Does changing a setting avoid unexpected context changes unless the user is advised beforehand? |
| 3.2.3 Consistent Navigation | AA | Do repeated navigation mechanisms retain the same relative order unless the user initiates a change? |
| 3.2.4 Consistent Identification | AA | Are components with the same functionality identified consistently within the set of pages? |
| 3.2.6 Consistent Help | A | Do repeated qualifying help mechanisms keep the same relative order unless the user initiates a change? |
| 3.3.1 Error Identification | A | Are automatically detected input errors identified and described in text? |
| 3.3.2 Labels or Instructions | A | Are labels or instructions provided when input is required? |
| 3.3.3 Error Suggestion | AA | Are known correction suggestions provided unless they would jeopardize security or the purpose? |
| 3.3.4 Error Prevention (Legal, Financial, Data) | AA | Do covered consequential submissions provide reversibility, checking or confirmation as specified? |
| 3.3.7 Redundant Entry | A | Is same-process information populated or selectable when needed again, unless an exception applies? |
| 3.3.8 Accessible Authentication (Minimum) | AA | Is each authentication step free of an unsupported cognitive-function test, with the actual alternatives, assistance and recognition exceptions assessed? |

### Robust

| Criterion | Level | Review prompt |
| --- | --- | --- |
| 4.1.2 Name, Role, Value | A | Are component names/roles and applicable values, states, changes and user-settable properties exposed correctly? |
| 4.1.3 Status Messages | AA | Are qualifying status messages programmatically available for presentation without receiving focus? |

AA conformance also needs the whole-page, complete-process, accessibility-supported-use and non-interference requirements. The table cannot convert an untested state into a pass. Requirements from EN 301 549, applicable law, contracts or selected stronger product conventions remain separate checks.

## 27. Check delivery readiness

Use this as a release decision aid alongside the full evaluation evidence.

- **Scope:** The team has identified critical journeys, platforms, languages, roles, states, outputs and providers. Legal/contractual applicability and exact standards are recorded.
- **Perception:** Meaningful text, graphics, media and feedback have usable representations; actual contrast and applicable alternatives are verified across supported themes and states.
- **Adaptation:** Enlargement, reflow, spacing overrides, orientation and relevant system preferences preserve information and function.
- **Operation:** Keyboard, pointer and selected alternative-input routes work. Focus is visible and logically managed; gestures, dragging, layers and cancellation have the required behaviors.
- **Understanding:** Labels, instructions, navigation, errors, timing, authentication and recovery let people complete the task without unnecessary memory or inference.
- **Compatibility:** Semantics, relationships, values and changes are exposed and verified in the selected browser/platform/assistive-technology combinations.
- **Outputs and providers:** Media, emails, documents, exports, payment, identity verification and support have been evaluated as part of the service.
- **Evidence:** Automated and manual checks complement each other; user/expert evaluation is included at the appropriate risk level. Untested scope and remaining limitations are explicit.
- **Remediation:** No unresolved critical access barrier remains in the release scope. Other barriers have accountable decisions, effective interim arrangements where needed, and owners; this does not turn failing criteria into conformance.
- **Operations:** Required public information is accurate, feedback is accessible, supplier responsibilities are clear, and regression/review triggers are in place.

A release decision and a conformance claim are different records. If the evidence shows a failure, describe it accurately and repair it. If evidence is missing, state what remains unverified. Do not convert an intention, checklist, automated score, or planned audit into a claim that people can use the service.
