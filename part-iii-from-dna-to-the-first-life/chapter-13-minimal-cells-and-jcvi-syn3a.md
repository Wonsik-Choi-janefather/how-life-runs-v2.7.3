# Chapter 13 — Minimal Cells and JCVI-syn3A

**Minimal cells and JCVI-syn3A**

> Minimal cell research asks for the minimum list of genes necessary for life, but a divisible cell is not automatically created based on the list alone.

## Established Scientific Starting Point

JCVI-syn3A is a cell with a minimal genome of 543,380 bp, which has become a benchmark for studying genome reduction, cell morphology, metabolism, and division mechanisms. Whole-cell models execute these components together in time and space.

## WRRA Reconstruction

WRRA distinguishes five components—genome, RNA, ribosomes, enzymes, and membranes—and five gates—replication, translation, metabolism, membrane growth, and division. The doubling time cannot be shorter than the completion time of the slowest essential gate.

## Comparative Reading

A minimal genome does not mean the smallest life form, but rather the result of eliminating as many genes as possible that can be removed in a specific environment. If the culture medium is rich in nutrients, the environment can take over the synthetic functions within the cell. Therefore, the fact that there are few genes does not necessarily mean there is high autonomy.

WRRA's minimal cell calculation does not hide the environment renderer from the ledger. It displays the medium, temperature, osmotic pressure, supplied metabolites, and the experimenter's splitting operations as external inputs. Minimality must be reported not only of the number of internal components but also of which functions are delegated to the environment.

> boundary replication limit for interpretation and prediction is a conditional calculation under assumptions and does not independently predict the observed approximately 50-minute replication and 105-minute splitting cycles. It separates the parameters derived from the data from the new predictions.

## Research Content and Validation Results

## Minimal Cells: Five-Component Autocatalysis and Five Gates

WRRA-Autocell formed a positive linear autocatalytic system with five extensive components: genome (G), RNA (R), ribosome (B), enzyme (P), and membrane (M).

dx/dt = Ax, Av\* = λ\*v\*, x → x/2 when Σx = 2Σx₀ (19)

| **Calculation items**                 | **result**                         | **verdict**                |
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

### The Five Gates of Cell Division

T\_cell = inf{t : G\_D(t) ∧ G\_P(t) ∧ G\_M(t) ∧ G\_E(t) ∧ G\_F(t)} (20)

| **Gate**                  | **Completion conditions**                                     | **Biological meaning**      |
| ------------------------- | ------------------------------------------------------------- | --------------------------- |
| G\_D: DNA                 | Whole genome replication and two-copy continuity              | Genetic persistence         |
| G\_P: Protein/Ribosome    | Regeneration of initial translation and catalytic capacity    | Launcher persistence        |
| G\_M: Mak                 | Area to wrap the increased volume                             | Continued vigilance         |
| G\_E: Energy/Metabolism   | ATP production ≥ consumption, essential metabolites ≥ minimum | Non-equilibrium maintenance |
| G\_F: Separation/Geometry | Chromosome separation, V≥2V₀, cleavage complete               | Create two execution units  |

Table 9. Simultaneous closure gate of WRRA minimal cells.

### JCVI-syn3A Loading and Geometric Calculations

T\_rep,lower = 543,380 / (2×600×60) = 7.546944 min (21)

If the genome is treated as a sphere at ideal packing density, its lower-bound diameter is obtained from the DNA contour volume. This is a geometric lower bound, not a prediction of actual chromosome organization.

r\_div = 2^(1/3)r₀ = 251.9842 nm (r₀=200 nm) (22)

A₀=502,654.8 nm², A\_div=797,914.8 nm², ΔA/A₀=58.7401% (23)

The volume-doubling spherical geometry is EXACT, but the time to reach that area depends on lipid and membrane protein synthesis, the initial number of molecules, and the growth rate. Since some coefficients from the open model and 105 minutes were used for correction, it is an observation-based reconstruction rather than an independent prediction by WRRA.

## Membrane transport and energy coupling

The cell membrane is not a simple packaging material. While small nonpolar molecules can diffuse through the membrane, ions and most polar molecules require channels, carriers, or pumps. Facilitated diffusion moves along concentration or electrochemical gradients, and primary active transport uses energy such as ATP directly. Secondary active transport combines the free energy stored in the gradient of one substance with the movement of another substance.

The electron transport chains of respiration and photosynthesis create a proton motive force across the membrane. ATP synthase combines this electrochemical gradient with ATP synthesis. Experiments linking light-induced proton transport and ATP formation in vesicles reconstituted with bacteriorhodopsin and ATPase have directly demonstrated the coupling of membrane boundaries and energy conversion \[66]. Even with the presence of boundaries, metabolism and synthesis do not continue without selective transport and gradient maintenance.

Metabolism is not limited to a list of catabolism and anabolism alone. The influx of carbon, nitrogen, phosphate, and sulfur, the regeneration of redox carriers, ATP, GTP, CoA, and various cofactors, and the elimination of byproducts must occur simultaneously. If one does not distinguish between substances provided by the external medium and substances that the cell regenerates itself, the autonomy of the synthetic cell is overestimated.

Table 14A. Performance audit of membranes and energy in minimal cells.

| **Gate**             | **First, the measured amount**             | **Unclosed**                                                    |
| -------------------- | ------------------------------------------ | --------------------------------------------------------------- |
| Selective Inflow     | Flux and transporter copy by substrate     | There is a barrier, but necessary substances cannot enter       |
| inclination          | Membrane potential, ΔpH, leakage rate      | Energy is not stored and is lost                                |
| ATP regeneration     | Production and consumption rates, ATP/ADP  | Translation and replication stop after single-shot fuel         |
| redox play           | NAD(P)H ratio and electron acceptor        | Simultaneous blockage of synthesis and detoxification reactions |
| dispose              | Toxic byproducts and efflux                | Growth is visible, but the next generation is suppressed.       |
| membrane maintenance | Lipid synthesis, area growth, permeability | Dilution, rupture, or gradient collapse during growth           |

## Cell-Cycle Controls Bind the Execution Sequence

Replication, growth, and division are not independent parallel processes. In bacteria, replication initiation, chromosome segregation, divisome assembly, and septation are linked according to trophic status and cell size. In eukaryotic cells, G1/S, G2/M, and spindle checkpoints check for DNA replication completion, damage, and chromosome attachment status. A checkpoint is not a device that corrects all errors, but rather a control layer that delays the next transition or allows for the selection of cell death or arrest.

In WRRA, the cell cycle can be recorded as a runtime permission between LAW and STATE. Division is not permitted merely by the fact that there are two copies of DNA. Damage status, energy, membrane area, chromosome location, and division machinery must pass the threshold. Conversely, in tumor cells or damaged synthetic cells, this permission may be incorrectly opened.

Specifying membrane transport, energy, and checkpoints in the five gates of a minimal cell prevents confusion between genome replication PASS and lineage closure PASS. Even if the same 105-minute division cycle is observed, if it relies on external ATP precursors, feeder membranes, completed transporters, or intact seed ribosomes, ownership remains with the external conditions and the initial STATE.

The existence of transport, chemiosmosis, and checkpoints at the boundary between interpretation and prediction is an established biological fact. To predict the doubling time and cause of failure of a specific minimal cell, data on the number of transporters, membrane leakage, metabolic flux, ATP turnover, DNA damage, and the timing of each gate are required.

## Next Step

How essential molecules are passed to the two daughters when the cell divides determines lineage closure.

### DOIs for This Chapter

> DOI 10.1126/science.aad6253 · Design and synthesis of a minimal bacterial genome
>
> DOI 10.7554/eLife.36842 · Essential metabolism for a minimal cell
>
> DOI 10.1016/j.cell.2021.03.008 · Genetic requirements for cell division in a genomically minimal cell
>
> DOI 10.1016/j.cell.2021.12.025 · Fundamental behaviors emerge from simulations of a living minimal cell
>
> DOI 10.5281/zenodo.22289266 · Life form model interpreted by WRRA
>
> One sentence from this chapter: A minimal cell is more than a gene list. Transport, energy, replication, quality control, and division must close within one lineage.

**WRRA BIOLOGY**
