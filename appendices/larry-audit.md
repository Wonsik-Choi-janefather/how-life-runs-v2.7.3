# LARRY labels and the limits of epigenetic memory validation

Wonsik Choi · Jeongin Choi | 26 October 2026 | Online supplement v0.1

This updates data readiness in Chapters 18 and 27 of How Life Runs. Full Korean and English technical manuscripts, audit code and results are in the [public research folder](https://github.com/Wonsik-Choi-janefather/how-life-runs-v2.7.3/tree/main/research/larry-audit-v0.1).

## Established results

The [official RDS endpoint](https://ndownloader.figshare.com/files/42479346) yielded a full 173,210,114-byte download. MD5 0cc0bc53add7acb3aee39c673ff8adba matches Figshare. This is verified accessibility of the existing version 2 file, not its first public release date.

| Experiment | All cells | Labeled cells | Barcodes | Label coverage |
| --- | ---: | ---: | ---: | ---: |
| M.1 | 13,885 | 8,923 | 367 | 64.26% |
| M.2 | 7,896 | 5,473 | 160 | 69.31% |
| M.3 | 7,001 | 0 | 0 | 0% |

All 527 barcodes have LARRYSize equal to observed cell counts. Counts agree between raw parsed strings and converted DataFrame extraction. Both routes share a parser and file, rather than constituting external replication. DNAm.data and integrated.data are 453 × 28,782; AB.data is 20 × 28,782. integrated.counts is empty.

Among 575,640 antibody entries, 415,365 are nonfinite. Only 454 M.1 cells have finite values for all antibodies; none do in M.2 or M.3. This does not establish an error in the original publication, but prevents immediate treatment of the full object as complete paired DNA–protein observations. The origin of these values and valid observation masks require further review.

## Completed and pending claims

Complete download, integrity, ID alignment, label denominators and internal clone-size consistency are established. Original AUC/ARI reproduction, conditional permutations, new-lineage prediction and causal memory tests remain uncompleted. M.3 and unlabeled M.1/M.2 cells must not be treated as having LARRY ground truth.

LARRY identifies clone membership, not an exact division tree. Pseudotime is neither elapsed time nor generation. Thus the chapter's per-generation decay and coupled eigenmode predictions remain OPEN. Barcodes shared across annotated cell types do not independently establish differentiation direction or a causal role for methylation. Intervention and functional rescue remain necessary.

WRRA is applied as an input–transformation–output–falsification audit profile. This is not new biological validation of the core, nor a demonstrated predictive advantage over ordinary quality control. No new DOI has been assigned to the report. The existing book DOI is not a DOI for this supplement. Archived v2.7.4 whole-book PDF and Word files remain fixed editions distinct from this online update.

## Sources

Original experiments and data are credited to Scherer and colleagues; source data are CC BY 4.0. Paper DOI [10.1038/s41586-025-09041-8](https://doi.org/10.1038/s41586-025-09041-8); dataset DOI [10.6084/m9.figshare.24204750.v2](https://doi.org/10.6084/m9.figshare.24204750.v2); [GSE282971](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282971); [original analysis code](https://github.com/veltenlab/EPI-clone).
