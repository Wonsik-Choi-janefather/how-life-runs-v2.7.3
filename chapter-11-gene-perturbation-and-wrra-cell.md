# **Chapter 11**

Gene Perturbation and WRRA-Cell

> While it might seem that removing or suppressing a gene would allow one to directly interpret its function, the cell cycle, compensation circuits, guidance efficiency, and survivor selection alter the outcome.

## Established Scientific Starting Point

Perturb-seq combines CRISPR perturbation and single-cell RNA measurements to create large-scale gene-phenotype maps. However, selecting and evaluating relationships within the same data leads to overfitting and leakage.

## WRRA Reconstruction

WRRA-Cell records the effect of gene g along with the current state x, residue r, environment e, and intervention u. Although the structure was recovered from the synthetic data, the K562 actual audit failed to confirm strong verification, with zero FDR significant relationships out of 12.

## Comparative Reading

Results where no significant relationship is found in the actual audit of WRRA-Cell are not failures to be discarded. Once it is determined which relationships are visible only in synthetic data and disappear in actual cells, omissions in state variables, disturbance intensity, temporal resolution, and sample size become design variables for the next experiment. Failed toy predictions actually reveal model ownership errors.

In future audits, the single-cell state before perturbation and the trajectory after perturbation must be connected within the same lineage. We will examine whether the residual term adds predictive power to new cells or experimental batches even after controlling for guide efficiency, off-target, cell cycle, batch, and survivor bias. If there is no additionality, the strong interpretation of the residual term should be reduced.

> Boundary between interpretation and prediction: This result is neither a complete failure nor a success for WRRA. It is a partial failure, indicating that the restricted toy relationship was not confirmed in the actual data. By preserving the failure as is, the next verification design was narrowed down.

## Gene Regulation Is Conditional Permission to Execute

In prokaryotes, multiple functionally linked genes can be transcribed into a single operon. In the lac operon, when a repressor binds to the operator, the progression of RNA polymerase is inhibited, and when an inducer changes the binding state of the repressor, the inhibition is released. The binding of cAMP and CAP, which increases when glucose is low, promotes the transcription of the promoter. Since both negative and positive regulation are contained within a single circuit, the expression level cannot be determined solely by the presence of a gene. The concept of the operon was formalized in the regulatory model of Jacob and Monod \[63\].

In eukaryotic cells, promoters, enhancers, silencers, transcription factors, mediators, chromatin remodelers, and histone modifications are coupled through long distances and three-dimensional folding. This layer connects to epigenetic memory from Chapter 17 onwards. However, regulation does not end with transcription. Alternative splicing, RNA stability, translation initiation, and protein modification and degradation also produce different outputs from the same source.

Table 8A. Location of gene regulation and WRRA correspondence.

| **Adjustment position** | **Representative mechanism**                 | **Items changing in WRRA**         |
|-------------------------|----------------------------------------------|------------------------------------|
| DNA access              | nucleosome, remodeler, methylation           | SOURCE Accessibility and STATE     |
| Start of war            | repressor, activator, enhancer, sigma factor | The initiation rate allowed by LAW |
| RNA processing          | alternative splicing, 3′ terminal selection  | Executable RNA SOURCE              |
| translation             | RBS·Kozak context, uORF, miRNA               | RENDERER output efficiency         |
| Protein turnover        | ubiquitin, protease, autophagy               | Duration of Function STATE         |

## CRISPR-Cas Is a Natural Memory-Based Immune System

CRISPR-Cas is not originally a gene editing tool, but an adaptive immune system in which bacteria and archaea respond to foreign nucleic acids such as viruses and plasmids. In the first stage, adaptation, parts of the invading nucleic acid are selected as spacers and inserted into the CRISPR array. This sequence serves as a record of past invaders and an immune memory passed down to offspring. It has been experimentally confirmed that the addition and removal of specific spacers alter phage resistance \[64\].

In the second step, expression, the CRISPR array is transcribed into long pre-crRNA and processed into small crRNAs. In the third step, interference, crRNAs guide the Cas protein to a complementary target nucleic acid. In many DNA target types, PAMs act as a clue to distinguish between the self-CRISPR array and foreign targets. In the Cas9 system, crRNAs and tracrRNAs guide Cas9 to the target DNA to produce a double-strand break \[65\]. Not all CRISPR-Cas use Cas9, and the complex and target differ depending on the class and type.

Table 8B. Three execution steps of natural CRISPR-Cas.

| **step**                  | **Input and Executor**                  | **Success output and failure**                                           |
|---------------------------|-----------------------------------------|--------------------------------------------------------------------------|
| adaptation                | Foreign nucleic acids, Cas1-Cas2, etc.  | New spacer record; Wrong choice is autoimmune risk                       |
| Expression and processing | CRISPR array, RNA polymerase, Cas·RNase | Mature crRNA; unable to read memory upon processing failure              |
| interference              | crRNA-Cas complex, targets, and PAM     | Foreign nucleic acid cleavage; can be avoided by mismatch or PAM changes |

From the perspective of WRRA, foreign nucleic acids are inputs outside the boundary, and acquired spacers are residue left within the source by past events. The crRNA-Cas complex is a renderer that compares these residue to the current target, and cleavage is observable. This case clearly demonstrates that defense is not automatically achieved simply because a record exists; rather, transcription, processing, target recognition, and cleavage of the record are all required.

Engineered CRISPR editing is a rearrangement of the target recognition and cleavage mechanisms of innate immunity. Single-guide RNA, dCas9 transcriptional regulation, base editors, and prime editors have different outputs and error structures. Therefore, spacer acquisition, innate immunity, DNA cleavage editing, and epigenomic editing should not be treated as the same event under the single name of CRISPR.

Spacer acquisition and RNA-induced cleavage, which lie at the boundary between interpretation and prediction, are established mechanisms. However, on-target efficiency, off-target, immunocost, and phage evasion at new targets can only be predicted by incorporating guide, PAM, chromatin, cellular state, and selection conditions.

## Research Content and Validation Results

## WRRA-Cell: Testing Gene Perturbation and Present Residue

WRRA-Cell deals with the vertical closure of DNA–protein–division and other axes. It tests whether the cell creates the following state with current fast program activity x, slow residue h, nutrition n, substrate s, biomass b, waste w, and damage d without calling up a list of past events.

Xₖ=(xₖ,hₖ,nₖ,sₖ,bₖ,wₖ,dₖ), Xₖ₊₁=F(Xₖ,Rₖ,Bₖ,Uₖ) (36)

| **program** | **Representative cover**             |
|-------------|--------------------------------------|
| GROWTH      | MYC, E2F1, PCNA, MKI67, CCNA2, CCNB1 |
| STRESS      | ATF3, DDIT3, HSPA1A/B, JUN, FOS      |
| REPAIR      | ATM, ATR, RAD51, BRCA1, XPC, PARP1   |
| AUTOPHAGY   | ATG5, ATG7, BECN1, MAP1LC3B, SQSTM1  |
| QUIESCENCE  | CDKN1A/B, RB1, FOXO3, BTG1           |
| DEATH       | BAX, BBC3, PMAIP1, CASP3/8, FAS      |

Table 15. Program cover page frozen before viewing results in 0.3.1.

### Versions 0.1–0.3.1: Synthetic-Data Validation

| **step** | **Key Results**                                                                                                            | **Precise meaning**                            |
|----------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| 0.1      | Ledger error 2.49×10⁻¹⁴, restart error 0, adaptive remnant death peak reduced by 15.13%                                    | Internal inspection of design toys             |
| 0.2      | M2 rollout dominance in residue-positive systems, initial precondition 3/4                                                 | Complexity condition failure preservation      |
| 0.3      | Separation of claims regarding static and temporal data                                                                    | Prohibit memory claims with static Perturb-seq |
| 0.3.1    | In the positive spectrum, M2 has an RMSE 16.87% lower than M0 and 25.00% lower than M1; in the negative spectrum, M1 wins. | Validator passed 4/4                           |

Table 16. WRRA-Cell Calculation Lineage.

### Version 0.4: Audit of Real K562 Perturb-seq Data

34 pre-frozen marker maps were applied to the standardized gene × perturb signature matrix (8,055 genes, 2,012 perturb signatures, 1,907 unique targets) of the Replogle K562 essential gene Perturb-seq. Only 12/36 outgoing relationships from growth and repair could be evaluated, and 20,000 randomized targeted tests and Benjamini–Hochberg correction were used.

| **characteristic**  | **result**          | **verdict**                        |
|---------------------|---------------------|------------------------------------|
| FDR 5% significance | 0/12                | No support for the evaluation part |
| toy symbol match    | 4/12=33.3%, p=0.388 | Not noteworthy                     |
| toy weight Pearson  | r=0.365, p=0.243    | Not noteworthy                     |
| toy weight Spearman | ρ=0.462, p=0.131    | Not noteworthy                     |

Table 17. Initial Actual K562 Static Audit.

| **PARTIAL NON-CONFIRMATION / INSUFFICIENT FOR GLOBAL VERDICT. The evaluated toy relationship network was not verified, but the entire time residual of WRRA cannot be determined due to the absence of 4/6 perturbation sources and all time information.** |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Next Step

In the next chapter, we evaluate the most direct experiment in which the translation machine creates itself outside the cell.

### DOIs for This Chapter

> DOI 10.5281/zenodo.22290829 · Executable Genetic Expression in WRRA
>
> One sentence of this chapter: Gene regulation and CRISPR-Cas determine when to read a sequence and which target to execute on. Perturbation results can only be interpreted by measuring the regulatory circuit, guide efficiency, and compensation and selection together.

**WRRA BIOLOGY**
