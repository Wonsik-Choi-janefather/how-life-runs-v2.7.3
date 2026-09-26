# **Chapter 1**

From a Structure for Interpreting the Universe to a Framework for Life

> WRRA began with the author's intuition that 'the universe will operate under the principle of least computation.' After structuring this intuition into the SOURCE, LAW, STATE, RENDERER, and OBSERVABLE layers of the universe and complex systems, it was extended into biological research by testing whether the same separation grammar is valid in DNA and cells.

## What is WRRA?

At the starting point of WRRA lies the author’s intuition that “the universe will operate under the principle of minimum computation necessary to realize reality, rather than performing arbitrary and unnecessary additional calculations.” This idea was not presented from the outset as a proven law of nature, but rather as a starting hypothesis for research seeking to break down the complex phenomena of the universe into SOURCE, LAW, STATE, RENDERER, and OBSERVABLE. WRRA was created to transform this intuition into computable structures and falsifiable questions.

WRRA is an acronym for Wonsik Reality-Renderer Architecture. Its Korean name is 'Wonsik Reality Transformer Architecture'. The core of the name lies in the distinction between Reality and Renderer. Reality is not a copy in which the possibilities written in the source are unfolded exactly as they are, but rather the result of the current state changing according to the transitions permitted by the law, with a material renderer actually implementing one of those phenotypes. The data we obtain is not the entirety of that reality, but the observable that has passed through measurement devices and analysis rules.

This structure was not created from the outset as a theory exclusively for life sciences. It was a declarative toy architecture designed to avoid mixing "what was initially given," "what rules determine possible transitions," "what exists now," "what mechanism executes possibilities into reality," and "what the observer actually recorded" when interpreting the universe and complex systems. The research in this book tests whether that separation grammar is valid for DNA, protein synthesis, cell differentiation, minimal cells, and the first life.

> The official name is Wonsik Reality-Renderer Architecture (WRRA). WRRA is not a single equation that replaces completed fundamental physical theories or existing biology, but rather a structural architecture that breaks down and examines the process of possibilities being realized into observable reality layer by layer.

## Why Separate Reality from Renderer?

Even with identical DNA sequences, cells can exist in completely different states, such as neurons, muscle cells, and immune cells. Even the same cell produces different proteins and functions depending on nutrients, oxygen, temperature, drugs, the cell cycle, and past stimuli. Therefore, if we assume that we can directly predict reality by reading only the source, the intermediate chromatin accessibility, transcription and translation machinery, metabolism, membranes, space, and lineage all disappear. WRRA restores these missing intermediate layers using a renderer and a state.

Furthermore, reality and records are not the same. RNA-seq at a single point in time does not record every molecule, location, binding state, and past history within the cell. Observations are projections that have passed through detection limits, sample processing, and analysis models. The reason WRRA places OBSERVABLE as a separate layer is to avoid misinterpreting "not measured" as "does not exist," and conversely, to avoid immediately elevating observed correlations to internal causes.

## The Seven Layers of WRRA

| **floor**  | **General meaning**                                                     | **Response in biotechnology**                                                       |
|------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| SOURCE     | Input that starts a history                                             | DNA/RNA sequences, initial molecules, cell/intervention inputs                      |
| LAW        | Rules that allow or prohibit possible transitions                       | Binding, reaction rate, diffusion, replication, transcription and translation rules |
| STATE      | Current actual existing internal state                                  | chromatin, RNA, protein, metabolism, location, cell cycle                           |
| RENDERER   | A device that executes input into a material result                     | Polymerase, ribosome, enzyme, membrane, organelle, cell                             |
| BOUNDARY   | Conditions of exchange and partition                                    | Membrane, medium, temperature, nutrients, oxygen, tissue niche                      |
| OBSERVABLE | Limited output recorded by the experiment                               | Expression level, morphology, function, survival, growth rate, differentiation      |
| PROVENANCE | The lineage and measurement history from which the result was generated | barcode, parent-daughter relationship, placement, intervention, analysis pipeline   |

> The Boundary Between SOURCE and LAW : SOURCE is the input that initiates a history under LAW, while LAW is the rule that determines how that input can change into a certain state. For example, a DNA sequence is a SOURCE, but the rules for base pairing, transcription, translation, and catalysis are LAW. Culture medium, temperature, and nutrition are recorded in a broad input ledger, but for biological interpretation, they are separated into sub-ledgers under BOUNDARY/ENVIRONMENT.

## Minimal Mathematical Structure

The general state description of WRRA can be written as the following tuple. This notation is a common coordinate system for identifying what is known and what is missing in each biological study.

M_WRRA = (S, L, X_t, R, O, B, Π) (1)

X\_(t+Δt) = L_B(X_t ; S_t, E_t) + ξ_t (2)

P_t = R\_(L,B)(X_t, S_t) (3)

Y_t = O(P_t ; Π_t) + ε_t (4)

Here, S is SOURCE, L is LAW, X_t is the current STATE, R is RENDERER, P_t is the actual implemented phenotype, O is the observation operation, B is BOUNDARY, and Π_t is the pedigree/measurement history. ξ_t and ε_t represent the probabilistic/unobserved variation remaining in the state transition and measurement, respectively. It is important to note that Y_t is not X_t, and P_t is not a simple copy of SOURCE.

The more specific internal framework used in the cosmology model is written as source data Ξ, open or implementation channel Ω, interface profile b_Ω, attribute binding, and visible phenotype blocks. This format is summarized as the following block structure of a self-adjoint master operator.

V_Ω = g \|b_Ω\>\<Ω\| ⊗ I_attribute (5)

H_WRRA(Ξ,Ω) = \[\[M_phenotype(Ξ,Ω), V_Ω\], \[V_Ω†, D_continuum\]\] (6)

M_phenotype is a phenotype block implemented in the current visible region, D_continuum is a continuous state space that has not yet closed into a visible output, and V_Ω is an interface connecting the two regions. In biology, this is used as a structural analogy in which a specific sequence and initial state open up into an observable function through chromatin, transcription, translation, membrane, and metabolic machinery. Equations (5) and (6) are not equations claiming to be established fundamental laws of biology, but rather explicit skeletons of the original WRRA internal structure intended to avoid confusing different execution layers.

## The Three Stages: Actual, Reality, and Record

| **step** | **WRRA's question**                                                            | **Biology example**                                                          |
|----------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| ACTUAL   | What are the actually possible states and inputs immediately before execution? | DNA, open chromatin, number of molecules, energy, membrane state             |
| REALITY  | What the renderer actually implemented                                         | Transcription and translation, protein complex, metabolism, growth, division |
| RECORD   | What did the experiment and analysis record?                                   | reads, fluorescence, image, growth curve, barcode                            |

These three steps may coincide, but not always. Even if a protein is present, the antibody may not recognize it, and even if RNA is detected, the functional protein complex may not be assembled. Conversely, an unmeasured low-copy number molecule may determine the success of the cleavage. WRRA’s ownership ledger tracks where the information determining the result was located—whether in the SOURCE, STATE, RENDERER, BOUNDARY, or measurement process.

## From DNA to Protein: One WRRA Trace

For example, let's assume that a gene is edited to precisely change the bases. The edited DNA is a change in the source. However, if the target site is closed chromatin, transcription may not occur; even if RNA is synthesized, the degradation rate and RNA splicing may differ; and even if the protein is translated, folding, transport, and complex assembly may fail. Membranes and niches may also block functional expression. Finally, the experiment records only the selected marker and time window without directly observing the entire process.

Therefore, the success determination does not stop at 'sequence changed'. SOURCE change, STATE transition, RENDERER execution, phenotypic function, safety, and pedigree continuation must be verified in sequence. This structure is the reason why WRRA-Cell, PURE self-renewal, Syn3A distribution, protocell lineage, epigenetic memory, and write-erase-rewrite experiments are grouped into a single language.

## Where Do Interpretation and Prediction Diverge?

Interpretation is the process of reconstructing the structure that produced a result from existing or recorded results. It estimates the source, state, renderer, or boundary conditions using observation Y and provenance Π. Prediction is the process of presenting the distribution of future outputs that have not yet been observed, based solely on current information.

Interpretation: p(S, X_t, R \| Y_t, Π_t) (7)

Prediction: p(Y\_(t+Δt) \| S_t, X_t, L, B_t, Π_t) (8)

A fit that aligns the structure after seeing the correct answer is an interpretation, not an independent prediction. To be called a prediction, it requires a holdout that masks the target value, the prevention of leakage at the lineage, individual, and batch levels, and pre-fixed inputs and evaluation quantities. Even if WRRA's structural correspondence is established, unique biological values and future transitions remain open until such external verification.

> the failure closure principle requires missing sources, states, boundary conditions, or provenance, success is estimated and the missing elements are not filled. Mathematically closed relationships are marked EXACT, internal model reproductions are marked COMPUTATIONAL PASS, passing through direct data is marked EMPIRICAL PASS, and if necessary data is unavailable, it is marked OPEN.

## WRRA Translated into Biology

Life is not defined by a single substance called DNA. The source must be replicated, read into RNA and protein under the law, the renderer maintains metabolism and membranes, and essential components are transferred to daughter cells during division to reconstruct the same execution capabilities in the next generation. Therefore, the life boundary of WRRA is described as a combination of information closure, execution closure, metabolic closure, boundary closure, and lineage closure.

When applied to the earliest life forms, SOURCE consists of replicable RNA-like information macromolecules; LAW consists of base pairs, catalysts, diffusion, and membrane binding rules; STATE consists of RNA, short peptides, lipids, and energy carriers; RENDERER consists of fatty acid vesicles, coacervates, and environmental cycles; and OBSERVABLE consists of growth, division, daughter compartment functions, and lineage survival. In modern cells, DNA, ribosomes, enzymes, membranes, organelles, and regulatory networks occupy the same sites in a more complex manner.

> What WRRA does in this book is not limited to renaming the discoveries of existing biology. It separates the inputs, executors, observations, and lineages of each claim, calculates whether the ownership of success lies within the system or in an external supply, and determines what data is required to allow stronger claims of life, memory, and prediction.

## Established Scientific Starting Point

Modern biology has precisely decomposed the components and interactions of life through molecular biology, systems biology, and synthetic biology. However, the problem of recording who determines what—genetic information, current state, implementers, environment, and observed phenotype—within a single grammar is scattered across discipline-specific languages.

## WRRA Reconstruction

WRRA does not replace existing biology. It relocates values already measured by different studies into the ownership ledger of sources and execution conditions. If this relocation is valid, the same structures must be repeated in DNA, minimal cells, epigenetic memory, the nervous system, and the earliest life forms.

## Comparative Reading

The first reason for applying WRRA to biology was not that DNA resembled the source of the universe. What is important is that in any system, explanation ceases if stored potential is confused with actual realization. Reading DNA does not mean one knows all the quantities and functions of proteins, nor does knowing the connectivity map mean one knows all their behavior. This recurring gap was the starting point for biological application.

Existing disciplines are already addressing this gap by field. Gene regulation connects sequence and expression, biochemistry connects proteins and reactions, cell biology connects reactions and boundaries, and embryology connects states and fates. The role of WRRA is to place these achievements on a single ownership map, enabling the successes and failures of different fields to be compared within the same sentence.

> The boundary between interpretation and prediction . The conclusion of this chapter is structural transplantability. It is not that biological truth has been newly proven, but rather that a common grammar has been established that separates what is information, what is practice, and what is observation.

## Research Content and Validation Results

## Research Objectives and Scope of Integration

This paper does not simply splice together separate biological research notes. Instead, it aligns the different closure boundaries addressed in previous studies into a single vertical structure. DNA represents the information closure, transcription and translation the execution closure, metabolism, membranes, and division the cell closure, daughter cell distribution the lineage closure, and primitive chemistry the closure of primordial life. WRRA-Cell and WRRA-Worm are extensions that test whether this structure can also be applied to cellular state transitions and the sense-behavior loop.

| **Scope of Research: This integrated version is not an experimental guideline for manufacturing life, but a computational study that examines the conditions under which genetic information is converted into an executable state of life using public data, synthetic data, and theoretical formulas.** |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Research series** | **Target**                        | **Role in this integrated version**                                         | **Current judgment**                                    |
|---------------------|-----------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------|
| Life Model II       | DNA → Protein                     | Coding lower bound, executor dependency, bootstrap, process                 | Formula EXACT / Autonomy OPEN                           |
| Life Model I        | Minimal modern cells              | Five gates, autocatalyst, Syn3A loading                                     | PASS                                                    |
| Life Model III      | daughter cells and lineages       | Partition noise, R_life, extinction, equalization, covariance               | Mathematical Closed / Empirical Open                    |
| Life Model 0        | First life                        | Chemistry → Living System Boundary                                          | Structural Inference / History OPEN                     |
| WRRA-Cell 0.1–0.4   | Cell state/distancing             | Residual Model and K562 Perturb-seq Audit                                   | Partially unconfirmed                                   |
| WRRA-Worm 0.1       | Neuro-behavioral loop             | Multicellular expansion of current state, relationships, and boundaries     | Internal Inspection PASS / Biological Verification OPEN |
| Life Model V        | Stratified epigenetic memory      | Generational attenuation, inter-floor transmission, and multiple eigenmodes | Differential Prediction / Empirical OPEN                |
| Life Model VI       | Cell fate order effect            | G–T–W Six Permutations and Non-commutativity                                | Experimental Design CLOSED / Results OPEN               |
| Life Model VII      | Aging · CH · Cancer               | Decomposition of Induced State and Clone Selection                          | Literature Contact / Causal Verification OPEN           |
| Life Model VIII     | Memory editing                    | Write-Erase-Rewrite Reversible Structure                                    | Technically Available / Iterative Verification OPEN     |
| Life Model IX       | Distributed organizational memory | Cell × niche crossover and interaction                                      | Structural Proposal / Demonstration OPEN                |
| Life Model X        | Minimum life closure              | The combination of memory–execution–recovery–boundary–selection             | Formalization / History OPEN                            |

Table 2. Integration Targets and Evidence Locations.

## Next Step

All subsequent chapters test whether this common grammar survives in actual calculations and public data.

### DOIs for This Chapter

> DOI 10.5281/zenodo.22289266 · Life form model interpreted by WRRA
>
> One sentence from this chapter: WRRA is a structural architecture that starts from the author's intuition that the universe operates under the principle of least computation, separates the layers of reality realization, and extends its grammar to the life sciences.

**WRRA BIOLOGY**
