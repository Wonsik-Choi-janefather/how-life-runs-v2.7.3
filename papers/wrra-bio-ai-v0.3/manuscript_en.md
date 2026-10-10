# Structuring AI assisted biological research with WRRA execution contracts

Wonsik Choi and Jeongin Choi

Independent Researchers

Correspondence: Wonsik Choi, janefather@gmail.com



## Abstract

Biological output, internal regeneration and reliable continuation are distinct endpoints, yet an AI-assisted explanation can connect them without preserving the conditions required for that inference. We introduce WRRA execution contracts that represent source information, present state, material machinery, boundary exchanges, phenotype and observation in a traceable claim ledger. Literature reconstructions concern a minimal genome, reconstituted translation and computational transporter annotation. Constructed calculations then connect resource ownership, partition reliability and regeneration capacity. Identical active output can arise from external replacement or internal regeneration. With fair partition of nine units and an immediate competence threshold of two, the probability that both daughters are competent is 0.9609375. Requiring each daughter to restore nine units within a fixed horizon reduces joint success to 0.8203125 when internal production capacity is six units per daughter; seven units are minimally sufficient for the stated 95% target. A separate feasibility argument makes the minimum internal inventory conditional on permitted imports. These results do not establish whole-cell autonomy or indefinite lineage survival. A three-valued checker preserves unresolved requirements and distinguishes satisfaction of necessary checks from evidential sufficiency. The accompanying source ledger and exact computations are reproducible. The contribution is a unified representation of biological dependencies and their consequences for claim admissibility; improved language-model performance is not asserted. A comparative protocol specifies how the proposed AI workflow could be tested.

Keywords: theoretical biology; artificial intelligence; execution contract; minimal cells; cell-free systems; provenance

## 1 Introduction

Biology already has extensive structural methods. SBML supports exchange of biochemical reaction models [1], and whole-cell modelling links multiple processes in a computational representation [2]. FAIR principles address reusable scientific data [3], while PROV-O provides an interoperable vocabulary for provenance [4]. The starting problem of this paper is therefore not a lack of structure in biology. It is the need to preserve the conditions under which findings from different experimental and representational levels may be connected.

A biological research question often spans a sequence, its cellular context, a molecular apparatus, an environmental exchange and a measured endpoint. A statement about one component may be valid while a broader inference is unsupported. Growth with a reduced genome is not the same question as identification of every required molecular function. Protein production in a supplied translation system is a different endpoint from regeneration of that system. These distinctions are useful targets for an AI-assisted workflow because they can be represented as explicit requirements instead of being left implicit in a narrative.

We propose an execution-contract method derived from WRRA Core 1.0 and the biological applications collected in How Life Runs [5,6]. In these source documents, WRRA names the Wonsik Reality-Renderer Architecture. The Core retains minimum viable computation, a common carrier and the separation of internal state from expressed phenotype. We preserve that specification and introduce a domain profile for organizing biological evidence. No cosmological equation or particle-channel count is imported as a biological law.

The contribution is the composition of execution roles, resource ownership and claim-specific admissibility in a reproducible workflow. Provenance, conditional modelling and three-valued logic are not claimed as new discoveries. Nor is independent numerical prediction imposed as the only form of contribution: an explicit reconstruction of established findings can provide explanatory value. Empirical performance claims about AI require their own evidence. The present paper offers a formal method, bounded case demonstrations and an evaluation protocol rather than reporting an unperformed comparative AI trial.

The central worked consequence is a joint partition and restoration criterion. A component inventory can support reliable immediate daughter competence while remaining insufficient for both daughters to rebuild the parent inventory before the next division. Under fixed attainable regeneration capacity, the two objectives can diverge as candidate inventory increases. This model-bound result connects the execution contract to a finite biological continuation question and makes the additional measurements needed for application explicit.

## 2 Representation and scope

### 2.1 Biological execution contract

For a target claim, define a contract K = (S, L, X, H, E, B, C, F, Phi, M, Pi, T). S denotes source information and supplied starting materials; L denotes declared relations; X is the current biological state; H is a currently instantiated residue of prior events; E is material execution machinery; B specifies the boundary and permitted exchange; C identifies shared biological transport or execution infrastructure; F is the update rule; Phi maps an executed state to phenotype; M is the measurement map; Pi records provenance; T fixes the endpoint, time horizon and acceptance criterion. C is a structural annotation specifying machinery available to E and F; T is evaluation metadata rather than a dynamical variable. Components may be unknown, but unknown entries cannot be silently replaced by favourable values.

The biological description has the form X(t+1) = F(X(t), H(t), S(t), E(t), B(t); L), P(t) = Phi(X(t), E(t), B(t)), and Y(t) = M(P(t); Pi). These are slots for a domain-specific model, not a universal fitted equation. H may be included in X in an implementation; its separate label draws attention to the physical or recorded owner of a history effect. A source sequence, a phenotype and an assay result must retain separate identities even when their numerical representations coincide.

The full specification calls for each quantity to carry an owner, unit, time, condition identifier and evidence status. The partial reference implementation validates claim-level roles, conditions, locators and adjudication states; it does not implement a quantity-level type system or unit checker. A biochemical factor can be supplied initially, regenerated internally, imported later, inherited or unmeasured. These labels specify a boundary-dependent accounting relation, not a judgment that an externally supported biological system is illegitimate. All living systems exchange resources. An autonomy claim must state which exchanges are allowed and which machinery must be regenerated within the chosen boundary.

### 2.2 Two distinct meanings of execution

The biological renderer is a material mechanism such as translation machinery. The AI renderer is a software procedure that converts source material and a structured ledger into an explanation or report. A software knowledge graph is not evidence of a common physical carrier inside a cell. The biological field C must therefore name the actual shared machinery being represented, or remain OPEN. At the workflow level, one reusable schema carries differently typed claims without merging their biological owners. This implements a common information-processing scaffold but does not prove a new biological transport mechanism.

Minimum computation is operationalized relative to a declared contract: among a specified candidate family, retain the least costly representation or resource allocation satisfying the endpoint. Cost may be the number of required components, annotations or computation steps. The cost and candidate family must be stated before calling a solution minimal. This paper computes a component-count minimum in the partition example; it does not measure a reduction in language-model tokens or researcher effort.

### 2.3 Claim records

A claim record contains claim_id, target, system_boundary, condition_id, time_window, execution_roles, required_evidence, evidence_locators, provenance_status, outcome and unresolved_requirements. Evidence locators point to an identifiable passage, figure, table, dataset row or generated result. A citation to a whole paper is sufficient for a broad background statement but does not automatically support an unreported experimental detail. Original observations, modelling assumptions and derived quantities receive distinct labels.

The ledger supports four reporting positions in fixed order: verified input, WRRA transformation, output and falsification condition. A reconstructed literature result is labelled reconstruction. A new value from a frozen model is a conditional model prediction if its target has not been measured; a numerical fixture chosen by the analyst is a constructed demonstration. None of these labels is a synonym for empirical truth.

## 3 Adjudication and AI workflow

### 3.1 Three-valued requirements

For each necessary requirement j of a claim, an adjudicator assigns g_j in {true, false, unknown}. The claim receives FAIL if any requirement is false, OPEN if no requirement is false and at least one is unknown, and CHECKS_SATISFIED if every requirement is true. FAIL means failure of the specified contract. When a document omits an observation, its status is unknown rather than false. CHECKS_SATISFIED means only that the declared necessary checks are satisfied. A separate sufficiency argument is required for a conclusion about the target claim; the validator records that argument but cannot certify it. Evidence-supported report statements and exact model consequences retain their narrower labels.

The checker evaluates the logic of supplied adjudications. It cannot determine whether a quoted passage is authentic, whether a measurement is valid, or whether the chosen requirements are biologically sufficient. Those tasks require source inspection and subject-matter judgment. A completely populated ledger can still be wrong. The source-verification step is therefore distinct from schema validation.

For a finite list of necessary requirements this rule has a simple no-unsupported-promotion property: if at least one requirement remains unknown and none is false, the output cannot be CHECKS_SATISFIED. This property does not cover omitted requirements or incorrectly adjudicated true entries. This follows directly from the second branch of the rule. It is a property of the algorithm on its inputs, not a guarantee that an AI extractor correctly labels those inputs. Supplementary code enumerates all 3^4 = 81 assignments for a four-requirement contract. These are logic verification cases, not independent biological samples or an AI accuracy benchmark.

### 3.2 Operational workflow

First, freeze the question, boundary, target and comparison before extraction. Second, provide the AI with a versioned evidence packet and the contract schema. Third, have it propose records with exact source locators, explicit assumptions and null entries for missing information. Fourth, verify extracted facts against the sources and adjudicate the requirements. Fifth, execute the deterministic checks and any declared quantitative model. Finally, generate an explanation directly from the accepted ledger, including unresolved requirements and the observations that could resolve them.

The minimal prompt is: “For the stated claim and supplied evidence only, identify source, current state, material executor, boundary exchange, phenotype, observation and provenance. Attach a passage or data locator to each factual entry. Mark absent information unknown. State which necessary requirement each entry supports or contradicts. Do not promote observed output to a stronger autonomy, causal or lineage claim. Return the ledger before the narrative.” This is a proposed reusable prompt, not a report that a particular model was experimentally evaluated using it.

An auditor may revise an incorrect adjudication with a reason and a new version. The previous state remains in an accessible present record. Re-running the same normalized ledger and checker gives the same verdict; re-running an AI model is not assumed to reproduce identical extraction. Model identifier, prompt, evidence-packet version, generation settings, generated response and human changes must be retained in any future comparative experiment.

## 4 Case demonstrations

### 4.1 Minimal genome and mechanistic completeness

Verified input. Hutchison and colleagues reported JCVI-syn3.0 with 473 genes, including 149 whose biological functions were unknown at publication [7]. These are historical report-level facts, not a statement about the present annotation status of every gene.

WRRA transformation. The genome is assigned to SOURCE, the functioning cell to STATE and RENDERER, and the culture environment to BOUNDARY. Reported replication is an output. Complete identification of each required mechanism is a separate target with its own evidence requirements.

Output. The record supports the reported minimal-cell achievement while leaving a complete mechanistic account OPEN on that evidence packet. No claim is made that the original authors asserted complete understanding, and the example is not presented as detection of an error in their paper.

Falsification condition. If a ledger reports every function as established from this packet, or treats an unassigned function as proof that the cell cannot grow, the representation has failed. This case demonstrates preservation of two different claims, not discovery of new gene function.

### 4.2 Translation output and machinery regeneration

Verified input. Shimizu and colleagues reported a protein-synthesizing system reconstituted using purified components [8]. This establishes a literature anchor for distinguishing supplied machinery from the output it produces. We do not reanalyse the original assay or attribute the following values to that study.

WRRA transformation. Translation factors are assigned to material execution machinery; their origin is tracked separately from product formation. Consider a constructed active-machinery amount e(g), measured in arbitrary functional units, with e(g+1) = q e(g) + u(g) + r(g). q is the retained fraction after a transfer; u is external replacement and r is internal regeneration. The example treats all active units as equivalent and omits degradation beyond the retention factor.

Output. With e(0)=100, q=0.5 and u=r=0, the sequence is 100, 50, 25, 12.5, 6.25 and 3.125. External replacement u=50 with r=0 maintains 100; internal regeneration r=50 with u=0 also maintains 100. If the observable is proportional to e, the latter two mechanisms produce identical output while differing in resource ownership. Consequently, this observable alone does not identify internal regeneration. This is a constructive non-identifiability result under the specified model.

Falsification condition. The logical demonstration fails if the two declared updates do not yield identical output. Applying it quantitatively to a biological system would additionally require measurements of retention, activity, turnover and input origin. A claim of machinery autonomy remains OPEN until its allowed boundary supplies and internal replacement are established. Stable production alone does not resolve the demonstrated ambiguity.

### 4.3 Partition and reliable continuation

Verified input. This case uses explicitly chosen model assumptions, not measured cell counts. A parent has n identical essential units; each unit independently enters either daughter with probability 1/2. A daughter is called competent for this one component if it receives at least k units. Competence is not defined as full cellular viability.

WRRA transformation. The parent inventory is STATE, random partition is the UPDATE, a shared allocation rule is recorded as an abstract model scaffold while the biological carrier C remains OPEN, and the threshold maps a molecular allocation to the competence phenotype. The measurement records the number D of competent daughters. With A distributed as Binomial(n,1/2), D = 1[A >= k] + 1[n-A >= k]. Thus E[D] = 2 Pr(A >= k), whereas Pr(D=2) = sum over a from k to n-k of binomial(n,a) 2^(-n), with an empty sum equal to zero.

Output. For n=4 and k=2, Pr(D=0)=0, Pr(D=1)=0.625, Pr(D=2)=0.375 and E[D]=1.375. An average greater than one therefore coexists with a joint-success probability below one half. For the separate contract Pr(D=2) >= 0.95 and fixed k=2, the smallest n is 9: n=8 gives 0.9296875 and n=9 gives 0.9609375. For n>=4 the probability equals 1-2(1+n)/2^n and increases with n, which establishes minimality within this candidate family.

Falsification condition. Direct enumeration must agree with the formula, and probabilities must sum to one. Biological use requires independent tests of partition bias, dependence, localization, regeneration and the competence threshold. An expected first-generation daughter count exceeding one does not establish indefinite lineage survival. A multigeneration conclusion would require a specified offspring process and restoration of parental inventories. The minimality result concerns this declared partition model only.

### 4.4 Environmental support and the meaning of a minimal genome

Verified input. Antczak, Michaelis and Wass combined computational annotation methods to assign functions to 66 of the 149 previously unresolved proteins and proposed 24 additional likely transporters [9]. These are inferred annotations, not 66 newly established biochemical mechanisms. Their Figure 4 uses MMSYN1_0879 to illustrate an inferred magnesium-importing ATPase. Their discussion of MMSYN1_0138 notes that homology to an ABC-transporter ATP-binding region is weakened by lack of conservation at the ATP-binding site. These source statements motivate preserving both supporting and limiting evidence in the same execution record.

WRRA transformation. A transporter is represented as a candidate boundary executor, with proposed substrate, energy dependence and evidential status kept separate. A predicted transporter does not by itself establish substrate flux, and measured growth does not uniquely establish which import route supplied a necessary metabolite. The boundary record therefore specifies what is permitted to enter; a second requirement asks whether the proposed apparatus actually supplies the needed flux. For the two protein examples, the proposed functions remain hypotheses for mechanistic adjudication even though the source-level report of those predictions is supported. The extended source ledger keeps these two levels separate.

Output. We formalize the boundary dependence using a deliberately restricted feasibility model. Let G be a candidate internal inventory and B a set of allowed import profiles. For fixed initial state, dynamics, time horizon and phenotype target, define V(B) as the inventories G for which at least one profile b in B satisfies the target. If B1 is a subset of B2, every feasible witness under B1 remains allowed under B2, so V(B1) is a subset of V(B2). With a fixed nonnegative inventory cost c(G), the minimum cost over V(B2) cannot exceed the minimum over V(B1), provided both minima exist. For an infeasible set the minimum is left undefined and the boundary is labelled infeasible. This elementary inclusion argument establishes a conditional relationship, not a claim that adding any particular nutrient improves real growth. It assumes optional use of added profiles and unchanged physiological constraints; compulsory or toxic exposure need not satisfy it.

For a fully enumerated illustration, consider one required metabolite Q and a fixed maintenance horizon. The candidate synthesis module costs three abstract units and can supply one unit of Q; a transporter costs one abstract unit and can import one unit if Q is available. At least one unit must be supplied. The synthesis module is feasible in either environment; the transporter alone is feasible only where Q can be imported. The minimum internal cost is therefore three when import is unavailable and one when import is permitted. Costs and capacities are analyst-selected and are not gene counts or measurements of JCVI-syn3.0. The biological implication is the scope of the minimum: a reduced internal inventory can transfer a requirement to environmental supply and transport without removing the requirement from the combined system. The model does not rank the total environmental cost of the two solutions.

Falsification condition. Enumeration must recover the stated feasible sets and minima. A biological application fails if its inferred transport route does not deliver sufficient active flux over the declared horizon, or if the supposedly fixed background changes across environments. The generic checklist comparison remains relevant: the present result shows the consequence of explicitly retaining B, not an exclusive capability of WRRA. The added case turns a broad autonomy claim into concrete questions about imported substrates, transport activity and the cost boundary.

### 4.5 A joint contract for partition and restoration

Verified input. The following synthesis combines the declared partition assumptions of Section 4.3 with an explicit regeneration capacity. It introduces no measured cell parameters. A parent contains n active units of one required component. Each daughter must immediately inherit at least k units and must restore that component to n active units before its next division. A competent daughter can synthesize any integer amount from zero through R within the fixed horizon using permitted substrates. R is an attainable capacity, independent of inherited amount once competence is satisfied, rather than an unverified upper bound. External active machinery is excluded. Turnover, unequal substrates and competition for shared resources are omitted.

WRRA transformation. The inherited amount a is STATE, newly active units are assigned to internal regeneration, and the next-division target is recorded separately from immediate competence. A daughter meets the joint contract exactly when a >= k and a + R >= n. Thus its effective inherited threshold is h = max(k, n - R). With A distributed as Binomial(n, 1/2), both daughters meet the contract exactly when h <= A <= n - h. The joint probability is the sum of binomial(n,a) / 2^n over integer a from max(0,h) through min(n,n-h), with an empty sum equal to zero. This is a direct consequence of the stated capacity model, not a new law of cell division.

Output. For n=9 and k=2, partition competence alone gives 0.9609375. Requiring restoration changes the result: R=4 gives zero joint success, R=6 gives 0.8203125, and R=7 restores the 0.9609375 probability. At this fixed n, seven is the smallest per-daughter capacity reaching the 95% joint target. The necessary aggregate capacity condition 2R >= n is not sufficient for the probability target, because an uneven split places a larger restoration demand on one daughter. The calculation identifies a specific implication of the execution contract: a partition-level resource minimum must be accompanied by a regeneration-capacity requirement before it can support the next division. It does not establish restoration of the entire cellular state or indefinite lineage survival.

The contract also exposes a reversal across candidate inventories. At fixed R=4 and k=2, increasing n from eight to nine raises immediate two-daughter competence from 0.9296875 to 0.9609375, but lowers joint restoration probability from 0.2734375 to zero. For n=8, both daughters must inherit four units; for n=9, both would need at least five, which is impossible. More generally, n > 2R makes simultaneous restoration impossible because the daughters together need n newly synthesized units and can supply at most 2R. Thus increasing the inherited inventory and increasing reliable restoration are not interchangeable design objectives. This comparison keeps the target defined as restoration to each candidate parent's own inventory; it does not claim deterioration at a common fixed endpoint of eight units. The general counting argument is established mathematics; the contribution here is its explicit connection to the boundary and regeneration contract used to interpret biological continuation.

Falsification condition. Exact enumeration must match the formula. Biological application requires measuring inherited active amounts and the attainable production capacity conditional on that inherited amount, substrate availability and the time horizon. If capacity depends on a, the criterion becomes a + R(a,B,T) >= n for each daughter and the constant-R example no longer applies unchanged. If daughters compete for shared resources, the two marginal capacity claims must be replaced by a joint feasible allocation. The proposed ledger makes these distinctions explicit; no experimental estimate of R is supplied here.

[FIGURE1]

Figure 1. Partition competence and finite restoration are different endpoints. A: At n=9 and k=2, joint restoration reaches the 95% target when attainable capacity R is at least seven units per daughter. B: At R=4 and k=2, immediate competence rises with n while restoration to each candidate parent's own n becomes impossible above eight. All curves are exact results under the declared constructed model; no biological data are fitted. Panel B compares candidate-specific restoration targets, not a common fixed inventory endpoint.

## 5 Results and reproducibility

The reference implementation produces the full seven-row partition table for n=2 through 8, the n=9 contract solution and the three machinery histories. It verifies probability normalization and agreement between direct daughter enumeration and the marginal expectation. All 81 four-requirement assignments satisfy the specified verdict function. Six malformed gate inputs and seven malformed ledger mutations are rejected. These counts refer to implementation checks, not independent validation samples. The enumeration confirms implementation fidelity to a definition; its size is not presented as biological validation strength.

The literature cases are manually curated reconstructions from bounded source statements. The other results are calculations from declared assumptions. No wet-lab experiment, quantitative reanalysis of the cited datasets, blinded expert annotation or equal-budget LLM comparison was conducted for this manuscript. The code uses the Python standard library and is run with “python reproduce.py”; it writes results.json. Input choices are embedded next to their calculations to avoid hidden fitted parameters. The package also includes evidence_ledger.json and audit.py. Running “python audit.py” validates the curated records and writes audit_results.json. The extended packet adds two report-level records and two unresolved mechanistic records from [9]. Running “python boundary_model.py” enumerates the environmental-support example and writes boundary_results.json. Running “python integrated_model.py” compares the joint restoration formula with exhaustive allocation enumeration for ten capacities, verifies the fixed-capacity contrast, and writes integrated_results.json. build_ledgers.py regenerates the authored evidence packet. The packet also represents the boundary and joint-restoration results as C12–C14. Across the fourteen records, nine satisfy declared checks, one fails its contract and four remain OPEN. The records were selected to demonstrate the method, not to estimate diagnostic accuracy.

### 5.1 A complete trace from evidence to unresolved observation

Record C4 maps the publicly accessible abstract of [8], first sentence, to the narrow statement that reconstituted machinery produced protein. Its source locator supports that statement and the declared check is satisfied. C5 reuses this evidence but changes the target to regeneration of the machinery. Its ledger exposes three missing requirements: permitted boundary exchanges, newly synthesized functional machinery, and the persistence horizon. The validator returns OPEN with those requirements listed; it does not assign a biological failure. C6 then supplies an explicit model counterexample showing why equal active output cannot fill these gaps: only the sum u+r is identified by the recurrence at known q and e. Explicit parent_claim_ids and relation fields link these records in the machine-readable trace. The audit validates their references; scientific entailment still requires human judgment.

Resolving the ambiguity requires observations that separate the origins and retained activity of machinery components, a record of permitted boundary additions, and functional persistence over a declared finite transfer horizon. This is an evidence specification, not a claim that such measurements have been collected here. A whole-system regeneration claim would require the inventory of all necessary machinery, not merely one reporter. The scope of this trace remains the selected evidence packet; absent abstract detail is not evidence that the full research field lacks it.

### 5.2 Structural comparison and omission analysis

| Representation of the same case | Distinction it retains | Consequence of the stated omission |
| --- | --- | --- |
| Source and observed output only | What source reports the output | Does not represent whether machinery was supplied or rebuilt |
| Source plus component provenance | Origin of components | Without time and boundary fields, later replacement can remain ambiguous |
| Full declared contract | Origin, update, allowed exchange and target horizon | Represents why stable output cannot identify u versus r |
| Full contract without phenotype target | Inputs and update | Can confuse expected daughter count with probability of two competent daughters |

This is a logical comparison of specified representations, not a measured comparison of AI systems or a claim that existing provenance standards cannot express these distinctions. A generic checklist containing all the same fields may represent the same information. WRRA's contribution is the explicit reusable execution contract and its worked explanatory use; exclusive expressive power has not been established.

### 5.3 Three levels of failure

Implementation failure means disagreement with the declared logic or formula. Biological model failure means that measured partition, activity or resource-flow assumptions do not describe the target system. Workflow usefulness failure means that the extra structure provides no benefit relative to an equally informative alternative at comparable cost and coverage. These levels require different tests. The present code addresses the first; source reconstruction addresses a narrow evidential question; the remaining levels require further biological or comparative evidence.

## 6 Comparative evaluation protocol

To test practical value, a future study should compare four workflows using identical evidence packets and models: a free-form answer, a generic structured checklist with provenance, the full WRRA contract and a human-only reference workflow. The generic checklist is essential because improvement over free-form prompting would not isolate the contribution of WRRA. Component ablations should remove ownership, boundary or phenotype distinctions one at a time. These conditions are proposed and have not been run.

Use independent biology experts to define claim requirements and adjudicate cases before exposing reference labels to the AI workflow. Include fully supported, contradicted and underdetermined claims so that blanket abstention cannot appear successful. Split packets by study or biological system rather than fragments from the same paper. Evaluate extraction separately from deterministic adjudication. Also report incorrect CHECKS_SATISFIED results caused by extraction errors separately from unsupported target-claim assertions; these are different error levels. Primary outcomes should include unsupported target-claim assertions among unsupported claims and supported-claim coverage; secondary outcomes can include source-locator correctness, missing-condition detection and expert correction time. Report uncertainty clustered by source study, reviewer disagreement and all excluded packets. Budget comparisons must account for tokens, retrieval, human verification and wall time.

Superiority is not assumed. If a generic checklist matches the full method at equal cost, the practical case for the additional WRRA structure narrows. If WRRA increases abstention without reducing unsupported promotion at comparable coverage, its workflow needs revision. These criteria test a usefulness claim; they do not erase the separate value of the formal counterexample or the explicit reconstruction of known biology.

## 7 Discussion

The biological question addressed here is how component inventory, environmental support and regeneration constrain continuation across a division. The methodological question is whether an AI-assisted explanation preserves these conditions when connecting evidence from different levels. The contract makes several common transitions explicit: source to executed output, output to regenerated machinery, and average output to joint reliability. The examples show what the ledger is intended to preserve without claiming that these distinctions were absent from earlier biology.

WRRA can reference an SBML model for its update rules, FAIR metadata for dataset identification and PROV-O entities and activities for evidence history. Such links would be interoperability features. The present implementation does not import, validate or execute these formats, so it is not described as an integration with those systems. Its distinctive proposed contribution is the joint operational use of minimal sufficiency, shared execution infrastructure, phenotype mapping and boundary-dependent ownership in claim adjudication.

This paper has three important limits. First, necessary conditions chosen by an analyst may be incomplete, and a syntactically correct ledger cannot prove their sufficiency. Second, the source cases were selected to illustrate distinctions and do not estimate their prevalence in published research. Third, the prototype starts from adjudicated values; reliable automated extraction is still an empirical research question. A useful next implementation must preserve unresolved conditions rather than merely fill every schema field.

The method offers a concrete way to organize collaboration between an AI system and a biologist: the AI proposes traceable mappings, calculation supplies bounded consequences, and the researcher determines whether the evidence and biological contract are appropriate. Mechanistic understanding can improve through this process even when all reproduced values are already known. Any claimed advantage in speed, accuracy or new biological discovery must be supported separately.

## 8 Conclusion

WRRA execution contracts provide an explicit representation for AI-assisted biological explanation. Literature reconstruction and constructed calculations distinguish mechanistic completeness, machinery regeneration and reliable daughter competence from weaker observations. The joint partition and restoration calculation connects an inherited-inventory requirement to a finite regeneration-capacity requirement. The present results support a theoretical synthesis, a formal method and a reproducible prototype. Comparative workflow effectiveness and biological generalization remain open to the stated tests.

## Declarations

Funding. This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

Competing interests. The authors declare no competing interests.

Author contributions. Wonsik Choi: Conceptualization, Methodology, Formal analysis, Software, Writing – original draft, Writing – review and editing. Jeongin Choi: Conceptualization, Writing – review and editing. Both authors approved submission.

Declaration of generative AI and AI assisted technologies in the writing process. During preparation of this work, the authors used ChatGPT for drafting, source organization and assistance with code development, and a separate Astra medium model review for editorial feedback. These uses are disclosed as assistance, not independent peer review or experimental validation. The authors approved submission of this manuscript and take responsibility for its content.

Data availability. All newly computed examples are specified in the accompanying code and results. The cited biological observations belong to their original publications. No private biological dataset was used.

Prior dissemination. This methods profile develops concepts from WRRA Core 1.0 and How Life Runs, version 2.7.3. Those works are disclosed as antecedents, not presented as newly collected evidence. No journal acceptance or external peer review is implied by this manuscript.

## References

[1] Hucka M et al. The systems biology markup language SBML a medium for representation and exchange of biochemical network models. Bioinformatics. 2003;19:524–531. https://doi.org/10.1093/bioinformatics/btg015

[2] Karr JR et al. A whole-cell computational model predicts phenotype from genotype. Cell. 2012;150:389–401. https://doi.org/10.1016/j.cell.2012.05.044

[3] Wilkinson MD et al. The FAIR Guiding Principles for scientific data management and stewardship. Scientific Data. 2016;3:160018. https://doi.org/10.1038/sdata.2016.18

[4] Lebo T, Sahoo S, McGuinness D, editors. PROV-O The PROV Ontology. W3C Recommendation. 2013. https://www.w3.org/TR/prov-o/

[5] Choi W. WRRA Core 1.0 A Domain-Agnostic Execution Architecture for the Wonsik Reality-Renderer Architecture. Frozen specification. 7 September 2026. Author-provided reference document.

[6] Choi W, Choi J. How Life Runs. English edition, version 2.7.3. 2026. Author-provided book. Chapters 1–4 establish the execution vocabulary and its biological scope.

[7] Hutchison CA III et al. Design and synthesis of a minimal bacterial genome. Science. 2016;351:aad6253. https://doi.org/10.1126/science.aad6253

[8] Shimizu Y et al. Cell-free translation reconstituted with purified components. Nature Biotechnology. 2001;19:751–755. https://doi.org/10.1038/90802

[9] Antczak M, Michaelis M, Wass MN. Environmental conditions shape the nature of a minimal bacterial genome. Nature Communications. 2019;10:3100. https://doi.org/10.1038/s41467-019-10837-2
