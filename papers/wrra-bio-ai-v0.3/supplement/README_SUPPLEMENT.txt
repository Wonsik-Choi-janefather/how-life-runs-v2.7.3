WRRA execution contracts for AI-assisted biological research
Supplement version 0.3 — Wonsik Choi and Jeongin Choi

Scope
Literature-anchored reconstruction and constructed finite models. No new
wet-lab data, fitted biological parameters, or comparative LLM benchmark.

Requirements
Python 3.10 or later for all calculations (standard library only).
Optional figure regeneration additionally requires matplotlib.

Run from this directory, in order:
  python reproduce.py
  python boundary_model.py
  python integrated_model.py
  python build_ledgers.py
  python audit.py
Optional:
  python make_figure.py

Generated outputs
results.json: partition, dilution, 81 adjudication combinations and 6
malformed gate checks.
boundary_results.json: four candidate inventories under two import settings.
integrated_results.json: restoration capacities and fixed-capacity contrast.
evidence_ledger.json: 14 source/model claim records with locators and links.
audit_results.json: 9 CHECKS_SATISFIED, 1 CONTRACT_FAIL, 4 OPEN; 7 malformed
ledger mutations rejected.

Key interpretation
CHECKS_SATISFIED means only declared necessary checks are satisfied. Manual
source verification and the sufficiency argument are separate. Unreported
evidence is unknown, not false. Model inputs n, k, R and costs are chosen
fixtures, not measurements of minimal cells. A source report of a predicted
function is distinct from experimental confirmation of that function.

The restoration calculation assumes each competent daughter can attain any
integer new active amount up to R within the stated horizon, with no losses,
allowed substrates, no external active machinery and no shared competition.
Changing these assumptions changes the biological application.

Fixed-R comparisons restore each candidate parent's own n. They do not show
harm from increasing n at one common fixed target, nor whole-cell closure.

Reproducibility
SHA256SUMS.json records hashes of packaged supplement files (excluding itself).
Sources are identified by URLs, DOI and locators in evidence_ledger.json.
Run outputs overwrite the corresponding output files in this directory.

Figure 1
The supplied vector PDF and high-resolution PNG plot exact constructed-model
values. make_figure.py regenerates both. Figure styling is not needed for any
calculation or adjudication.
