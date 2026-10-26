# Agent translation: human creativity techniques that can improve AI-generated ideas

**Research brief**\
**Evidence searched:** 27 October 2026\
**Question:** Which human creativity techniques improve AI-generated ideas when adapted as explicit agent steps, tools, or changes in representation?

## Executive summary

The best-supported answer is to translate creativity techniques into **workflow structure**, not just add an instruction to “be creative.” LLMs often generate plausible, useful ideas, but repeated outputs can cluster around familiar concepts. Techniques that create separate search paths, vary the starting conditions, and delay evaluation have the clearest support. Results are strongest when a technique changes the agent’s actual search or the representation it works over.

The evidence supports five practical choices, with different levels of confidence:

1. **Separate divergent generation from selection.** First generate candidate ideas without judging them; then deduplicate, score novelty and usefulness separately, and select a portfolio. A direct LLM experiment found that a brainstorm-then-select sequence improved Alternate Uses Task performance over brainstorming alone (Summers-Stay et al., 2023). This is task-specific evidence rather than proof that one universal two-stage prompt will improve every kind of idea.
2. **Vary task-relevant starting points.** Generate across a structured set of distinct user needs, ordinary personas, functions, constraints, and domains. Recent experiments with product ideas report that heterogeneous personas and functional constraints improved response-set diversity; unrelated text injection was weaker. Varying prompts is therefore more defensible than merely increasing temperature or requesting “more original” ideas.
3. **Use analogy as a relational mapping operation.** Retrieve or generate source domains, identify the source’s underlying relation or function, map it to the target, and produce several adaptations. Do not merely show the model a striking example and ask it to imitate it. Human–AI analogy work finds useful changes to problem formulations, but also identifies potentially harmful suggestions and limits to generalization.
4. **Change the representation before generating.** Move from a surface brief or exemplar to functions, needs, users, constraints, causal relations, or a parameter-by-option matrix. This is a promising transfer hypothesis from human design methods, while visual generative AI can itself induce fixation. However, one large CHI experiment found that a theory-based LLM problem-reframing workflow did not improve human-rated frame quality (Shin et al., 2025). Representation changes need testing against the target task rather than being assumed to help.
5. **Make divergence measurable.** Ask for ideas that occupy different solution categories, then measure pairwise similarity, category coverage, novelty, feasibility, and usefulness. Keep multiple candidates and a diverse shortlist instead of collapsing immediately to one “best” answer. Direct prompting and training interventions have increased semantic diversity on creative-generation benchmarks, but gains depend on the model, task, and metric (Deshpande et al., 2025; Zhao et al., 2025).

The most practical agent pattern is a **portfolio workflow**: understand the need; represent it in several different ways; create varied search lanes; generate independently within each lane; map analogies and recombinations; cluster and remove duplicates; score each candidate on novelty and usefulness; then return a diverse shortlist with rationale and unresolved assumptions. Treat this as a deployable hypothesis, not a universally validated recipe. Direct intervention studies remain concentrated in short text ideation, product concepts, and benchmark tasks. Evidence is weaker for long-horizon scientific discovery, visual design, complex professional work, and the quality of ideas after implementation.

The evidence has three levels. **Direct intervention evidence** tests a change to an LLM prompt, model, or workflow, such as brainstorm-then-select, task-relevant personas and constraints, or breadth-first co-creation. **Human–AI interaction evidence** tests what happens when people receive or use model outputs, including the risk of fixation and the benefit of ChatGPT for some everyday creative tasks. **Transfer evidence** comes from human creativity methods or theory—analogy, morphological analysis, incubation, and constraint design—and supports a plausible agent operation without proving that the operation improves LLM outputs. The recommendations below keep these levels separate because a method can make sense cognitively and still fail when implemented through a language model.

| Technique | Agent implementation | Evidence for the translation | Confidence and main limit |
|---|---|---|---|
| Divergent then convergent phases | Candidate bank first; scoring and selection in a later pass | Direct LLM Alternate Uses experiment; human process precedent | Promising; tested on a bounded task |
| Heterogeneous starting points | Lane matrix of user contexts, needs, and functional constraints | Direct product-idea interventions and broad-vs-narrow task studies | Strongest practical signal; domain and prompt dependent |
| Analogical transfer | Retrieve source, map relations, adapt, list what fails to transfer | Human–AI analogy studies and analogy benchmarks | Promising but early; suggestions can mislead or anchor |
| Representation change | Need/function/parameter frames; matrix of options | Human methods plus a direct LLM reframing null result | Hypothesis only; do not assume structured reframing helps |
| Constraints | Separate batches under one varied constraint each | Human meta-analysis plus direct LLM constraint experiments | Useful when task-relevant; more restriction is not always better |
| Role and strategy prompts | Relevant perspective sampler with explicit changed context | LLM creativity benchmarks and co-creation studies | Effects vary; a role label alone is not an intervention |

This ranking reflects directness and consistency, not a universal effect-size comparison. Studies use different tasks, models, outcomes, and protocols, so comparing their reported scores numerically would be misleading. “Strongest practical signal” means that the method has direct empirical support relevant to the proposed agent behavior, not that it has been replicated widely across current models.

## Scope and interpretation

“Improve AI-generated ideas” can mean higher average quality, more useful ideas, more original ideas, a wider set of distinct ideas, better ideas after human selection, or better human–AI collaboration. These outcomes can move in different directions. The report treats **idea quality** as a candidate’s novelty and usefulness, and **set diversity** as how broadly a candidate set covers distinct concepts or solution paths. An intervention that improves one idea’s ratings may still reduce the diversity of a whole pool.

“Agent translation” means converting a creativity method into one or more of: (a) a named step with an input and output, (b) a tool or operation such as clustering, retrieval, a constraint sampler, or a rubric, or (c) a changed representation of the problem or ideas. Evidence is strongest when studies actually test an LLM prompt or workflow. Where recommendations come from human creativity or design research, they are marked as **transfer hypotheses**.

## How the evidence was gathered

I searched on 27 October 2026. The OpenAlex API request failed at DNS resolution. A direct OpenAlex website URL was not accessible through the available search tool, so I did not treat ordinary web results that point to OpenAlex as an OpenAlex search. Instead, I used web search for scholarly discovery and inspected primary publisher, conference, repository, or author-hosted records for central claims. Representative search strings included “large language model creativity idea generation techniques prompt methods,” “LLM creativity structured ideation techniques divergent thinking experiment,” “LLM creative idea generation problem reframing representation change,” “analogical reasoning large language models design ideation,” and “human creativity techniques brainstorming constraints idea generation meta-analysis.” I followed references from central papers and checked counterevidence.

The repository’s default journal screen was applied where a cited source is a journal article: Article Influence at least 2.5 **or** influence percentile at least 80, using the supplied snapshot in `disciplines/research-literature/references/journals.csv`. Eligible journal sources used here include *Nature Human Behaviour*, *Science Advances*, *Technovation*, *Journal of Organizational Behavior*, *Wiley Interdisciplinary Reviews: Cognitive Science*, *Proceedings of the National Academy of Sciences of the United States of America*, and *Machine Intelligence Research*. Conference papers, preprints, and books were assessed separately and were not filtered by journal metrics. The supplied CSV has no metric year or percentile derivation, and the preset is a venue screen rather than an assessment of any individual article.

This is a narrative synthesis, not a systematic review. The search tool did not provide a reproducible OpenAlex query or result count; therefore, no claim of exhaustive coverage is made. Full texts were inspected where accessible for central claims. The primary product-idea intervention paper was consulted in its SSRN working-paper form (last revised August 2026); its later journal version appeared in a venue below the repository’s default cutoff, so the SSRN record is cited as a preprint and its findings should be read with that status in mind. Some sources were available only as abstracts or publisher summaries; those are used for discovery and bounded claims, not detailed methodological judgments.

## Findings

### 1. Generate first, evaluate later

**What the technique does.** Classic divergent–convergent models separate producing possibilities from choosing among them. For an agent, this should be a hard workflow boundary: during generation, it records candidates and postpones ranking; during selection, it applies explicit criteria to the stored pool.

**Direct LLM evidence.** Summers-Stay, Lukin, and Voss tested a two-stage “Brainstorm, then Select” prompt on the Alternate Uses Task. The sequence improved the model’s creativity score over brainstorming alone. This is a direct, task-specific result, reported in a preprint record rather than a broad field trial. Zhao et al.’s benchmark study also found that prompt and role-play conditions can change performance, while highlighting originality as a relative weakness and elaboration as a relative strength. These findings support staged prompting, but do not establish that one universal two-stage prompt will improve every kind of idea.

**Caution.** The lesson for agents is not “generate as much as possible.” It is to separate search and selection, and make the selector’s criteria visible and testable. If the agent is asked to invent and judge in one pass, early plausible ideas can anchor the rest of its search. A diversity-preserving training study also shows that optimization can distort the target: common diversity metrics favored shorter outputs, so the authors controlled for length while improving diversity (Deshpande et al., 2025).

**Agent translation.** Store a candidate bank before ranking. Require each generation lane to return a fixed number of ideas and a short description of the mechanism or need addressed. In a later pass, cluster duplicates, rate novelty and usefulness independently, check feasibility, and select a *portfolio* that spans clusters. Preserve low-confidence outliers for human review rather than discarding every candidate that looks unusual.

### 2. Deliberately diversify starting conditions

**What the technique does.** Human ideation methods often use different people, prompts, constraints, and points of view to reduce local search. An agent can implement this as a controlled set of alternative “lenses,” not as a vague persona role-play.

**Direct LLM evidence.** A multi-study product-idea working paper compared interventions intended to reduce LLM idea homogeneity. Heterogeneous ordinary personas and functional constraints improved diversity; structured chain-of-thought instructions also improved diversity, while unrelated sonnet stimuli produced smaller gains (Terwiesch et al., 2026). Its tests suggest that the *kind* of heterogeneity matters: a persona or constraint can steer generation toward a different semantic region, whereas arbitrary randomness may not. A separate study of task breadth found that fine-tuned LLM stimuli increased exploration breadth for broad tasks but not narrow tasks (Sorin & Pagani, 2026), suggesting task scope moderates the effect.

**Agent translation.** Build a small “search-lane” matrix before generating. For a product brief, lanes might vary (1) user situation, (2) underlying job, (3) operating constraint, (4) setting or channel, and (5) business or social model. Give every lane a distinct seed and ask for solutions that satisfy the same core need. Use ordinary, task-relevant personas or constraints; avoid random fictional identities unless there is a reason they change the problem. Generate in separate calls or isolated contexts if context leakage makes all lanes converge, but then deduplicate and compare the outputs. Existing evidence does not show that independent calls alone increase diversity: some studies instead find that repeated outputs from one model can provide stronger collective yield than one idea per independent session.

**Why a diversity metric matters.** In studies of AI-assisted stories and brainstorming, AI access can improve the average individual output while increasing similarity across outputs (Doshi & Hauser, 2024; Lee & Chung, 2024; Meincke et al., 2025). This is a collective trade-off. Evaluate both individual quality and the portfolio: concept coverage, pairwise semantic similarity, and cluster count, alongside human judgments of novelty and usefulness. Embedding distance is a diagnostic, not a substitute for human judgment; distant ideas can be irrelevant or incoherent.

### 3. Use analogies to transfer structure, not surface features

**What the technique does.** Analogy compares relations in a source domain to relations in the target. A useful agent operation is therefore: find a source that solves a structurally similar problem; extract what it does and how its parts relate; map that structure to the target; note what does not transfer; and generate several adaptations.

**Evidence.** Work on scalable analogical innovation argues that crowds and computational systems can help retrieve cross-domain examples and overcome fixation, while also identifying challenges in finding and applying deep structural matches (Kittur & Yu, 2019; Yu & Kittur, 2014). Ding et al. (2023) studied LLM-generated cross-domain analogies across three studies. People often rated them helpful for problem reformulation, and many led to observable changes in problem framing; a minority were potentially harmful, most often because of upsetting content. At the cognitive level, Gentner and Forbus (2011) describe relational structure mapping as central to analogy; that theory helps define the agent operation but is not itself a test of LLM ideation quality. Separate benchmark work suggests that current LLMs can solve some analogy tasks (Webb et al., 2023), which establishes a capability premise rather than proof of creative benefit.

**Caution.** An analogy can become a highly salient exemplar and anchor the agent—or a human user—on its visible features. A visual ideation experiment found that participants using AI-generated images showed higher fixation and lower fluency, variety, and originality than controls (Wadinambiarachchi et al., 2024). It also described “fixation displacement”: the user may leave the original example only to become fixed on the model’s output. Analogy is therefore better used as a **structured transformation** than as a gallery of polished examples.

**Agent translation.** Use an analogy tool that returns (a) the source domain, (b) the shared function or relation, (c) a mapping table, (d) a breakage/assumption note, and (e) at least three target-specific adaptations. Generate analogies from multiple source domains and do not expose users to one highly polished visual solution before they have explored the problem. Ask the agent to abstract before adapting: “What function is performed? What relationship makes it work? Which parts are incidental?”

### 4. Change the representation to loosen fixation

**What the technique does.** A short natural-language brief often bundles a need, a proposed solution, and an example. Creative work can improve when the problem is represented in a form that makes alternatives easier to see: user needs, functions, constraints, causal relations, process steps, or combinations of parameters and values.

**Transfer hypothesis.** Morphological analysis offers a concrete representation change: list important parameters, enumerate plausible values, and explore combinations (Zwicky, 1969). A tool can externalize this as a table or graph and ask the agent to generate solutions from combinations not already present in the brief. This is a human-origin method; its adaptation to language models needs controlled testing. Relevant representation studies in engineering design were screened out because their journals fall below the repository’s default threshold.

**Important counterevidence.** Shin et al.’s CHI 2025 experiment compared free-form, direct-generation, and a theory-informed structured LLM approach for problem reframing with 280 participants. It found no improvement in the quality of problem frames from LLM use; the intervention widened the gap between experienced and inexperienced designers, and inexperienced users reported lower agency. Thus, “ask the model to reframe the problem” is not a reliably helpful step on its own. A representation change may work better when it exposes concrete task structure and keeps the human in control, but that is a design hypothesis, not a settled result.

**Agent translation.** Add a “brief decomposition” operation before idea generation. Extract the beneficiary, desired outcome, current workaround, constraints, measurable success conditions, and assumptions. Then create three parallel representations: (1) function-based (“what must happen?”), (2) need-based (“for whom, in what situation?”), and (3) parameter-based (“which components can vary?”). Have the user confirm or edit these frames when stakes are material. A morphological matrix or constraint graph can then generate combinations, but apply compatibility checks so the output is not a list of impossible Cartesian products.

### 5. Use constraints as search directions, not as a pile of restrictions

Constraints can focus effort and trigger recombination, but their effect depends on kind, timing, and task. A meta-analysis of 111 published and unpublished studies found an overall positive relationship between constraints and creative performance, with meaningful moderators; it does not justify the rule that more constraints are always better (Damadzic et al., 2022). The LLM product-idea experiments likewise found functional constraints more effective than some unrelated stimuli (Terwiesch et al., 2026), while an LLM-supported design study found that narrow tasks did not show the exploration benefit seen with broad tasks (Sorin & Pagani, 2026).

**Agent translation.** Ask the agent to generate separate batches under different *single* constraints—no electricity, repairable with common tools, deployable in ten minutes, accessible offline, or useful to a different user group—then include an unconstrained batch. This makes the causal role of each constraint inspectable and avoids overconstraining every idea at once. Have the evaluator verify that a candidate respects its assigned constraint and still meets the core need. Treat the constraint set as a sampling plan, not as mandatory conditions that every final idea must satisfy. Morphological analysis (Zwicky, 1969) provides a paper-and-pencil precedent for systematically exploring parameter combinations; Osborn’s applied-imagination method (1953) and Wallas’s account of preparation, incubation, illumination, and verification (1926) are historical process models, not direct evidence that agent implementations work.

### 6. Treat role prompts as perspective samplers, not magic expertise

“Act as a famous entrepreneur” or “be extremely creative” may change style without creating a meaningful new search path. A benchmark of LLM creativity found prompts and role-play can alter outcomes, but prompt effects vary by model and task (Zhao et al., 2025). Evidence from the direct diversity experiments favors a set of distinct, ordinary personas over one prestigious “creative expert” persona (Terwiesch et al., 2026). A broader survey catalogs many prompt techniques but does not establish that all are effective for creative ideation (Schulhoff et al., 2024). A co-creation prototype found that breadth-first generation was perceived as more creative and trustworthy after the task, while depth-first generation was perceived as more creative during the task (Liu et al., 2023). These findings support explicit perspective variation, not the claim that simulated expertise reliably improves originality.

**Agent translation.** Prefer a controlled perspective prompt with a concrete information difference: “Generate for a night-shift nurse with limited storage,” not “think like a genius.” Ask the model to state which user need or constraint changed. Keep persona attributes relevant, avoid demographic stereotyping, and compare each persona’s idea set against a no-persona baseline. Personas should expose alternative needs rather than stand in for lived expertise.

### 7. Ask for semantic distance, then check whether it is useful

The Divergent Association Task asks for concepts that are semantically far apart. Recent LLM studies show that explicit task instructions, prompt variation, and role-play can change measured creative performance, although effects vary by model and task (Zhao et al., 2025). A response-diversity intervention also cautions that the metric itself can reward brevity unless length is controlled (Deshpande et al., 2025). This supports concrete strategies that alter associative search, but results should not be overgeneralized from benchmark tasks to product or scientific ideation.

**Agent translation.** For ideas, ask for different mechanisms, user groups, contexts, or resource models rather than different wording. Track diversity through category coverage and pairwise similarity. Then apply a usefulness/feasibility screen. A semantic-distance maximizer can return remote but irrelevant ideas; divergence and convergence remain separate jobs.

## Recommended agent workflow

The following combines the most directly supported interventions and the most defensible transfer hypotheses. It is suitable as a starting point for an agent prototype, not as a validated universal procedure.

1. **Parse the brief.** Extract need, beneficiary, context, success criteria, constraints, examples, and assumptions. Do not treat a proposed solution embedded in the brief as a requirement unless it is explicitly fixed.
2. **Create representations.** Produce need-based, function-based, and parameter-based versions of the problem. Mark uncertain interpretations. Ask for human correction when the target or constraints are ambiguous.
3. **Define search lanes.** Select several task-relevant lanes, such as user situation, function, constraint, analogy domain, and delivery model. Ensure that lanes differ in a named way.
4. **Generate without ranking.** Generate a fixed number per lane. Avoid evaluating each idea immediately. Store candidates with lane, mechanism, beneficiary, and constraint tags.
5. **Run transformations.** Use analogical mapping, parameter recombination, and “different mechanism for the same need” prompts to extend promising regions. Do not merely paraphrase or embellish candidates.
6. **Deduplicate and measure coverage.** Cluster near-duplicates, retain one representative per cluster, and identify unoccupied regions in the lane matrix. Use embedding similarity as a screening signal, then inspect borderline cases semantically.
7. **Select a portfolio.** Rate novelty, usefulness, feasibility, and evidence/assumption burden separately. Select a small set that balances quality and coverage rather than only the highest-scoring cluster.
8. **Return provenance.** For each selected idea, show the need, transformation or lane that produced it, key assumptions, and what would need validation. Include a few distinct alternatives and invite the user to steer another generation pass.

### Compact prompt scaffold

```text
Goal: [need and beneficiary]
Fixed constraints: [must-haves]
Open variables: [dimensions that may change]

First, represent the problem in three ways: user need, required function, and
variable parameters. Keep these frames distinct and mark uncertain assumptions.

Then generate [N] ideas in each of these lanes: [lane list]. Do not rank ideas
yet. Each idea must state its target user, mechanism, and the lane that produced it.
Make ideas differ in mechanism or context, not just wording. Include at least one
analogy lane: identify a structurally relevant source, map its relation to this
problem, state what does not transfer, and adapt the structure into multiple ideas.

After generation, cluster duplicates and report which parts of the solution space
the pool covers or misses. Score novelty, usefulness, feasibility, and key
assumptions separately. Return a diverse shortlist and retain high-novelty
outliers with unresolved feasibility questions. Do not claim that a semantic
distance score proves creativity.
```

## Evidence strength and open questions

The strongest intervention evidence currently concerns relatively bounded tasks, including Alternate Uses, short stories, product concepts, research-question co-creation, and design challenges. It supports measurable changes to quantity, judged quality, semantic diversity, or fixation under specified experimental conditions. It does **not** establish that these techniques improve all creative work, that more ideas always improve outcomes, or that LLM process emulation is equivalent to human creativity.

Several design implications remain unproven. The combined workflow above has not been tested as one package. We do not know whether morphological matrices or analogy maps consistently improve modern agent performance across domains. More output can raise the chance of finding a strong idea, but can also raise review cost and duplicate volume. Similarity metrics can miss distinct ideas expressed in similar language and overrate incoherent outliers. Prompt and model versions change, and the relevant experiments span different systems and sampling settings. Human outcomes also depend on expertise: some AI support helps novices while structured reframing may widen the skill gap.

The practical standard should therefore be an intervention test, not a creativity claim: compare the proposed agent procedure with a direct-prompt baseline on the same tasks, keep model and sampling settings constant, and have blinded reviewers rate novelty and usefulness. Measure diversity at the set level, track feasibility and task compliance, and report which groups of users benefit. A method should be retained only when it improves the intended outcome without unacceptable losses on the others.

### A test plan for an agent implementation

The literature does not validate the full workflow above, so a team adopting it should evaluate the specific translation before treating it as a capability. The comparison can be small and still informative if it isolates the intervention.

**Conditions.** Use the same base model, task brief, output budget, and decoding settings across at least three conditions: (A) direct prompting; (B) staged generation followed by a selector; and (C) staged generation plus one additional intervention, such as distinct task-relevant personas or functional constraints. Add analogy or representation changes as separate conditions rather than bundling all changes in one treatment. This reveals which step produced any observed gain. For an interactive product, test the human-in-the-loop interface separately from raw model output; users may accept, discard, or transform ideas differently from evaluators.

**Tasks and sampling.** Include several tasks that vary in breadth and domain, since task breadth and creative domain affect measured performance. For example, include one broad open-ended challenge, one constrained product or service challenge, and one domain with a clear user need and feasibility criteria. Run multiple samples per condition, because the same model and prompt can produce materially different results. Preserve prompts, model identifier/version, parameters, candidate counts, and all unfiltered generations.

**Measures.** Have multiple reviewers, blind to condition, rate each idea’s novelty and usefulness independently with a shared rubric. Include feasibility or constraint compliance where relevant. For the pool, report duplicate rate, semantic similarity, number and size of clusters, and coverage across pre-defined need/function/constraint categories. Use both machine measures and human judgment. Report candidate-level quality before selection, the quality and diversity of the selected shortlist, and reviewer effort. Otherwise a selector may appear to improve the final set by silently discarding most candidates or transferring substantial work to a person.

**Decision rule.** Keep an intervention only if it improves its intended outcome against the direct-prompt baseline and does not create a material loss on another outcome. If the goal is a shortlist, higher top-idea quality may be the primary outcome, with minimum diversity and feasibility guardrails. If the goal is an innovation portfolio, breadth and non-redundancy should be primary. Pre-specify the desired trade-off. If ratings disagree or the test is too small to distinguish a meaningful effect, retain the result as uncertain rather than claiming that the agent is more creative.

This test plan is a practical extension of the evidence, not an outside validation of the recommendations in this report. A true external check would require an independent replication or a held-out evaluation run; none was conducted here. The strongest challenge to the synthesis is the null result in structured problem reframing (Shin et al., 2025), which shows that formal steps can fail to improve outcomes and may affect users unevenly. Accordingly, all transfer hypotheses should be opt-in or measurable in the target agent, not described as settled best practice.

## Conclusion

Translate creativity techniques into explicit operations that change where the agent searches and how it represents the problem. Start with staged generation and selection, task-relevant variation across lanes, and analogy that transfers relations rather than surface features. Add function- or parameter-based representations and structured constraints as testable extensions. Evaluate the whole pool for both quality and diversity, and keep a human in charge of problem framing and final selection. Avoid treating role labels, arbitrary randomness, polished examples, or “be creative” instructions as reliable interventions by themselves.

## References

### Direct LLM and human–AI ideation evidence

1. **Ding, Z., Srinivasan, A., MacNeil, S., & Chan, J. (2023).** Fluid transformers and creative analogies: Exploring large language models’ capacity for augmenting cross-domain analogical creativity. In *Proceedings of Creativity and Cognition 2023*. https://doi.org/10.1145/3591196.3593516.
2. **Doshi, A. R., & Hauser, O. P. (2024).** Generative AI enhances individual creativity but reduces the collective diversity of novel content. *Science Advances, 10*(28), eadn5290. https://doi.org/10.1126/sciadv.adn5290.
3. **Lee, B. C., & Chung, J. (2024).** An empirical investigation of the impact of ChatGPT on creativity. *Nature Human Behaviour, 8*(10), 1906–1914. https://doi.org/10.1038/s41562-024-01953-1.
4. **Liu, Y., et al. (2023).** CoQuest: Exploring research question co-creation with an LLM-based agent. arXiv preprint. https://arxiv.org/abs/2310.06155.
5. **Meincke, L., Nave, G., & Terwiesch, C. (2025).** ChatGPT decreases idea diversity in brainstorming. *Nature Human Behaviour, 9*, 1107–1109. https://doi.org/10.1038/s41562-025-02173-x.
6. **Schulhoff, S., et al. (2024).** The Prompt Report: A systematic survey of prompting techniques. arXiv preprint. https://arxiv.org/abs/2406.06608.
7. **Shin, J., Polyanskaya, A., Lucero, A., & Oulasvirta, A. (2025).** No evidence for LLMs being useful in problem reframing. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3706598.3713273.
8. **Summers-Stay, D., Lukin, S., & Voss, C. (2023).** Brainstorm, then select: A generative language model improves its creativity score. OpenReview manuscript. https://openreview.net/forum?id=8HwKaJ1wvl.
9. **Terwiesch, C., Meincke, L., Girotra, K., Mollick, E. R., Nave, G., & Ulrich, K. T. (2026).** AI and its impact on creativity and diversity: An empirical study of LLM-generated product ideas. SSRN working paper, last revised August 2026. https://doi.org/10.2139/ssrn.4526071. (A later journal version appeared in *Production and Operations Management*, below the supplied default journal screen; this reference is the non-journal working-paper version.)
10. **Wadinambiarachchi, S., Kelly, R. M., Pareek, S., Zhou, Q., & Velloso, E. (2024).** The effects of generative AI on design fixation and divergent thinking. In *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*, Article 380. https://doi.org/10.1145/3613904.3642919.
11. **Zhao, Y., Zhang, R., Li, W., et al. (2025).** Assessing and understanding creativity in large language models. *Machine Intelligence Research, 22*, 417–436. https://doi.org/10.1007/s11633-025-1546-4.
12. **Sorin, N., & Pagani, M. (2026).** The role of task breadth and cognitive flexibility in generative AI-supported creative idea generation. *Technovation, 153*, 103540. https://doi.org/10.1016/j.technovation.2026.103540.
13. **Deshpande, V., Ghose, D., Patterson, J. D., Beaty, R. E., & Rumshisky, A. (2025).** Diverse, not short: A length-controlled data selection strategy for improving response diversity of language models. In *Proceedings of EMNLP 2025*, 33917–33938. https://doi.org/10.18653/v1/2025.emnlp-main.1721.
14. **Webb, T. W., Holyoak, K. J., & Lu, H. (2023).** Large-scale AI language systems display an emergent ability to reason by analogy. *Nature Human Behaviour, 7*, 1426–1427. https://doi.org/10.1038/s41562-023-01671-0.

### Human creativity and design methods used for transfer hypotheses

15. **Damadzic, A., et al. (2022).** [Re]thinking outside the box: A meta-analysis of constraints and creative performance. *Journal of Organizational Behavior*. https://doi.org/10.1002/job.2655.
16. **Gentner, D., & Forbus, K. D. (2011).** Computational models of analogy. *Wiley Interdisciplinary Reviews: Cognitive Science, 2*(3), 266–276. https://doi.org/10.1002/wcs.105.
17. **Kittur, A., & Yu, L. (2019).** Scaling up analogical innovation with crowds and AI. *Proceedings of the National Academy of Sciences, 116*(6), 1870–1877. https://doi.org/10.1073/pnas.1807185116.
18. **Linsey, J. S., & Becker, B. (2011).** Effectiveness of brainwriting techniques: Comparing nominal groups to real teams. In *Design Creativity 2010* (pp. 165–171). https://doi.org/10.1007/978-0-85729-224-7_22.
19. **Osborn, A. F. (1953).** *Applied imagination: Principles and procedures of creative problem-solving*. Scribner.
20. **Wallas, G. (1926).** *The art of thought*. Jonathan Cape.
21. **Yu, L., & Kittur, A. (2014).** Distributed analogical innovation: Leveraging online communities to generate novel solutions. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/2556288.2557172.
22. **Zwicky, F. (1969).** *Discovery, invention, research through the morphological approach*. Macmillan.

### Methods and context

OpenAlex API and website searching could not be completed: the API request failed at DNS resolution and the website query endpoint was inaccessible to the available search tool. Ordinary web discovery and primary-source inspection were used as a bounded fallback. The journal eligibility snapshot and cutoff method are documented in `disciplines/research-literature/references/journals.csv` and `disciplines/research-literature/references/journal-selection.md` in the repository.

**Objective checks:** word count passed (5,254); source inventory passed (22); all identified journal articles passed the default eligibility screen. Article-link reachability is **unverified** because the environment could not resolve the DOI URLs; this does not establish that any cited link is broken. Overall status: **NOT PASSED — UNVERIFIED**. These checks validate length, inventory count, journal screening, and link reachability only; they do not validate the accuracy of the synthesis.
