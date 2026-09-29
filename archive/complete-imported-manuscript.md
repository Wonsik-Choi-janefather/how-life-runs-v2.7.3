# Complete Imported Manuscript

## WRRA BIOLOGY & BIOTECHNOLOGY

### How Life Runs

Rereading DNA, Proteins, Epigenetic Memory,\
Cell Differentiation, Minimal Cells, and the First Life through WRRA

Wonsik Choi · Jeongin Choi

janefather@gmail.com

English Edition · 2026

## About This Book

WRRA began with the author’s intuition that the universe might operate under a principle of least computation. The name abbreviates Wonsik Reality-Renderer Architecture. First proposed as a declarative toy architecture for interpreting the universe, it became a biological research framework when the same separation of POSSIBILITY, LAW, STATE, RENDERER, and OBSERVABLE was tested in living systems. Chapter 1 independently introduces the name, its origin, its internal equations, and its biological correspondences.

This book reconstructs a series of WRRA-based biological studies as a single narrative. Its first axis runs from DNA sequence through protein execution, minimal cells, daughter-cell partitioning, synthetic protocells, and the first life. Its second axis runs from epigenetic memory through cell differentiation, aging, cancer, spatial niches, and causal editing.

This revised edition strengthens the molecular execution layer connecting those two axes. It integrates DNA replication and repair, transcription and RNA processing, post-translational protein quality control, prokaryotic and eukaryotic gene regulation, natural CRISPR-Cas immunity, membrane transport, and energy coupling into the existing chapters. These mechanisms are not claimed as original WRRA discoveries; they are used as established biological routes by which SOURCE becomes function and lineage. The edition also adds WRRA-Motor H2 as a case study and provides a reproducible procedure for using WRRA Core 1.0 from Zenodo as a reference document in AI-assisted research.

Established science is the starting point of this book. The central dogma, cell-free translation, minimal genomes, whole-cell models, lineage tracing, epigenome editing, and protocell research are presented first; what WRRA newly rearranges or calculates is then identified separately. Restatements of prior work, original WRRA claims, and untested predictions are therefore not conflated.

Every chapter follows the same contract. Reconstructing an observed structure is classified as INTERPRETATION. A conditional distribution for a future transition not fixed by present information is classified as PREDICTION. Mathematically closed relations are marked EXACT; success inside a model is marked COMPUTATIONAL PASS; and claims lacking sufficient direct evidence remain OPEN. This discipline supports strong claims when warranted and requires withdrawal when they fail.

Core proposition: DNA is not life itself; it is SOURCE. Life is the recurrent process by which SOURCE passes through LAW and STATE and is materially rendered as proteins, metabolism, membranes, division, and lineage.

## Part I: How WRRA Views Life

By separating possibility, law, present state, and material execution machinery, WRRA rereads life as an executable architecture.

## Chapter 1: From a Structure for Interpreting the Universe to a Framework for Life

WRRA began with the author's intuition that “the universe will operate under the principle of least computation.” After structuring this intuition into the SOURCE, LAW, STATE, RENDERER, and OBSERVABLE layers of the universe and complex systems, it was extended into biological research by testing whether the same separation grammar is valid in DNA and cells.

### What Is WRRA?

At the starting point of WRRA lies the author’s intuition that “the universe will operate under the principle of minimum computation necessary to realize reality, rather than performing arbitrary and unnecessary additional calculations.” This idea was not presented from the outset as a proven law of nature, but rather as a starting hypothesis for research seeking to break down the complex phenomena of the universe into SOURCE, LAW, STATE, RENDERER, and OBSERVABLE. WRRA was created to transform this intuition into computable structures and falsifiable questions.

WRRA is an acronym for Wonsik Reality-Renderer Architecture. Its Korean name is “Wonsik Reality Transformer Architecture.” The core of the name lies in the distinction between Reality and Renderer. Reality is not a copy in which the possibilities written in the source are unfolded exactly as they are, but rather the result of the current state changing according to the transitions permitted by the law, with a material renderer actually implementing one of those phenotypes. The data we obtain is not the entirety of that reality, but the observable that has passed through measurement devices and analysis rules.

This structure was not created from the outset as a theory exclusively for life sciences. It was a declarative toy architecture designed to avoid mixing “what was initially given,” “what rules determine possible transitions,” “what exists now,” “what mechanism executes possibilities into reality,” and “what the observer actually recorded” when interpreting the universe and complex systems. The research in this book tests whether that separation grammar is valid for DNA, protein synthesis, cell differentiation, minimal cells, and the first life.

The official name is Wonsik Reality-Renderer Architecture (WRRA). WRRA is not a single equation that replaces completed fundamental physical theories or existing biology, but rather a structural architecture that breaks down and examines the process of possibilities being realized into observable reality layer by layer.

### Why Separate Reality from Renderer?

Even with identical DNA sequences, cells can exist in completely different states, such as neurons, muscle cells, and immune cells. Even the same cell produces different proteins and functions depending on nutrients, oxygen, temperature, drugs, the cell cycle, and past stimuli. Therefore, if we assume that we can directly predict reality by reading only the source, the intermediate chromatin accessibility, transcription and translation machinery, metabolism, membranes, space, and lineage all disappear. WRRA restores these missing intermediate layers using a renderer and a state.

Furthermore, reality and records are not the same. RNA-seq at a single point in time does not record every molecule, location, binding state, and past history within the cell. Observations are projections that have passed through detection limits, sample processing, and analysis models. The reason WRRA places OBSERVABLE as a separate layer is to avoid misinterpreting “not measured” as “does not exist,” and conversely, to avoid immediately elevating observed correlations to internal causes.

### The Seven Layers of WRRA

| floor      | General meaning                                                         | Response in biotechnology                                                           |
| ---------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| SOURCE     | Input that starts a history                                             | DNA/RNA sequences, initial molecules, cell/intervention inputs                      |
| LAW        | Rules that allow or prohibit possible transitions                       | Binding, reaction rate, diffusion, replication, transcription and translation rules |
| STATE      | Current actual existing internal state                                  | Chromatin, RNA, protein, metabolism, location, cell cycle                           |
| RENDERER   | A device that executes input into a material result                     | Polymerase, ribosome, enzyme, membrane, organelle, cell                             |
| BOUNDARY   | Conditions of exchange and partition                                    | Membrane, medium, temperature, nutrients, oxygen, tissue niche                      |
| OBSERVABLE | Limited output recorded by the experiment                               | Expression level, morphology, function, survival, growth rate, differentiation      |
| PROVENANCE | The lineage and measurement history from which the result was generated | Barcode, parent-daughter relationship, placement, intervention, analysis pipeline   |

**The boundary between SOURCE and LAW:** SOURCE is the input that initiates a history under LAW, while LAW is the rule that determines how that input can change into a certain state. For example, a DNA sequence is a SOURCE, but the rules for base pairing, transcription, translation, and catalysis are LAW. Culture medium, temperature, and nutrition are recorded in a broad input ledger, but for biological interpretation, they are separated into sub-ledgers under BOUNDARY/ENVIRONMENT.

### Minimal Mathematical Structure

The general state description of WRRA can be written as the following tuple. This notation is a common coordinate system for identifying what is known and what is missing in each biological study.

$$
M_{\text{WRRA}} = (S, L, X_t, R, O, B, \Pi)
\tag{1}
$$

$$
X_{(t+\Delta t)} = L_B(X_t ; S_t, E_t) + \xi_t
\tag{2}
$$

$$
P_t = R_{(L,B)}(X_t, S_t)
\tag{3}
$$

$$
Y_t = O(P_t ; \Pi_t) + \varepsilon_t
\tag{4}
$$

Here, S is SOURCE, L is LAW, X\_t is the current STATE, R is RENDERER, P\_t is the actual implemented phenotype, O is the observation operation, B is BOUNDARY, and Π\_t is the pedigree/measurement history. ξ\_t and ε\_t represent the probabilistic/unobserved variation remaining in the state transition and measurement, respectively. It is important to note that Y\_t is not X\_t, and P\_t is not a simple copy of SOURCE.

The more specific internal framework used in the cosmology model is written as source data Ξ, open or implementation channel Ω, interface profile b\_Ω, attribute binding, and visible phenotype blocks. This format is summarized as the following block structure of a self-adjoint master operator.

$$
V_\Omega = g |b_\Omega\rangle\langle\Omega| \otimes I_{\text{attribute}}
\tag{5}
$$

$$
H_{\text{WRRA}}(\Xi,\Omega) =
\begin{bmatrix}
M_{\text{phenotype}}(\Xi,\Omega) & V_\Omega \\
V_\Omega^\dagger & D_{\text{continuum}}
\end{bmatrix}
\tag{6}
$$

M\_phenotype is a phenotype block implemented in the current visible region, D\_continuum is a continuous state space that has not yet closed into a visible output, and V\_Ω is an interface connecting the two regions. In biology, this is used as a structural analogy in which a specific sequence and initial state open up into an observable function through chromatin, transcription, translation, membrane, and metabolic machinery. Equations (5) and (6) are not equations claiming to be established fundamental laws of biology, but rather explicit skeletons of the original WRRA internal structure intended to avoid confusing different execution layers.

### The Three Stages: Actual, Reality, and Record

| Step    | WRRA's question                                                                | Biology example                                                              |
| ------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| ACTUAL  | What are the actually possible states and inputs immediately before execution? | DNA, open chromatin, number of molecules, energy, membrane state             |
| REALITY | What the renderer actually implemented                                         | Transcription and translation, protein complex, metabolism, growth, division |
| RECORD  | What did the experiment and analysis record?                                   | Reads, fluorescence, image, growth curve, barcode                            |

These three steps may coincide, but not always. Even if a protein is present, the antibody may not recognize it, and even if RNA is detected, the functional protein complex may not be assembled. Conversely, an unmeasured low-copy-number molecule may determine the success of the cleavage. WRRA’s ownership ledger tracks where the information determining the result was located—whether in the SOURCE, STATE, RENDERER, BOUNDARY, or measurement process.

### From DNA to Protein: One WRRA Trace

For example, assume that a gene is edited to precisely change the bases. The edited DNA is a change in the source. However, if the target site is closed chromatin, transcription may not occur; even if RNA is synthesized, the degradation rate and RNA splicing may differ; and even if the protein is translated, folding, transport, and complex assembly may fail. Membranes and niches may also block functional expression. Finally, the experiment records only the selected marker and time window without directly observing the entire process.

Therefore, the success determination does not stop at “sequence changed.” SOURCE change, STATE transition, RENDERER execution, phenotypic function, safety, and pedigree continuation must be verified in sequence. This structure is the reason why WRRA-Cell, PURE self-renewal, Syn3A distribution, protocell lineage, epigenetic memory, and write-erase-rewrite experiments are grouped into a single language.

### Where Do Interpretation and Prediction Diverge?

Interpretation is the process of reconstructing the structure that produced a result from existing or recorded results. It estimates the source, state, renderer, or boundary conditions using observation Y and provenance Π. Prediction is the process of presenting the distribution of future outputs that have not yet been observed, based solely on current information.

$$
\text{Interpretation: } p(S, X_t, R \mid Y_t, \Pi_t)
\tag{7}
$$

$$
\text{Prediction: } p(Y_{(t+\Delta t)} \mid S_t, X_t, L, B_t, \Pi_t)
\tag{8}
$$

A fit that aligns the structure after seeing the correct answer is an interpretation, not an independent prediction. To be called a prediction, it requires a holdout that masks the target value, the prevention of leakage at the lineage, individual, and batch levels, and pre-fixed inputs and evaluation quantities. Even if WRRA's structural correspondence is established, unique biological values and future transitions remain open until such external verification.

The failure closure principle requires missing sources, states, boundary conditions, or provenance to remain missing; success is estimated and the missing elements are not filled. Mathematically closed relationships are marked EXACT, internal model reproductions are marked COMPUTATIONAL PASS, passing through direct data is marked EMPIRICAL PASS, and if necessary data is unavailable, it is marked OPEN.

### WRRA Translated into Biology

Life is not defined by a single substance called DNA. The source must be replicated, read into RNA and protein under the law, the renderer maintains metabolism and membranes, and essential components are transferred to daughter cells during division to reconstruct the same execution capabilities in the next generation. Therefore, the life boundary of WRRA is described as a combination of information closure, execution closure, metabolic closure, boundary closure, and lineage closure.

When applied to the earliest life forms, SOURCE consists of replicable RNA-like information macromolecules; LAW consists of base pairs, catalysts, diffusion, and membrane binding rules; STATE consists of RNA, short peptides, lipids, and energy carriers; RENDERER consists of fatty acid vesicles, coacervates, and environmental cycles; and OBSERVABLE consists of growth, division, daughter compartment functions, and lineage survival. In modern cells, DNA, ribosomes, enzymes, membranes, organelles, and regulatory networks occupy the same sites in a more complex manner.

What WRRA does in this book is not limited to renaming the discoveries of existing biology. It separates the inputs, executors, observations, and lineages of each claim, calculates whether the ownership of success lies within the system or in an external supply, and determines what data is required to allow stronger claims of life, memory, and prediction.

### Established Scientific Starting Point

Modern biology has precisely decomposed the components and interactions of life through molecular biology, systems biology, and synthetic biology. However, the problem of recording who determines what—genetic information, current state, implementers, environment, and observed phenotype—within a single grammar is scattered across discipline-specific languages.

### WRRA Reconstruction

WRRA does not replace existing biology. It relocates values already measured by different studies into the ownership ledger of sources and execution conditions. If this relocation is valid, the same structures must be repeated in DNA, minimal cells, epigenetic memory, the nervous system, and the earliest life forms.

### Comparative Reading

The first reason for applying WRRA to biology was not that DNA resembled the source of the universe. What is important is that in any system, explanation ceases if stored potential is confused with actual realization. Reading DNA does not mean one knows all the quantities and functions of proteins, nor does knowing the connectivity map mean one knows all their behavior. This recurring gap was the starting point for biological application.

Existing disciplines are already addressing this gap by field. Gene regulation connects sequence and expression, biochemistry connects proteins and reactions, cell biology connects reactions and boundaries, and embryology connects states and fates. The role of WRRA is to place these achievements on a single ownership map, enabling the successes and failures of different fields to be compared within the same sentence.

**The boundary between interpretation and prediction:** The conclusion of this chapter is structural transplantability. It is not that biological truth has been newly proven, but rather that a common grammar has been established that separates what is information, what is practice, and what is observation.

### Research Content and Validation Results

#### Research Objectives and Scope of Integration

This paper does not simply splice together separate biological research notes. Instead, it aligns the different closure boundaries addressed in previous studies into a single vertical structure. DNA represents the information closure, transcription and translation the execution closure, metabolism, membranes, and division the cell closure, daughter cell distribution the lineage closure, and primitive chemistry the closure of primordial life. WRRA-Cell and WRRA-Worm are extensions that test whether this structure can also be applied to cellular state transitions and the sense-behavior loop.

{% hint style="info" %}
**Scope of Research:** This integrated version is not an experimental guideline for manufacturing life, but a computational study that examines the conditions under which genetic information is converted into an executable state of life using public data, synthetic data, and theoretical formulas.
{% endhint %}

| Research series   | Target                            | Role in this integrated version                                             | Current judgment                                        |
| ----------------- | --------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------- |
| Life Model II     | DNA → Protein                     | Coding lower bound, executor dependency, bootstrap, process                 | Formula EXACT / Autonomy OPEN                           |
| Life Model I      | Minimal modern cells              | Five gates, autocatalyst, Syn3A loading                                     | PASS                                                    |
| Life Model III    | Daughter cells and lineages       | Partition noise, R\_life, extinction, equalization, covariance              | Mathematical Closed / Empirical Open                    |
| Life Model 0      | First life                        | Chemistry → Living System Boundary                                          | Structural Inference / History OPEN                     |
| WRRA-Cell 0.1–0.4 | Cell state/distancing             | Residual Model and K562 Perturb-seq Audit                                   | Partially unconfirmed                                   |
| WRRA-Worm 0.1     | Neuro-behavioral loop             | Multicellular expansion of current state, relationships, and boundaries     | Internal Inspection PASS / Biological Verification OPEN |
| Life Model V      | Stratified epigenetic memory      | Generational attenuation, inter-floor transmission, and multiple eigenmodes | Differential Prediction / Empirical OPEN                |
| Life Model VI     | Cell fate order effect            | G–T–W Six Permutations and Non-commutativity                                | Experimental Design CLOSED / Results OPEN               |
| Life Model VII    | Aging · CH · Cancer               | Decomposition of Induced State and Clone Selection                          | Literature Contact / Causal Verification OPEN           |
| Life Model VIII   | Memory editing                    | Write-Erase-Rewrite Reversible Structure                                    | Technically Available / Iterative Verification OPEN     |
| Life Model IX     | Distributed organizational memory | Cell × niche crossover and interaction                                      | Structural Proposal / Demonstration OPEN                |
| Life Model X      | Minimum life closure              | The combination of memory–execution–recovery–boundary–selection             | Formalization / History OPEN                            |

_Table 2. Integration Targets and Evidence Locations._

### Next Step

All subsequent chapters test whether this common grammar survives in actual calculations and public data.

#### DOIs for This Chapter

DOI 10.5281/zenodo.22289266 · Life form model interpreted by WRRA

> WRRA is a structural architecture that starts from the author's intuition that the universe operates under the principle of least computation, separates the layers of reality realization, and extends its grammar to the life sciences.

## Chapter 2: The Formal Structure of WRRA

WRRA stands for Wonsik Reality-Renderer Architecture, and its Korean name is Wonsik Reality-Renderer Architecture. The key is not to mix what is possible, what is allowed, what is currently given, what actually works, and what is observed into a single sentence.

### Established Scientific Starting Point

Biology’s genotype-phenotype maps, state-space models, causal graphs, and reaction networks also perform a similar separation. The difference with WRRA lies in grouping them into an execution sequence and ownership ledger called SOURCE-LAW-STATE-RENDERER-OBSERVABLE.

### WRRA Reconstruction

Observations are written as O\_t=R(S,L,X\_t,E\_t). Even with the same S, different phenotypes are produced if the state X\_t, environment E\_t, and material renderer R are different. This formula is not a universal prediction formula, but an auditing formula that detects missing necessary inputs.

### Comparative Reading

SOURCE does not necessarily refer only to DNA. Depending on the experiment, the genome, input signal, culture medium composition, or initial cell population can serve as the SOURCE. LAW refers to the physical, chemical, and biological rules that permit the reaction, and STATE describes the conditions under which those rules are executed. RENDERER refers to the polymerases, ribosomes, enzymes, membranes, and cellular structures that actually carry out the reaction.

OBSERVABLE is an output selected by the observer. Even within the same cell, measuring RNA reveals the transcriptome state, measuring proteins reveals the executed functional layer, and measuring morphology reveals the results of boundaries and dynamics. While a change in observation technology does not change life itself, it alters the location of the questions we can close and the uncertainties we face. Therefore, measurement methods are also part of the WRRA ledger.

If the boundary between interpretation and prediction is not measured, the result remains in structural interpretation. Conversely, if the terms are measured independently and the output is correctly predicted in a new sample, it moves to a predictive model.

### Research Content and Validation Results

#### Background of WRRA: From Possibility to Realization

{% hint style="info" %}
The official name is WRRA = Wonsik Reality–Renderer Architecture. In this paper, it is abbreviated as WRRA after the first definition.
{% endhint %}

Wonsik Reality–Renderer Architecture does not deny the motion of classical mechanics, the spacetime of relativity, or the description of possibilities in quantum mechanics. Upon this foundation, it asks, “How are the possibilities permitted by laws realized as an observable phenomenal form through material execution and records?” In biology, the same question is transformed into, “How is the fact that possible proteins are written in DNA realized in actual molecules, cellular states, behaviors, and offspring?”

SOURCE → Lawful Support → Quantum/Statistical Refinement → Event Rendering → Visible Phenotype (1)

At the biological scale, quantum layers provide the physical basis for chemical bonds and reaction possibilities, but most models are coarseened into reaction rates, probability distributions, and molecular numbers. Therefore, the practical core of WRRA biology lies not in exaggerating quantum effects, but in separating allowance rules, current states, execution devices, boundaries, and observations, and preserving the source of each number.

#### Five Execution Layers

$$
M_{\text{WRRA}} = (S, L, X_0, R, O, \Pi)
\tag{2}
$$

| Floor          | General definition                                    | Biological realization                                                    | Question                         |
| -------------- | ----------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------------- |
| SOURCE (S)     | Initial Information · External Input                  | DNA/RNA sequences, maternal molecular stock, culture media                | What was given?                  |
| LAW (L)        | Permission Relationships · Renewal Rules              | Genetic Code, Laws of Combination, Reaction, Transport, and Decomposition | What is possible?                |
| STATE (X)      | Current execution status                              | Number of molecules, concentration, charge, shape, location, residue      | What exists now?                 |
| RENDERER (R)   | A device that converts potential into material output | Polymerase, ribosome, enzyme, membrane, division geometry                 | What actually does it?           |
| OBSERVABLE (O) | Measurable output                                     | Peptide yield, growth rate, daughter cell composition, survival           | What is used for testing?        |
| PROVENANCE (Π) | Ownership, Source, Predictor's Qualification          | Observation/Correction/Derivation/Prediction/Undetermined Ledger          | Where did that number come from? |

_Table 3. WRRA's internal working layer and biological correspondence._

#### Lawful Support and Event Probability

$$
a \notin \Gamma_{\text{lawful}}(X) \Rightarrow P_{\text{WRRA}}(a \mid X) = 0
\tag{3}
$$

$$
P_{\text{WRRA}}(a \mid X) \propto P_{\text{QM/stat}}(a \mid X), \quad a \in \Gamma_{\text{lawful}}(X)
\tag{4}
$$

Probability does not create impossible biochemical pathways. Even with a DNA cassette, if the necessary polymerase, ribosome, substrate, and energy are not present, the protein synthesis event does not enter the support set Γ\_lawful. Conversely, if the necessary implementer is present, thermal and stochastic variations determine the yield, error, distribution, and distribution of cell fate.

#### Fixed-Present, Relations, Boundaries, Residue, and Resources

$$
X_k = (x_k, h_k, b_k, e_k, g_k); \quad X_{k+1} = F_L(X_k, u_k, \xi_k)
\tag{5}
$$

x\_k is fast activity, h\_k is slow residue physically remaining in the present, b\_k is boundary state, e\_k is resource and energy ledger, and g\_k is genetic and structural state. Instead of rereading the entire past, the past effects required for the next present are compressed into the weights of h\_k and the present relationship. This does not mean erasing time, but is a modeling principle of closing updates with a sufficient current state.

$$
h_{k+1} = \lambda h_k + (1-\lambda)\phi(x_{k+1}), \quad 0 \le \lambda < 1
\tag{6}
$$

$$
B_{k+1} = B_k + J_{\text{in}} - J_{\text{out}} - D, \quad b_{\min} \le b_k \le b_{\max}
\tag{7}
$$

Since actual cells are open non-equilibrium systems, the resource ledger must be broken down into carbon, nitrogen, ATP, reducing power, membrane potential, heat, and boundary flux, rather than a single dimensionless total. The role of WRRA is not to declare conservation, but to not hide the movement between the inside and the outside from the calculation.

#### Ownership Ledger and Failure Closure

| Rating          | Meaning                                              | Example                                          |
| --------------- | ---------------------------------------------------- | ------------------------------------------------ |
| STRUCTURAL      | Definition or structure is enforced                  | Five execution layers, gate logic                |
| OBSERVED\_INPUT | Loading from experimental and public data            | 543,380 bp, number of molecules                  |
| CALIBRATION     | Used to match the same result                        | 105-minute period correction factor              |
| DERIVED / EXACT | Calculation based on explicit input and assumptions  | 3n+3, geometric critical area                    |
| PREDICTION      | Holdout output not used for calibration              | Candidates for paired daughter cell distribution |
| OPEN / NULL     | Insufficient independent information or undetermined | First sequence, independent doubling time        |

_Table 4. WRRA Claimed Ownership System._

{% hint style="warning" %}
**Meaning of NULL:** Null is not a value that hides zero or failure. It is a failure closure indicator that a number not qualified to be calculated with the current input and rules alone has not been created.
{% endhint %}

_Figure 1. WRRA structure connecting SOURCE-LAW-STATE-RENDERER-OBSERVABLE and memory/environment._

### Next Step

The next chapter expands on the roles that traces of the present and past, relationships and boundaries play within this execution formula.

#### DOIs for This Chapter

DOI 10.5281/zenodo.22289266 · Life form model interpreted by WRRA

> WRRA stands for Wonsik Reality-Renderer Architecture, and its Korean name is Wonsik Reality-Renderer Architecture. The key is not to mix what is possible, what is allowed, what is currently given, what actually works, and what is observed into a single sentence.

## Chapter 3: Fixed-Present, Residue, Relations, and Boundaries

Cells do not function by returning to the past. Past events remain effective only as residue in the form of current DNA methylation, protein concentration, damage, metabolites, structure, and location. The fixed present of WRRA refers precisely to this computational rule.

### Established Scientific Starting Point

Non-Markov processes, hysteresis, cellular state memory, and developmental pathway dependence are phenomena already addressed by the academic community. WRRA requires that the entire past not be called up as a hidden explanation, but reduced to presently measurable residual terms.

### WRRA Reconstruction

Relationships are binding structures that do not appear in the list of molecules alone, and boundaries are conditions that control the entry and exit of matter and information. Membranes, nuclear membranes, chromatin compartments, and tissue niches are all boundaries whose functions change depending on the state.

### Comparative Reading

The fixed present is not an assertion that the past is unimportant. Rather, it is an assertion that only the physical traces left by the past in the present can participate in current reactions. If embryonic stimulation affects adult cells, that influence must remain somewhere within the present chromatin, protein circuits, tissue structures, or composition of cell populations. A past whose location cannot be found is not an explanation, but an unmeasured variable.

This principle changes experimental design. If only the difference after treatment is compared without measuring the state before treatment, it is impossible to know whether the intervention created a new state or selected an existing one. Lineage tracing, sister cell comparison, and time-resolved measurements are techniques for translating the past into the residue of the present. The remnant term in WRRA reserves space in advance for such measurements.

Explaining results without actually measuring the residuals at the boundary between interpretation and prediction is hindsight interpretation. Measuring residuals in advance to improve the distribution of the next state creates predictive power.

### Next Step

This distinction returns to the problem of direct verification in the fields of epigenetic memory and cell differentiation.

#### DOIs for This Chapter

DOI 10.1038/s41467-024-47158-y · Gene-expression memory-based prediction of cell lineages

DOI 10.1038/s41587-021-01109-w Fluctuating methylation clocks for cell lineage tracing

> Cells do not function by going back to the past. Past events are effective only as residue in the form of current DNA methylation, protein concentration, damage, metabolites, structure, and location. The fixed present of WRRA refers to this computational rule.

## Chapter 4: The Five Closures of Life

Life is not closed off by a single component. Even if information is preserved, it dies if it is not read; even if translation is possible, the system ends if energy and the membrane disappear. Therefore, life must be viewed as the simultaneous establishment of multiple closures.

### Established Scientific Starting Point

Autocatalytic assemblies, autopoiesis, systems biology, and minimal cell research have emphasized catalysis, boundaries, metabolism, and replication, respectively. WRRA divides these into five gates—information, execution, metabolism, boundaries, and systems—to identify points of failure.

### WRRA Reconstruction

The strongest life check is defined by the minimum gate. If any one essential gate is 0, the total autoclosure is 0. This is a fail-closed rule that does not hide weak links.

### Comparative Reading

Information closure asks whether replicable genetic information is maintained, and execution closure asks whether the device reading that information is recreated. Metabolic closure asks whether energy and precursors are supplied, boundary closure asks whether components are maintained within a system and selectively exchanged, and lineage closure asks whether functional offspring continue to be produced. The five questions are not interchangeable.

This decomposition is necessary to avoid exaggerating the success of a synthetic biology module into the success of life as a whole. A membrane may grow but the genome may not replicate, and even if the genome replicates, the translation system may be diluted. The success of one generation does not guarantee the continuation of the lineage. Therefore, the final verdict is determined not by the average score, but by the weakest essential gate.

Representing the boundary between interpretation and prediction is conceptually necessary as a structural argument. Determining whether an actual system has passed those thresholds requires generational material balances and functional data.

### Research Content and Validation Results

#### Translation into Biology: Executable Closure, Not DNA Alone

$$
\text{LIFE INSTANCE} = (\text{Genome, Proteome, Metabolism, Membrane, Geometry, Environment, Division Predicate})
\tag{8}
$$

DNA is the core of the rules to be passed on to the next generation, but the ribosomes and polymerases that read the DNA, the metabolism that sustains the reaction, the membrane that separates the interior, the geometry that creates two daughter cells, and the environment that provides matter and energy must all be closed together. Therefore, a living organism is not a file, but an interdependent execution graph.

$$
\text{Living closure} \Leftrightarrow \text{bounded openness} \land \text{renderer self-reconstruction} \land \text{intergenerational executability}
\tag{9}
$$

| Closing            | Minimum conditions                                                    | In case of failure                           |
| ------------------ | --------------------------------------------------------------------- | -------------------------------------------- |
| Information closed | Inheritance of functional sequences/configurations                    | Cumulative evolution is not possible         |
| Execution closure  | Continuation of transcription, translation, and catalyst              | Description exists, but no material output   |
| Metabolic closure  | Resupply of energy and precursors                                     | Dilution and decomposition exceed production |
| Boundary closure   | Growing sections and selectable individuality                         | The reaction system is dispersed             |
| Split closure      | Simultaneous distribution of DNA, proteins, membranes, and metabolism | Daughter cell execution failure              |
| System closure     | Expected number of functional daughter cells > 1                      | Extinction in the long term                  |

_Table 5. Vertical hierarchy of life closures._

### Next Step

PURE, Syn3A, and synthetic protocells test different parts of these five closures from the back.

#### DOIs for This Chapter

DOI 10.1038/35053176 · Synthesizing life

DOI 10.1073/pnas.0408236101 · A vesicle bioreactor as a step toward an artificial cell assembly

DOI 10.5281/zenodo.22289266 · Life form model interpreted by WRRA

> Life is not closed off by a single component. Even if information is preserved, it dies if it is not read; even if translation is possible, the system ends if energy and membranes disappear. Therefore, life must be viewed as the simultaneous establishment of multiple closures.

## Part II: Where Interpretation and Prediction Diverge

It distinguishes between observed current restorations and future transitions that are not yet fixed, and assigns a legitimate output format to all claims.

## Chapter 5: Reconstructing the Observed Present Is Interpretation

Interpretation and prediction are distinguished not by the type of object, but by the temporal structure of the question. Reading an existing DNA sequence is interpretation, while predicting what phenotype the same sequence will produce in a new environment is prediction.

### Established Scientific Starting Point

Statistical identifiability, inverse problems, Bayesian inference, and measurement theory deal with the conditions for reconstructing hidden values from current data. As long as the reconstruction is stable and within the margin of error, even complex calculations are interpreted.

### WRRA Reconstruction

Fix the task T=(I\_t,Q,tau,epsilon,B,L). If the current information I\_t, the goal Q, the time tau, the tolerance epsilon, the computational budget B, and the loss function L are not declared, the argument that the interpretation is not closed is also not closed.

### Comparative Reading

For example, discovering a specific mutation in a cancer patient's tumor and explaining the function of that protein is an interpretation of current data. To predict which treatment other patients with the same mutation will respond to, tissue environment, clonal composition, dosage, treatment history, and the time axis are added. The moment the question shifts to future metastasis, the answer becomes not a single name, but a verifiable probability distribution.

Interpretation also has failure conditions. The inverse problem is not closed if the value differs significantly when read by different measuring instruments, if the conclusion is overturned by small changes in preprocessing, or if multiple current states can produce the same observation. WRRA does not view interpretation as an easier subtask than prediction, but rather audits whether the target value can be identified from the current information.

At the boundary between interpretation and prediction, explanations following observations are not described as future predictions. Interpretation is evaluated based on stability against repeated measurements, equipment replacement, sample replacement, and disturbances.

### Next Step

The next chapter discusses the reason why the same information cannot close a future single path at the micro-macro boundary.

> Interpretation and prediction are distinguished not by the type of object, but by the temporal structure of the question. Reading an existing DNA sequence is interpretation, while predicting what phenotype the same sequence will produce in a new environment is prediction.

## Chapter 6: The Micro–Macro Boundary Where Prediction Opens

The reason for future uncertainty cannot be reduced simply to the single word “quantum.” Implied event probability, classical chaos, measurement error, omitted variables, and model error are distinct causes.

### Established Scientific Starting Point

Quantum measurement provides possible events and Born probabilities, and detectors or biological thresholds convert continuous signals into distinguishable records. Subsequently, nonlinear amplification and repetitive branching can magnify small differences into macroscopic phenotypic differences.

### WRRA Reconstruction

Before recording, non-degenerative conditional distributions remain, while after recording, distinguishability, persistence, and redundancy create macroscopic determinism. In cells, transcriptional bursts, critical signals, low-copy-number molecules, and mitotic distributions are candidates for this boundary.

### Comparative Reading

Low-copy-number molecules in cell division are a good example of how microscopic differences magnify into macroscopic outcomes. If a mother cell has only two or three essential complexes, a single random distribution can determine the survival of the daughter cells. Conversely, thousands of ribosomes average out the randomness of individual molecules, creating a relatively stable ratio at the cellular level. Probability and certainty are linked not only by size but also by copy number and amplification structure.

This perspective prevents viewing single-cell data solely as the mean. Even if the population mean is stable, rare branching cells can lead to treatment resistance or differentiation failure. Therefore, predictions must report variance, tail risk, threshold probability, and lineage heterogeneity along with the mean. As data is compressed into a single number, important boundary events may disappear.

**The boundary between interpretation and prediction:** Macroscopic determinism does not mean ontological infallibility, but rather a stable record within a defined margin of error. Therefore, the legitimate output of a prediction can be not only a single value but also a distribution, interval, and scenario.

### Next Step

Now, fix the claim grades and verification contracts to be applied to all chapters.

> The reason the future is uncertain cannot be reduced simply to the single word “quantum.” Implied event probability, classical chaos, measurement error, omitted variables, and model error are different causes.

## Chapter 7: What Has Been Established and What Remains Open

A new framework does not become stronger simply because it explains many phenomena. It becomes stronger when it indicates how far the measurement goes and where the inference begins.

### Established Scientific Starting Point

Reproducibility, external validation, pre-registration, and null model comparison are the standards of modern life science. In particular, high-dimensional single-cell data require individual, sample, and pedigree-level holdouts rather than cell-level random splits.

### WRRA Reconstruction

This book distinguishes between EXACT, EMPIRICAL PASS, COMPUTATIONAL PASS, INFERRED, FAIL, OPEN, and NOT ESTABLISHED. Passing the narrow threshold does not automatically elevate to a stronger claim of life or causality.

### Comparative Reading

EXACT does not mean that the entirety of reality has been proven, but rather that the equation is accurate within the declared assumptions. For example, the variance of binomial distribution or the R\_life baseline is calculated accurately when the assumptions are fixed. However, whether actual cells follow independent distributions and what K and f are are empirical questions. Mathematical accuracy and biological fitness must be separated.

COMPUTATIONAL PASS is also limited for the same reason. If a simulation passes internal testing, the consistency of the implemented model is confirmed, but it is not a verification of natural independence. Conversely, if a specific prediction fails in actual data, that failure is very significant. This book places greater value on accurately indicating which layer each success belongs to, rather than on increasing the number of successes.

The boundary between interpretation and prediction includes the WRRA-Cell non-confirmation, the failure of the PURE mass ratio, and the OPEN status of total autonomous closure.

### Research Content and Validation Results

#### Consolidated Adjudication Register for All Cases

| Example                 | The strongest performance                             | Evidence grade                 | Open boundary                                 |
| ----------------------- | ----------------------------------------------------- | ------------------------------ | --------------------------------------------- |
| Coding length           | L=3n+3                                                | EXACT                          | Function cassettes depend on the executor.    |
| DNA bootstrap           | If E=∅, the translation output is usually 0           | STRUCTURAL                     | RNA-based first executor                      |
| PURE                    | Seeded DNA → protein                                  | EMPIRICAL PASS                 | Continuous full playback                      |
| Process                 | P\_full=(1−δ)^n                                       | DERIVED                        | Correlation error and ordination effect       |
| Autocell                | Balanced Growth · Recovery of the 20s Generation      | STRUCTURAL                     | Real molecules and thermodynamics             |
| Syn3A                   | Reconstruction of the Five Gates                      | RECONSTRUCTION PASS            | Independent doubling time                     |
| Distribution and System | P0/P1/P2·R\_life·Extinction                           | EXACT UNDER MODEL              | Paired daughter cell data                     |
| HupA Cliff              | R<1 immediately after φ=6/7                           | CONDITIONAL                    | Actual survival threshold                     |
| First life              | R\_life>1 boundary                                    | STRUCTURAL/INFERENCE           | First order, place, and route                 |
| WRRA-Cell               | Synthesis Verifier 4/4                                | PIPELINE VALIDATED             | Temporal residue                              |
| K562                    | Actual 0/12 significance                              | PARTIAL NON-CONFIRMATION       | Sufficient range and time                     |
| C. elegans              | 23 Run/Restart Node                                   | INTERNAL PASS                  | Live animal holdout                           |
| Layered Memory V        | Multiple eigenmodes, transfer matrices, and pedigrees | TESTABLE MODEL                 | Independent generational tracking empirical   |
| Order Effect VI         | G/T/W six non-commutative permutations                | DIFFERENTIAL PREDICTION        | Wet-lab matching actual AUC                   |
| Aging and Cancer VII    | Induction–Selection–Collective Memory Decomposition   | STRUCTURAL + EMPIRICAL ANCHORS | Same lineage verification                     |
| Memory Editing VIII     | Write–erase–rewrite rescue                            | CAUSAL TEST                    | Multigenerational functional reversibility    |
| Distributed Memory IX   | Cell × niche interaction                              | PROPOSED MODEL                 | Cross-transplantation · Spatial holdout       |
| Minimal closure X       | Joint audit by Λ\_auto and R\_life                    | STRUCTURAL                     | Synthetic primitive cell repeating generation |

_Table 27. Integrated Evidence Ladder._

#### Four Validation Tracks: Scope, Models, and Claim Discipline

The epigenetic memory and cell differentiation axes consist of two reanalyses of publicly available data, one sequential stress test of the declared kinetic model, and one causal write-deletion-rewrite experimental contract. Computational results and actual biological measurements are not treated as the same evidence, and each track fixes the data units, holdouts, thresholds, alternative explanations, and rejection conditions.

_Table 30. Final status of the four verification tracks._

| Track                        | Question                                                                               | Reason                                                        | Verdict                                                |
| ---------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------ |
| 1. DNA–protein state         | Do epigenetic markers predict protein-defined cellular states in external individuals? | Public single-cell multi-omics reanalysis                     | Partial support; Direct LARRY residue audit incomplete |
| 2. Spatial Genealogy – niche | Does the spatial module explain pedigree characteristics even in sample holdouts?      | Public processing data of 150 tumors and 39 samples           | Selective support; the full-module model is rejected.  |
| 3. G→T→W order               | Is the gate–transform–write operation non-commutative?                                 | 6 permutations of the declared model · 1,000 robustness tests | Internal model support; wet-lab unverified             |
| 4. Write–Delete–Rewrite      | Does reversible labeling causally restore function and memory?                         | Simulation and pre-registration experiment contract           | Before experiment; OPEN                                |

$$
z_t=[m_t,h_t,a_t,r_t,p_t,n_t]^T
\tag{70}
$$

DNA methylation, histone state, accessibility, RNA, protein, and niche state at time t.

$$
z_{(t+1)}=A z_t + B u_t + C e_t + \varepsilon_t
\tag{71}
$$

State transition driven by intracellular memory, intervention, environment, and residual error.

$$
y_t=D z_t+\eta_t
\tag{72}
$$

Observed data are an incomplete projection of the latent state.

For each result, the raw data identifier, preprocessing, split unit, random seed, evaluation amount, and failure condition are recorded in the reproduction contract. Observational associations are not promoted to causality, and simulation passes are not changed to in vivo passes.

### Next Step

The next chapter explains how this rating operates as a counter-contract that does not hide failure.

#### DOIs for This Chapter

DOI 10.5281/zenodo.22289266 · Life form model interpreted by WRRA

DOI 10.5281/zenodo.22290829 · Executable Genetic Expression in WRRA

DOI 10.5281/zenodo.22291113 · Lineage Closure in WRRA

DOI 10.5281/zenodo.22291862 · The First Living System in WRRA

> A framework does not become stronger simply because it explains many phenomena. It becomes stronger when it indicates how far the measurement has gone and where the inference begins.

## Chapter 8: Failure Closure and Falsifiable Research

Failure closure is a rule that does not fill unknown values with success. If no necessary terms are found, the check is rolled down to a weaker one, and if the declared threshold is not crossed, the implementation is recorded as a failure.

### Established Scientific Starting Point

A good theory presents not only success stories but also conditions for self-reduction. Strong claims should be withdrawn if they fall below the baseline in an external cohort, if the reproduction ratio by generation is below 1, or if the function in causal editing is not reversible.

### WRRA Reconstruction

The ownership ledger reveals the location of failure. It is a false closure if the information that actually determined the outcome existed in the environment or existing devices, yet it is recorded as internal system autonomy.

### Comparative Reading

A falsification condition is not a list of every possible failure. One must specify a decisive observation that separates the claim from competing explanations. For a GTW order effect, the falsification is that the order difference disappears after matching total dose and toxicity; for niche memory, the falsification is that space does not improve external sample predictions after controlling for cellular state.

Failure closure does not make research passive; rather, it enables strong hypotheses to be pushed to the very end. By predetermining which terms to discard if something fails, one can prevent the practice of changing the explanation after an experiment to turn all results into successes. Bold hypotheses and rigorous verification are not opposites, but rather follow and end in the same research process.

The boundary between interpretation and prediction does not mean merely the immediate discarding of the entire WRRA. It involves reducing specific renderer, residual term, order effect, or autonomy claim to a size allowed by the data.

### Research Content and Validation Results

#### Limitations, Safety, and Research Ethics

WRRA's biological layer does not replace existing molecular biology, systems biology, or synthetic biology. The strongest contribution to date is the separation of ownership and failure-preserving execution contracts.

The coefficients of Autocell and WRRA-Cell are toy design values, not biological constants. They cannot be elevated to actual cell conservation laws until physical units, boundary flux, and thermodynamics are incorporated.

The six molecular pools and φ of Life Model III are not the simultaneously measured complete blastocyst state and actual survival threshold.

The independent factor assumption of the primordial life formula simplifies correlation errors, neutral mutations, and constituent inheritance. It fails to restore the primordial event that was historically erased.

K562 0/12 results are not hidden, but are not exaggerated as global falsification due to the absence of time data and 4/6 perturbation sources.

This study is not a procedure for pathogen design, clinical treatment, or manipulation of human or animal individuals. Actual genetic engineering must comply with the institution's biosafety, ethics, and regulatory reviews.

The final verdict of Version 4.1 is clear. On Axis I, the PURE non-ribosomal mass reproduction threshold fails at 0.08, Syn3A distribution passes only under computational surrogacy grounds, and the 3rd generation persistence of synthetic protocells passes under external support conditions. Therefore, the first self-sustaining life consisting solely of DNA has not yet been demonstrated. On Axis II, open data and the declarative model have narrowed the scope of epigenetic memory research, but causal inheritance in paired lineages remains the final wet-lab boundary. This paper is not a document declaring the synthesis of life, but rather a research contract that fixes what has been identified and what needs to be measured next in a failure-closed form.

#### Integrated Falsification Conditions

* If executor exchange does not alter expression outcomes in the same source and sufficiently measured state, it reduces the strong executor dependency hypothesis.
* If the functional ratio by generation remains less than 1 after seed dilution, the claim of cell-free self-renewal is a failure.
* If none of the binomial, geometric, or localization models explain the holdout distribution in paired daughter cells, the current distribution renderer is incomplete.
* If a strong Markov baseline is repeatedly equal to or better than M2 in new time-distorted data, the empirical necessity of the residual layer is discarded.
* If the maximum completion time of the five gates as an independent parameter does not predict the doubling time, modify the current minimal cell closure model.
* If the first life analogue shows only single-stage proliferation and R\_life≤1, it cannot cross the living lineage boundary.
* In layered memory data, if combined multimodes do not predict the external lineage as well as the common single clock, Life V is reduced.
* If the actual AUC of G/T/W and the six permutations controlled for washout are equivalent, reject the non-commutative P3 of Life VI.
* If only the clone frequency changes without any state change within the same barcode, remove the induction term of Life VII.
* If write–erase–rewrite does not produce a reversible function, it retracts the causal memory claim of the corresponding marker.
* If the niche history does not have additional predictive power after controlling the cell state, the distributed memory term of Life IX is reduced.

### Next Step

With this contract, we enter the first research axis from DNA to the first life.

> Failure closure is a rule that does not fill unknown values with success. If there are no necessary terms, it goes down to a weaker check, and if it does not cross a declared threshold, the implementation is recorded as a failure.

## Part III: From DNA to the First Life

It tracks the boundary where DNA information is executed into RNA and proteins, and closes into a living system through membranes, metabolism, division, and lineage.

## Chapter 9: Is DNA the Blueprint of Life?

While it is intuitive to call DNA a blueprint, a blueprint does not build a factory on its own. DNA contains strong constraints and replicable information, but the molecular machinery and states necessary for execution are currently provided by the cell.

### Established Scientific Starting Point

The central principle organized the flow of information from DNA to RNA and then to protein. Subsequently, research on regulatory genomics, chromatin, RNA processing, translation regulation, and protein quality control expanded the layer between sequence and phenotype.

### WRRA Reconstruction

In WRRA, DNA is the center of the source but is not a complete observable. Reading frames, codons, and regulatory sequences can be interpreted, but protein mass and cell fate require both a state and a renderer.

### Comparative Reading

The four bases of DNA are simple letters, but their sequences are read within reading frames, regulatory motifs, repetitive structures, and three-dimensional folding. The same variant can produce completely different effects depending on the cell type and the stage of development. Therefore, the genotype-phenotype relationship is not a string transformation but a state-conditioned execution process.

This difference is particularly important in genetic engineering. Even if the target base is changed precisely, the corresponding gene may not be expressed, alternative pathways may compensate, proteins may misfold, or edited cells may selectively disappear from the cell population. If editing success rates and functional success rates are reported as a single figure, the owners of the failures become invisible.

The boundary between interpretation and prediction separates reading possible proteins from sequences from matching functional amounts in actual cells. The latter is a prediction only when verified under new conditions.

### Research Content and Validation Results

#### DNA: Information Storage, Coding Lower Bounds, and Renderer Dependence

In a general triplet genetic code, n sense codons and one stop codon are required to specify a peptide of n residues including the start amino acid. The grammatical coding lower bounds, excluding regulatory sequences, non-translation regions, and cloning handles, are as follows.

$$
L_{\text{coding,min}}(n) = 3n + 3 \text{ nucleotides}
\tag{10}
$$

$$
L_{\text{cassette}} = 3n + 3 + R_{\text{executor}}
\tag{11}
$$

The R\_executor is not a fixed universal constant. The promoter depends on which polymerase recognizes it, the ribosome, temperature, salt, and RNA structure under which the RBS operates, and the mechanism used for termination. Therefore, the question of “shortest expressed DNA” is a misdefined question unless the executor is fixed.

| Peptide residue n | Coding lower bound (nt) | Sequence selection information (bit, n log₂20) | High-loss boundary P\_full |
| ----------------- | ----------------------- | ---------------------------------------------- | -------------------------- |
| 5                 | 18                      | 21.6                                           | 0.936                      |
| 10                | 33                      | 43.2                                           | 0.876                      |
| 20                | 63                      | 86.4                                           | 0.767                      |
| 50                | 153                     | 216.1                                          | 0.515                      |
| 100               | 303                     | 432.2                                          | 0.265                      |
| 300               | 903                     | 1296.6                                         | 0.019                      |

_Table 6. Coding Length and Simple Process Loss Scenarios._

#### Why DNA Does Not Execute by Itself

$$
Y_{\text{protein}}(t) = \Phi(D, E, X_0, t)
\tag{12}
$$

$$
E = \varnothing \Rightarrow Y_{\text{protein}}(t) = 0 \text{ (ordinary DNA-directed translation)}
\tag{13}
$$

D is DNA, and E is an executor including polymerase, ribosomes, tRNA, aminoacyl-tRNA synthetase, initiation/elongation/termination factors, and the energy recovery system. Even though DNA encodes these proteins, an executor is required to read them at the initial moment. This is the DNA-only bootstrap problem. The RNA catalysis hypothesis shifts the executor boundaries, but it still requires specifying replication chemistry, substrates, energy, compartments, and heredity.

#### Mutations and Information Budget

$$
P_{\text{intact}}(L \mid f) = f^L
\tag{14}
$$

When replication fidelity f is constant, the probability that L independent positions are copied without errors that destroy function is f^L. Longer genetic information requires higher fidelity, repair, and redundancy. Although this equation is a baseline that omits actual error correlations, neutral mutations, and sequence-specific tolerances, it clearly demonstrates the genetic engineering trade-off that “increasing the genome size increases possible functions but also increases the cost of errors.”

#### The Actual Execution Sequence of DNA Replication

DNA replication is not a symbolic operation that copies a sequence, but a material process in which various enzymes and structures combine in chronological order. The replication origin opens, helicase separates the two strands, and topoisomerase reduces the forward torsional stress. The exposed single strand is stabilized by SSB proteins or eukaryotic RPA. If any of these steps are delayed, the subsequent polymerization reaction cannot begin.

DNA polymerase synthesizes new strands only in the 5′ to 3′ direction. Since the two template strands are antiparallel, one becomes the leading strand, which is synthesized continuously along the direction of the replication fork, while the other becomes the lagging strand, which is synthesized by splitting into short Okazaki fragments. Primase provides RNA primers, and in bacteria, DNA polymerase III primarily performs elongation. In eukaryotic cells, polymerase α is involved in primer formation, while polymerases ε and δ share the responsibility of leading and lagging strand synthesis. The specific division of labor may vary depending on the biological species and organelles.

Even after elongation is complete, the new DNA is not finished. RNA primers must be removed, the empty spaces filled with DNA, and ligase must close the phosphodiester bonds between the fragments. In bacteria, DNA polymerase I and RNase H are involved in primer removal, while in eukaryotic cells, RNase H and FEN1 perform this function. Finally, the termination of the replication fork, the separation of entangled DNA, and the distribution of chromosomes or plasmids follow. Semi-conservative replication and discontinuous synthesis of the lagging strand were established by experiments of Meselson, Stahl, Okazaki, and others \[56,57].

_Table 6A. Execution stages and failure points of DNA replication._

| Execution step             | Representative components                     | The state remaining when failing                                             |
| -------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------- |
| Initiation                 | Replication origin, DNA or ORC·MCM            | Replication does not start or origin is used redundantly                     |
| Release                    | Helicase, topoisomerase, SSB·RPA              | Branch stop, single-strand damage, twist accumulation                        |
| Primer formation           | Primase, polymerase α                         | Polymerase fails to start synthesis                                          |
| Height                     | Bacteria Pol III, Eukaryotes Pol ε·δ          | Incomplete replication, errors, and fork collapse                            |
| Primer removal             | Pol I, RNase H, FEN1                          | RNA residue or empty space                                                   |
| Connection                 | DNA ligase                                    | Nick duration between Okazaki segments                                       |
| Termination and separation | Topoisomerase, chromosome distribution device | Replication is complete, but it could not be delivered to the daughter cells |

#### DNA Repair Maintains Information Closure

Replication errors and DNA damage are not the same thing. Replication errors originate from incorrectly inserted bases during polymerization, whereas DNA damage can occur at any time before or after replication due to ultraviolet radiation, oxidation, alkylation, hydrolysis, radiation, or metabolic byproducts. If damaged bases are repaired before replication, sequence information can be restored. Conversely, if the damage transforms into fixed base substitutions, insertions, or deletions, that state becomes the source for the next generation.

Direct repair reverses damaged chemical bonds. Base excision repair (BER) cleaves the AP site created by DNA glycosylase removing the damaged base, and polymerase and ligase fill the empty space. Uracil-DNA glycosylase isolated by Lindahl is a classic example demonstrating this principle \[58]. Nucleotide excision repair (NER) removes short oligonucleotides by cleaving both ends of a region that significantly distorts the helical structure, such as a UV dimer. Bacterial UvrABC excinuclease directly demonstrated a mechanism of cleaving both ends of the damaged site \[59].

Mismatch repair MMR finds incorrect base pairs and small insertion/deletion loops remaining immediately after replication and corrects the new strand. In the purified system of _Escherichia coli_, it was reconstructed as a reaction involving MutS, MutL, MutH, helicase, exonuclease, polymerase, and ligase \[60]. Double-strand breaks are more dangerous. Homologous recombination HR is relatively accurate because it restores information using homologous templates such as sister chromatids, but there are limitations on the cell cycles and templates that can be used. Non-homologous end ligation NHEJ directly connects severed ends, which is fast but can leave small insertions or deletions.

_Table 6B. Ownership and Limitations of Major DNA Repair Routes._

| Repair route    | Main targets                                             | Execution logic and remaining risks                                      |
| --------------- | -------------------------------------------------------- | ------------------------------------------------------------------------ |
| Direct recovery | Specific alkylation and photodamage                      | Directly reverses damage bonding but is limited to applicable damage     |
| BER             | Individual base damage such as oxidation and deamination | Synthesize one or two nucleotides again after removing a base            |
| NER             | UV dimer and bulky adduct                                | Cut out the entire distorted section and re-synthesize                   |
| MMR             | Mismatch and small loop after duplication                | New strands must be identified, and if they fail, the mutation is fixed. |
| HR              | Double-strand breakage and collapsed fork                | High-accuracy restoration using identical molds                          |
| NHEJ            | Double-strand cut                                        | Directly connects the ends but may leave small sequence changes          |

In WRRA, replication and repair are separate from the source and act as a renderer. Even for the same sequence, the probability of preservation varies depending on the replication enzyme, nucleotide pool, damage burden, checkpoint, and repair inventory. Therefore, f in Equation (14) represents not only the accuracy of the polymerase itself but also effective fidelity, which combines proofreading, damage occurrence, repair success, and pre-replication selection. If these values are not distinguished, the owner of the mutation is incorrectly attributed to the DNA itself.

The pathways of replication and repair at the boundary between interpretation and prediction are established biological processes. However, predicting which damage will lead to which mutation in a specific cell can only be achieved by measuring the damage amount, cell cycle, enzyme inventory, template availability, apoptosis, and selection together.

### Next Step

The next chapter covers the process by which conserved DNA is converted into actual function through transcription, RNA processing, translation, and protein quality control.

#### DOIs for This Chapter

DOI 10.5281/zenodo.22290829 · Executable Genetic Expression in WRRA

> DNA is maintained as a source across generations only when it is replicated and repaired. Sequence information and the execution unit that preserves that information are different layers.

## Chapter 10: RNA and Proteins as Material Execution Machinery

In life, information carries a material cost the moment it is read. Transcription requires polymerases and nucleotides, while translation requires ribosomes, tRNA, amino acids, and energy.

### Established Scientific Starting Point

The PURE system, composed of purified components, enabled the disassembly and reassembly of the minimal execution unit of translation. Protein length, folding, complex assembly, and concentration balance are execution constraints that do not disappear with sequence alone.

### WRRA Reconstruction

RNA and proteins are material devices that render a source into a phenotype. If the renderer is damaged, execution stops even if the information is preserved. For this reason, life must simultaneously handle information replication and executor reproduction.

### Comparative Reading

The translation apparatus possesses a cycle in which it is both the product of translation and the cause that performs translation. Ribosomal proteins can be produced by translation, but separate apparatus is required for rRNA and ribosome assembly. When including the synthesis and charging of tRNA, energy regeneration, and protein folding and degradation, the executor is not a single enzyme but an interdependent network.

This cycle is the most difficult point in the first life and synthetic cells. Synthesizing a protein once by inserting an already completed ribosome demonstrates execution, but the lineage closes only when a new translation machine is reconstructed before the ribosome is diluted or damaged. The existence of a function and the generational conservation of the ability to produce that function must be separated.

At the boundary between interpretation and prediction, the translatability of a sequence can be interpreted, but the yield, folding, and function of the new protein are conditional predictions. Length-dependent processivity and instrument configuration must be included in the input.

### Research Content and Validation Results

#### RNA and Proteins: Material Renderers of Phenotype

DNA → transcription → RNA → translation → peptide → folding/modification → functional protein (15)

Each arrow is not a simple symbolic transformation but a material execution event. Even with the same DNA, changing the executor can alter the start point, yield, whole-length protein ratio, error spectrum, folding, and degradation. WRRA formalizes this as an executor exchange signature stating that “even if the source is the same, if the renderer and state are different, the observable changes.”

#### Length-Dependent Processivity Limits

$$
P_{\text{full}}(n \mid \delta) = (1-\delta)^n
\tag{16}
$$

$$
n_{50} = \ln(0.5) / \ln(1-\delta)
\tag{17}
$$

Published studies of purified translation systems report a per-codon processivity-loss range of δ=1.3×10⁻³–13.2×10⁻³. Under an independent-dropout baseline, this corresponds to a 50% full-length product length of approximately 532.8–52.2 residues. Because this extrapolation assumes independent errors and transfers measurements across systems, it remains an INFERRED range rather than a universal constant.

#### Transcription Transfers DNA Possibilities into RNA States

Transcription proceeds in the order of promoter recognition, initiation, elongation, and termination. In bacteria, the sigma factor induces RNA polymerase to a specific promoter, whereas protein-coding genes in eukaryotic cells require the assembly of general transcription factors and RNA polymerase II. RNA polymerase synthesizes RNA in the 5′ to 3′ direction while reading the DNA template strand from 3′ to 5′. The presence of a promoter merely indicates that transcription is possible; the actual initiation frequency depends on chromatin accessibility, transcription factors, polymerase stock, and signaling status.

During elongation, polymerase can temporarily stop or reverse, and RNA structure and binding proteins influence processivity. Bacterial termination includes intrinsic termination formed by RNA hairpins and U-rich regions, and termination involving Rho helicase. In eukaryotic cells, RNA cleavage and 3′ end formation are linked to polymerase II termination. Since the executors differ even under the same name of “transcription termination,” not all transcription can be explained by a single flowchart that does not specify the biological species.

#### RNA Processing Selects Executable Transcripts

Eukaryotic pre-mRNA is not translated exactly as it is produced. The 5′ cap protects the 5′ end of the RNA and serves as a recognition marker for cap-binding proteins, extranuclear transport, and translation initiation. The spliceosome removes introns and connects exons. Selecting different exon combinations from a single pre-mRNA can result in different protein isoforms. The poly(A) tail attached after 3′ end cleavage affects stability, transport, and translation efficiency. The fact that the separated exons are connected in the actual mRNA has been directly confirmed by adenovirus transcriptome studies \[61].

RNA processing is not limited to mRNA alone. rRNA must be cleaved and modified and assembled with ribosomal proteins, and tRNA must undergo 5′ and 3′ end processing, removal of some introns, and base modification to be accurately loaded and read codons. If this step fails, translation renderers may be insufficient even if the amounts of DNA and RNA are normal.

Exnuclear transport is a boundary-transiting event that moves completed mRNA into the cytoplasm. Conversely, nuclear exosomes, cytoplasmic exosomes, bacterial degradosomes, and various ribonucleases degrade RNA. Surveillance systems, such as nonsense-mediated decay which removes transcripts containing premature stop codons, reduce the production of error proteins. Therefore, RNA quantity is determined not solely by the synthesis rate, but by the difference between transcription, processing, transport, and degradation.

_Table 7A. Running layer from DNA to translatable RNA._

| Floor                            | Representative process                                     | Observations and failures                                        |
| -------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------- |
| Start of war                     | Promoter, transcription factor, and RNA polymerase binding | Initiation frequency, incorrect starting point, no transcription |
| Warrior God                      | RNA 5′→3′ synthesis                                        | Process, pause, early termination                                |
| 5′·3′ end machining              | Cap, cut, poly(A) tail                                     | Decreased stability, transport, and translation initiation       |
| Splicing                         | Intron removal and exon connection                         | Isoform change, frame loss, intron residue                       |
| Transport                        | Nuclear pore complex and RNA binding protein               | Nucleus retention or mislocation                                 |
| RNA surveillance and degradation | NMD, exosome, degradosome                                  | Accumulation of defective RNA or over-degradation of normal RNA  |

#### Translation Repeats Selection and Proofreading

Translation initiation begins when a small ribosomal subunit locates the start region of the mRNA and an initiator tRNA pairs with a start codon. Bacteria commonly utilize Shine-Dalgarno interactions, while eukaryotic cells typically employ a method that starts at the 5′ cap and searches for an appropriate AUG. However, AUGs are not always read with the same efficiency. Surrounding sequences, RNA secondary structure, upstream open reading frames, and the state of the initiator factor alter the actual amount of initiation.

In the kidney, aminoacyl-tRNA enters the A site, and if it passes codon-anticodon selection, a peptide bond is formed. As the ribosome moves one codon, the tRNA passes through the A, P, and E sites before exiting. When UAA, UAG, or UGA arrives at the A site, a release factor binds instead of the corresponding tRNA, releasing the polypeptide. The same mechanism can only be reused after ribosome recycling is complete. If tRNA replenishment, GTP and ATP supply, and rescue factors are insufficient, the full-length protein decreases even if mRNA is present.

#### Protein Quality Control Continues after Translation

A new polypeptide must fold correctly, undergo necessary covalent modifications, move to the correct location, and assemble with other subunits to become a functional protein. Chaperones reduce misfolding and aggregation but cannot salvage the entire structure. If signal peptides and membrane transport systems fail, the protein cannot reach the target compartment even if enzyme activity is normal.

Proteins that do not meet quality standards are refolded or degraded. The ubiquitin-proteasome pathway in eukaryotic cells covalently attaches ubiquitin to target proteins and sends them for ATP-dependent degradation. The fact that ubiquitin complexes are intermediates of protein degradation has been confirmed by reconstitution experiments \[62]. Lysosomes and autophagy process large complexes and organelles, while bacteria use ATP-dependent proteases such as Lon and Clp. If only the production amount is measured and the degradation rate is omitted, the steady-state concentration of the protein cannot be explained.

_Table 7B. Four judgment layers of protein execution._

| Judgment layer          | Essential questions                                                | Representative failure                                                          |
| ----------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| Battlefield Synthesis   | Has the stop codon been completed?                                 | Early termination, frameshift, ribosome stall                                   |
| Folding and deformation | Have you obtained the functional structure and the necessary PTM?  | Aggregation, incorrect disulfide, missing modifications                         |
| Location and assembly   | Did it enter the target area and complex?                          | Mistransport, membrane insertion failure, subunit imbalance                     |
| Turnover                | Do generation and decomposition maintain functional concentration? | Hyperdegradation, accumulation of defective proteins, breakdown of proteostasis |

In the WRRA execution ledger, DNA, pre-mRNA, mature mRNA, peptides in translation, folded proteins, and functional complexes are recorded as different STATES. Each transition requires a separate RENDERER and resources. If measurements from a single layer replace the layer below, the location of failure disappears.

**The boundary between interpretation and prediction:** The sequence of transcription, processing, translation, and quality control is an established mechanism. However, the RNA isoform ratio, full-length yield, folding, and half-life of new sequences vary depending on cell type and conditions. For quantitative prediction, the speed and inventory of each layer must be entered separately.

Chapter 26 applies the translation, folding, and assembly principles of this chapter to the design of a “walking protein.” For WRRA-Motor H2, which combines a KIF5B motor core with a new coiled-coil gate, to actually walk, not only the sequence but also dimer assembly, ATPase, alternating coupling of the two heads, 8 nm directional shift, and load response must be verified together.

### Next Step

The next chapter covers how this multilayer execution is turned on and off, and what natural CRISPR-Cas and genetic perturbation data measure.

#### DOIs for This Chapter

DOI 10.1038/90802 · Cell-free translation reconstituted with purified components

DOI 10.1038/s41598-020-80827-8 · In vitro synthesis of 32 translation-factor proteins

DOI 10.5281/zenodo.22290829 · Executable Genetic Expression in WRRA

> DNA must pass through transcription, RNA processing, translation, folding, transport, and quality control to become a functional protein. Each step can fail independently.

## Chapter 11: Gene Perturbation and WRRA-Cell

While it might seem that removing or suppressing a gene would allow one to directly interpret its function, the cell cycle, compensation circuits, guidance efficiency, and survivor selection alter the outcome.

### Established Scientific Starting Point

Perturb-seq combines CRISPR perturbation and single-cell RNA measurements to create large-scale gene-phenotype maps. However, selecting and evaluating relationships within the same data leads to overfitting and leakage.

### WRRA Reconstruction

WRRA-Cell records the effect of gene g along with the current state x, residue r, environment e, and intervention u. Although the structure was recovered from the synthetic data, the K562 actual audit failed to confirm strong verification, with zero FDR significant relationships out of 12.

### Comparative Reading

Results where no significant relationship is found in the actual audit of WRRA-Cell are not failures to be discarded. Once it is determined which relationships are visible only in synthetic data and disappear in actual cells, omissions in state variables, disturbance intensity, temporal resolution, and sample size become design variables for the next experiment. Failed toy predictions actually reveal model ownership errors.

In future audits, the single-cell state before perturbation and the trajectory after perturbation must be connected within the same lineage. We will examine whether the residual term adds predictive power to new cells or experimental batches even after controlling for guide efficiency, off-target, cell cycle, batch, and survivor bias. If there is no additionality, the strong interpretation of the residual term should be reduced.

**Boundary between interpretation and prediction:** This result is neither a complete failure nor a success for WRRA. It is a partial failure, indicating that the restricted toy relationship was not confirmed in the actual data. By preserving the failure as is, the next verification design was narrowed down.

### Gene Regulation Is Conditional Permission to Execute

In prokaryotes, multiple functionally linked genes can be transcribed into a single operon. In the lac operon, when a repressor binds to the operator, the progression of RNA polymerase is inhibited, and when an inducer changes the binding state of the repressor, the inhibition is released. The binding of cAMP and CAP, which increases when glucose is low, promotes the transcription of the promoter. Since both negative and positive regulation are contained within a single circuit, the expression level cannot be determined solely by the presence of a gene. The concept of the operon was formalized in the regulatory model of Jacob and Monod \[63].

In eukaryotic cells, promoters, enhancers, silencers, transcription factors, mediators, chromatin remodelers, and histone modifications are coupled through long distances and three-dimensional folding. This layer connects to epigenetic memory from Chapter 17 onwards. However, regulation does not end with transcription. Alternative splicing, RNA stability, translation initiation, and protein modification and degradation also produce different outputs from the same source.

_Table 8A. Location of gene regulation and WRRA correspondence._

| Adjustment position | Representative mechanism                     | Items changing in WRRA             |
| ------------------- | -------------------------------------------- | ---------------------------------- |
| DNA access          | Nucleosome, remodeler, methylation           | SOURCE Accessibility and STATE     |
| Start of war        | Repressor, activator, enhancer, sigma factor | The initiation rate allowed by LAW |
| RNA processing      | Alternative splicing, 3′ terminal selection  | Executable RNA SOURCE              |
| Translation         | RBS·Kozak context, uORF, miRNA               | RENDERER output efficiency         |
| Protein turnover    | Ubiquitin, protease, autophagy               | Duration of Function STATE         |

### CRISPR-Cas Is a Natural Memory-Based Immune System

CRISPR-Cas is not originally a gene editing tool, but an adaptive immune system in which bacteria and archaea respond to foreign nucleic acids such as viruses and plasmids. In the first stage, adaptation, parts of the invading nucleic acid are selected as spacers and inserted into the CRISPR array. This sequence serves as a record of past invaders and an immune memory passed down to offspring. It has been experimentally confirmed that the addition and removal of specific spacers alter phage resistance \[64].

In the second step, expression, the CRISPR array is transcribed into long pre-crRNA and processed into small crRNAs. In the third step, interference, crRNAs guide the Cas protein to a complementary target nucleic acid. In many DNA target types, PAMs act as a clue to distinguish between the self-CRISPR array and foreign targets. In the Cas9 system, crRNAs and tracrRNAs guide Cas9 to the target DNA to produce a double-strand break \[65]. Not all CRISPR-Cas use Cas9, and the complex and target differ depending on the class and type.

_Table 8B. Three execution steps of natural CRISPR-Cas._

| Step                      | Input and Executor                      | Success output and failure                                               |
| ------------------------- | --------------------------------------- | ------------------------------------------------------------------------ |
| Adaptation                | Foreign nucleic acids, Cas1-Cas2, etc.  | New spacer record; Wrong choice is autoimmune risk                       |
| Expression and processing | CRISPR array, RNA polymerase, Cas·RNase | Mature crRNA; unable to read memory upon processing failure              |
| Interference              | crRNA-Cas complex, targets, and PAM     | Foreign nucleic acid cleavage; can be avoided by mismatch or PAM changes |

From the perspective of WRRA, foreign nucleic acids are inputs outside the boundary, and acquired spacers are residue left within the source by past events. The crRNA-Cas complex is a renderer that compares these residues to the current target, and cleavage is observable. This case clearly demonstrates that defense is not automatically achieved simply because a record exists; rather, transcription, processing, target recognition, and cleavage of the record are all required.

Engineered CRISPR editing is a rearrangement of the target recognition and cleavage mechanisms of innate immunity. Single-guide RNA, dCas9 transcriptional regulation, base editors, and prime editors have different outputs and error structures. Therefore, spacer acquisition, innate immunity, DNA cleavage editing, and epigenomic editing should not be treated as the same event under the single name of CRISPR.

Spacer acquisition and RNA-induced cleavage, which lie at the boundary between interpretation and prediction, are established mechanisms. However, on-target efficiency, off-target, immunocost, and phage evasion at new targets can only be predicted by incorporating guide, PAM, chromatin, cellular state, and selection conditions.

### Research Content and Validation Results

#### WRRA-Cell: Testing Gene Perturbation and Present Residue

WRRA-Cell deals with the vertical closure of DNA–protein–division and other axes. It tests whether the cell creates the following state with current fast program activity x, slow residue h, nutrition n, substrate s, biomass b, waste w, and damage d without calling up a list of past events.

$$
X_k=(x_k,h_k,n_k,s_k,b_k,w_k,d_k), \quad X_{k+1}=F(X_k,R_k,B_k,U_k)
\tag{36}
$$

| Program    | Representative cover                 |
| ---------- | ------------------------------------ |
| GROWTH     | MYC, E2F1, PCNA, MKI67, CCNA2, CCNB1 |
| STRESS     | ATF3, DDIT3, HSPA1A/B, JUN, FOS      |
| REPAIR     | ATM, ATR, RAD51, BRCA1, XPC, PARP1   |
| AUTOPHAGY  | ATG5, ATG7, BECN1, MAP1LC3B, SQSTM1  |
| QUIESCENCE | CDKN1A/B, RB1, FOXO3, BTG1           |
| DEATH      | BAX, BBC3, PMAIP1, CASP3/8, FAS      |

_Table 15. Program cover page frozen before viewing results in 0.3.1._

#### Versions 0.1–0.3.1: Synthetic-Data Validation

| Step  | Key Results                                                                                                                | Precise meaning                                |
| ----- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| 0.1   | Ledger error 2.49×10⁻¹⁴, restart error 0, adaptive remnant death peak reduced by 15.13%                                    | Internal inspection of design toys             |
| 0.2   | M2 rollout dominance in residue-positive systems, initial precondition 3/4                                                 | Complexity condition failure preservation      |
| 0.3   | Separation of claims regarding static and temporal data                                                                    | Prohibit memory claims with static Perturb-seq |
| 0.3.1 | In the positive spectrum, M2 has an RMSE 16.87% lower than M0 and 25.00% lower than M1; in the negative spectrum, M1 wins. | Validator passed 4/4                           |

_Table 16. WRRA-Cell Calculation Lineage._

#### Version 0.4: Audit of Real K562 Perturb-seq Data

34 pre-frozen marker maps were applied to the standardized gene × perturb signature matrix (8,055 genes, 2,012 perturb signatures, 1,907 unique targets) of the Replogle K562 essential gene Perturb-seq. Only 12/36 outgoing relationships from growth and repair could be evaluated, and 20,000 randomized targeted tests and Benjamini–Hochberg correction were used.

| Characteristic      | Result              | Verdict                            |
| ------------------- | ------------------- | ---------------------------------- |
| FDR 5% significance | 0/12                | No support for the evaluation part |
| Toy symbol match    | 4/12=33.3%, p=0.388 | Not noteworthy                     |
| Toy weight Pearson  | r=0.365, p=0.243    | Not noteworthy                     |
| Toy weight Spearman | ρ=0.462, p=0.131    | Not noteworthy                     |

_Table 17. Initial Actual K562 Static Audit._

{% hint style="warning" %}
**PARTIAL NON-CONFIRMATION / INSUFFICIENT FOR GLOBAL VERDICT.** The evaluated toy relationship network was not verified, but the entire time residual of WRRA cannot be determined due to the absence of 4/6 perturbation sources and all time information.
{% endhint %}

### Next Step

In the next chapter, we evaluate the most direct experiment in which the translation machine creates itself outside the cell.

#### DOIs for This Chapter

DOI 10.5281/zenodo.22290829 · Executable Genetic Expression in WRRA

One sentence of this chapter: Gene regulation and CRISPR-Cas determine when to read a sequence and which target to execute on. Perturbation results can only be interpreted by measuring the regulatory circuit, guide efficiency, and compensation and selection together.

## Chapter 12

### Can the PURE System Regenerate Itself?

When PURE synthesizes its own proteins, it appears close to life. However, the ability to produce something only once and the ability to replace its own devices without diminishing with each generation represent a different threshold.

### Established Scientific Starting Point

The 2026 study synthesized 36 non-ribosomal PURE proteins in a single reaction and reconstructed a second-generation functional translation system. This is a significant advance toward partial self-production of a complex device.

### WRRA Reconstruction

The amount recovered from the starting non-ribosomal protein of 350 micrograms is 28 micrograms, so R\_mass,nr=0.08. Therefore, synthesis and one-time functional reconstruction pass, but non-regressive mass replacement R>=1 fails.

### Comparative Reading

PURE's 8% is not a small technical figure, but rather a rearrangement of the entire self-regenerating argument. The fact that all 36 proteins were created is an achievement of component integrity, while the mass balance of 28/350 is a constraint on generational persistence. Both results are simultaneously true. If one is erased to emphasize the other, the true position of the research becomes invisible.

The following PURE experiment must fix the same generation definition and previous rules. You must pre-register how much seed is taken in each generation, how newly synthesized mass is distinguished from the remaining input protein, and how concentration-corrected functional activity and total mass are measured. You must verify that R\_mass and the functional ratio are both 1 or greater in at least three generations.

The boundary between interpretation and prediction, 0.08, is the mass recovery ratio, not the functional output ratio of consecutive generations. Since ribosomes, rRNA, tRNA, DNA replication, energy, and boundaries were not regenerated in one lineage, the entire PURE autoclosure is OPEN.

### Research Content and Validation Results

#### PURE and Partial Self-Regeneration

| **Total**                                 | **Protein output**                                  | **Playback in launcher**             | **System regeneration** | **Verdict**          |
| ----------------------------------------- | --------------------------------------------------- | ------------------------------------ | ----------------------- | -------------------- |
| DNA alone                                 | doesn't exist                                       | doesn't exist                        | doesn't exist           | FAIL                 |
| DNA + seeded PURE                         | is available                                        | Use external launcher                | doesn't exist           | EXPRESSION PASS      |
| Multi-protein PURE                        | Presence · Amputation burden                        | partial product                      | doesn't exist           | PROCESSIVITY LIMIT   |
| 2026 Non-ribosomal protein reorganization | 36 types of synthesis and functional reconstruction | 8% efficiency                        | doesn't exist           | PARTIAL CLOSURE      |
| JCVI-syn3A                                | Sustained in living cells                           | Tissue inheritance from mother cells | is available            | BIOLOGICAL BENCHMARK |
| seed-free bottom-up cell                  | Unclosed                                            | Unclosed                             | Unclosed                | OPEN                 |

Table 7. Closed ledger of execution from DNA to autonomous life.

R\_nonribosomal = 0.08 < 1 ⇒ sustained replacement fails (18)

The results to be released in 2026 showed that PURE can produce all non-ribosomal PURE proteins and reconstitute functional second-generation PURE, but the single-reaction regeneration efficiency of 8% falls short of the continuous replacement threshold of 1. Ribosome, rRNA, tRNA, DNA replication, energy, and boundary regeneration are also still outside the scope. Therefore, a distinction must be made between “protein was produced” and “executors are reconstructed in each generation.”

#### PURE: Is the Generational Reproduction Ratio Actually at Least One?

Let M\_nr,g be the mass of non-ribosomal protein available for use in the g generation. The mass reproduction ratio is distinguished from functional activity and the overall system closure score.

R\_mass,nr(g)=M\_nr,g+1/M\_nr,g; non-regressive persistence requires R\_mass,nr≥1 (78)

C\_PURE=min(R\_mass,nr,R\_ribosome,R\_tRNA,R\_DNA-replication,R\_energy,R\_boundary) (79)

The 2026 study synthesized 36 non-ribosomal PURE proteins in a single PURE reaction and reconstituted a functional second-generation translation system. However, starting with 350 µg of non-ribosomal protein, 28 µg was recovered after purification and concentration, so R\_mass,nr=28/350=0.08<1. Therefore, synthesis and a single functional reconstitution pass, but sustained mass replacement of the tested implementation fails. Functional activity relative to the concentration-adjusted control is a separate indicator.

M\_nr(n)/M\_nr(0)=(0.08)^n; (0.08)^3=5.12×10^−4 (80)

Equation (80) is a mass balance extrapolation where efficiency is constant and is not the observed third-generation functional trajectory. Equation (79) is also a conservative sufficient condition score for WRRA and is not a standard biochemical identity. Since ribosomes, rRNA, tRNA, DNA replication, energy, and boundaries are not regenerated together in the same closed system, the entire PURE self-renewal is OPEN.

| **Floor**                   | **Observations in the 2026 study**                       | **Closed state** |
| --------------------------- | -------------------------------------------------------- | ---------------- |
| biribosomal factor 36       | Synthesis in one reaction                                | SYNTHESIS PASS   |
| 2nd generation translation  | Reorganization of functional systems                     | ONE-STEP PASS    |
| biribosome mass replacement | 28/350 µg                                                | FAIL: 0.08<1     |
| Ribosome/rRNA/tRNA          | Unplayed inside the watch loop                           | OPEN             |
| Genome, Energy, Boundary    | External supply or outside the module                    | OPEN             |
| Repetitive system           | Continuous multi-generational replacement mis-experience | OPEN             |

Table 39. Current status of the PURE closed layer.

### Next Step

The minimal cell extends this partial device into the gate of the entire actual cell.

#### DOIs for This Chapter

DOI 10.1038/90802 · Cell-free translation reconstituted with purified components

DOI 10.1038/s41598-020-80827-8 · In vitro synthesis of 32 translation-factor proteins

DOI 10.1038/s41467-026-73337-0 · PURE makes PURE

One sentence from this chapter: If PURE synthesizes its own proteins, it appears close to life. However, the ability to create them once and the ability to replace its own devices without diminishing with each generation are different thresholds.

## Chapter 13

### Minimal Cells and JCVI-syn3A

Minimal cell research asks for the minimum list of genes necessary for life, but a divisible cell is not automatically created based on the list alone.

### Established Scientific Starting Point

JCVI-syn3A is a cell with a minimal genome of 543,380 bp, which has become a benchmark for studying genome reduction, cell morphology, metabolism, and division mechanisms. Whole-cell models execute these components together in time and space.

### WRRA Reconstruction

WRRA distinguishes five components—genome, RNA, ribosomes, enzymes, and membranes—and five gates—replication, translation, metabolism, membrane growth, and division. The doubling time cannot be shorter than the completion time of the slowest essential gate.

### Comparative Reading

A minimal genome does not mean the smallest life form, but rather the result of eliminating as many genes as possible that can be removed in a specific environment. If the culture medium is rich in nutrients, the environment can take over the synthetic functions within the cell. Therefore, the fact that there are few genes does not necessarily mean there is high autonomy.

WRRA's minimal cell calculation does not hide the environment renderer from the ledger. It displays the medium, temperature, osmotic pressure, supplied metabolites, and the experimenter's splitting operations as external inputs. Minimality must be reported not only of the number of internal components but also of which functions are delegated to the environment.

Boundary replication limit for interpretation and prediction is a conditional calculation under assumptions and does not independently predict the observed approximately 50-minute replication and 105-minute splitting cycles. It separates the parameters derived from the data from the new predictions.

### Research Content and Validation Results

#### Minimal Cells: Five-Component Autocatalysis and Five Gates

WRRA-Autocell formed a positive linear autocatalytic system with five extensive components: genome (G), RNA (R), ribosome (B), enzyme (P), and membrane (M).

dx/dt = Ax, Av\* = &#x3BB;_&#x76;_, x → x/2 when Σx = 2Σx₀ (19)

| **Calculation items**                 | **Result**                         | **Verdict**                |
| ------------------------------------- | ---------------------------------- | -------------------------- |
| Dominant growth rate λ\*              | 0.2373258491                       | amniotic fluid             |
| Boat time                             | 2.9206560649 Normalization Unit    | arrival                    |
| Balance Composition G/R/B/P/M         | 0.2112/0.2181/0.1718/0.2023/0.1965 | All positive               |
| eigenvalue residuals                  | 9.13×10⁻¹⁷                         | Numerical error passed     |
| Energy supply/demand                  | 1.3033228333                       | ≥1                         |
| Material supply/demand                | 1.4336551166                       | ≥1                         |
| 20th generation L1 street             | 3.02×10⁻⁸                          | Restoration of balance     |
| 20th generation population equivalent | 2²⁰=1,048,576                      | Repeated division map pass |

Table 8. WRRA-Autocell-0.1 Internal Calculation.

Removing G, R, B, and P respectively lowered the dominant growth rate to -0.02. Removing the membrane M leaves the chemical growth rate of +0.2373258491, but the boundary disappears. Therefore, growing chemistry and life forms with boundaries are not identical. In WRRA, the membrane is not a simple component but an address space for self-executing units.

#### The Five Gates of Cell Division

T\_cell = inf{t : G\_D(t) ∧ G\_P(t) ∧ G\_M(t) ∧ G\_E(t) ∧ G\_F(t)} (20)

| **Gate**                  | **Completion conditions**                                     | **Biological meaning**      |
| ------------------------- | ------------------------------------------------------------- | --------------------------- |
| G\_D: DNA                 | Whole genome replication and two-copy continuity              | Genetic persistence         |
| G\_P: Protein/Ribosome    | Regeneration of initial translation and catalytic capacity    | Launcher persistence        |
| G\_M: Mak                 | Area to wrap the increased volume                             | Continued vigilance         |
| G\_E: Energy/Metabolism   | ATP production ≥ consumption, essential metabolites ≥ minimum | Non-equilibrium maintenance |
| G\_F: Separation/Geometry | Chromosome separation, V≥2V₀, cleavage complete               | Create two execution units  |

Table 9. Simultaneous closure gate of WRRA minimal cells.

#### JCVI-syn3A Loading and Geometric Calculations

T\_rep,lower = 543,380 / (2×600×60) = 7.546944 min (21)

If the genome is treated as a sphere at ideal packing density, its lower-bound diameter is obtained from the DNA contour volume. This is a geometric lower bound, not a prediction of actual chromosome organization.

r\_div = 2^(1/3)r₀ = 251.9842 nm (r₀=200 nm) (22)

A₀=502,654.8 nm², A\_div=797,914.8 nm², ΔA/A₀=58.7401% (23)

The volume-doubling spherical geometry is EXACT, but the time to reach that area depends on lipid and membrane protein synthesis, the initial number of molecules, and the growth rate. Since some coefficients from the open model and 105 minutes were used for correction, it is an observation-based reconstruction rather than an independent prediction by WRRA.

#### Membrane Transport and Energy Coupling

The cell membrane is not a simple packaging material. While small nonpolar molecules can diffuse through the membrane, ions and most polar molecules require channels, carriers, or pumps. Facilitated diffusion moves along concentration or electrochemical gradients, and primary active transport uses energy such as ATP directly. Secondary active transport combines the free energy stored in the gradient of one substance with the movement of another substance.

The electron transport chains of respiration and photosynthesis create a proton motive force across the membrane. ATP synthase combines this electrochemical gradient with ATP synthesis. Experiments linking light-induced proton transport and ATP formation in vesicles reconstituted with bacteriorhodopsin and ATPase have directly demonstrated the coupling of membrane boundaries and energy conversion \[66]. Even with the presence of boundaries, metabolism and synthesis do not continue without selective transport and gradient maintenance.

Metabolism is not limited to a list of catabolism and anabolism alone. The influx of carbon, nitrogen, phosphate, and sulfur, the regeneration of redox carriers, ATP, GTP, CoA, and various cofactors, and the elimination of byproducts must occur simultaneously. If one does not distinguish between substances provided by the external medium and substances that the cell regenerates itself, the autonomy of the synthetic cell is overestimated.

| **Gate**             | **First, the measured amount**             | **Unclosed**                                                    |
| -------------------- | ------------------------------------------ | --------------------------------------------------------------- |
| Selective Inflow     | Flux and transporter copy by substrate     | There is a barrier, but necessary substances cannot enter       |
| inclination          | Membrane potential, ΔpH, leakage rate      | Energy is not stored and is lost                                |
| ATP regeneration     | Production and consumption rates, ATP/ADP  | Translation and replication stop after single-shot fuel         |
| redox play           | NAD(P)H ratio and electron acceptor        | Simultaneous blockage of synthesis and detoxification reactions |
| dispose              | Toxic byproducts and efflux                | Growth is visible, but the next generation is suppressed.       |
| membrane maintenance | Lipid synthesis, area growth, permeability | Dilution, rupture, or gradient collapse during growth           |

Table 14A. Performance audit of membranes and energy in minimal cells.

#### Cell-Cycle Controls Bind the Execution Sequence

Replication, growth, and division are not independent parallel processes. In bacteria, replication initiation, chromosome segregation, divisome assembly, and septation are linked according to trophic status and cell size. In eukaryotic cells, G1/S, G2/M, and spindle checkpoints check for DNA replication completion, damage, and chromosome attachment status. A checkpoint is not a device that corrects all errors, but rather a control layer that delays the next transition or allows for the selection of cell death or arrest.

In WRRA, the cell cycle can be recorded as a runtime permission between LAW and STATE. Division is not permitted merely by the fact that there are two copies of DNA. Damage status, energy, membrane area, chromosome location, and division machinery must pass the threshold. Conversely, in tumor cells or damaged synthetic cells, this permission may be incorrectly opened.

Specifying membrane transport, energy, and checkpoints in the five gates of a minimal cell prevents confusion between genome replication PASS and lineage closure PASS. Even if the same 105-minute division cycle is observed, if it relies on external ATP precursors, feeder membranes, completed transporters, or intact seed ribosomes, ownership remains with the external conditions and the initial STATE.

The existence of transport, chemiosmosis, and checkpoints at the boundary between interpretation and prediction is an established biological fact. To predict the doubling time and cause of failure of a specific minimal cell, data on the number of transporters, membrane leakage, metabolic flux, ATP turnover, DNA damage, and the timing of each gate are required.

### Next Step

How essential molecules are passed to the two daughters when the cell divides determines lineage closure.

#### DOIs for This Chapter

DOI 10.1126/science.aad6253 · Design and synthesis of a minimal bacterial genome

DOI 10.7554/eLife.36842 · Essential metabolism for a minimal cell

DOI 10.1016/j.cell.2021.03.008 · Genetic requirements for cell division in a genomically minimal cell

DOI 10.1016/j.cell.2021.12.025 · Fundamental behaviors emerge from simulations of a living minimal cell

DOI 10.5281/zenodo.22289266 · Life form model interpreted by WRRA

One sentence from this chapter: A minimal cell is more than a gene list. Transport, energy, replication, quality control, and division must close within one lineage.

## Chapter 14

### What Does a Mother Cell Distribute to Its Two Daughters?

Division doubles the number of cells but does not divide every molecule exactly in half. Essential complexes with small copy numbers can disappear from one daughter through random distribution alone.

### Established Scientific Starting Point

In unbiased binomial distribution, X is equal to Binomial(N, 1/2) and relative variation is on the scale of 1/sqrt(N). Cells reduce this risk through localization, binding, active transport, and redundancy.

### WRRA Reconstruction

The molecular partition error D\_x is defined as the difference between the molecular ratio and volume ratio of daughter cells. In the 50-cycle of the Syn3A 4D model, ribosomes, degradosome, PtsG, and GapDH exhibited approximate binomial partitions without directional bias.

### Comparative Reading

A molecular ratio differing from half in two daughter cells of equal volume is not immediately a bias. When N is small, binomial noise alone can cause significant differences. Conversely, if specific molecules are localized around cell poles or DNA, a spatial signature different from that of a binomial model with the same mean is generated. Both coefficients and geometry are required for the distribution test.

A deterministic experiment involves selecting a single mother cell, preserving both daughters, and linking them. The total mother cell mass, daughter cell volume, molecular counts, and subsequent survival must be measured. Analyzing only the successful daughters leads to selection bias. Paired designs can, for the first time, directly demonstrate the causal link between molecular distribution and phylogenetic success.

The boundary between interpretation and prediction is a computational pass. In reality, molecular counting, volume correction, and survival threshold measurements linking one mother cell and two daughter cells are still open.

### Research Content and Validation Results

#### Daughter-Cell Partitioning and Lineage Closure

When the number of mother cell molecules N is distributed independently and unbiased, the number of first daughters X follows a finite binomial distribution. The two daughters are not independent because the gain of one is the loss of the other.

X \~ Binomial(N, 1/2), E\[X]=N/2, Var(X)=N/4, CV=1/√N (24)

P₂=∏ᵢPᵢ(both pass), P₁=2(q−P₂), P₀=1−2q+P₂ (25)

R\_life = E\[Y] = P₁ + 2P₂ = 2q (26)

f(s)=P₀+P₁s+P₂s²; ζ=1 if R\_life≤1, else ζ=P₀/P₂ (27)

| **φ**  | **R\_life** | **P₀** | **P₁** | **100 Generations of Survival** | **Ultimate Survival** |
| ------ | ----------- | ------ | ------ | ------------------------------- | --------------------- |
| 0.50   | 1.991       | 0.000  | 0.009  | 100.00%                         | 100.00%               |
| 0.70   | 1.789       | 0.007  | 0.197  | 99.10%                          | 99.10%                |
| 0.80   | 1.400       | 0.061  | 0.478  | 86.80%                          | 86.80%                |
| 0.85   | 1.134       | 0.148  | 0.570  | 47.60%                          | 47.60%                |
| 0.8571 | 1.133       | 0.148  | 0.570  | 47.23%                          | 47.23%                |
| 0.8572 | 0.978       | 0.206  | 0.610  | 1.18%                           | 0.00%                 |
| 0.90   | 0.742       | 0.344  | 0.570  | 0.00%                           | 0.00%                 |

Table 10. Systematic results of the six declared molecular pool scenarios.

At φ=6/7, the minimum daughter cell count of 28-copy HupA is 12, but immediately afterwards it changes to 13, and R\_life drops discontinuously from 1.133 to 0.978. In this scenario, the owner of the critical cliff is the low-copy number HupA. Even if the total biomass is nearly the same, a single essential low-copy number component can shift a lineage from supercritical to extinction.

#### Active Equalization and Redundancy Design

| **φ** | **Minimum equalization a required for R\_life≥1** | **Remaining random proportion** |
| ----- | ------------------------------------------------- | ------------------------------- |
| 0.80  | 0.00%                                             | 100.00%                         |
| 0.85  | 0.00%                                             | 100.00%                         |
| 0.86  | 2.96%                                             | 97.04%                          |
| 0.90  | 26.85%                                            | 73.15%                          |
| 0.95  | 56.42%                                            | 43.58%                          |
| 1.00  | 76.24%                                            | 23.76%                          |

Table 11. Equalization requirement to restore system critical point.

Fixing the minimum number of daughter cells of HupA at 12 copies results in parental cells of 35/39/45 copies providing 95/99/99.9% passing probabilities for both daughters, respectively. This is a reserve of +7/+11/+17 compared to the input of 28 copies. This is not a natural optimum, but an example of a genetic engineering design that calculates the Pareto front of replication cost and genetic reliability.

#### The Covariance Signature of Division Geometry

Var(Xᵢ)=Nᵢ/4 + Nᵢ(Nᵢ−1)σ\_p² (28)

κᵢ=4Var(Xᵢ)/Nᵢ = 1 + 4(Nᵢ−1)σ\_p² (29)

Cov(Xᵢ,Xⱼ)=NᵢNⱼσ\_p², i≠j (30)

For a paired mother–two-daughter measurement, the total molecular count should be conserved within the declared recovery tolerance after correction for sampling loss.

#### Syn3A: Molecular Partitioning from One Mother Cell to Two Daughters

The existing φ is maintained as the survival threshold ratio for each essential molecular group, and the distribution error is separated as D\_x. For molecular group x:

p\_x=N\_x,1/(N\_x,1+N\_x,2); v=V\_1/(V\_1+V\_2); D\_x=|p\_x−v| (81)

If D\_x=0, it is a volume-proportional distribution. In an unbiased binomial distribution with equal volume, the rarer the complex, the greater the relative variation, and the primitive daughter cell difference rate D\*\_x=2D\_x.

RMS(D\_x)=1/(2√N\_x); E\[D\_x]≈1/√(2πN\_x) (82)

The 2026 Syn3A four-dimensional whole-cell model simulated 50 complete cell cycles. At 105 minutes, the mean mother cell contained 881 ribosomes, 176 RNA polymerases, and 192 degradosomes. The paired daughter distributions of ribosomes, degradosomes, DNA polymerase complexes, and membrane proteins form the reference ledger for the proposed experiment.

| **Molecular groups** | **Mother cell N** | **RMS D\_x** | **Average D\_x approximation** | **RMS D\*\_x** |
| -------------------- | ----------------- | ------------ | ------------------------------ | -------------- |
| ribosome             | 881               | 1.68%        | 1.34%                          | 3.37%          |
| degradosome          | 192               | 3.61%        | 2.88%                          | 7.22%          |

Table 40. Binomial variation magnitude calculated using reported Syn3A blastocyst counts.

This percentage is the analytical expectation of the approximate binomial null model, not a sampled measurement per daughter cell. Direct completion requires time tracking of one mother cell and two daughter cells, volume correction, molecular counting, pre-registered D\_x allowable intervals, and verification of the φ threshold of all essential molecular groups.

### Next Step

The next chapter separates persistence and autonomy when externally supported synthetic cells continue through generations.

#### DOIs for This Chapter

DOI 10.1016/j.cell.2021.03.008 · Genetic requirements for cell division in a genomically minimal cell

DOI 10.3389/fcell.2023.1214962 · Dynamics of chromosome organization in a minimal bacterial cell

DOI 10.1016/j.cell.2026.02.009 · Bringing the genetically minimal cell to life on a computer in 4D

DOI 10.5281/zenodo.22291113 · Lineage Closure in WRRA

One sentence of this chapter: Cell division doubles the number of cells but does not divide every molecule exactly in half. Essential complexes with small copy numbers can disappear from one daughter through random distribution alone.

## Chapter 15

### Synthetic Protocells and the Birth of Generations

The decisive question in protocell research is not whether it grows once and then divides, but whether functional offspring continue to be produced over several generations.

### Established Scientific Starting Point

The growth and division of fatty acid vesicles, internal nucleic acid replication, membrane synthesis, and protein expression have long developed as separate modules. Recently, SpudCell combined a defined PURE device with seven plasmid 90-kbp genomes.

### WRRA Reconstruction

Five lineage experiments of the preprint pass the third-generation persistence threshold. About 30% of the fifth-generation daughter cells retained a complete plasmid set. However, the external feeder and existing ribosomes possess part of the run.

### Comparative Reading

The multigenerational results of SpudCell represent a significant boundary in synthetic cell research, but they do not represent the removal of external supply. Feeder liposomes supply membrane material, streptavidin linkages aid in capture, and existing ribosomes perform translation. To respect what the system actually does, this external mechanism should not be renamed as an internal function of life.

Nevertheless, five-cycle phylogenetic experiments yield much stronger results than simple one-time vesicle growth. Replication, growth, division, and selection produce linked offspring. The next threshold is to measure whether the complete genome, translational ability, membrane growth, and division are maintained simultaneously in the same lineage over generations, and whether R\_life exceeds 1 even with reduced material replacement.

Simultaneously records the boundary between interpretation and prediction, phylogenetic continuity PASS, and autonomous first life NOT ESTABLISHED. R\_genome,eff approximately 1.57 is a heuristic based on ideal binary fission and sample assumptions, not an actual value of R\_life.

### Research Content and Validation Results

#### Synthetic Protocells: Does a Functional Lineage Persist for at Least Three Generations?

Gaut et al. reported chemically defined synthetic cells with a defined PURE expression device and a 90-kbp genome dispersed across seven plasmids. The preprints directly describe five phylogenetic experiments combining genome replication, feeder-liposome growth, division, and competition for selectable mutations. The official Biotic study description separately states that the non-renewing ribosomes operate for approximately 5–10 generations before degradation.

G\_persist,preprint≥5>3; G\_operating,official≈5–10 generations (83)

Approximately 30% of the 5th generation daughter cells retained all 7 plasmids. The transparent surrogates of full-genome offspring, assuming ideal binary fission and comparable viability and sampling, are as follows.

R\_genome,eff=\[2^5×0.30]^(1/5)=2(0.30)^(1/5)≈1.57>1 (84)

Equation (84) is a heuristic inference of this paper based on assumptions rather than author-reported values and is not identical to R\_life. R\_life includes the persistence of translation, energy, boundary, division, and environmental support. This system relies on repeat external feeder vesicles, streptavidin-linked membrane capture, pre-formed ribosomes, etc., and cannot reconstruct degraded ribosomes. Therefore, 3-generation persistence is passed, but autonomy Λ\_auto=1 is not established.

| **Gate**                       | **Reason**                                 | **Verdict**                     |
| ------------------------------ | ------------------------------------------ | ------------------------------- |
| Genome replication             | 7-Plasmid 90-kbp Genome                    | PASS, separation loss exists    |
| Membrane growth                | feeder liposome absorption                 | External supply conditions PASS |
| split                          | genetically encoded division               | PASS                            |
| ≥3 generations continued       | Preprint 5 Systematic Experiments          | PASS; Preprint                  |
| Longer operating period        | Official description 5th–10th generation   | auxiliary statement             |
| 5th generation complete genome | daughter cells about 30%                   | PARTIAL                         |
| Ribosome renewal               | Decomposes but is not reconstructed        | FAIL/OPEN                       |
| Autonomous closure Λ\_auto     | External feeder/molecular support required | NOT ESTABLISHED                 |

Table 41. Determination of separation between protocell persistence and autonomy.

### Next Step

Then, under what conditions should the strong threshold of the first life be defined?

#### DOIs for This Chapter

DOI 10.1073/pnas.0408236101 · A vesicle bioreactor as a step toward an artificial cell assembly

DOI 10.64898/2026.07.01.735724 · A chemically defined synthetic cell capable of growth and replication

DOI 10.1038/s41467-026-69531-9 · Integration of DNA replication and phospholipid synthesis in a synthetic cell

One sentence from this chapter: The decisive question in protocell research is not whether it grows once and then divides, but whether functional descendants continue to appear over several generations.

## Chapter 16

### When Does the First Life Begin?

First life is different from LUCA. LUCA is an already evolved common ancestor, and first life is the earliest boundary where chemical reactions transitioned into heritable functional lineages.

### Established Scientific Starting Point

The RNA world, metabolism-first, membrane-first, and hybrid models view the antecedent relationships of replication, catalysis, energy, and compartments differently, respectively. Experiments demonstrate the potential of each module, but a single fully autonomous system does not yet exist.

### WRRA Reconstruction

At baseline, R\_life=2Kf^L and critical accuracy f\_c=(2K)^(-1/L). This equation is accurate under the declared independent error and binary fission assumptions, but does not determine the initial molecular sequence or location.

### Comparative Reading

Fixing the first life candidate to a single specific chemical substance can cause one to miss the structure of the actual transition. What is important is not the name—whether RNA or peptide—but the bonds where information is replicated, errors accumulate, catalysts aid execution, boundaries hold components together, and energy enables the next cycle.

R\_life > 1 does not replace the entire philosophical definition of life. Rather, it provides a minimum operational criterion for determining whether a system is supercritical in experiments. Instead of counting only the number of offspring, only those that retain essential functions should be included in K, and functions provided by the environment must be reported as a separate autonomy index.

The boundary between interpretation and prediction, RNA-like polymers, peptide catalysts, and fatty acid boundaries, are strong non-perfect candidates. Distinguishing between the probability and historical reality of the candidates, we leave the experimental demonstration of self-sustaining systems as the final threshold.

### Research Content and Validation Results

#### First Life: From Chemistry to Heritable Lineages

The first life is not LUCA. Chemical proliferation, boundaryed primitive cells, living lineages, autonomous cells, and LUCA are different stages. The goal of WRRA is not to restore a single historically erased first organism, but to define the practice boundary where chemistry first becomes a living lineage.

| **Target**               | **Operational definition**                                        | **Life judgment**   |
| ------------------------ | ----------------------------------------------------------------- | ------------------- |
| chemical reproducer      | Growth and reproduction of material patterns                      | insufficiency       |
| protocell                | A boundary-forming chemical system capable of growth and division | Required candidates |
| The first living lineage | Heritable functional closure and R\_life>1                        | WRRA boundary       |
| Autonomous cells         | Most renderer functions play internally                           | Later stages        |
| LUCA                     | The last common ancestral group of modern cellular life           | Not the first life  |

Table 12. Distinction between the first life and subsequent life.

#### Five Owners and Exact Threshold Equations

| **Owner**    | **Minimum task**                                          | **Types of failure**         |
| ------------ | --------------------------------------------------------- | ---------------------------- |
| information  | Conservation of functional sequence and composition       | No cumulative inheritance    |
| catalyst     | Accelerated closed support response                       | Dilution exceeds production  |
| boundary     | Concentration and selectable individuality                | component dispersion         |
| energy       | Maintaining out-of-equilibrium reactions                  | Inactivation                 |
| distribution | Passing on sufficient functionality to future generations | Growth exists but no lineage |

Table 13. The five smallest owners of the first life.

q = Kfᴸ, R\_life = 2Kfᴸ (31)

f\_c(L,K) = (2K)^(-1/L), K > 1/2 (32)

K is the joint success probability under non-replication conditions such as boundary continuity, catalytic closure, energy binding, and distribution maintenance. If K ≤ 1/2, even perfect sequence copying cannot make the expected value of the two daughter processes greater than 1. In other words, improving only the genetic information cannot compensate for renderers that fail frequently.

| **Declaration Input** | **Value** |
| --------------------- | --------- |
| Boundary continuity   | 0.90      |
| Catalytic closure     | 0.85      |
| Energy binding        | 0.90      |
| Maintain distribution | 0.90      |
| K                     | 0.61965   |
| f\_c of L=100         | 0.997856  |
| R\_life of f=0.999    | 1.121     |

Table 14. Initial life sensitivity scenarios. Not historical measurements.

#### Environmental Renderers and Candidate Architectures

FIRST LIFE = PROTOCELL + LOCAL GEOCHEMICAL RENDERER (33)

Wetness-dryness, temperature oscillations, light and radiation, mineral surfaces, and redox gradients may have taken over some of the concentration, activation, separation, and correction functions internalized by subsequent cells. This does not mean that the environment itself is alive. The boundary lineage in which internal information changes the number of functional offspring is the unit of selection.

L₀ = RNA-like information + short peptides + fatty-acid boundary + energy cycle (34)

The candidate most compatible with current evidence is a combination of RNA-like information macromolecules, short catalytic peptides, permeable fatty acid compartments, activated monomers, and repeating environmental cycles, rather than bare DNA cells. It is possible that initially, heterogeneous primitive cell populations with frequent leakage, fusion, and horizontal exchange crossed a critical threshold multiple times.

πₜ₊₁(y) ∝ ∫ B(y|x)πₜ(x)dx (35)

Lineages with a spectral radius greater than 1 remain in the subsequent distribution more than lower critical lines. Here, selection does not refer to the addition of a selecting agent, but rather summarizes the differential proliferation of already existing variations.

#### Life Model X: Reformulating the Minimal Closure Conditions for the First Life

We reconnect the initial life model of Section 8 with epigenetic memory research. The existence of a replication molecule or a vesicle dividing once does not immediately result in a living lineage. Minimal life must be closed enough so that boundaries, resource acquisition, information replication, function execution, error correction, and boundary reproduction can be performed again in the next generation.

L\_min = {B, S, R, P, E, C} (66)

B represents the boundary, S represents the replicable information source, R represents the information decoding relationship, P represents the catalyst/functional polymer, E represents the energy/material flow, and C represents the reproductive closure of the entire cycle. An autonomous closure rate is defined to avoid concealing the extent to which the external entity takes its place.

Λ\_auto = (essential operations regenerated internally)/(all essential operations), 0≤Λ\_auto≤1 (67)

| **Owner**     | **Minimum task**                                             | **Why One Generation of Success Is Not Enough**                    |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------------ |
| Boundary B    | Concentration, individuality, and re-suturing after division | Can rely on external parcel supply                                 |
| Information S | Inheritance of functional differences                        | It will only be copied and may not be linked to the function.      |
| Detox R       | Execution of information as a catalyst and structure         | Environmental catalysts can replace everything                     |
| Catalyst P    | Support for the speed of replication, metabolism, and repair | If slower than dilution and decomposition, system loss             |
| Energy E      | Non-equilibrium reaction and precursor replenishment         | Repeating generations are impossible with single-fuel power alone. |
| Closed C      | Reconstructing the entire execution graph in Daughter        | Even if only some components are replicated, the whole collapses   |

Table 25. Minimum life audit of Life Model X.

I(X\_parent;X\_offspring)>0, Var(w|X)>0, R\_life=2Kfᴸ>1 (68)

The first condition requires inherited memory, the second differential proliferation based on that memory, and the third supercritical persistence of functional offspring. Therefore, the critical point of primordial life is not the moment a specific molecule first appeared, but the moment when memory–execution–recovery–boundary reproduction–selection closes into a single repeatable lineage. This is not a historical proposition that restores the exact initial sequence, location, and pathway, but an operational test that synthetic primitive cells must pass.

#### The Integrated V–X Transition Equation

X\_g₊₁ = F(X\_g,u\_g;G)+ξ\_g (69)

This equation does not assert that chemistry alone automatically becomes life. It states the ownership conditions under which a candidate system can cross from chemical persistence into a heritable lineage.

| **Thanksgiving**               | **Judgment on failure**                                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Independent measurement        | If genealogy and memory are assumed to be the same signal, the result is invalidated.                    |
| Competitive null model         | If simple AUC, common clock, selection-only, and independent cell models are dominant, WRRA reduction    |
| Holdout                        | Prohibit generalization if not reproducible in new cell lines, lineages, locus, or stimuli               |
| Causal editing                 | If the function does not change even if the label is changed, withdraw the claim of the causative label. |
| Multi-generational maintenance | If it disappears after a washout, it is judged as a temporary reaction rather than a memory.             |
| safety                         | If any of the identity, genomic, or tumorigenesis gates fails, the application is terminated.            |

Table 26. Common rejection principle for the entire V–X study.

### Next Step

Now, let's move to the second axis and see how the same genome remembers different cell fates.

#### DOIs for This Chapter

DOI 10.1038/35053176 · Synthesizing life

DOI 10.1073/pnas.0408236101 · A vesicle bioreactor as a step toward an artificial cell assembly

DOI 10.5281/zenodo.22291862 · The First Living System in WRRA

One sentence from this chapter: First life is different from LUCA. LUCA is an already evolved common ancestor, and first life is the earliest boundary where chemical reactions transitioned into heritable functional lines.

## Part 4

### From Epigenetic Memory to Cell Fate

It verifies multilayer memory and sequence effects where the same DNA creates different cells, as well as the genealogical dynamics of aging, cancer, and spatial niches.

## Chapter 17

### Why Does the Same DNA Produce Different Cells?

Skin cells and neurons generally have the same DNA, but they read different genes and maintain different proteins. The difference lies in the execution state outside the sequence.

### Established Scientific Starting Point

DNA methylation, histone modifications, chromatin accessibility, transcription factors, and RNA and protein circuits collectively create cellular identity. It is insufficient to view memory as a whole based on only one marker.

### WRRA Reconstruction

The common state z\_t=\[m,h,a,r,p,n]^T links methylation, histones, accessibility, RNA, proteins, and niches. Observation is an incomplete projection of this latent state, and manipulation and the environment change the state transition.

### Comparative Reading

The term epigenetics makes it easy to lump everything outside the DNA sequence into one basket. However, methylation, histones, accessibility, transcription, proteins, and metabolism differ in both measurement methods and time scales. To locate the actual position of a memory, one must separate the direction and delay in the transmission of changes from one layer to another.

Cell differentiation should not be evaluated based on a single final cell marker alone. Measurements must be taken step-by-step to determine whether the initial gate opened, intermediate signals were active, stability markers were recorded, function was actually manifested, and the results were maintained in the lineage even after the manipulation was removed. This sequence constitutes the common experimental grammar of the Life Model VX.

At the boundary between interpretation and prediction is an integrated grammar. The actual values of the inter-layer transfer matrix A and operation matrix B must be estimated from genealogical data and intervention experiments.

### Research Content and Validation Results

#### A Common WRRA State Model for Epigenetic Memory

While the previous section dealt with the execution of DNA information and lineage closure, Life Model V–X deals with the process by which identical or similar genomes produce different present and future outputs based on past inputs. In WRRA, epigenetic memory is not an ornament on DNA, but a state-dependent boundary that alters the availability, responsiveness, and restoration speed of the pathway through which the source is transmitted to the present executer.

Xᵢ(t) = \[Gᵢ, Mᵢ, Hᵢ, Aᵢ, Rᵢ, Pᵢ, Qᵢ, Nᵢ] (39)

G is the genome, M is DNA methylation, H is histones and heterochromatin, A is accessibility and three-dimensional contact, R is RNA, P is proteins and signals, Q is metabolism, cell cycle, and stress, and N is the extracellular niche. External input U includes nutrition, inflammation, drugs, mechanical forces, and intercellular signals.

Xᵢ(t+Δt) = F(Xᵢ(t), U(t), Gᵢ, Lᵢ) + ξᵢ(t) (40)

M\_res(Δ) = I(X\_past ; Y\_future | G, U\_future, lineage, cell state) (41)

Conditional mutual information M\_res asks whether past states additionally predict future responses even after controlling for the genome, current environment, lineage, and current cell state. Simple age prediction or cluster separation is not a sufficient condition for working memory.

| **Model** | **Key question**                                          | **Main operation**                      | **Decisive judgment**                                          |
| --------- | --------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------- |
| V         | How long does memory last, and where is it transmitted?   | Attenuation and transmission estimation | Covariance prediction of the holdout lineage                   |
| VI        | Does the same total amount differ depending on the order? | G/T/W permutation                       | Stable fate difference after washout                           |
| VII       | How is memory amplified in disease?                       | Derivative and selective decomposition  | Changes within the same barcode and changes in the clone ratio |
| VIII      | Are memory markers the cause of the phenotype?            | Write, Delete, Rewrite                  | Reversible rescue and functional recovery                      |
| IX        | Are memories stored outside of cells as well?             | Cell × niche intersection               | Decomposition of main effects and interactions                 |
| X         | When does self-replicating chemistry become life?         | Minimal closure audit                   | Repeat generation R\_life>1                                    |

Table 19. Continuous study structure of Life Model V–X.

### Next Step

The next chapter develops the hypothesis that the time of memory is not a single one but consists of multiple decay modes.

#### DOIs for This Chapter

DOI 10.1038/s41586-025-08656-1 · Genome-coverage single-cell histone modifications for embryo lineage tracing

DOI 10.1038/s41587-024-02241-z · Tracking single-cell evolution using clock-like chromatin accessibility

DOI 10.1038/s41556-025-01687-w · Sequential chromatin reorganization during X inactivation

One sentence from this chapter: Skin cells and neurons have generally the same DNA, but they read different genes and maintain different proteins. The difference lies in the execution state outside the sequence.

## Chapter 18

### How Do Cells Remember the Past?

Memory does not merely mean that markers remain for a long time. Even short-lived cellular states can persist for a long time within a population through lineage transmission and selection.

### Established Scientific Starting Point

Epigenetic clocks and lineage tracing utilize marker changes over time and division. However, if temporal distance, phylogenetic distance, stratified attenuation, and selection effects are not separated, they can appear as a single clock.

### WRRA Reconstruction

Life Model V views the eigenmodes of the binding state matrix as the time scale of memory. The binding of DNA, chromatin, RNA, proteins, and niches can create various slow modes.

### Comparative Reading

If the half-life of a memory is measured solely by the decline curve of a single marker, interlayer compensation is not visible. Even if methylation disappears quickly, transcription factor autocircuits can maintain their state, and even if intracellular markers disappear, the selective proliferation of specific clones can maintain population proportions. Observed long memories may be a combination of multiple short memories.

Genealogical distance and actual time must also be distinguished. Cells that divide rapidly and those that divide barely over the same period of time have different label dilutions. Therefore, to identify stratified genealogical clocks, time t and generation g must be recorded together, and whether the state correlation between sister and cousin cells is maintained beyond the common environment must be measured.

At the boundary between interpretation and prediction, a strong argument survives only if it predicts better in the external lineage compared to the common single clock, independent layer, and Markov transition. This eigenmode itself is still an OPEN prediction.

### Research Content and Validation Results

#### Life Model V: Layer-Specific Lineage Clocks of Epigenetic Memory

The goal is not to rank DNA methylation, parental histones, accessibility, and RNA and protein memory into a single independent half-life. It is to identify the intrinsic modes and layered loadings shared by the combined molecular layers to separate accurate cell division distances from actual elapsed times. EPI-Clone tracked large-scale lineages by reading single CpG methylation and blood cell status together \[34], and TACIT provided a single-cell map of seven histone modifications in early embryos \[35]. EpiTrace showed that division age can be estimated using clock-like accessibility \[36], and fluctuating methylation clocks showed that high-temporal-resolution lineage tracking is possible in human tissues \[43].

#### Lineage Distance, Elapsed Time, and Coupled Eigenmodes

Rᵥ⁽ˡ⁾ = Yᵥ⁽ˡ⁾ − μₗ(cell type, cell cycle, batch, size, environment) (42)

Cₗᴾᴰ(g) = Corr(R\_parent⁽ˡ⁾, R\_descendant⁽ˡ⁾) = Aₗρₗᵍ + Bₗ (43)

τₗ = −1 / ln|ρₗ|, g₁⁄₂,ₗ = τₗ ln2 (44)

If two sister cells have each passed one generation from a common mother cell, the lineage distance is 2, so the covariance is proportional to ρ². Misinterpreting sister correlation as parent-offspring correlation leads to an overestimation of memory time. Additionally, since the elapsed times of the stationary phase and the rapid proliferation phase differ even with the same number of generations, the two decay axes are separated.

Cₗ(d,tᵢ,tⱼ) = Aₗ exp(−d/τₗ,g) exp\[−(tᵢ+tⱼ)/τₗ,t] + Bₗ (45)

Z\_child = A\_state Z\_parent + ΓX + ξ, Cov(Zᵢ,Zⱼ|a)=A\_stateʰⁱΣₐ(A\_stateʰʲ)ᵀ (46)

Cₗ(d) = Σᵣ aₗᵣ λᵣᵈ + Bₗ, τᵣ = −1/ln|λᵣ| (47)

Therefore, the enhanced P4 is not “there is one clock per layer” but “each layer has a different damping fingerprint of the combined eigenmodes and predicts the next generation covariance of the unseen lineage with the non-diagonal transfer matrix.”

#### Competitive Model and Experiment

| **Model**             | **Structure**                                      | **Support/Rejection Criteria**                                              |
| --------------------- | -------------------------------------------------- | --------------------------------------------------------------------------- |
| M0: No memory         | Conditional covariance 0 after generation distance | If M1/M2 fails to improve in the holdout, maintain                          |
| M1: Independent layer | A\_state diagonal, stratigraphic ρ                 | There is layer-by-layer attenuation, but the transport term is unnecessary. |
| M2: Bonding layer     | Sparse non-diagonal A\_state and multiple λ        | Significantly improve C(d+1) of the unseen lineage                          |

Table 20. Competitive Models and Judgment of Life Model V.

The recommended experiment combines 5th–6th generation live imaging with independent DNA barcodes and uses a portion of sister cells from each branch for destructive multiome analysis. Circular reasoning, such as estimating lineage by methylation and then testing methylation memory with the same CpG, or estimating lineage by RNA and then testing memory with the same RNA, is prohibited. MCM2·POLE3, DNMT1·UHRF1, writer/eraser, and RNA/protein half-life disturbances must target specific terms in the transfer matrix.

#### Falsification Conditions

* The common single damping rate is substantially equivalent to the layered and combined model.
* The non-diagonal transfer term is indistinguishable from 0 or its direction is reversed in repeated experiments.
* M2 does not have higher predictive power than M0/M1 in cell lines and lineages that have not been observed.
* The memory effect disappears when cell type, cycle, environment, and survivor bias are controlled.

### Next Step

Verify whether the DNA layer predicts the protein definition state in external organisms using public multi-omics data.

#### DOIs for This Chapter

DOI 10.1038/s41586-025-09041-8 Clonal tracing with somatic epimutations reveals dynamics of blood aging

DOI 10.1038/s41587-024-02241-z · Tracking single-cell evolution using clock-like chromatin accessibility

DOI 10.1038/s41587-021-01109-w Fluctuating methylation clocks for cell lineage tracing

One sentence of this chapter: Memory does not mean only that markers remain for a long time. Even short-lived cellular states can persist for a long time in a population through lineage transmission and selection.

## Chapter 19

### Predicting Protein States from the DNA Layer

If epigenetic memory is real, the state of the DNA layer must have a reproducible relationship with the RNA or protein layer. Fitness within the same individual alone is not sufficient.

### Established Scientific Starting Point

Single-cell multi-omics has enabled the reading of methylation and surface proteins within the same cell. Inter-individual holdouts prevent batch and individual-specific signals from taking the place of prediction.

### WRRA Reconstruction

8,850 cells, 663 amplicons, 20 ADTs, and 6 states from the EPI-Clone series were used. The mean balance accuracy of the whole DNA feature model was 0.487, and the inclusion of descriptive covariates was 0.502, exceeding the multi-category criterion of 0.167.

### Comparative Reading

A balanced accuracy of 0.502 is not a perfect prediction. Compared to the six-state random standard of 0.167, there is a meaningful crossover signal, but about half the uncertainty remains. If this number is interpreted as “DNA determined cell fate,” it exceeds the range indicated by the data.

The next strong test is time-sequenced pedigree data. It verifies whether early DNA methylation predicts subsequent protein states and functions within the same barcode, and whether independent information remains even when RNA and the current protein are added. A holdout is required to exclude the entire individuals, experimental batches, and pedigrees.

The boundary results of interpretation and prediction partially support DNA-protein state binding but do not prove causal inheritance of future fate or LARRY residual terms.

### Research Content and Validation Results

#### Track 1: Epigenetic Memory and Cell Differentiation across DNA and Protein Layers

We used 8,850 fully observed cells, 663 methylation amplicons, 20 antibody-derived tags (ADTs), and 6 protein definitions from the publicly available EPI-Clone dataset. The key evaluation is a reciprocal holdout, where one individual learns and another tests. This blocks individual-specific leakage more strongly than cell-level random splitting.

| **Model**                       | **Object A→B** | **Individual B→A** | **Average balance accuracy** |
| ------------------------------- | -------------- | ------------------ | ---------------------------- |
| E0 Multi-category Standard      | 0.167          | 0.167              | 0.167                        |
| E1 single optimal amplicon      | 0.221          | 0.229              | 0.225                        |
| E2 Total 663 amplicons          | 0.476          | 0.497              | 0.487                        |
| E3 Total + Technical Covariates | 0.487          | 0.517              | 0.502                        |

Table 31. Prediction of DNA methylation-based protein status of exogenous holdouts.

The significant improvement in total DNA features compared to baseline and the maintenance of performance even with the addition of descriptive covariates support the state coupling between the DNA and protein layers. However, this analysis does not provide evidence that lineage residues in the same cell causally determine future fate. Cell lineage-level residue terms must be verified separately when access to raw data with LARRY barcodes and complete time-series data is secured.

Figure 2. Prediction of protein definition status of DNA methylation features in crossover holdout.

### Next Step

The next chapter asks whether cell fate can differ depending on the order of action, even with the same amount of action.

#### DOIs for This Chapter

DOI 10.1038/s41586-025-09041-8 Clonal tracing with somatic epimutations reveals dynamics of blood aging

DOI 10.1038/s41587-021-01109-w Fluctuating methylation clocks for cell lineage tracing

One sentence from this chapter: If epigenetic memory is real, the state of the DNA layer must have a reproducible relationship with the RNA or protein layer. Fitness within the same individual alone is not sufficient.

## Chapter 20

### Does Cell Differentiation Have an Order?

Cell differentiation manipulation may be a matter of sequence rather than just the sum of the materials. The process of first opening up the possibility of a reaction, converting the signal, and finally applying a stability label may not be the same as the reverse order.

### Established Scientific Starting Point

Developmental biology has long dealt with competence windows, the temporal ordering of signals, and chromatin priming. The addition of WRRA specifies this as the non-commutativity of the three operations G, T, and W, comparing all six permutations.

### WRRA Reconstruction

In the declarative model, GTW had the largest final memory at 0.5021 and maintained the top position across a sample of 1,000 parameters. This is a clear differential prediction made by the model.

### Comparative Reading

Non-commutativity differs from the mere observation that the first treatment was stronger. To discuss the effect of the operation sequence itself, the actual dose received by the cells, exposure time, cell count, toxicity, and cell cycle distribution must be identical across each sequence. It is necessary to verify whether the difference persists after washing to distinguish between transient signals and memory.

If GTW is indeed superior, the design of cell differentiation protocols changes. Instead of injecting the final factor all at once, a step-by-step protocol that opens competence, switches the transcription program, and uses stability markers can increase yield and homogeneity. Conversely, if the six permutations are equal, the strong sequence prediction of WRRA is withdrawn.

The boundary results between interpretation and prediction are merely internal model robustness and not evidence of actual cells. Six-permutation experiments matching the same delivered AUC, interval, toxicity, cell cycle, and washing conditions are required.

### Research Content and Validation Results

#### Life Model VI: Noncommutative Order Effects in Cell-Fate Formation

The narrow prediction of P3 is that the order alters long-term cell fate, even when chromatin gate opening G, lineage transcription factor pulse T, and maintenance marker recording W are all applied at the same actual intracellular exposure levels. Rather than repeating the general propositions of conventional chronology, differential tests such as six permutations, actual AUC match, washout, and multigenerational maintenance are pre-registered.

x\_GTW = Φ\_W Φ\_T Φ\_G x₀, x\_TGW = Φ\_W Φ\_G Φ\_T x₀ (48)

Φ\_TΦ\_G − Φ\_GΦ\_T ≃ τ\_Gτ\_T\[L\_T,L\_G] (49)

\[Lᵢ,Lⱼ] = LᵢLⱼ − LⱼLᵢ; additive null ⇒ \[Lᵢ,Lⱼ]=0 (50)

The minimum kinetics of target accessibility a, transcription factor activity q, maintenance label m, and system circuit p can be set as follows. The label recording term a·h(q) specifies a non-commutative combination in which preceding accessibility and transcription factor occupancy change the effect of the writer.

ȧ=k\_Gu\_G(1−a)−λₐ(a−a₀); q̇=k\_Tu\_Ta−λ\_q q (51)

ṁ=k\_Wu\_W a·qⁿ/(K\_qⁿ+qⁿ)−λ\_m m; ṗ=αq+βm+γpʳ/(K\_pʳ+pʳ)−δp (52)

| **Division**           | **Protocol**                     | **Key Interpretation**                                             |
| ---------------------- | -------------------------------- | ------------------------------------------------------------------ |
| Stock Price Theory     | G→T→W                            | Record of TF occupation and maintenance markers after gate opening |
| Adjacent Exchange 1    | T→G→W                            | \[L\_T,L\_G] test                                                  |
| Adjacent Exchange 2    | G→W→T                            | \[L\_W,L\_T] Black                                                 |
| Remainder permutation  | T→W→G / W→G→T / W→T→G            | Overall rankings and unproductive records                          |
| Simultaneous/Exclusive | G+T+W / G / T / W                | Separation of order effects and single operation effects           |
| Technology comparison  | catalytic-dead / non-target gRNA | Blocking non-specific effects of editors and inducers              |

Table 21. Six permutations of Life Model VI and the essential control group.

The primary cell line is the differentiation of primitive endoderm in embryonic stem cells using inducible GATA6/SOX17. Since the pioneer function of GATA6 itself causes G and T to overlap, in synthetic separation tests, G is separated by dCas9–P300 or remodeler, T by SOX17 or restricted GATA6 pulse, and W by H3K4me3 writer. Precise targeted epigenome editing combined nine types of chromatin modifications with single-cell readout \[37], and CRISPRai performed activation and inhibition operations of two loci in the same cell \[38]. The results of Dam & ChIC separating the chronological order of lamina separation and polycomb accumulation during X inactivation support the feasibility of sequencing measurements \[41].

Dᵢ = ∫₀ᵀ uᵢⁿᵘᶜˡᵉᵃʳ(t)dt; Dᵢ⁽π⁾ ≈ Dᵢ⁽π′⁾ (53)

P(F\_stable|GTW) > (1/5)Σ\_{π≠GTW}P(F\_stable|π) (54)

After removing the input and after at least 3–5 divisions, SOX17, GATA4, PDGFRA, PrE transcriptome, PrE chromatin score, and function are used as co-endpoints. Instead of the nominal dose, nuclear effector AUC and target occupancy are matched, and residual pulse, cell cycle, apoptosis, and proliferation rate are controlled as covariates.

#### Falsification Conditions

* After adjusting for actual AUC, target occupancy, washout, cell cycle, and survival, the order factor falls within the equivalence range.
* GTW is not superior to TGW and GWT. If other orders are superior, the order effect remains, but the GTW optimality hypothesis is rejected.
* The difference exists only immediately after the washout and disappears after several divisions.
* Exchangers are not detected in both the synthetic separation system and the actual separation system.

#### Track 3: G→T→W Noncommutative Order Effects

G stands for the reactive possibility gate, T for the transcription/signal transform, and W for the stability label write. The non-commutative hypothesis, which states that the order of operations alters the final memory and function even with the same total amount of action, was tested within the declared dynamics.

G∘T ≠ T∘G, T∘W ≠ W∘T, G∘W ≠ W∘G (73)

M\_π = final memory marker, F\_π = final functional output, π∈S₃ (74)

Δ\_order = M\_GTW − max\_(π≠GTW) M\_π (75)

H₀: all permutations are equivalent after matching delivered AUC and washout; H₁: at least one permutation differs (76)

| **Permutation** | **Final Memory M** | **Final function F** | **Cumulative Function AUC** |
| --------------- | ------------------ | -------------------- | --------------------------- |
| G→T→W           | 0.5021             | 0.1034               | 23.04                       |
| T→G→W           | 0.1630             | 0.0739               | 13.49                       |
| G→W→T           | 0.0620             | 0.0619               | 12.17                       |
| T→W→G           | 0.0137             | 0.0000               | 1.58                        |
| W→T→G           | 0.0039             | 0.0108               | 2.11                        |
| W→G→T           | 0.0039             | 0.0580               | 11.33                       |

Table 34. Results of the declaration model for six permutations.

In a sample of 1,000 parameters, the proportion of G→T→W maintaining the top final memory was 100%, the median gap with competing permutations was 0.3385, and the minimum gap was 0.2296. This is the internal robustness of the disjunctive model, not a proof in actual cells.

| **Item**    | **Fixed conditions**                                                                                  |
| ----------- | ----------------------------------------------------------------------------------------------------- |
| design      | 6 permutations in the same cell background, same total dose and interval, wash control                |
| measurement | Gate accessibility, transcriptional response, label retention, functional output, minimum 3 divisions |
| verdict     | GTW is superior to the pre-designated control group in memory and inter-iteration orientation.        |
| Dismissal   | Permutation differences disappear after realization AUC, toxicity, and cell cycle correction          |

Table 35. Minimum pre-registration contracts for the actual G/T/W experiment.

Figure 3. Comparison of final memory and function of six G/T/W permutations.

### Next Step

Whether the order effect leads to the causality of the stability marker is tested in the write-delete-rewrite test.

#### DOIs for This Chapter

DOI 10.1038/s41588-024-01706-w Systematic epigenome editing captures context-dependent chromatin function

DOI 10.1038/s41587-024-02213-3 Bidirectional epigenetic editing reveals hierarchies in gene regulation

One sentence from this chapter: Cell differentiation operations may be a matter of order rather than just the sum of the materials. The process of first opening up the possibility of reaction, converting the signal, and finally applying a stability label may not be the same as the reverse order.

## Chapter 21

### Can Memory Be Written, Erased, and Rewritten?

If correlated markers are the cause of functional memory, then the function must also be reversible when the markers are written, erased, and rewritten at the same locus.

### Established Scientific Starting Point

CRISPR-based epigenome editing regulates methylation or histone states without altering DNA sequences. Bidirectional editing reveals the hierarchy and context dependence between markers.

### WRRA Reconstruction

The label value of the declaration model changed from 0.5050 to 0.0008 after deletion and 0.5090 after rewriting, and the rescue was 1.008. These values are not experimental results but simulations of creating a pre-registration threshold.

### Comparative Reading

Write-erase-rewrite is the most intuitive reversible experiment that transforms the correlation between a label and function into causality. However, since the act of the editing tool binding to the same site itself can alter transcription, catalytic inactivation of the effector and sham control are necessary. The selection effect, where cells die after deletion and only the remaining cells are analyzed, must also be blocked.

The strongest result is that within the same barcode lineage, markers, RNA, proteins, and functions change during write, revert during erase, and are restored again during rewrite. Genealogical inheritance of memory can only be spoken of if the orientation is maintained even after at least three divisions following the removal of the manipulation. If only the marker is reversible and the function remains immobile, that marker is more likely to be the marker than the cause.

The boundary experiment between interpretation and prediction, non-target guidance, catalytic inactivation effectors, off-target, toxicity, and selection bias must be blocked, and functional recovery must be confirmed after at least three divisions.

### Research Content and Validation Results

#### Life Model VIII: Writing, Erasing, and Rewriting Epigenetic Memory

Life VIII is a model that transitions from correlation to causation. It requires phenotypic reversibility by selectively recording, deleting, and rewriting only candidate memory states Z while maintaining genomic G and the current environment U. Unidirectional changes in expression alone cannot exclude off-target, toxicity, selection, or general stress.

G′=G, U′=U, Z′≠Z ⇒ Y′=R\_bio(G,Z′,U) (60)

Z₀ →write Z₁ →erase Z₀′ →rewrite Z₁′; Y₀ → Y₁ → Y₀′ → Y₁′ (61)

| **Step**                       | **Essential observations**                            | **Failure interpretation**                                       |
| ------------------------------ | ----------------------------------------------------- | ---------------------------------------------------------------- |
| record                         | Target Z change and Y change                          | No effect or locus context inappropriate                         |
| delete                         | Z and Y return to the baseline direction              | The marker is the result or memory is dispersed                  |
| Re-record                      | Z and Y reproducible at the same locus                | The possibility that the first change is selective or off-target |
| Multi-generational maintenance | Features continue in the lineage after editor removal | It is merely temporary transcriptional activation, not memory.   |
| Orthogonal Reproduction        | Same direction in other effectors, gRNAs, and clones  | Tool unique effects                                              |

Table 23. Causality Ladder of Life Model VIII.

The key endpoint is not the presence of a single marker, but differentiation function, restimulation response, lineage maintenance, and rescue. Since targeted editing platforms have demonstrated context-dependent causal effects of chromatin marks \[37,38], the additional requirement for WRRA is to combine editor removal, reversible rescue, sister-lineage control, and multi-generational functions into a single pre-registration contract.

#### Safety Boundary

Along with functional recovery, cell identity, genomic stability, tumorigenicity, and reversibility are jointly assessed.

* In partial reprogramming, clock reduction is not automatically promoted to functional rejuvenation.
* Heritable editing of germ cells and embryos is excluded from the scope of this study.
* If even one safety gate fails, it is not judged as clinical memory correction.

Release = Function ∧ Identity ∧ Genome stability ∧ No tumorigenicity ∧ Controllability (62)

#### Track 4: Writing–Erasing–Rewriting Epigenetic Memory

To determine whether correlated markers are the cause of functional memory, the reversibility of the function must be measured by writing, deleting, and rewriting the markers at the same target. The amount of markers in the deleting model changed from 0.5050 to 0.0008 to 0.5090, and the recovery rate after rewriting was 1.008.

Rescue = (M\_rewrite−M\_erase)/(M\_write−M\_erase) = 1.008 (77)

| **Composition**      | **Requirements**                                                                                                            |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Target and contrast  | Identical locus, non-target guide, catalytically inactive effector, sham manipulation                                       |
| order                | write→washout→erase→washout→rewrite; check editing efficiency at each stage                                                 |
| result               | Markers, RNA, proteins, function, cell survival, sustained at least 3 divisions per lineage                                 |
| Causal determination | Writing and rewriting create directional functional changes, deletion reverses them, and the rescue threshold is satisfied. |
| Dismissal            | Only the label is reversible and the function is invariant, or described as off-target selection                            |

Table 36. Pre-registration contract for causal reversible editing.

| **Claim**                                 | **Current judgment**                          | **Next decision experiment**                 |
| ----------------------------------------- | --------------------------------------------- | -------------------------------------------- |
| Binding of DNA layer and protein state    | Support for the external subject holdout part | Direct genealogy tracing and time prediction |
| Additional information on the space niche | Supports only selected modules                | Spatial Intervention and External Cohort     |
| G→T→W non-commutative                     | Internal support of the model                 | 6 permutations equivalent wet-lab            |
| Causal memory of the cover                | OPEN                                          | Genealogical resolution write–erase–rewrite  |

Table 37. Integration of the Epigenetics–Cell Fate Axis.

Figure 4. Reversibility of memory markers and functional outputs in the write-erase-rewrite model.

### Next Step

It extends how cellular memory is prolonged amidst disease and herd selection to aging and cancer.

#### DOIs for This Chapter

DOI 10.1038/s41588-024-01706-w Systematic epigenome editing captures context-dependent chromatin function

DOI 10.1038/s41587-024-02213-3 Bidirectional epigenetic editing reveals hierarchies in gene regulation

One sentence from this chapter: A correlated marker is the cause of functional memory, then the function must also be reversible when the marker is written, erased, and rewritten at the same locus.

## Chapter 22

### Are Aging and Cancer Diseases of Memory?

In aging and cancer recurrence, changes in cellular state and clonal frequency occur simultaneously. It is necessary to distinguish whether the cells remaining after treatment have changed or if the original clones were selected.

### Established Scientific Starting Point

Clonal hematopoiesis, persister cells, sister cell tracking, and multi-omics lineage studies provide data that can separate induction and selection.

### WRRA Reconstruction

Life Model VII establishes the coupling dynamics between intracellular memory states and clonal frequencies. The key prediction is that even short-state memory can be transformed into long-group memory when combined with selection coefficients.

### Comparative Reading

Whether cells that have relapsed after cancer treatment have learned a new resistance state due to the drug, or whether originally rare resistant clones have survived, changes the treatment strategy. In the former case, re-establishment of the state is important, while in the latter, selective pressure and cloning are crucial. Both processes may occur simultaneously.

Sister cell designs are robust to this distinction. By treating one sister and observing the response, while preserving the other to read the pre-treatment state, one can evaluate whether future resistance is linked to existing residue. Clonal frequency and intracellular state must be tracked within the same model to avoid mistaking population-level memory for cellular memory.

At the boundary between interpretation and prediction, if only the frequency changes without the cell state changing, the induction term must be removed. Conversely, if state transitions are repeated within the same barcode, a selection-only model is insufficient.

### Research Content and Validation Results

#### Life Model VII: Memory Dynamics in Aging, Clonal Hematopoiesis, and Cancer Recurrence

Aging, clonal hematopoiesis (CH), and non-genetic resistance in cancer are not single diseases and cannot be reduced to the same molecular mechanisms. However, they can be compared through common dynamics in which past inputs alter multilayered states, which in turn change current responsiveness, survival, and proliferation, while selection reshapes population composition.

p\_post(y) = Z⁻¹∫K\_U(y|x)s\_U(x)p\_pre(x)dx (55)

K\_U is an induced state transition within the same lineage, and s\_U is a choice based on the existing state. If there is only a choice, K\_U(y|x)=δ(y−x); if there is only an induction, s\_U is independent of the state. The bulk difference before and after does not separate the two terms.

ΔȲ = Cov(wᵢ,Yᵢ)/w̄ + E\[wᵢΔYᵢ]/w̄ (56)

| **Memory level**  | **Definition**                                                       | **Key observations**                                |
| ----------------- | -------------------------------------------------------------------- | --------------------------------------------------- |
| molecular memory  | M/H/A/R/P/Q states remaining in a cell                               | Multiome re-stimulation after washout               |
| Genealogy memory  | Molecular state is passed on to offspring after division.            | barcode·EPI-Clone·sister-cell                       |
| collective memory | The frequency of specific states/clones itself is a long-term change | clone size · VAF · suitability · time to recurrence |

Table 22. Three memory levels and observation method of Life Model VII.

ReSisTrace traced the readiness for resistance before treatment based on the shared transcriptional characteristics of sister cells \[39], and cancer studies combining a single-cell multiome and barcode showed that both the transcriptional and accessibility status and genetic amplification before treatment can predict tumor formation and drug tolerance \[40]. EPI-Clone results from older blood showed that many young-type lineages coexist with a few extended and myeloid-biased lineages, leading to the direct consideration of population composition memory \[34].

#### Disease-Specific Differential Predictions

Ḃ\_age = ε\_write + ε\_restore + ε\_selection (57)

The predictive accuracy of the aging clock does not imply causality. Successful rejuvenation requires not only a reduction in the number of markers but also the restoration of stimulus-recovery trajectories, identity, and function similar to young cells.

s\_c(t)=f\_c(G\_c,Z\_c,U\_aged)−f\_WT(Z\_WT,U\_aged) (58)

In CH, DNMT3A and TET2 mutations alter the memory recording and erasing operators, and the aging and inflammatory environment may select the difference. The results showing that metformin lowered the competitive advantage and reversed abnormal DNA methylation and H3K27me3 in DNMT3A mutation HSPCs are preclinical evidence showing that a combination of genotype × state × environment may be involved \[42].

S ⇄ P → R; H\_relapse(T)=1−exp{−∫₀ᵀ\[αN\_P(t)+βN\_R(t)]dt} (59)

In cancer, sensitive S, reversible persister P, and stable genetically resistant R are isolated. Since the time window for R to develop widens as P survives longer, the risk of recurrence cannot be assessed solely by the number of residual cells immediately after treatment. A unique conclusion of Life VII is that even short-term cellular memory can become long-term collective memory through selective proliferation.

#### Falsification Conditions

* If the genome and current environment are controlled, past history does not provide additional predictive power for future responses.
* There are no induced transitions within the same barcode, and all changes are explained solely by existing clone selection.
* Directly erasing or editing candidate memory markers does not change restimulation, persistence, or differentiation.
* The WRRA mixed model does not predict external data as well as the genotype+current environment reference model.

### Next Step

We examine through spatial genealogy data whether the extracellular environment stores and returns such memories.

#### DOIs for This Chapter

DOI 10.1038/s41586-025-09041-8 Clonal tracing with somatic epimutations reveals dynamics of blood aging

DOI 10.1038/s41467-024-45478-7 Tracing back primed resistance in cancer via sister cells

DOI 10.1038/s41467-024-51424-4 · Multi-omic lineage tracing predicts determinants of cancer evolution

DOI 10.1038/s41586-025-08871-w · Metformin reduces the competitive advantage of Dnmt3aR878H HSPCs

One sentence from this chapter: In aging and cancer recurrence, changes in cellular state and changes in clone frequency occur simultaneously. It is necessary to distinguish whether the cells remaining after treatment have changed or whether the original clones were selected.

## Chapter 23

### Does Memory Exist Outside the Cell?

Cells do not live alone within tissues. The ECM, blood vessels, immune cells, oxygen, metabolites, and spatial structures preserve traces of past events and can alter subsequent reactions.

### Established Scientific Starting Point

Spatial transcriptomes and spatial lineage tracing measure the relationship between lineage and niche during tumor growth and metastasis. However, randomly dividing spatial points within the same sample overestimates generalization performance.

### WRRA Reconstruction

673,263 observations, 150 tumors, and 39 samples were aggregated at the tumor level, and sample group holdouts were performed. The selection module had an R2 of 0.201, but all module models deteriorated to an R2 of -0.023.

### Comparative Reading

Spatial niches are not merely backgrounds. Hypoxic regions, perivascular areas, the distribution of immune cells, and ECM rigidity alter cellular signaling and metabolism, and substances secreted by cells, in turn, change the niche. Ownership of memory can circulate between the cell and the environment.

The result where only the selected modules survive in the exogenous sample and the entire module model fails is an important warning. In high-dimensional spatial data, including many variables does not always mean capturing more biology. The entire sample must be held out, and it must be verified whether the pre-specified modules are reproduced in the new tumor.

At the boundary between interpretation and prediction is selectively supported, but cause and effect were not distinguished. External cohorts and spatial intervention determine the strong distributed memory claim.

### Research Content and Validation Results

#### Life Model IX: Distributed Biological Memory Stored Outside the Cell

The future of a cell is not determined solely by its internal epigenome. Stem cell niches, the extracellular matrix, immune cell composition, inflammatory cytokines, spatial structure, and microbiota can preserve the results of past stimuli and reconstruct internal states. Therefore, the ownership of memory is separated into cells, lineages, niches, and populations.

M\_total = M\_cell + M\_lineage + M\_niche + M\_population + M\_interaction (63)

Xᵢ(t+1)=F\[Xᵢ(t), ΣⱼWᵢⱼXⱼ(t), N(t), U(t)] (64)

| **Cell**                 | **Niche**                | **Key Interpretation**                                |
| ------------------------ | ------------------------ | ----------------------------------------------------- |
| young state/no treatment | young state/no treatment | base line                                             |
| young state/no treatment | Aging/Past Stimulation   | sufficiency of niche memory                           |
| Aging/Memory status      | young state/no treatment | Persistence and Reversibility of Intracellular Memory |
| Aging/Memory status      | Aging/Past Stimulation   | Combination, interaction, and reinforcement           |

Table 24. Cell × niche 2 × 2 crossover design of Life Model IX.

ΔY = ΔY\_cell + ΔY\_niche + ΔY\_cell×niche (65)

Each term is separated using cross-transplantation, conditioned medium, decellularized matrix, immune cell reorganization, or spatial omics. If the young niche restores senescent cells, the cell-autonomous strong memory model is reduced, and if cells that have erased their memory form the same state again in the senescent niche, it means that the niche is a memory restorer.

#### Falsification Conditions

* There is no additional effect of niche history after controlling the internal cellular state.
* The niche exchange effect is entirely explained by cell viability, cell type composition, or a single medium component.
* Even including the spatial relationship W, holdout prediction is not improved compared to the independent cell model.

#### Track 2: Spatial Tumor Lineages and Niche Memory

The total number of observations in the spatial lineage data is 673,263, including 150 tumors and 39 biological specimens. After aggregating at the tumor level, Spearman associations were calculated, and cross-validation that excluded entire sample populations was used to prevent leakage of spatial points within the same specimen.

| **Module** | **Spearman ρ** | **p**  | **FDR** |
| ---------- | -------------- | ------ | ------- |
| M2         | 0.486          | 0.0002 | 0.0011  |
| M7         | 0.382          | 0.0002 | 0.0011  |
| M6         | 0.317          | 0.0210 | 0.0330  |
| M8         | 0.222          | 0.0114 | 0.0220  |
| M3         | −0.169         | 0.0120 | 0.0220  |
| M10        | −0.281         | 0.0004 | 0.0015  |
| M4         | −0.386         | 0.0008 | 0.0022  |

Table 32. Significant spatial module–pedigree association after multiple test correction.

| **Model** | **Explanation**       | **R²** | **MAE** |
| --------- | --------------------- | ------ | ------- |
| S0        | Segmentation standard | −0.130 | 0.0648  |
| S1        | Pre-selection module  | 0.201  | 0.0549  |
| S2        | All modules           | −0.023 | 0.0605  |

Table 33. Sample group holdout prediction performance.

The results selectively support the idea that niche information can provide additional predictive power regarding lineage or tumor status. Since the model with all modules deteriorates at the holdout stage, the strong proposition that “more spatial information is better” is rejected. Lineage-specific temporal data and interventions are required to determine whether the associated niche is a cause or an effect.

Figure 5. Spatial module association and sample group holdout generalization.

### Next Step

The final extension example is WRRA-Worm, which examines whether the execution grammar of cells applies to the nervous system and behavior.

#### DOIs for This Chapter

DOI 10.1038/s41588-026-02739-z Spatiotemporal lineage tracing of tumor growth and metastasis

DOI 10.5281/zenodo.19771805 · Processed spatial lineage-tracing data

One sentence from this chapter: Cells do not live alone within a tissue. The ECM, blood vessels, immune cells, oxygen, metabolites, and spatial structures can preserve traces of past events and alter subsequent reactions.

## Chapter 24

### Extending WRRA to the Nervous System and Behavior

Just because genetic information creates a cell does not mean that behavior is output directly from DNA. Neural connections, current activities, sensory inputs, the body's state, and the environment form a closed loop.

### Established Scientific Starting Point

C. elegans has a known connectivity map of 302 neurons and has accumulated calcium imaging and behavioral data, making it a testing ground for the whole nervous system-body-environment model.

### WRRA Reconstruction

WRRA-Worm 0.1 constructed a sensorimotor loop of 23 nodes and 57 relationships. It passed AVA and AVB removal, same-current restart, and resource ledger internal inspection.

### Comparative Reading

The connectome provides part of the source or law of behavior, but it does not fix the actual trajectory. Even with the same connections, behavior changes if neuromodulators, sensory inputs, body posture, and feedback from muscles and the environment differ. Reading the nervous system solely as a wiring diagram is the same kind of abbreviation as reading DNA solely as a sequence.

The next step of WRRA-Worm is to connect the 23-node toy circuit with actual 302-neuron data. It must simultaneously predict calcium activity and behavior, and make predictions in experiments involving neuronal ablation and the absence of sensory stimulation. Closed-loop external validation is a stronger threshold than open-loop fitting with the body and environment removed.

The boundary between interpretation and prediction is not an independent biological discovery, but rather a PASS for the internal consistency of the toy circuit. The closed-loop external verification of the formal connectome, actual calcium kinetics, and behavior is OPEN.

### Research Content and Validation Results

#### WRRA-Worm: Extending Relations and Behavior beyond Genetic Information

Life does not end with gene expression. WRRA-Worm 0.1 implements the sensory–neuromotor loop of C. elegans with 23 nodes and 57 relationships. This model places neurons as information sources, chemical synapses and electrical connections as relationships, senses, muscles, the body, and the environment as boundaries, and adaptive states and resources as current residue.

vₖ₊₁=tanh{0.72vₖ+qₖ⊙\[W\[vₖ]₊+GΔvₖ+0.85uₖ−0.62aₖ]} (37)

aₖ₊₁=clip(0.94aₖ+0.06|vₖ₊₁|,0,1) (38)

| **Internal inspection**        | **Result** | **Margin**                                 |
| ------------------------------ | ---------- | ------------------------------------------ |
| Reversal after forward contact | 0.071587   | Design path operation                      |
| AVA Reversal                   | 0          | Wired dependency                           |
| Forward after rear contact     | 0.021224   | Design path operation                      |
| AVB removal forward            | 0          | Wired dependency                           |
| Same current restart error     | 0          | Verification of determinism implementation |
| Initial/Final Resource Ledger  | 23/23      | Dimensionless internal preservation        |

Table 18. WRRA-Worm 0.1 Internal Results.

This case illustrates an upper renderer layer where cellular components generated from genes lead to behavioral phenotypes through network-state-environment loops. However, the full 302-neuron model, polarity and weight measurements, calcium imaging, muscle-body-environment closed loops, and holdout excision verification are open.

### Next Step

Now, the research results are translated into audit procedures for actual gene editing and cell design.

One sentence from this chapter: Just because genetic information creates a cell does not mean that behavior is output directly from DNA. Neural connections, current activity, sensory input, the state of the body, and the environment form a closed loop.

## Part 5

### Biotechnology Applications of WRRA

It transforms the success of gene editing and cell design from sequence alteration into a continuous audit contract of execution, function, boundaries, and lineage.

## Chapter 25

### How Should Gene Editing Be Audited?

Treatment or functional design is not complete simply because the edited bases match the target. Editing efficiency, expression, protein, cellular function, lineage stability, and tissue environment must be verified in sequence.

### Established Scientific Starting Point

The field of gene editing evaluates on-target, off-target, delivery efficiency, mosaicism, immune response, and long-term safety. The WRRA organizes these items according to information ownership and implementation phases.

### WRRA Reconstruction

An audit contract separates source changes, state disturbances, renderer sufficiency, observable functions, boundary delivery, and lineage persistence. It must be possible to identify which layer failed in order to fix the next design.

### Comparative Reading

The first question in a gene editing audit is whether the target base has changed. The second is whether that change has been delivered to RNA and proteins; the third is whether it has altered cellular function; the fourth is whether it is safely maintained within the tissue; and the fifth is whether efficacy and safety persist across the lineage. Success in the previous step does not guarantee the next.

This procedure is not intended to punish failure, but to make it correctable. If editing is accurate but the protein is deficient, the expression renderer must be modified rather than the delivery vehicle; if it succeeds in vitro but disappears in vivo, the niche and immune boundary must be corrected. The direction of process improvement becomes clear when the owner of the failure is identified.

The boundary between interpretation and prediction: In vitro editing success is not elevated to bio-therapeutic prediction. If cell type, dose, time, tissue environment, and follow-up generation change, new prediction and external validation are required.

### Research Content and Validation Results

#### The WRRA Audit Contract for Gene Editing

Before editing, not only the target sequence but also the expected off-target, cell line, medium, and replication status, required implementers, growth selection bias, measurement time, and daughter cell delivery are frozen together. After editing, instead of looking solely at expression levels, the full-length protein, activity, metabolic burden, membrane/mitosis, and lineage persistence are verified stepwise. This is not an experimental recipe for a specific editing technique, but a causal ledger for interpreting results.

### Next Step

This contract expands to protein design, organoids, cell therapy, cancer, and biomanufacturing.

#### DOIs for This Chapter

DOI 10.5281/zenodo.22290829 · Executable Genetic Expression in WRRA

One sentence from this chapter: Treatment or functional design is not complete simply because the edited bases match the target. Editing efficiency, expression, protein, cellular function, lineage stability, and tissue environment must be verified in sequence.

## Chapter 26

### Biotechnology Applications of WRRA

The practicality of WRRA lies not in giving it a new name, but in finding the missing layer of action in complex biotechnological processes.

### Established Scientific Starting Point

iPSCs, organoids, immunocell engineering, regenerative medicine, protein design, and biomanufacturing all combine genetic information and environmental control. Failure often occurs in the state, process, space, and lineage, rather than in the target sequence.

### WRRA Reconstruction

In iPSCs, initialization residue and differentiation sequences are recorded as key renderers; in organoids, spatial niches and boundaries; in cell therapy, in vivo viability and lineage stability; and in protein design, folding and complex assembly.

### Comparative Reading

In iPSCs and organoids, the initial state and processing sequence determine quality, even within the same genetic background. In cell therapy, in vivo survival, migration, function, and organ lineage are more important than pre-administration phenotype. In protein design, it is necessary to verify that the calculated structure is actually expressed, folds, assembles into complexes, and functions within the cellular environment.

For WRRA to contribute as a biotechnology platform, the SOURCE, STATE, RENDERER, BOUNDARY, OBSERVABLE, and LINEAGE fields must be standardized for each process, and inter-batch failures must be predicted using these fields. If external batch performance is improved compared to existing quality control, it gains practical value; otherwise, it remains merely a useful record system.

The boundary between interpretation and prediction: For WRRA to be considered successful, it must improve the quality, yield, safety, or failure prediction of external batches compared to existing process models. Simple reclassification alone does not constitute a predictive contribution.

### Research Content and Validation Results

### Applications in Genetic Engineering and Synthetic Biology

The practicality of WRRA lies in changing the order of design and verification rather than in new terminology. Instead of starting with “which DNA to insert?”, it simultaneously specifies the source, law, state, renderer, boundary, and phylogenetic transfer necessary to create target observations.

* Degrading the target OBSERVABLE into yield, activity, error, cell viability, and progeny functions.
* Separate DNA/RNA SOURCE and executer inventory, and indicate the provenance of external supply, inheritance, and self-regeneration.
* Freezes the gates and failure conditions of Warrior, Translation, Dialogue, Act, and Split in advance.
* Measure executor dependencies by swapping the same source in different executors.
* It traces from the mother cell to the two daughters and granddaughter generations to separate single-shot output and line closure.
* Separate the variables used for correction and the holdout prediction, and set uncalculated items to null.

| **Applications**                            | **Tools provided by WRRA**                                          | **First, the measured amount**                     |
| ------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------- |
| Minimum expression cassette                 | 3n+3 lower bound + R ledger per executor                            | Startup · Fully Yield · Error                      |
| Protein expression optimization             | Length–Processivity·Executor Swap                                   | Total equipment ratio, activity, and decomposition |
| cell-free system                            | Seed inventory and regeneration ratio                               | 2nd Generation Active/Parent Active                |
| Minimal Genome Design                       | Five Gates and Single Removal Audit                                 | Not only growth, but also division and recovery    |
| synthetic primitive cells                   | Information, Catalyst, Membrane, Energy, Distribution Joint Closure | P0/P1/P2 and R\_life                               |
| Gene circuit                                | Fixed Current · Residual State · Boundary Input                     | Restimulation/Recovery Holdout                     |
| CRISPR/Perturb-seq                          | Static/Time claim gate, target exclusion, FDR                       | External cell line prediction                      |
| System stability                            | copy-number frontier · active equalization                          | Number of paired daughters                         |
| Control of cell division                    | geometry covariance signature                                       | Volume ratio, cleavage surface, covariance         |
| whole cell digital twin                     | Module-specific provenance and fail-closed output                   | Independent doubling time and disturbance response |
| Evolutionary Engineering                    | R\_life and error threshold/environment renderer                    | Functional survival by generation                  |
| Neurobehavioral genetics                    | Gene → State → Relationship → Body–Environment Closed Loop          | Restraint, recovery, and behavioral transference   |
| Epigenetic memory map                       | pedigree distance × time × inter-layer transfer matrix              | C(d), λ\_r, A\_state                               |
| Cell Fate Programming                       | G/T/W Order Optimization and Washout                                | Multigenerational Fate Score                       |
| Aging and CH Risk Stratification            | Genotype + Clonal Growth + Inflammatory Memory                      | VAF, growth rate, restimulation                    |
| Cancer minimal residual disease             | persister number × memory time integral                             | Recurrence time · barcode                          |
| Regenerative and cell therapy manufacturing | Shipment audit of culture, freezing, and inflammation history       | Identity and genealogical functions                |
| Tissues and Organoids                       | cell × niche distributed memory intersection                        | Spatial state and condition exchange               |

_Table 28. Future Application Areas of Genetic Engineering._

#### A WRRA Interpretation of Protein and Enzyme Design

The theoretical function of a sequence is at the SOURCE/Law level, while actual expression, folding, cofactor binding, intracellular localization, toxicity, and degradation are at the Renderer/State level. Therefore, function is not declared solely by sequence scores; executor swaps, length holdouts, separation of activity and yield, and seed carryover audits are necessary. The low whole-length ratio of long proteins can be broken down into processivity, resource, structure, and quality control layers rather than being absorbed as a single promoter issue.

### Case Study: WRRA-Motor H2

WRRA-Motor H2 is an actual research case that went beyond merely imagining a “walking protein” in words; it involved separating the validated execution unit of existing kinesin-1 and a newly designed regulatory unit, leaving behind candidate sequences, calculations, failure conditions, and experimental plans. Candidate H2-b2f820d18e is a total 385 α protein that preserves the human KIF5B motor core 1–353 α and adds a 32 α coiled-coil WRRA gate. The design gate sequence is VQNIEQKIANLKEEGAAALQQVEQKIQNLKAE, and the CDS, back-translated assuming human cell expression, is 1,158 nt including the stop codon.

The current determination for this case is PREDICTED\_SEQUENCE\_ONLY · Actual walking OPEN. While the sequence and DNA design exist, the atomic structure, proper folding, dimeric walking, ATPase conservation, and cargo transport have not yet been verified. Therefore, calling H2 a “walking protein” refers to the target function and candidate lineage, not to an experimentally closed phenotype. Preserving this boundary is the first rule of WRRA-style AI collaboration.

_Table 28A. Domain Profile rewritten with H2 gait problem as WRRA Core field._

| **Core field**          | **Correspondence in H2**                            | **Questions to close**                                                 |
| ----------------------- | --------------------------------------------------- | ---------------------------------------------------------------------- |
| SOURCE                  | KIF5B 1–353 aa + 32 aa gate                         | Which residue is inherited and which residue is designed               |
| LAW / RELATION          | ATP hydrolysis, microtubule polarity, head gating   | Does the energy input combine with the directional transition?         |
| STATE / RESIDUE         | Bonding of two heads · nucleotide state, gate state | Does the current state uniquely restrict the next transition?          |
| BOUNDARY                | Protein–microtubule–solution–cargo boundary         | How are the externally provided structures, fuel, and tracks recorded? |
| COMMON CARRIER / UPDATE | Mechanochemical transition of linked dimers         | Does a change in one head alter the probability of another head?       |
| RENDERER                | Folding, dimerization, ATPase, binding and stepping | Is the sequence realized as an actual exercise machine?                |
| PHENOTYPE / OBSERVABLE  | Speed, run length, 8 nm step, load response         | Is directional walking observed at the single-molecule level?          |

#### From a Minimal Walking Contract to Candidate Sequences

Prior to design, the minimum contract for “walking” was frozen. Two alternating contact points, an energy input that disrupts equilibrium, a polarized track, a record of the current state, and coordination between the two contact points must all be present. If the state vector is set as Xₜ=(B\_A, B\_B, N\_A, N\_B, E, G), B represents the combination of two heads, N represents the nucleotide, E represents the energy state, and G represents the gate state. One period is recorded as S₀(x)→S₁(x)→S₂(x+8 nm)→S₀(x+8 nm). However, this equation does not prove an 8 nm shift. xₙ=x₀+8n nm holds only when the physical system actually implements each transition.

The directionality can be expressed as k₊/k₋=exp(A) and A=(Δμ−W\_load)/(kBT). Under the simple condition of no separation, p₊=1/(1+exp(−A)), and the average displacement per period is d·tanh(A/2). The ideal upper bound for Fd<Δμ, substituting Δμ≈20kBT, T=310 K, and d=8 nm, is approximately 10.7 pN, but this is not a predicted value for the stall force of H2. It is merely an energy boundary excluding efficiency, internal losses, gate deformation, and multipath.

_Table 28B. Candidate lineage and questions answered by each candidate._

| **Candidate** | **composition**                 | **Usage and current judgment**                                     |
| ------------- | ------------------------------- | ------------------------------------------------------------------ |
| P0            | KIF5B 1–560                     | Positive control; criteria including known stalks                  |
| H1            | KIF5B 1–353 + GCN4              | Correction candidates for the dimerization and gait test system    |
| H2            | KIF5B 1–353 + Design gate 32 aa | Core Candidate; PREDICTED\_SEQUENCE\_ONLY                          |
| N1            | completely de novo motor        | FAIL\_CLOSED\_NO\_SEQUENCE\_EMITTED due to insufficient validators |

H2's 353 aa represents 91.69% of the inheritance domain, and 32 aa represents 8.31% of the design domain. Gate candidates were selected by generating 512 samples in Protein Renderer 0.3 using a fixed seed of 260908, filtering them, and preserving the top 5. The gate score of 5.0806 is a heuristic rank value, not a walking probability. The reverse translation DNA is also PREDICTED\_NOT\_SYNTHESIS\_READY. Since it lacks a promoter, Kozak, UTR, poly(A), vector, and fluorescent/cargo tag, it cannot be immediately referred to as a construct for cell experiments.

#### Conditional Walking Simulation: The First Trajectory of H2

Since actual speeds and separation rates cannot be calculated solely from candidate sequences, Figure 6 was constructed as a conditional Monte Carlo experiment to demonstrate “what trajectories emerge if these probabilities are correct,” without simulating actual values. Assuming 400 motors perform a maximum of 60 ATP drive cycles, forward speeds of 0.905, backward speeds of 0.075, and track separation speeds of 0.020 were assumed for each cycle. The step was set to 8 nm, and the random seed was fixed at 260908, the same as in candidate generation. Separated motors were recorded as not moving further from that position.

Figure 6. Functional conceptual diagram of WRRA-Motor H2 and actual conditional Monte Carlo simulation. The average of 400 iterations was 240.5 nm after 60 cycles, and 66.5% were separated at least once. These figures are the result of assumptions, not the measured values of H2. When single-molecule TIRF or optical trap results are input, the probabilities are replaced with estimates, and the prediction-observation difference is calculated using the same code.

The reproduction algorithm is simple. For each cycle, a random number u between 0 and 1 is drawn for the motor that is still attached. If u < 0.905, it is recorded as +8 nm; if 0.905 ≤ u < 0.980, as -8 nm; and if u ≥ 0.980, as detachment. The average of 400 trajectories, the 10–90 percentiles, and the attachment rate are calculated for each cycle. By changing the seed, probability, and number of cycles, the reader can first explore conditions such as “where directionality is maintained but processivity breaks down” or “where the probability of reverse increases with increasing load.”

### Using WRRA Core 1.0 as an AI Reference Document

The official frozen version is WRRA Core 1.0: A Domain-Agnostic Execution Architecture, published at https://doi.org/10.5281/zenodo.22650956. The publication date is 2026-09-08, the version is 1.0, and the license is CC BY 4.0. Download the English PDF frozen version from Zenodo Files and save it in the research folder as is. In 00\_manifest, record the full filename, DOI, version, download date, and MD5 b2c77039ab202a1f9da7baf1b1c9d3fc as displayed in Zenodo. If no one else receives the same input, it cannot be said that the AI results have been reproduced \[75].

Here, the term “training AI” must be divided into three layers. First, attaching PDFs to conversations or projects to use as reference documents does not constitute retraining that changes model weights. Second, RAG, which fragments documents into search indexes and retrieves relevant sections for each question, is also a method of attaching external memory. Third, fine-tuning is a separate training process that adjusts the model's response behavior using multiple input-correct answer examples. Rather than attempting to memorize the core through fine-tuning from the start, a document-based approach that maintains original text search and citations is more advantageous for revision, auditing, and error correction.

_Table 28C. Three ways to connect WRRA Core to AI._

| **method**            | **What actually changes**                      | **Recommended Uses and Precautions**                                                                        |
| --------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Conversation attached | context of the current conversation            | Suitable for the first practice session; re-attach/instruct in the new conversation                         |
| Project / RAG         | Searchable external document memory            | Recommended for long-term studies; save searched sections and answers together                              |
| Fine-tuning           | Model weights that influence response patterns | Only when sufficient examples and evaluation sets are available; the latest Core search is still necessary. |

For document-based setup, the following sequence is safe:

{% stepper %}
{% step %}
#### Create a new study space

Attach the Core PDF.
{% endstep %}

{% step %}
#### Restore Core elements

Before generating a solution for the AI, have it restore the fixed elements of Core and selectable elements from applications into a table.
{% endstep %}

{% step %}
#### Separate source text and inference

For each answer, have it separate the clauses/expressions of the original text from the AI's inference.
{% endstep %}

{% step %}
#### Create a Domain Profile

Create a Domain Profile for the current problem.
{% endstep %}

{% step %}
#### Obtain human approval

A human researcher approves the question, exclusion range, observations, and stopping conditions.
{% endstep %}

{% step %}
#### Generate only after approval

Allow candidate generation or computation only after that.
{% endstep %}

{% step %}
#### Store reproducibility information

Store the input document, prompt, model/tool version, date, seed, and failure candidates together with each output.
{% endstep %}
{% endstepper %}

#### Reference Prompt for the First Conversation

{% prompt description="Reference prompt for the first conversation" icon="sparkles" openInAIProviders="true" defaultExpanded="full" %}
```markdown
Use the attached frozen version of WRRA Core 1.0 as the constitutional reference document for this study. Do not replace the term "Core" itself with a new one or omit it. First, restore the sequence of SOURCE→RELATION/LAW→STATE/RESIDUE→BOUNDARY→COMMON CARRIER→UPDATE→RENDERER→PHENOTYPE→OBSERVABLE/RECORD/LEDGER along with the original source. Next, convert this problem into a Domain Profile, distinguishing between FACTS, ASSUMPTIONS, DERIVATIONS, PREDICTIONS, and OPENS. Do not generate candidates before human verification. If a validator or necessary input is missing, do not fill it with guesses; instead, return FAIL_CLOSED and null. Attach the owner, input data, basis for calculation or citation, and counter-evidence conditions to all conclusions. First, output only (1) the Core reconstruction table, (2) missing information, and (3) questions to be decided by a human.
```
{% endprompt %}

Since AI can confidently generate incorrect Core summaries, the initial response is not used as is for the study. A human verifies whether the minimum calculation, common carrier, phenotype, fixed-present, ownership, boundary, renderer, record/ledger, and fail-closed information have all been restored from the original text. If any omissions are found, the relevant pages are provided again, and the responses before and after the correction are recorded together in the ledger.

#### Standard Workflow for AI-Assisted Research

{% stepper %}
{% step %}
#### Question freezing

Instead of “create a new protein,” write an observable goal such as “create a candidate showing an ATP-dependent 8 nm directional shift in a polar microtubule and determine which data determines actual walking.”
{% endstep %}

{% step %}
#### Separation of Evidence

Place standard biology, WRRA reconstructions, researcher's assumptions, AI-generated candidates, and open items in different columns. Since AI statements are not primary evidence, return to the original papers and database texts.
{% endstep %}

{% step %}
#### Minimum Contract

First, fix the conditions required for success and failure. In H2, this corresponds to two contacts, energy, track polarity, state recording, and head coordination.
{% endstep %}

{% step %}
#### Baseline and Negative Control

Determine a control such as P0, H1, generic coiled coil, or scrambled gate before the candidate. If you only calculate the candidate, you cannot know the reason even if a good result is obtained.
{% endstep %}

{% step %}
#### Search and provenance

When AI enumerates structures and sequences, it stores the search space, filters, scoring formulas, seeds, and reasons for elimination. In H2, the top 5 were kept after going through 64 structure proposals and 512 gate candidates.
{% endstep %}

{% step %}
#### Independent Verification

Do not use the self-evaluation of the same AI as verification. Connect different tools and physical measurements such as sequence QC, structure predictor, oligomer-state analysis, ATPase, single-molecule imaging, and loading tests.
{% endstep %}

{% step %}
#### Claim Ledger

Distinguishes between “calculated”, “predicted”, “experimented”, and “independently reproducible”. H2 is currently closed only up to candidate sequence calculation and DNA back-translation.
{% endstep %}

{% step %}
#### Final Human Approval

Researchers are responsible for objectives, biosafety and ethics, data disclosure scope, experimental design, and the final sentences of the paper. Scientific ownership and responsibility are not transferred to AI.
{% endstep %}
{% endstepper %}

_Table 28D. Tasks performed by humans, AI, and external verifiers in H2._

| **Subject**      | **Key roles**                                                                                    | **A judgment that should not be entrusted**  |
| ---------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| human researcher | Question, Scope, Judgment Criteria, Safety, Final Claim Approval                                 | Automatic approval without reading the basis |
| AI               | Literature structuring, omission checking, calculation, candidate enumeration, code and drafting | Declaring an untested feature as a fact      |
| External tools   | Sequence testing, structure and oligomer prediction, statistics and simulation                   | Replace self-scores with biological proof    |
| experiment       | Measurement of expression, solubility, ATPase, single molecule transfer, and load response       | Single success video without a control group |

#### Reader Exercise Following H2

On the first day, the Domain Profile and OPEN list for H2 are constructed using only the Core PDF and the above standard prompts. On the second day, a comparison table for P0/H1/H2/C1/C2 is created, and each measurement is linked to which claim is closed. On the third day, the effects of forward bias and detachment on speed and run length are calculated by modifying the probabilities in Figure 6. On the fourth day, the AI is instructed to create three blind datasets assuming experimental results, and PASS/FAIL/OPEN are classified using pre-frozen decision rules. Finally, the sentence initially proposed by the AI is compared with the sentence accepted after verification.

The measurement sequence of the experimental phase is expression/solubility → oligomer state → ATPase → microtubule landing rate → velocity and run length → frequency of simultaneous separation of two heads → load response. P0 is set as the positive control, B0 as the motor core alone, H1 as the known dimerization correction, C1 as the standard coiled coil, and C2 as the scrambled gate. Even if H2 is expressed, if there is no ATPase, motor execution is considered a failure; even if ATPase is present, if there is no directional step, walking is considered a failure; and if walking occurs without cargo transport, the transport claim is left OPEN.

#### Reproducible research ledger

It is recommended to arrange the research folder in the following order: 00\_manifest, 01\_sources, 02\_prompts, 03\_domain\_profile, 04\_candidates, 05\_code, 06\_results, 07\_failures, and 08\_claim\_ledger. In the manifest, record the WRRA Core DOI, version, and checksum, as well as the exact names, versions, and dates of the models and tools used. For each candidate, attach the ID, parent sequence, inheritance/design boundaries, generation prompt, seed, filters, and reason for rejection. In the results file, separate the raw and processed data, and save the code and parameters used to generate the figures. Since deleting failed candidates prevents the auditing of search bias and hindsight bias, the FAIL\_CLOSED record should also be preserved as a research outcome.

Fine-tuning is considered after a sufficient number of iterations have been accumulated through this document-based procedure. Example pairs are created for WRRA compliance and violation analyses, and training, validation, and final test sets are separated. Evaluation metrics are set based on Core field omission rates, unsubstantiated closure rates, provenance omission rates, identical input reproducibility, and inter-rater agreement, rather than literary style. The fine-tuned model must also continue to use Core source search and the argument ledger, and if the frozen version is revised, it is re-evaluated with the new version.

{% hint style="warning" %}
Undisclosed patient data, pre-patent sequences, or institutionally restricted data are not uploaded until the preservation, learning, and sharing policies and research ethics of the AI service being used are verified. Sensitive operations are performed in an approved closed environment or local model, and only the minimum necessary provenance is retained in the public version. Reproducibility and openness cannot take precedence over personal information, biosafety, or intellectual property rights.
{% endhint %}

### Next Step

In the final chapter, the closed results and remaining decisive experiments are organized into a single research lineage.

#### DOIs for This Chapter

DOI 10.1038/s41588-024-01706-w Systematic epigenome editing captures context-dependent chromatin function

DOI 10.1038/s41587-024-02213-3 Bidirectional epigenetic editing reveals hierarchies in gene regulation

DOI 10.1038/s41467-026-69531-9 · Integration of DNA replication and phospholipid synthesis in a synthetic cell

The practicality of WRRA in this chapter lies in freezing the Core as a reference document and separating the roles of humans, AI, and validators to track candidates like H2 to observable experiments and claim ledgers in the sequence.

**WRRA BIOLOGY**

## Chapter 27

### Decisive Experiments for the Next Generation

This book does not end by declaring that life has been completed. It ends by specifically stating what needs to be measured to close the next boundary.

### Established Scientific Starting Point

Strong biotechnological claims require external verification, lineage tracing, material balances, functional rescue, and independent reproduction. The success of different modules should not be aggregated as the autonomy of a single system.

### WRRA Reconstruction

The priority is complete PURE self-regeneration, live Syn3A all-daughter molecular distribution, 3rd generation autonomous protocell without external material replacement, LARRY original data residue verification, 6-permutation GTW, and pedigree resolution write-erase-rewrite.

### Comparative Reading

The remaining experiments are not independent lists. PURE's translator reproduction, Syn3A's distribution, and Protocell's phylogenetic persistence form a single axis of autonomous life. LARRY residue, GTW sequences, and write-erase-rewrite form the causal axis of epigenetic memory. Both axes require the direct measurement of generations and lineages to cross the final threshold.

The most efficient next step in research is to precisely target the weak links of each axis rather than conducting a single massive experiment. Voice results are also used to reduce the decision rules. Ultimately, what this book leaves behind is not a declaration of completion, but a map of measurable next questions, and that map must be continuously updated according to new data.

Boundary between interpretation and prediction: The most accurate conclusion at present is that while the two-axis audit structure is complete, strong causality and the closure of autonomous life remain. The determination rule has already been fixed to reduce the relevant term if the following data yields a contradictory result.

### Research Content and Validation Results

### Priority Research Plan

| **priority** | **research**                                            | **Pre-registration Key Points**                                                    | **Success/Failure Criteria**                                     |
| ------------ | ------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| 1            | Paired Syn3A all-daughter molecular coefficients        | Molecular panel · Error model · Critical value · Split surface                     | P0/P1/P2 · Covariance holdout                                    |
| 2            | PURE Generational Regeneration                          | seed dilution · whole protein · functional activity                                | 2nd generation ratio≥1 or failure to freeze                      |
| 3            | Time Perturb-seq Retry                                  | M0/M1/M2 Same Budget · New Perturbation                                            | M2 Holdout Advantage or Residual Disposal                        |
| 4            | Syn3A independent doubling time                         | 105 minutes unused parameters                                                      | Five Gates Maximum Time Hit                                      |
| 5            | analogue of first life                                  | Mother-daughter-granddaughter tracking, K and f freezing                           | R\_life > 1 repetition or insufficient                           |
| 6            | C. elegans c302 closed loop                             | connectome hash · polarity uncertainty · resection holdout                         | New stimulus/Direction and timing of abstinence hitting the mark |
| VA           | Independent genealogy-based multilayered memory map     | Prohibition of Separating Generations and Elapsed Time, and Circular Argumentation | Reject M2 holdout dominance or combined model                    |
| VI-A         | G/T/W six permutations                                  | Actual nuclear AUC, occupancy, and washout match                                   | GTW differential or P3 rejection                                 |
| VII-A        | Cancer sister-lineage induction–selective decomposition | Pre-treatment sister preservation · barcode time series                            | Mixed model external forecasting or downsizing                   |
| VIII-A       | Reversible editing of memory markers                    | write–erase–rewrite · Multigenerational function                                   | Reversible rescue or withdrawal of causal claim                  |
| IX-A         | Cell × Niche 2×2 Cross                                  | Independence of cell state and environmental history                               | Reproduction of interactions or reduction of distributed memory  |
| XA           | synthetic primitive cell repetitive closure             | Simultaneous measurement of Λ\_auto·K·f·R\_life                                    | 3rd generation or more R\_life>1 or failure                      |

_Table 29. Next step of the power criterion._

#### The Decisive Paired-Daughter-Cell Experiment

Two daughters from the same mother cell must be paired to preserve sister anticorrelation.

Connect the number of mother cell molecules, the number of daughter molecules, the volume ratio, the division plane, and the next growth and division of each daughter.

A separate error model is frozen so that measurement errors are not mistaken for biological overdispersion.

Compare the binomial baseline, common geometric model, localized block model, and active equalization model with the same data and complexity.

If the threshold is changed after viewing the result, it is demoted to CALIBRATION.

#### Completing the Two Axes: What Is Closed and What Remains Open

Axis I connects DNA information to RNA and protein execution, partial self-renewal, finite distribution, proto-cell lineage continuity, and the boundary of primordial life. Axis II connects the molecular state to epigenetic memory, differentiation, spatial context, computational sequence, and reversible causality. Integration at the structural and audit levels is complete in the sense that operational variables, thresholds, present judgments, and falsification conditions have been assigned to all questions, but not all biological closures have been passed.

_Table 42. Final two-axis base map._

| **axis**               | **Confirmed evidence of a positive result**                                                                   | **Voice · Basis for restriction**                                                           | **The decisive remaining experiment**                                                                                                   |
| ---------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| I. DNA → First Life    | DNA/Protein Execution, PURE Single Reconstitution, Syn3A Computational Distribution, Protocell ≥3 Generations | PURE mass ratio 0.08; absence of direct daughter cell measurement; protocell non-autonomous | A single lineage of ≥3 generations with R\_life > 1 that updates genome, translation, energy, and boundaries without material exchange. |
| II. Memory → Cell Fate | Cross-individual DNA–protein binding, selective niche generalization, declarative model GTW order             | Direct LARRY residue, lineage of GTW and reversible editing, causality unmeasured           | Paired lineage resolution write–erase–rewrite and function recovery, maintaining ≥3 fission                                             |

_Table 43. Argument terms to be fixed in subsequent revisions._

| **cover**          | **Significance in this paper**                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| PASS               | Declared operational thresholds are satisfied by direct or author-reported evidence. Scope restrictions remain in place. |
| COMPUTATIONAL PASS | The simulation and interpretation null model meets the threshold. This is not a claim of biometrics.                     |
| INFERRED           | Inferences calculated based on reported figures and stated assumptions. Not the author's actual measurements.            |
| FAIL               | The measurement is on the rejection side of the declaration threshold.                                                   |
| OPEN               | Measurement of required resolution is unavailable or inaccessible.                                                       |
| NOT ESTABLISHED    | Even if the narrow threshold is passed, there is insufficient evidence to support a stronger argument.                   |

### Conclusion

The entire flow of WRRA biological research now connects two closures. First, while DNA is a source of possible proteins, polymerases, ribosomes, metabolism, membranes, mitotic geometry, and daughter cell distribution must be reconstructed together to form a living lineage. Second, already living cells do not determine the present solely by the genome, but render past inputs into present responsiveness and future destiny through methylation, histones, accessibility, RNA, proteins, metabolism, and memories distributed across niches.

Life Model V–X makes this second closure a measurable research program. V covers multiple proper modes of memory and interlayer transmission, VI covers the non-commutative order of fate manipulation, VII covers induction states and clonal selection, VIII covers the reversible causal editing of memory markers, IX covers extracellular distributed memory, and X covers the critical conditions under which memory–execution–retrieval–boundary–selection closes to the original biological lineage. The most important new conclusion is that short cellular memory can be converted into long collective memory through lineage transmission and selection even without the long half-life of a single marker.

This paper does not declare the empirical verification of new laws of biology. The precise coding lower bound, finite distribution, and branching equations were closed under specified assumptions, and the minimal cell, first life, and memory models were formulated to be structurally executable. However, the interlayer memory matrix, GTW optimal order, memory integrals for aging and cancer, write–erase–rewrite rescue, niche memory, and Λ\_auto are OPEN predictions awaiting independent data and experiments. The core scientific contract of the integrated version is designed to reduce WRRA not only in success but also when the common clock, simple AUC, selection-only, independent cell, and non-causal marker null models win.

> **The final frozen text of WRRA’s interpretation of life is structurally integrated and mathematically executable. The closed boundaries of DNA, proteins, minimal cells, lineages, and primordial life are connected within a single book. However, the independent verification of WRRA’s unique biology is still open, and the next battle will be decided by paired daughter cells, generational implementer regeneration, and time-disruption holdouts.**

### Next Step

Life is not a finished product, but a process of passing on feasibility to the next generation. I conclude the main body of this book with this definition.

#### DOIs for This Chapter

DOI 10.1038/s41467-026-73337-0 · PURE makes PURE

DOI 10.1016/j.cell.2026.02.009 · Bringing the genetically minimal cell to life on a computer in 4D

DOI 10.64898/2026.07.01.735724 · A chemically defined synthetic cell capable of growth and replication

DOI 10.5281/zenodo.22291862 · The First Living System in WRRA

One sentence from this chapter: This book does not end by declaring that life has been completed. It ends by specifically leaving behind what needs to be measured for the next boundary to close.

## Research Lineage and DOIs

The following four DOIs are the publicly available research records of the authors who constitute the DNA-life research axis of this book. They are classified as independent Zenodo research records to avoid confusion with academic journal article DOIs.

Life Models Interpreted via DOI WRRA · https://doi.org/10.5281/zenodo.22289266

Author Research DOI Executable Genetic Expression in WRRA · https://doi.org/10.5281/zenodo.22290829

Author Research DOI Lineage Closure in WRRA · https://doi.org/10.5281/zenodo.22291113

Author Research DOI The First Living System in WRRA · https://doi.org/10.5281/zenodo.22291862

## References

1. Choi W, Choi J. A WRRA Interpretation of a Living-System Model. Zenodo. 2026. doi:10.5281/zenodo.22289266.
2. Choi W, Choi J. Executable Genetic Expression in WRRA. Zenodo. 2026. doi:10.5281/zenodo.22290829.
3. Choi W, Choi J. Lineage Closure in WRRA. Zenodo. 2026. doi:10.5281/zenodo.22291113.
4. Choi W, Choi J. The First Living System in WRRA. Zenodo. 2026. doi:10.5281/zenodo.22291862.
5. Choi W. Four Axiomatic Frameworks for Describing Reality: Motion, Spacetime, Possibility, and Realization in WRRA. 2026.
6. Choi W. Life Models Interpreted via WRRA: Minimal Cell Extensions of Execution Structures Built for Cosmic Interpretation. 2026.
7. Choi W, Choi J. Executable Genetic Expression in WRRA: From DNA Sequence to Protein and the Missing Constructor. 2026.
8. Choi W, Choi J. Lineage Closure in WRRA: Stochastic Partition, Active Equalization, and the Reproduction Number of a Minimal Cell. 2026.
9. Choi W, Choi J. The First Living System in WRRA: A Fail-Closed Inference from Prebiotic Chemistry to Heritable Lineage Closure. 2026.
10. Choi W. WRRA-Cell 0.1–0.4: From a fixed current cell toy model to a real Perturb-seq audit. 2026.
11. Choi W. WRRA-Worm 0.1: A Fixed-Present Relational Model of the C. elegans Sensorimotor Loop. 2026.
12. Shimizu Y, et al. Cell-free translation reconstituted with purified components. Nature Biotechnology. 2001;19:751–755. doi:10.1038/90802.
13. Noireaux V, Libchaber A. A vesicle bioreactor as a step toward an artificial cell assembly. PNAS. 2004;101:17669–17674. doi:10.1073/pnas.0408236101.
14. Szostak JW, Bartel DP, Luisi PL. Synthesizing life. Nature. 2001;409:387–390. doi:10.1038/35053176.
15. Hutchison CA III, et al. Design and synthesis of a minimal bacterial genome. Science. 2016;351:aad6253. doi:10.1126/science.aad6253.
16. Doerr A, et al. In vitro synthesis of 32 translation-factor proteins from a single template reveals impaired ribosomal processivity. Scientific Reports. 2021;11:1898. doi:10.1038/s41598-020-80827-8.
17. Thornburg ZR, et al. Fundamental behaviors emerge from simulations of a living minimal cell. Cell. 2022;185:345–360.e28. doi:10.1016/j.cell.2021.12.025.
18. Mottaghi SS, Maerkl SJ. PURE makes PURE: reconstitution of the PURE cell-free system from self-synthesized proteins. Nature Communications. 2026;17:6756. doi:10.1038/s41467-026-73337-0.
19. Breuer M, et al. Essential metabolism for a minimal cell. eLife. 2019;8:e36842. doi:10.7554/eLife.36842.
20. Pelletier JF, et al. Genetic requirements for cell division in a genomically minimal cell. Cell. 2021;184:2430–2440.e16. doi:10.1016/j.cell.2021.03.008.
21. Bianchi DM, et al. The division machinery of the minimal cell. 2022. Public full text: PMC9483919.
22. Gilbert BR, et al. Dynamics of chromosome organization in a minimal bacterial cell. Frontiers in Cell and Developmental Biology. 2023;11:1214962. doi:10.3389/fcell.2023.1214962.
23. Thornburg ZR, et al. Bringing the genetically minimal cell to life on a computer in 4D. Cell. 2026;189:2582–2597.e27. doi:10.1016/j.cell.2026.02.009.
24. Replogle JM, et al. Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. Cell. 2022;185:2559–2575.e28.
25. White JG, Southgate E, Thomson JN, Brenner S. The structure of the nervous system of C. elegans. Philosophical Transactions B. 1986;314:1–340.
26. Kato S, et al. Global brain dynamics embed the motor command sequence of C. elegans. Cell. 2015;163:656–669.
27. Gleeson P, et al. c302: a multiscale framework for modeling the nervous system of C. elegans. Philosophical Transactions B. 2018;373:20170379.
28. Zhao M, et al. An integrative data-driven model simulating C. elegans brain, body and environment interactions. Nature Computational Science. 2024.
29. Moody ERR, et al. The nature of the last universal common ancestor and its impact on the early Earth system. Nature Ecology & Evolution. 2024;8:1654–1666.
30. Patel BH, et al. Common origins of RNA, protein and lipid precursors in a cyanosulfidic protometabolism. Nature Chemistry. 2015;7:301–307.
31. Hanczyc MM, Fujikawa SM, Szostak JW. Experimental models of primitive cellular compartments: encapsulation, growth, and division. Science. 2003;302:618–622.
32. Mansy SS, et al. Template-directed synthesis of a genetic polymer in a model protocell. Nature. 2008;454:122–125.
33. Zhu TF, Szostak JW. Coupled growth and division of model protocell membranes. JACS. 2009;131:5705–5713.
34. Adamala K, Szostak JW. Nonenzymatic template-directed RNA synthesis inside model protocells. Science. 2013;342:1098–1100.
35. Matsuo M, Kurihara K. Proliferating coacervate droplets as the missing link between chemistry and biology. Nature Communications. 2021;12:5487.
36. Yonekura K, et al. Growth of fatty acid vesicles coupled with amino acid sequences of peptides toward evolvable protocells. Communications Chemistry. 2026;9:234.
37. Abil Z, et al. Darwinian evolution of self-replicating DNA in a synthetic protocell. Nature Communications. 2024;15:8874.
38. Scherer M, et al. Clonal tracing with somatic epimutations reveals dynamics of blood aging. Nature. 2025. doi:10.1038/s41586-025-09041-8.
39. Liu M, Yue Y, Chen X, et al. Genome-coverage single-cell histone modifications for embryo lineage tracing. Nature. 2025;640:828–839. doi:10.1038/s41586-025-08656-1.
40. Xiao Y, et al. Tracking single-cell evolution using clock-like chromatin accessibility. Nature Biotechnology. 2025. doi:10.1038/s41587-024-02241-z.
41. Policarpi C, Munafò M, Tsagkris S, Carlini V, Hackett JA. Systematic epigenome editing captures the context-dependent instructive function of chromatin modifications. Nature Genetics. 2024;56:1168–1180. doi:10.1038/s41588-024-01706-w.
42. Pacalin NM, et al. Bidirectional epigenetic editing reveals hierarchies in gene regulation. Nature Biotechnology. 2025. doi:10.1038/s41587-024-02213-3.
43. Dai J, et al. Tracing back primed resistance in cancer via sister cells. Nature Communications. 2024. doi:10.1038/s41467-024-45478-7.
44. Nadalin F, Marzi MJ, Pirra Piscazzi M, et al. Multi-omic lineage tracing predicts the transcriptional, epigenetic and genetic determinants of cancer evolution. Nature Communications. 2024;15:7609. doi:10.1038/s41467-024-51424-4.
45. Kefalopoulou S, et al. Retrospective and multifactorial single-cell profiling reveals sequential chromatin reorganization during X inactivation. Nature Cell Biology. 2025;27:1186–1198. doi:10.1038/s41556-025-01687-w.
46. Hosseini M, Voisin V, Chegini A, et al. Metformin reduces the competitive advantage of Dnmt3aR878H HSPCs. Nature. 2025;642:421–430. doi:10.1038/s41586-025-08871-w.
47. Gabbutt C, et al. Fluctuating methylation clocks for cell lineage tracing at high temporal resolution in human tissues. Nature Biotechnology. 2022;40:720–730. doi:10.1038/s41587-021-01109-w.
48. Eisele AS, Tarbier M, Dormann AA, Pelechano V, Suter DM, et al. Gene-expression memory-based prediction of cell lineages from scRNA-seq datasets. Nature Communications. 2024;15:2744. doi:10.1038/s41467-024-47158-y.
49. Jones MG, Sun D, Min KHJ, et al. Spatiotemporal lineage tracing reveals the dynamic spatial architecture of tumor growth and metastasis. Nature Genetics. 2026. doi:10.1038/s41588-026-02739-z.
50. NCBI GEO. GSE282971: Clonal tracing with somatic epimutations reveals dynamics of blood aging. 2024.
51. Velten Laboratory. EPI-clone analysis code, version 2.0. GitHub repository. https://github.com/veltenlab/EPI-clone.
52. Jones MG, et al. Processed spatial lineage-tracing data. Zenodo. 2026. doi:10.5281/zenodo.19771805.
53. Gaut NJ, et al. A chemically defined synthetic cell capable of growth and replication. bioRxiv. 2026. doi:10.64898/2026.07.01.735724.
54. Biotic. SpudCell: A Chemically Defined Synthetic Cell Capable of Growth and Replication. Official project page. 2026. https://biotic.org/research/spudcell/.
55. Blanken D, et al. Integration of DNA replication and phospholipid synthesis in a synthetic cell. Nature Communications. 2026. doi:10.1038/s41467-026-69531-9.
56. Meselson M, Stahl FW. The replication of DNA in Escherichia coli. Proceedings of the National Academy of Sciences USA. 1958;44:671–682. doi:10.1073/pnas.44.7.671.
57. Okazaki R, Okazaki T, Sakabe K, Sugimoto K, Sugino A. Mechanism of DNA chain growth I Possible discontinuity and unusual secondary structure of newly synthesized chains. Proceedings of the National Academy of Sciences USA. 1968;59:598–605. doi:10.1073/pnas.59.2.598.
58. Lindahl T. An N-glycosidase from Escherichia coli that releases free uracil from DNA containing deaminated cytosine residues. Proceedings of the National Academy of Sciences USA. 1974;71:3649–3653. doi:10.1073/pnas.71.9.3649.
59. Sancar A, Rupp W.D. A novel repair enzyme UVRABC excision nuclease of Escherichia coli cuts a DNA strand on both sides of the damaged region. Cell. 1983;33:249–260.
60. Lahue RS, Au KG, Modrich P. DNA mismatch correction in a defined system. Science. 1989;245:160–164. doi:10.1126/science.2665076.
61. Berget SM, Moore C, Sharp PA. Spliced segments at the 5′ terminus of adenovirus 2 late mRNA. Proceedings of the National Academy of Sciences USA. 1977;74:3171–3175. doi:10.1073/pnas.74.8.3171.
62. Ciechanover A, Heller H, Elias S, Haas AL, Hershko A. ATP-dependent conjugation of reticulocyte proteins with the polypeptide required for protein degradation. Proceedings of the National Academy of Sciences USA. 1980;77:1365–1368. doi:10.1073/pnas.77.3.1365.
63. Jacob F, Monod J. Genetic regulatory mechanisms in the synthesis of proteins. Journal of Molecular Biology. 1961;3:318–356. doi:10.1016/S0022-2836(61)80072-7.
64. Barrangou R, Fremaux C, Deveau H, et al. CRISPR provides acquired resistance against viruses in prokaryotes. Science. 2007;315:1709–1712. doi:10.1126/science.1138140.
65. Jinek M, Chylinski K, Fonfara I, Hauer M, Doudna JA, Charpentier E. A programmable dual-RNA-guided DNA endonuclease in adaptive bacterial immunity. Science. 2012;337:816–821. doi:10.1126/science.1225829.
66. Racker E, Stoeckenius W. Reconstitution of purple membrane vesicles catalyzing light-driven proton uptake and adenosine triphosphate formation. Journal of Biological Chemistry. 1974;249:662–663.
67. Hua W, Young EC, Fleming ML, Gelles J. Coupling of kinesin steps to ATP hydrolysis. Nature. 1997;388:390–393. PMID:9237757.
68. Dogan MY, Can S, Cleary FB, Purde V, Yildiz A. Kinesin's front head is gated by the backward orientation of its neck linker. Cell Reports. 2015;10:1967–1973.
69. Budaitis BG, Jariwala S, Rao L, et al. Pathogenic mutations in the kinesin-3 motor KIF1A diminish force generation and movement through allosteric mechanisms. eLife. 2019;8:e44146. doi:10.7554/eLife.44146.
70. Burute M, et al. Kinesin-1 orchestration in mammalian cells. Science Advances. 2022;8:eabo2343. doi:10.1126/sciadv.abo2343.
71. Dauparas J, Anishchenko I, Bennett N, et al. Robust deep learning–based protein sequence design using ProteinMPNN. Science. 2022;378:49–56. doi:10.1126/science.add2187.
72. Cross J. A., et al. A de novo designed coiled coil-based switch regulates the microtubule motor kinesin-1. Nature Chemical Biology. 2024. doi:10.1038/s41589-024-01640-2.
73. UniProt Consortium. Kinesin-1 heavy chain KIF5B, human. UniProtKB accession P33176.
74. Protein Data Bank. Kinesin motor-domain structure. PDB accession 1MKJ.
75. Choi W. WRRA Core 1.0: A Domain-Agnostic Execution Architecture. Zenodo. 2026. doi:10.5281/zenodo.22650956.

## Key Formula Index

| **subject**                | **formula**                                      | **analysis**                                                        |
| -------------------------- | ------------------------------------------------ | ------------------------------------------------------------------- |
| WRRA object                | M=(S,L,X₀,R,O,Π)                                 | Information, Law, State, Execution, Observation, Source             |
| Fixed current              | Xₖ₊₁=F(Xₖ,uₖ,ξₖ)                                 | The next state is calculated from a sufficient current.             |
| Coding lower limit         | L\_min=3n+3                                      | The grammatical lower bound of a general triplet cipher             |
| Protein execution          | Y=Φ(D,E,X₀,t)                                    | Separate DNA and executor                                           |
| Process                    | P\_full=(1−δ)^n                                  | Length-dependent battlefield generation baseline                    |
| cell division              | T\_cell=inf{t:∧G\_i}                             | Simultaneous completion of five gates                               |
| Binomial distribution      | X\~Bin(N,1/2)                                    | Finite copy number daughter cell noise                              |
| system                     | R\_life=P₁+2P₂=2q                                | Expected number of functional daughter cells                        |
| First life                 | R\_life=2Kf^L                                    | Common Threshold of Closure Between Replication and Non-Replication |
| Error threshold            | f\_c=(2K)^(-1/L)                                 | Fidelity by Length and Renderer Success Rate                        |
| Geometric covariance       | Cov(X\_i,X\_j)=N\_iN\_jσ\_p²                     | Signal of common schist geometry                                    |
| Memory capacity            | M\_res=I(X\_past;Y\_future\|G,U,L)               | Past future prediction information that exceeds current conditions  |
| Layer-by-layer attenuation | C\_l(d)=Σ\_r a\_lr λ\_r^d+B\_l                   | Multiple combined memory mode                                       |
| Non-commutative            | \[L\_i,L\_j]=L\_iL\_j−L\_jL\_i                   | Differential effect of the order of operations                      |
| Induction–Selection        | ΔȲ=Cov(w,Y)/w̄+E\[wΔY]/w̄                        | Separation of group proportions and changes in kinship              |
| Memory reversibility       | Z0→Z1→Z0′→Z1′                                    | Causal write–erase–rewrite of the cover                             |
| Distributed memory         | M\_total=M\_cell+M\_lineage+M\_niche+M\_pop      | Multilayered decomposition of memory ownership                      |
| Autonomous closure         | Λ\_auto=internal\_operation/mandatory\_operation | Environment renderer dependency ledger                              |

_Table A1. Core formulas of the integrated model._

## Decisive Experiment Reproduction Protocols

### Protocol 1. PURE Generational Self-Regeneration

Generation g of input and g+1 of recovered material are defined using the same criteria. Prior to the experiment, the seed amount, external supplements, purification loss, and the method for distinguishing between newly synthesized proteins and residual input proteins are fixed. The total mass of non-ribosomal proteins, the stoichiometry of individual components, concentration-corrected translational activity, and the residual amount of essential auxiliary systems are measured simultaneously.

Run at least three independent lineages with equivalent transfers, fixed dilution, and prespecified failure criteria. Record every externally supplied catalyst, template, membrane component, and energy source in the ownership ledger.

{% hint style="info" %}
**Judgment Principle:** Passing a narrow operational threshold does not automatically elevate it to a stronger claim of autonomy or causality.
{% endhint %}

### Protocol 2. Syn3A Partitioning from One Mother Cell to Two Daughters

One mother cell is tracked via temporal imaging, and both daughter cells are recovered after division. The total molecular weight of the mother cell immediately before division and the volumes, ribosomes, RNA polymerases, degradosomes, membrane proteins, and low-copy number essential complexes of the two daughters immediately after division are counted under the same detection correction. Analysis that selects only one daughter or retains only the surviving daughter is not permitted.

Calculate D\_x for each molecular group and compare unbiased binomial, volume-proportional, and spatial-localized models in out-of-sample lineages. If directional bias persists even after controlling for detection efficiency, DNA exclusion, cell cycle, and geometry, reject the binomial null model. Estimate the phi threshold for each essential molecular group by linking the distribution error with subsequent growth and division success.

{% hint style="info" %}
**Judgment Principle:** Passing a narrow operational threshold does not automatically elevate it to a stronger claim of autonomy or causality.
{% endhint %}

### Protocol 3. Autonomous Lineages of Synthetic Protocells

Starting from a single compartment, genome replication, translation, energy regeneration, membrane growth, and cleavage are tracked as the same lineage for at least three generations. The feeders, membrane materials, ribosomes, enzymes, and energy substrates supplied to each generation are quantified and distinguished from the amounts synthesized and regenerated within the system. The rate of complete genome preservation and the number of functional progeny are recorded together.

External material replacement is gradually reduced while simultaneously evaluating R\_life and the autonomy index. If only the number of generations passes and the translator or energy depends on external supply, it is judged as Sustainability PASS and Autonomous Closure NOT ESTABLISHED. The strong operational threshold of the initial life is passed only if the essential module is regenerated in the same system and R\_life > 1 is repeated.

{% hint style="info" %}
**Judgment Principle:** Passing a narrow operational threshold does not automatically elevate it to a stronger claim of autonomy or causality.
{% endhint %}

### Protocol 4. LARRY Lineage Residue

Single-cell states and barcodes are measured before intervention, and RNA, proteins, and functions of the same clone are linked after a period of time. Entire individuals, batches, and lineages are held out as a whole, rather than at the cell level. Standard Markov models, current state-only models, clone frequency-only models, and WRRA residual models are compared using the same preprocessing and loss functions.

The residual term must improve the prediction of the future state of the external lineage even after controlling for current state, cell cycle, batch, guide efficiency, and survivor selection. If there is no improvement, the independent residual term is removed. If access to the raw data is incomplete, the results of the alternative data are not labeled as LARRY direct verification but are left as a preliminary audit.

{% hint style="info" %}
**Judgment Principle:** Passing a narrow operational threshold does not automatically elevate it to a stronger claim of autonomy or causality.
{% endhint %}

### Protocol 5. GTW Six Permutations

All six permutations of G, T, and W are performed in the same cellular background. The actual intracellular dose, exposure time, interval, wash, toxicity, cell cycle, and initial state of each operation are matched. Gate accessibility, transcriptional conversion, stability markers, proteins, and functions are measured at each step and tracked for at least three divisions after the operation is removed.

The pre-specified principal evaluation is the final memory, function, and GTW gap relative to competing permutations. If GTW is consistently superior after adjusting for delivered AUC and survivor composition, non-commutative prediction is supported. If the permutation gap disappears or another permutation is stably superior, the current WRRA GTW priority hypothesis is rejected or modified.

{% hint style="info" %}
**Judgment Principle:** Passing a narrow operational threshold does not automatically elevate it to a stronger claim of autonomy or causality.
{% endhint %}

### Protocol 6. write-erase-rewrite

A reversible operation is performed at the same locus by labeling, thoroughly washing, deleting, and relabeling. This includes non-target guides, catalytically inactive effectors, sham, toxicity, and off-target controls. At each step, labeling, accessibility, RNA, protein, function, viability, and clone composition are measured.

Functional causality is supported when a change in directionality in write, reversal in erase, rescue in rewrite, and persistence after at least three divisions occur together. If only the marker is reversible and the function is immobile or the result is explained by clone selection, the claim of causal memory for that marker is withdrawn. The analysis code, exclusion criteria, and primary assessment amount are disclosed regardless of the outcome.

{% hint style="info" %}
**Judgment Principle:** Passing a narrow operational threshold does not automatically elevate it to a stronger claim of autonomy or causality.
{% endhint %}

## Quick DOI Index

The core DOIs used in the text and bibliography have been reorganized along with their subject headings. DOI strings are presented in their original form for search and citation purposes.

| **DOI**                    | **Subject**                                                                   |
| -------------------------- | ----------------------------------------------------------------------------- |
| 10.5281/zenodo.22289266    | Life form model interpreted with WRRA                                         |
| 10.5281/zenodo.22290829    | Executable Genetic Expression in WRRA                                         |
| 10.5281/zenodo.22291113    | Lineage Closure in WRRA                                                       |
| 10.5281/zenodo.22291862    | The First Living System in WRRA                                               |
| 10.1038/90802              | Cell-free translation reconstituted with purified components                  |
| 10.1073/pnas.0408236101    | A vesicle bioreactor as a step toward an artificial cell assembly             |
| 10.1038/35053176           | Synthesizing life                                                             |
| 10.1126/science.aad6253    | Design and synthesis of a minimal bacterial genome                            |
| 10.1038/s41598-020-80827-8 | In vitro synthesis of 32 translation-factor proteins                          |
| 10.1016/j.cell.2021.12.025 | Fundamental behaviors emerge from simulations of a living minimal cell        |
| 10.1038/s41467-026-73337-0 | PURE makes PURE                                                               |
| 10.7554/eLife.36842        | Essential metabolism for a minimal cell                                       |
| 10.1016/j.cell.2021.03.008 | Genetic requirements for cell division in a genomically minimal cell          |
| 10.3389/fcell.2023.1214962 | Dynamics of chromosome organization in a minimal bacterial cell               |
| 10.1016/j.cell.2026.02.009 | Bringing the genetically minimal cell to life on a computer in 4D             |
| 10.1038/s41586-025-09041-8 | Clonal tracing with somatic epimutations reveals dynamics of blood aging      |
| 10.1038/s41586-025-08656-1 | Genome-coverage single-cell histone modifications for embryo lineage tracing  |
| 10.1038/s41587-024-02241-z | Tracking single-cell evolution using clock-like chromatin accessibility       |
| 10.1038/s41588-024-01706-w | Systematic epigenome editing captures context-dependent chromatin function    |
| 10.1038/s41587-024-02213-3 | Bidirectional epigenetic editing reveals hierarchies in gene regulation       |
| 10.1038/s41467-024-45478-7 | Tracing back primed resistance in cancer via sister cells                     |
| 10.1038/s41467-024-51424-4 | Multi-omic lineage tracing predicts determinants of cancer evolution          |
| 10.1038/s41556-025-01687-w | Sequential chromatin reorganization during X inactivation                     |
| 10.1038/s41586-025-08871-w | Metformin reduces the competitive advantage of Dnmt3aR878H HSPCs              |
| 10.1038/s41587-021-01109-w | Fluctuating methylation clocks for cell lineage tracing                       |
| 10.1038/s41467-024-47158-y | Gene-expression memory-based prediction of cell lineages                      |
| 10.1038/s41588-026-02739-z | Spatiotemporal lineage tracing of tumor growth and metastasis                 |
| 10.5281/zenodo.19771805    | Processed spatial lineage-tracing data                                        |
| 10.64898/2026.07.01.735724 | A chemically defined synthetic cell capable of growth and replication         |
| 10.1038/s41467-026-69531-9 | Integration of DNA replication and phospholipid synthesis in a synthetic cell |

## Glossary

**SOURCE**\
Information, material, or input given before execution. In biology, it may be a genome, an initial cellular state, a stimulus, or a culture condition.

**LAW**\
Physical, chemical, and biological rules that permit or prohibit possible transitions and reactions.

**STATE**\
Concentrations, structures, locations, cell-cycle phase, metabolism, and environmental conditions that determine execution at the present time.

**RENDERER**\
Polymerases, ribosomes, enzymes, membranes, cells, and experimental apparatus that materialize SOURCE as products and functions.

**OBSERVABLE**\
RNA, proteins, morphology, function, or behavior recorded under a declared measurement and analysis protocol.

**Fixed-Present**\
The computational principle that the past can influence present execution only through physical residue remaining now.

**Residue**\
Measurable traces of past events retained in present methylation, proteins, damage, structures, locations, and population composition.

**Ownership Ledger**\
A table recording whether the information that determined an observation resided in the system, environment, experimenter, or pre-existing apparatus.

**Failure Closure**\
A rule that assigns a weaker verdict or OPEN, rather than assuming success, when required inputs or evidence are absent.

**Interpretation**\
Reconstruction of an already existing structure or value from present information within a declared tolerance.

**Prediction**\
A testable conditional distribution for a future target not already fixed by present information.

**EXACT**\
A mathematically exact relation under stated assumptions; it does not by itself establish empirical adequacy.

**EMPIRICAL PASS**\
A declared operational threshold satisfied by direct data or by experimental data reported by the authors.

**COMPUTATIONAL PASS**\
A threshold satisfied inside a simulation or analytic model, distinct from direct biological measurement.

**INFERRED**\
A result calculated from reported quantities and explicit assumptions but not directly measured in the source study.

**OPEN**\
A claim that cannot yet be adjudicated because required data are absent or resolution is insufficient.

**Information Closure**\
A condition in which reproducible genetic information is sufficiently preserved for the next generation.

**Execution Closure**\
A condition in which translation and catalytic machinery are reproduced while being used to read information.

**Metabolic Closure**\
A condition in which energy and precursors are supplied and regenerated at levels sufficient to sustain essential reactions.

**Boundary Closure**\
A condition in which membranes and compartments retain components while selectively exchanging required materials.

**Lineage Closure**\
A condition in which descendants retaining essential functions continue to be produced beyond a single generation.

**R\_life**\
The effective generational reproduction number of a living lineage that preserves essential functions. Supercritical persistence requires R\_life>1.

**PURE System**\
A cell-free protein synthesis system reconstituted from purified translation components.

**Non-ribosomal Mass Reproduction Ratio**\
The next-generation recovery of non-ribosomal PURE proteins divided by their input in the preceding generation.

**Minimal Cell**\
An experimental or computational cell with genetic functions minimized for survival and division in a specified environment.

**JCVI-syn3A**\
A synthetic minimal cell with a 543,380-bp genome and a reference system for whole-cell modeling and cell-division studies.

**Binomial Partitioning**\
The baseline null model in which each independent molecule is allocated with equal probability to either of two daughter cells.

**D\_x**\
The absolute difference between the daughter-cell molecular ratio for class x and the daughter-cell volume ratio.

**Protocell**\
A prebiotic or synthetic-cell model combining a genome, catalysts, a membrane, and selected growth or division functions.

**Autonomy Index**\
A ledger separating the fraction of essential operations regenerated internally from the fraction dependent on external supply.

**Epigenetic Memory**\
A persistent multilayer state that changes response probabilities in present and descendant cells without altering DNA sequence.

**Chromatin Accessibility**\
The physical and structural state that permits transcription factors and regulatory proteins to reach a DNA region.

**Lineage Tracing**\
Reconstruction of parent–offspring relations among cells using barcodes, mutations, epigenetic marks, or time-lapse imaging.

**Balanced Accuracy**\
The unweighted mean of recall across classes, used to evaluate classification in imbalanced data.

**Subject Holdout**\
Validation in which a model is trained on one subject and tested on another to reduce subject-specific leakage.

**G–T–W**\
Three operations: response-potential Gate, transcription/signal Transform, and stable-mark Write.

**Noncommutativity**\
The property that changing the order of the same operations changes the final state and function.

**Write–Erase–Rewrite**\
A design that writes, erases, and rewrites an epigenetic mark to test functional reversibility and causality.

**Niche Memory**\
Preservation of past states in extracellular matrix, immune cells, vasculature, oxygen gradients, and spatial structure, which then feed back into cell responses.

**Sample-Group Holdout**\
External validation that excludes all observations from the same biological sample together, preventing leakage across spatial spots or cells.

**WRRA-Cell**\
A cell model that audits present state, residue, environment, and phenotype before and after gene perturbation as separate layers.

**WRRA-Worm**\
A toy model implementing the sensory–neural–body–behavior–environment closed loop of C. elegans through the Fixed-Present and a relation ledger.

## Authors and Contact

Wonsik Choi develops WRRA as an executable framework for studying life, heredity, minimal cells, lineage closure, the first life, epigenetic memory, and cell differentiation. His books include _The New Matriarchal Society_. Jeongin Choi, his daughter and co-author, studies biotechnology at Korea University and contributes a life-science perspective to the joint research and editorial work presented here.

Correspondence Wonsik Choi · janefather@gmail.com
