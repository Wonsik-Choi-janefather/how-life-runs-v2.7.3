# EPI Clone LARRY audit v0.1

Wonsik Choi and Jeongin Choi, 26 October 2026.

[Korean technical manuscript](paper-ko.md) · [English technical manuscript](paper-en.md)

This is a completed structural and metadata audit, not a completed rerun of EPI-Clone, an AUC/ARI reproduction, or a causal epigenetic memory experiment.

## Reproduction

Download the original object from https://ndownloader.figshare.com/files/42479346 and verify its MD5 0cc0bc53add7acb3aee39c673ff8adba.

Install Python 3.12 and `rdata==1.1.0`, then run:

```bash
python audit.py /path/to/seurat_for_figshare.rds --out results
```

The script checks dimensions, cell order, sparse matrix storage, label missingness and clone sizes; it also records antibody nonfinite coverage. A second extraction route counts raw parsed LARRY strings before DataFrame conversion. Both routes share a parser and source file.

The script regenerates full cell-lineage JSONL and clone-summary JSONL locally. Only the small audit JSON outputs are committed here. The source RDS is not redistributed. JSONL is one JSON record per line, preserving cell IDs and experiment annotations.

## Attribution and reuse

Original experiments and source data: Scherer et al., Nature (2025), DOI 10.1038/s41586-025-09041-8. Source dataset: DOI 10.6084/m9.figshare.24204750.v2, CC BY 4.0. Derived mappings are extractions, not newly measured ground truth. Code and manuscript additions by Wonsik Choi and Jeongin Choi are released under CC BY 4.0; existing repository materials retain their existing rights.

This report has no newly assigned DOI. The book's existing DOI is not a DOI for this supplement. Archived whole-book PDFs retain their original versions unless separately regenerated.
