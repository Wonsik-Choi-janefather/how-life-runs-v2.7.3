# An independent audit of EPI Clone data with LARRY clonal labels

## Integrity of the integrated Seurat object and readiness for epigenetic memory analysis

Wonsik Choi · Jeongin Choi | 최원식 · 최정인

Independent Researchers, Republic of Korea

Correspondence: janefather@gmail.com | Jeongin Choi: cjeongin024@gmail.com

Research report v0.1 · 26 October 2026 · Public technical manuscript, not a claim of completed journal peer review.

## Abstract

Independent assessment of methylation-based clonal inference requires cell-level linkage between methylation and an independent lineage label. We downloaded and audited the public EPI-Clone M.1–M.3 Seurat object, checking hashes, matrix structure, cell identifiers, LARRY barcodes and recorded clone sizes. The file contained 173,210,114 bytes and matched the Figshare MD5. The object included 28,782 cells, 453 methylation features and 20 antibody features. There were 14,396 labeled cells assigned to 527 barcodes, with recorded LARRYSize agreeing with observed cell counts for every barcode. Label coverage was 64.26% in M.1 and 69.31% in M.2; M.3 had no LARRY labels. Of 575,640 antibody matrix entries, 415,365 were nonfinite, preventing interpretation as complete protein observations for all cells. These results establish input readiness, not reproduction of EPI-Clone performance or causal epigenetic memory. We distinguish structural validation, clonal association, temporal persistence and causal memory, and specify subsequent tests.

## 1 Background and objective

Scherer and colleagues developed EPI-Clone using jointly observed methylation and clonal information[1]. The experimental discoveries and original algorithm belong to those authors. Our question is narrower: does the publicly downloadable M.1–M.3 object contain the cell-level correspondence needed to begin an independent analysis? We track GEO accession GSE282971, the Figshare dataset and the authors' analysis repository separately[2–4].

Earlier HTTP 403 responses were access observations in our execution environment. On 26 October 2026, the official endpoint advertised by the Figshare API yielded a complete download. This is restored or newly verified accessibility to the existing version 2 file, not evidence that the data were first released that day or that the authors changed their publication status. A failed HTTP request alone does not establish that a dataset is private.

## 2 Data and methods

The source was seurat_for_figshare.rds in Figshare item 24204750, DOI 10.6084/m9.figshare.24204750.v2. The metadata report a modification date of 16 December 2024 and a CC BY 4.0 license. We checked full byte length and MD5, and computed SHA256. A matching MD5 is a transfer-integrity check; it does not independently authenticate biological truth or authorship.

We used Python 3.12.14 and rdata 1.1.0 rather than an R runtime. Classes without dedicated constructors, including Seurat and dgCMatrix, remained namespaces retaining their underlying attributes. Conversion warnings are preserved in the output. We checked sparse matrix dimensions, column pointers, row index bounds and cell order. This verifies storage structure; it does not execute Seurat methods in R.

Metadata checks included unique cell IDs, required fields, identical missingness of LARRY and LARRYSize, within-barcode invariance of LARRYSize, and equality between reported size and the number of matching cell rows. A second extraction counted LARRY strings directly in the parsed object before DataFrame conversion. Both routes share the file and parser, so they are not an external laboratory replication.

Missing labels were excluded from barcode counts and were not pooled into a synthetic clone. Antibody coverage was counted as finite entries and cells with finite values, stratified by experiment. This audit does not resolve whether nonfinite entries originate from missing measurements, preprocessing or transformation.

## 3 Results

The downloaded file contained 173,210,114 bytes. MD5 was 0cc0bc53add7acb3aee39c673ff8adba. SHA256 was d321321b7b3e9fddd038f7707ce5d0d6039c758efe2100c6f2baef01be42c2d1. These identifiers allow exact comparison of the audited input.

Metadata had 28,782 rows and 10 columns, with unique cell IDs. DNAm.data and integrated.data each had 453 × 28,782 entries; AB.data had 20 × 28,782. The integrated.counts slot was empty, with dimensions 0 × 0. PCA and UMAP had dimensions 28,782 × 30 and 28,782 × 2. Tested matrix and embedding cell order matched the metadata. Structural agreement does not establish the biological validity of upstream batch correction or methylation preprocessing.

M.1 contained 13,885 cells, including 8,923 labeled cells and 367 barcodes. M.2 contained 7,896 cells, including 5,473 labeled cells and 160 barcodes. M.3 contained 7,001 cells without LARRY labels. Consequently, the entire 28,782-cell object cannot be treated as a fully labeled evaluation set. Results after excluding unlabeled cells concern the label-bearing subset.

The 14,396 labeled cells and 527 distinct barcodes agreed across raw-string and converted-DataFrame extraction. All 527 barcodes had constant LARRYSize values equal to observed cell counts. This establishes internal metadata consistency, not an independent biological measurement of clone size. Agreement may be expected if the original sizes were calculated from the same table.

Of 527 barcodes, 276 occurred in more than one annotated CellType and 216 in more than one ProcessingBatch. These are descriptive counts over existing annotations. They do not establish multipotency, transmission direction or environment-independent memory. Barcode collisions, doublets, annotation error and experimental design require separate consideration.

AB.data contained 160,275 finite and 415,365 nonfinite entries among 575,640 elements. In M.1, 7,217 cells had at least one finite antibody value and 454 had finite values for all 20 features. Corresponding counts were 3,849 and zero in M.2, and 6,980 and zero in M.3. Complete-case restriction across all 20 antibodies therefore retains only a subset of M.1. Nonfinite values must not be silently interpreted as zero expression. These checks do not determine the source of nonfinite values or a valid imputation method.

## 4 WRRA audit structure and interpretation

WRRA here means Wonsik Reality-Renderer Architecture, as introduced in How Life Runs. Its origin in the author's intuition that the universe might follow a principle of least computation is historical motivation, not a biological hypothesis tested by this dataset. We apply a bounded audit profile without changing the frozen core or claiming evidence for cosmology.

Inputs are the hash-pinned object and source annotations. Transformations are ID alignment, definition of labeled subsets, barcode aggregation and matrix checks. Outputs are cell-level label mappings, experiment-specific denominators, missingness records and integrity results. A mismatched file, duplicated IDs, wrong column order or inconsistent clone sizes stops the affected audit. Unlabeled cells remain OPEN for ground-truth evaluation rather than being declared biological negatives.

The present WRRA contribution is an executable, traceable separation of evidence and decision boundaries. We did not compare predictive accuracy or efficiency against conventional quality-control workflows. We therefore make no claim that WRRA uniquely enables these checks or establishes a new biological law.

## 5 Subsequent performance and memory tests

First, restore the authors' R environment and recover the original inclusion rules, static CpG selection, clone-size denominators, density criteria and clustering settings. Do not apply the 0.25% expansion threshold using an assumed denominator. Freeze M.1 settings before application to M.2, and compare ARI and AUC with the original publication only after computing them.

Second, use barcode permutations conditional on cell type, batch and measurement coverage, assess feature-selection leakage and sample-size sensitivity, and resample at clone level. Claims of generalization to new lineages require clone-level separation rather than splitting cells from the same clone across training and evaluation. M.2 is a biological replicate, but these data have now been inspected; the proposed analyses are not preregistered or fully blinded prospective tests.

Third, distinguish clone membership from generation and elapsed time. A shared LARRY barcode is not a complete mother–daughter division tree. Pseudotime is neither elapsed time nor an exact generation counter. The object alone cannot identify per-generation memory half-lives, a multilayer transfer matrix, sister-cell covariance or transmission direction. Those quantities require additional time-resolved lineage observations and suitable molecular layers.

Finally, causal memory requires lineage-aware write–erase–rewrite interventions, controls, functional rescue and follow-up. Clonal association of static CpGs cannot substitute for those experiments. Performance reproduction, confounder control and causal memory testing remain uncompleted in this version.

## 6 Conclusion

The public object supplies methylation matrices and cell-level LARRY correspondence sufficient to begin independent clonal reanalysis. Established results concern file integrity, aligned structure, labeled denominators, internally consistent clone sizes and the extent of nonfinite antibody values. This resolves a data-access boundary in the book, without establishing causal epigenetic memory or independently validating WRRA-specific biology.

## Data and research declarations

The original data and experiments are credited to Scherer and colleagues. Derived cell mappings and clone summaries retain original identifiers and are extractions, not newly measured ground truth. They follow the source CC BY 4.0 terms. audit.py regenerates audit_results.json, raw_parser_check.json, cell_lineage.jsonl and clone_summary.jsonl. The original 173 MB RDS is linked by DOI and official endpoint rather than duplicated.

No new human or animal experiments were performed. The analysis uses public mouse data. There was no external funding and no competing interest. Generative AI assisted manuscript and code preparation. Computational audit is not described as external peer review or approval by the original authors. No DOI has yet been assigned to this new report; the DOIs below identify the cited source publication and dataset.

## References

1. Scherer M, Singh I, Braun MM, et al. Clonal tracing with somatic epimutations reveals dynamics of blood ageing. Nature 643, 478–487 (2025). https://doi.org/10.1038/s41586-025-09041-8
2. Scherer M et al. EPI-Clone datasets M.1–M.3. Figshare, version 2. https://doi.org/10.6084/m9.figshare.24204750.v2
3. NCBI GEO. GSE282971. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282971
4. veltenlab. EPI-clone analysis repository. https://github.com/veltenlab/EPI-clone
5. Official RDS download. https://ndownloader.figshare.com/files/42479346
