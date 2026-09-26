# **Chapter 23**

**Does memory exist outside the cell?**

> Cells do not live alone within tissues. The ECM, blood vessels, immune cells, oxygen, metabolites, and spatial structures preserve traces of past events and can alter subsequent reactions.

## Established Scientific Starting Point

Spatial transcriptomes and spatial lineage tracing measure the relationship between lineage and niche during tumor growth and metastasis. However, randomly dividing spatial points within the same sample overestimates generalization performance.

## WRRA Reconstruction

673,263 observations, 150 tumors, and 39 samples were aggregated at the tumor level, and sample group holdouts were performed. The selection module had an R2 of 0.201, but all module models deteriorated to an R2 of -0.023.

## Comparative Reading

Spatial niches are not merely backgrounds. Hypoxic regions, perivascular areas, the distribution of immune cells, and ECM rigidity alter cellular signaling and metabolism, and substances secreted by cells, in turn, change the niche. Ownership of memory can circulate between the cell and the environment.

The result where only the selected modules survive in the exogenous sample and the entire module model fails is an important warning. In high-dimensional spatial data, including many variables does not always mean capturing more biology. The entire sample must be held out, and it must be verified whether the pre-specified modules are reproduced in the new tumor.

> at the boundary between interpretation and prediction is selectively supported, but cause and effect were not distinguished. External cohorts and spatial intervention determine the strong distributed memory claim.

## Research Content and Validation Results

## Life Model IX: Distributed Biological Memory Stored outside the Cell

The future of a cell is not determined solely by its internal epigenome. Stem cell niches, the extracellular matrix, immune cell composition, inflammatory cytokines, spatial structure, and microbiota can preserve the results of past stimuli and reconstruct internal states. Therefore, the ownership of memory is separated into cells, lineages, niches, and populations.

M_total = M_cell + M_lineage + M_niche + M_population + M_interaction (63)

Xᵢ(t+1)=F\[Xᵢ(t), ΣⱼWᵢⱼXⱼ(t), N(t), U(t)\] (64)

Table 24. Cell × niche 2 × 2 crossover design of Life Model IX.

| **cell**                 | **Niche**                | **Key Interpretation**                                |
|--------------------------|--------------------------|-------------------------------------------------------|
| young state/no treatment | young state/no treatment | base line                                             |
| young state/no treatment | Aging/Past Stimulation   | sufficiency of niche memory                           |
| Aging/Memory status      | young state/no treatment | Persistence and Reversibility of Intracellular Memory |
| Aging/Memory status      | Aging/Past Stimulation   | Combination, interaction, and reinforcement           |

ΔY = ΔY_cell + ΔY_niche + ΔY_cell×niche (65)

Each term is separated using cross-transplantation, conditioned medium, decellularized matrix, immune cell reorganization, or spatial omics. If the young niche restores senescent cells, the cell-autonomous strong memory model is reduced, and if cells that have erased their memory form the same state again in the senescent niche, it means that the niche is a memory restorer.

### Falsification Conditions

There is no additional effect of niche history after controlling the internal cellular state.

The niche exchange effect is entirely explained by cell viability, cell type composition, or a single medium component.

Even including the spatial relationship W, holdout prediction is not improved compared to the independent cell model.

## Track 2: Spatial Tumor Lineages and Niche Memory

The total number of observations in the spatial lineage data is 673,263, including 150 tumors and 39 biological specimens. After aggregating at the tumor level, Spearman associations were calculated, and cross-validation that excluded entire sample populations was used to prevent leakage of spatial points within the same specimen.

Table 32. Significant spatial module–pedigree association after multiple test correction.

| **Module** | **Spearman ρ** | **p**  | **FDR** |
|------------|----------------|--------|---------|
| M2         | 0.486          | 0.0002 | 0.0011  |
| M7         | 0.382          | 0.0002 | 0.0011  |
| M6         | 0.317          | 0.0210 | 0.0330  |
| M8         | 0.222          | 0.0114 | 0.0220  |
| M3         | −0.169         | 0.0120 | 0.0220  |
| M10        | −0.281         | 0.0004 | 0.0015  |
| M4         | −0.386         | 0.0008 | 0.0022  |

Table 33. Sample group holdout prediction performance.

| **model** | **explanation**       | **R²** | **MAE** |
|-----------|-----------------------|--------|---------|
| S0        | Segmentation standard | −0.130 | 0.0648  |
| S1        | Pre-selection module  | 0.201  | 0.0549  |
| S2        | All modules           | −0.023 | 0.0605  |

The results selectively support the idea that niche information can provide additional predictive power regarding lineage or tumor status. Since the model with all modules deteriorates at the holdout stage, the strong proposition that 'more spatial information is better' is rejected. Lineage-specific temporal data and interventions are required to determine whether the associated niche is a cause or an effect.

Figure 5. Spatial module association and sample group holdout generalization.

## Next Step

The final extension example is WRRA-Worm, which examines whether the execution grammar of cells applies to the nervous system and behavior.

### DOIs for This Chapter

> DOI 10.1038/s41588-026-02739-z Spatiotemporal lineage tracing of tumor growth and metastasis
>
> DOI 10.5281/zenodo.19771805 · Processed spatial lineage-tracing data
>
> One sentence from this chapter: Cells do not live alone within a tissue. The ECM, blood vessels, immune cells, oxygen, metabolites, and spatial structures can preserve traces of past events and alter subsequent reactions.

**WRRA BIOLOGY**
