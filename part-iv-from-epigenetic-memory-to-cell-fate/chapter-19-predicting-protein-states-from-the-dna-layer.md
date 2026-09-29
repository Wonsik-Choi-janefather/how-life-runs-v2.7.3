# Chapter 19 — Predicting Protein States from the DNA Layer

Predicting Protein States from the DNA Layer

> If epigenetic memory is real, the state of the DNA layer must have a reproducible relationship with the RNA or protein layer. Fitness within the same individual alone is not sufficient.

## Established Scientific Starting Point

Single-cell multi-omics has enabled the reading of methylation and surface proteins within the same cell. Inter-individual holdouts prevent batch and individual-specific signals from taking the place of prediction.

## WRRA Reconstruction

8,850 cells, 663 amplicons, 20 ADTs, and 6 states from the EPI-Clone series were used. The mean balance accuracy of the whole DNA feature model was 0.487, and the inclusion of descriptive covariates was 0.502, exceeding the multi-category criterion of 0.167.

## Comparative Reading

A balanced accuracy of 0.502 is not a perfect prediction. Compared to the six-state random standard of 0.167, there is a meaningful crossover signal, but about half the uncertainty remains. If this number is interpreted as 'DNA determined cell fate,' it exceeds the range indicated by the data.

The next strong test is time-sequenced pedigree data. It verifies whether early DNA methylation predicts subsequent protein states and functions within the same barcode, and whether independent information remains even when RNA and the current protein are added. A holdout is required to exclude the entire individuals, experimental batches, and pedigrees.

> The boundary results of interpretation and prediction partially support DNA-protein state binding but do not prove causal inheritance of future fate or LARRY residual terms.

## Research Content and Validation Results

## Track 1: Epigenetic Memory and Cell Differentiation across DNA and Protein Layers

We used 8,850 fully observed cells, 663 methylation amplicons, 20 antibody-derived tags (ADTs), and 6 protein definitions from the publicly available EPI-Clone dataset. The key evaluation is a reciprocal holdout, where one individual learns and another tests. This blocks individual-specific leakage more strongly than cell-level random splitting.

Table 31. Prediction of DNA methylation-based protein status of exogenous holdouts.

| **model**                       | **Object A→B** | **Individual B→A** | **Average balance accuracy** |
| ------------------------------- | -------------- | ------------------ | ---------------------------- |
| E0 Multi-category Standard      | 0.167          | 0.167              | 0.167                        |
| E1 single optimal amplicon      | 0.221          | 0.229              | 0.225                        |
| E2 Total 663 amplicons          | 0.476          | 0.497              | 0.487                        |
| E3 Total + Technical Covariates | 0.487          | 0.517              | 0.502                        |

The significant improvement in total DNA features compared to baseline and the maintenance of performance even with the addition of descriptive covariates support the state coupling between the DNA and protein layers. However, this analysis does not provide evidence that lineage residues in the same cell causally determine future fate. Cell lineage-level residue terms must be verified separately when access to raw data with LARRY barcodes and complete time-series data is secured.

Figure 2. Prediction of protein definition status of DNA methylation features in crossover holdout.

## Next Step

The next chapter asks whether cell fate can differ depending on the order of action, even with the same amount of action.

### DOIs for This Chapter

> DOI 10.1038/s41586-025-09041-8 Clonal tracing with somatic epimutations reveals dynamics of blood aging
>
> DOI 10.1038/s41587-021-01109-w Fluctuating methylation clocks for cell lineage tracing
>
> One sentence from this chapter: If epigenetic memory is real, the state of the DNA layer must have a reproducible relationship with the RNA or protein layer. Fitness within the same individual alone is not sufficient.

**WRRA BIOLOGY**
