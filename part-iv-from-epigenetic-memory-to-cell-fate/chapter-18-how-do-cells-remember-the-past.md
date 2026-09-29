# Chapter 18 — How do cells remember the past?

**How do cells remember the past?**

> Memory does not merely mean that markers remain for a long time. Even short-lived cellular states can persist for a long time within a population through lineage transmission and selection.

## Established Scientific Starting Point

Epigenetic clocks and lineage tracing utilize marker changes over time and division. However, if temporal distance, phylogenetic distance, stratified attenuation, and selection effects are not separated, they can appear as a single clock.

## WRRA Reconstruction

Life Model V views the eigenmodes of the binding state matrix as the time scale of memory. The binding of DNA, chromatin, RNA, proteins, and niches can create various slow modes.

## Comparative Reading

If the half-life of a memory is measured solely by the decline curve of a single marker, interlayer compensation is not visible. Even if methylation disappears quickly, transcription factor autocircuits can maintain their state, and even if intracellular markers disappear, the selective proliferation of specific clones can maintain population proportions. Observed long memories may be a combination of multiple short memories.

Genealogical distance and actual time must also be distinguished. Cells that divide rapidly and those that divide barely over the same period of time have different label dilutions. Therefore, to identify stratified genealogical clocks, time t and generation g must be recorded together, and whether the state correlation between sister and cousin cells is maintained beyond the common environment must be measured.

> At the boundary between interpretation and prediction, a strong argument survives only if it predicts better in the external lineage compared to the common single clock, independent layer, and Markov transition. This eigenmode itself is still an OPEN prediction.

## Research Content and Validation Results

## Life Model V: Layer-Specific Lineage Clocks of Epigenetic Memory

The goal is not to rank DNA methylation, parental histones, accessibility, and RNA and protein memory into a single independent half-life. It is to identify the intrinsic modes and layered loadings shared by the combined molecular layers to separate accurate cell division distances from actual elapsed times. EPI-Clone tracked large-scale lineages by reading single CpG methylation and blood cell status together \[34], and TACIT provided a single-cell map of seven histone modifications in early embryos \[35]. EpiTrace showed that division age can be estimated using clock-like accessibility \[36], and fluctuating methylation clocks showed that high-temporal-resolution lineage tracking is possible in human tissues \[43].

### Lineage Distance, Elapsed Time, and Coupled Eigenmodes

Rᵥ⁽ˡ⁾ = Yᵥ⁽ˡ⁾ − μₗ(cell type, cell cycle, batch, size, environment) (42)

Cₗᴾᴰ(g) = Corr(R\_parent⁽ˡ⁾, R\_descendant⁽ˡ⁾) = Aₗρₗᵍ + Bₗ (43)

τₗ = −1 / ln|ρₗ|, g₁⁄₂,ₗ = τₗ ln2 (44)

If two sister cells have each passed one generation from a common mother cell, the lineage distance is 2, so the covariance is proportional to ρ². Misinterpreting sister correlation as parent-offspring correlation leads to an overestimation of memory time. Additionally, since the elapsed times of the stationary phase and the rapid proliferation phase differ even with the same number of generations, the two decay axes are separated.

Cₗ(d,tᵢ,tⱼ) = Aₗ exp(−d/τₗ,g) exp\[−(tᵢ+tⱼ)/τₗ,t] + Bₗ (45)

Z\_child = A\_state Z\_parent + ΓX + ξ, Cov(Zᵢ,Zⱼ|a)=A\_stateʰⁱΣₐ(A\_stateʰʲ)ᵀ (46)

Cₗ(d) = Σᵣ aₗᵣ λᵣᵈ + Bₗ, τᵣ = −1/ln|λᵣ| (47)

Therefore, the enhanced P4 is not “there is one clock per layer” but “each layer has a different damping fingerprint of the combined eigenmodes and predicts the next generation covariance of the unseen lineage with the non-diagonal transfer matrix.”

### Competitive Model and Experiment

Table 20. Competitive Models and Judgment of Life Model V.

| **model**             | **structure**                                      | **Support/Rejection Criteria**                                              |
| --------------------- | -------------------------------------------------- | --------------------------------------------------------------------------- |
| M0: No memory         | Conditional covariance 0 after generation distance | If M1/M2 fails to improve in the holdout, maintain                          |
| M1: Independent layer | A\_state diagonal, stratigraphic ρ                 | There is layer-by-layer attenuation, but the transport term is unnecessary. |
| M2: Bonding layer     | Sparse non-diagonal A\_state and multiple λ        | Significantly improve C(d+1) of the unseen lineage                          |

The recommended experiment combines 5th–6th generation live imaging with independent DNA barcodes and uses a portion of sister cells from each branch for destructive multiome analysis. Circular reasoning, such as estimating lineage by methylation and then testing methylation memory with the same CpG, or estimating lineage by RNA and then testing memory with the same RNA, is prohibited. MCM2·POLE3, DNMT1·UHRF1, writer/eraser, and RNA/protein half-life disturbances must target specific terms in the transfer matrix.

### Falsification Conditions

The common single damping rate is substantially equivalent to the layered and combined model.

The non-diagonal transfer term is indistinguishable from 0 or its direction is reversed in repeated experiments.

M2 does not have higher predictive power than M0/M1 in cell lines and lineages that have not been observed.

The memory effect disappears when cell type, cycle, environment, and survivor bias are controlled.

## Next Step

Verify whether the DNA layer predicts the protein definition state in external organisms using public multi-omics data.

### DOIs for This Chapter

> DOI 10.1038/s41586-025-09041-8 Clonal tracing with somatic epimutations reveals dynamics of blood aging
>
> DOI 10.1038/s41587-024-02241-z · Tracking single-cell evolution using clock-like chromatin accessibility
>
> DOI 10.1038/s41587-021-01109-w Fluctuating methylation clocks for cell lineage tracing
>
> One sentence of this chapter: Memory does not mean only that markers remain for a long time. Even short-lived cellular states can persist for a long time in a population through lineage transmission and selection.

**WRRA BIOLOGY**
