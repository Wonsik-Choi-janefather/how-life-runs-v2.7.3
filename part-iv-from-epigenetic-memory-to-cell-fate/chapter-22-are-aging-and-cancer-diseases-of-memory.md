# Chapter 22 — Are aging and cancer diseases of memory?

**Are aging and cancer diseases of memory?**

> In aging and cancer recurrence, changes in cellular state and clonal frequency occur simultaneously. It is necessary to distinguish whether the cells remaining after treatment have changed or if the original clones were selected.

## Established Scientific Starting Point

Clonal hematopoiesis, persister cells, sister cell tracking, and multi-omics lineage studies provide data that can separate induction and selection.

## WRRA Reconstruction

Life Model VII establishes the coupling dynamics between intracellular memory states and clonal frequencies. The key prediction is that even short-state memory can be transformed into long-group memory when combined with selection coefficients.

## Comparative Reading

Whether cells that have relapsed after cancer treatment have learned a new resistance state due to the drug, or whether originally rare resistant clones have survived, changes the treatment strategy. In the former case, re-establishment of the state is important, while in the latter, selective pressure and cloning are crucial. Both processes may occur simultaneously.

Sister cell designs are robust to this distinction. By treating one sister and observing the response, while preserving the other to read the pre-treatment state, one can evaluate whether future resistance is linked to existing residue. Clonal frequency and intracellular state must be tracked within the same model to avoid mistaking population-level memory for cellular memory.

> At the boundary between interpretation and prediction, if only the frequency changes without the cell state changing, the induction term must be removed. Conversely, if state transitions are repeated within the same barcode, a selection-only model is insufficient.

## Research Content and Validation Results

## Life Model VII: Memory Dynamics in Aging, Clonal Hematopoiesis, and Cancer Recurrence

Aging, clonal hematopoiesis (CH), and non-genetic resistance in cancer are not single diseases and cannot be reduced to the same molecular mechanisms. However, they can be compared through common dynamics in which past inputs alter multilayered states, which in turn change current responsiveness, survival, and proliferation, while selection reshapes population composition.

p\_post(y) = Z⁻¹∫K\_U(y|x)s\_U(x)p\_pre(x)dx (55)

K\_U is an induced state transition within the same lineage, and s\_U is a choice based on the existing state. If there is only a choice, K\_U(y|x)=δ(y−x); if there is only an induction, s\_U is independent of the state. The bulk difference before and after does not separate the two terms.

ΔȲ = Cov(wᵢ,Yᵢ)/w̄ + E\[wᵢΔYᵢ]/w̄ (56)

Table 22. Three memory levels and observation method of Life Model VII.

| **Memory level**  | **definition**                                                       | **Key observations**                                |
| ----------------- | -------------------------------------------------------------------- | --------------------------------------------------- |
| molecular memory  | M/H/A/R/P/Q states remaining in a cell                               | Multiome re-stimulation after washout               |
| Genealogy memory  | Molecular state is passed on to offspring after division.            | barcode·EPI-Clone·sister-cell                       |
| collective memory | The frequency of specific states/clones itself is a long-term change | clone size · VAF · suitability · time to recurrence |

ReSisTrace traced the readiness for resistance before treatment based on the shared transcriptional characteristics of sister cells \[39], and cancer studies combining a single-cell multiome and barcode showed that both the transcriptional and accessibility status and genetic amplification before treatment can predict tumor formation and drug tolerance \[40]. EPI-Clone results from older blood showed that many young-type lineages coexist with a few extended and myeloid-biased lineages, leading to the direct consideration of population composition memory \[34].

### Disease-Specific Differential Predictions

Ḃ\_age = ε\_write + ε\_restore + ε\_selection (57)

The predictive accuracy of the aging clock does not imply causality. Successful rejuvenation requires not only a reduction in the number of markers but also the restoration of stimulus-recovery trajectories, identity, and function similar to young cells.

s\_c(t)=f\_c(G\_c,Z\_c,U\_aged)−f\_WT(Z\_WT,U\_aged) (58)

In CH, DNMT3A and TET2 mutations alter the memory recording and erasing operators, and the aging and inflammatory environment may select the difference. The results showing that metformin lowered the competitive advantage and reversed abnormal DNA methylation and H3K27me3 in DNMT3A mutation HSPCs are preclinical evidence showing that a combination of genotype × state × environment may be involved \[42].

S ⇄ P → R; H\_relapse(T)=1−exp{−∫₀ᵀ\[αN\_P(t)+βN\_R(t)]dt} (59)

In cancer, sensitive S, reversible persister P, and stable genetically resistant R are isolated. Since the time window for R to develop widens as P survives longer, the risk of recurrence cannot be assessed solely by the number of residual cells immediately after treatment. A unique conclusion of Life VII is that even short-term cellular memory can become long-term collective memory through selective proliferation.

### Falsification Conditions

If the genome and current environment are controlled, past history does not provide additional predictive power for future responses.

There are no induced transitions within the same barcode, and all changes are explained solely by existing clone selection.

Directly erasing or editing candidate memory markers does not change restimulation, persistence, or differentiation.

The WRRA mixed model does not predict external data as well as the genotype+current environment reference model.

## Next Step

We examine through spatial genealogy data whether the extracellular environment stores and returns such memories.

### DOIs for This Chapter

> DOI 10.1038/s41586-025-09041-8 Clonal tracing with somatic epimutations reveals dynamics of blood aging
>
> DOI 10.1038/s41467-024-45478-7 Tracing back primed resistance in cancer via sister cells
>
> DOI 10.1038/s41467-024-51424-4 · Multi-omic lineage tracing predicts determinants of cancer evolution
>
> DOI 10.1038/s41586-025-08871-w · Metformin reduces the competitive advantage of Dnmt3aR878H HSPCs
>
> One sentence from this chapter: In aging and cancer recurrence, changes in cellular state and changes in clone frequency occur simultaneously. It is necessary to distinguish whether the cells remaining after treatment have changed or whether the original clones were selected.

**WRRA BIOLOGY**
