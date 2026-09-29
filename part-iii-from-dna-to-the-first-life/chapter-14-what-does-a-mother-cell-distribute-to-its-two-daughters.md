# Chapter 14 — What Does a Mother Cell Distribute to Its Two Daughters?

What Does a Mother Cell Distribute to Its Two Daughters?

> Division doubles the number of cells but does not divide every molecule exactly in half. Essential complexes with small copy numbers can disappear from one daughter through random distribution alone.

## Established Scientific Starting Point

In unbiased binomial distribution, X is equal to Binomial(N, 1/2) and relative variation is on the scale of 1/sqrt(N). Cells reduce this risk through localization, binding, active transport, and redundancy.

## WRRA Reconstruction

The molecular partition error D\_x is defined as the difference between the molecular ratio and volume ratio of daughter cells. In the 50-cycle of the Syn3A 4D model, ribosomes, degradosome, PtsG, and GapDH exhibited approximate binomial partitions without directional bias.

## Comparative Reading

A molecular ratio differing from half in two daughter cells of equal volume is not immediately a bias. When N is small, binomial noise alone can cause significant differences. Conversely, if specific molecules are localized around cell poles or DNA, a spatial signature different from that of a binomial model with the same mean is generated. Both coefficients and geometry are required for the distribution test.

A deterministic experiment involves selecting a single mother cell, preserving both daughters, and linking them. The total mother cell mass, daughter cell volume, molecular counts, and subsequent survival must be measured. Analyzing only the successful daughters leads to selection bias. Paired designs can, for the first time, directly demonstrate the causal link between molecular distribution and phylogenetic success.

> The boundary between interpretation and prediction is a computational pass. In reality, molecular counting, volume correction, and survival threshold measurements linking one mother cell and two daughter cells are still open.

## Research Content and Validation Results

## Daughter-Cell Partitioning and Lineage Closure

When the number of mother cell molecules N is distributed independently and unbiased, the number of first daughters X follows a finite binomial distribution. The two daughters are not independent because the gain of one is the loss of the other.

X \~ Binomial(N, 1/2), E\[X]=N/2, Var(X)=N/4, CV=1/√N (24)

P₂=∏ᵢPᵢ(both pass), P₁=2(q−P₂), P₀=1−2q+P₂ (25)

R\_life = E\[Y] = P₁ + 2P₂ = 2q (26)

f(s)=P₀+P₁s+P₂s²; ζ=1 if R\_life≤1, else ζ=P₀/P₂ (27)

| **φ**  | **R\_life** | **P₀** | **P₁** | **100 Generations of Survival** | **Ultimate Survival** |
| ------ | ----------- | ------ | ------ | ------------------------------- | --------------------- |
| 0.50   | 1.991       | 0.000  | 0.009  | 100.00%                         | 100.00%               |
| 0.70   | 1.789       | 0.007  | 0.197  | 99.10%                          | 99.10%                |
| 0.80   | 1.400       | 0.061  | 0.478  | 86.80%                          | 86.80%                |
| 0.85   | 1.134       | 0.148  | 0.570  | 47.60%                          | 47.60%                |
| 0.8571 | 1.133       | 0.148  | 0.570  | 47.23%                          | 47.23%                |
| 0.8572 | 0.978       | 0.206  | 0.610  | 1.18%                           | 0.00%                 |
| 0.90   | 0.742       | 0.344  | 0.570  | 0.00%                           | 0.00%                 |

Table 10. Systematic results of the six declared molecular pool scenarios.

At φ=6/7, the minimum daughter cell count of 28-copy HupA is 12, but immediately afterwards it changes to 13, and R\_life drops discontinuously from 1.133 to 0.978. In this scenario, the owner of the critical cliff is the low-copy number HupA. Even if the total biomass is nearly the same, a single essential low-copy number component can shift a lineage from supercritical to extinction.

### Active Equalization and Redundancy Design

| **φ** | **Minimum equalization a required for R\_life≥1** | **Remaining random proportion** |
| ----- | ------------------------------------------------- | ------------------------------- |
| 0.80  | 0.00%                                             | 100.00%                         |
| 0.85  | 0.00%                                             | 100.00%                         |
| 0.86  | 2.96%                                             | 97.04%                          |
| 0.90  | 26.85%                                            | 73.15%                          |
| 0.95  | 56.42%                                            | 43.58%                          |
| 1.00  | 76.24%                                            | 23.76%                          |

Table 11. Equalization requirement to restore system critical point.

Fixing the minimum number of daughter cells of HupA at 12 copies results in parental cells of 35/39/45 copies providing 95/99/99.9% passing probabilities for both daughters, respectively. This is a reserve of +7/+11/+17 compared to the input of 28 copies. This is not a natural optimum, but an example of a genetic engineering design that calculates the Pareto front of replication cost and genetic reliability.

### The Covariance Signature of Division Geometry

Var(Xᵢ)=Nᵢ/4 + Nᵢ(Nᵢ−1)σ\_p² (28)

κᵢ=4Var(Xᵢ)/Nᵢ = 1 + 4(Nᵢ−1)σ\_p² (29)

Cov(Xᵢ,Xⱼ)=NᵢNⱼσ\_p², i≠j (30)

For a paired mother–two-daughter measurement, the total molecular count should be conserved within the declared recovery tolerance after correction for sampling loss.

### Syn3A: Molecular Partitioning from One Mother Cell to Two Daughters

The existing φ is maintained as the survival threshold ratio for each essential molecular group, and the distribution error is separated as D\_x. For molecular group x:

p\_x=N\_x,1/(N\_x,1+N\_x,2); v=V\_1/(V\_1+V\_2); D\_x=|p\_x−v| (81)

If D\_x=0, it is a volume-proportional distribution. In an unbiased binomial distribution with equal volume, the rarer the complex, the greater the relative variation, and the primitive daughter cell difference rate D\*\_x=2D\_x.

RMS(D\_x)=1/(2√N\_x); E\[D\_x]≈1/√(2πN\_x) (82)

The 2026 Syn3A four-dimensional whole-cell model simulated 50 complete cell cycles. At 105 minutes, the mean mother cell contained 881 ribosomes, 176 RNA polymerases, and 192 degradosomes. The paired daughter distributions of ribosomes, degradosomes, DNA polymerase complexes, and membrane proteins form the reference ledger for the proposed experiment.

Table 40. Binomial variation magnitude calculated using reported Syn3A blastocyst counts.

| **molecular groups** | **Mother cell N** | **RMS D\_x** | **Average D\_x approximation** | **RMS D\*\_x** |
| -------------------- | ----------------- | ------------ | ------------------------------ | -------------- |
| ribosome             | 881               | 1.68%        | 1.34%                          | 3.37%          |
| degradosome          | 192               | 3.61%        | 2.88%                          | 7.22%          |

This percentage is the analytical expectation of the approximate binomial null model, not a sampled measurement per daughter cell. Direct completion requires time tracking of one mother cell and two daughter cells, volume correction, molecular counting, pre-registered D\_x allowable intervals, and verification of the φ threshold of all essential molecular groups.

## Next Step

The next chapter separates persistence and autonomy when externally supported synthetic cells continue through generations.

### DOIs for This Chapter

> DOI 10.1016/j.cell.2021.03.008 · Genetic requirements for cell division in a genomically minimal cell
>
> DOI 10.3389/fcell.2023.1214962 · Dynamics of chromosome organization in a minimal bacterial cell
>
> DOI 10.1016/j.cell.2026.02.009 · Bringing the genetically minimal cell to life on a computer in 4D
>
> DOI 10.5281/zenodo.22291113 · Lineage Closure in WRRA
>
> One sentence of this chapter : Cell division doubles the number of cells but does not divide every molecule exactly in half. Essential complexes with small copy numbers can disappear from one daughter through random distribution alone.

**WRRA BIOLOGY**
