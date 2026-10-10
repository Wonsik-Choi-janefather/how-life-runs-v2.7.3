# Structuring AI assisted biological research with WRRA execution contracts

**Wonsik Choi and Jeongin Choi** — Independent Researchers  
Version 0.3 · 11 October 2026

## Publication status
Author manuscript submitted to the Journal of Theoretical Biology on 11 October 2026. This is a preprint, not an accepted or peer-reviewed journal publication. The submitted manuscript is preserved unchanged. Zenodo DOI: pending publication.

WRRA means **Wonsik Reality-Renderer Architecture**.

## Contents
- `WRRA_Bio_AI_JTB_Manuscript_v0.3.docx`: final submitted English manuscript.
- `manuscript_en.md`: editable English source.
- `WRRA_Bio_AI_Supplement_v0.3.zip`: original reproducibility supplement.
- `supplement/`: unpacked code, source-linked evidence ledger, outputs and Figure 1.

## Reproduce
Python 3.10 or later; standard library for calculations. Matplotlib is optional for regenerating the figure.

```sh
cd supplement
python reproduce.py
python boundary_model.py
python integrated_model.py
python build_ledgers.py
python audit.py
```

## Verified input → WRRA transformation → output → falsification
- Input: cited minimal-cell, cell-free translation and transporter-annotation reports; declared finite partition and regeneration assumptions.
- Transformation: execution roles, resource ownership, boundary exchanges and phenotype targets represented in traceable contracts.
- Output: n=9, k=2 gives joint competence 0.9609375; restoration capacity R=6 gives 0.8203125 and R=7 gives 0.9609375. The ledger contains 9 CHECKS_SATISFIED, 1 CONTRACT_FAIL and 4 OPEN records.
- Falsification: enumeration must match formulas; applying the model to biology requires measured partition and attainable regeneration conditions. Workflow superiority requires the proposed comparison and is not asserted.

No external funding. No competing interests. Generative AI assistance is disclosed in the manuscript. Internal model review is not external peer review. Internal reviews, submission correspondence and older versions are not included in this public package.

Copyright 2026 Wonsik Choi and Jeongin Choi. No additional software license is granted by this README; original cited materials retain their own rights.
