# Chapter 9 — Is DNA the Blueprint of Life?

**Is DNA the blueprint of life?**

> While it is intuitive to call DNA a blueprint, a blueprint does not build a factory on its own. DNA contains strong constraints and replicable information, but the molecular machinery and states necessary for execution are currently provided by the cell.

## Established Scientific Starting Point

The central principle organized the flow of information from DNA to RNA and then to protein. Subsequently, research on regulatory genomics, chromatin, RNA processing, translation regulation, and protein quality control expanded the layer between sequence and phenotype.

## WRRA Reconstruction

In WRRA, DNA is the center of the source but is not a complete observable. Reading frames, codons, and regulatory sequences can be interpreted, but protein mass and cell fate require both a state and a renderer.

## Comparative Reading

The four bases of DNA are simple letters, but their sequences are read within reading frames, regulatory motifs, repetitive structures, and three-dimensional folding. The same variant can produce completely different effects depending on the cell type and the stage of development. Therefore, the genotype-phenotype relationship is not a string transformation but a state-conditioned execution process.

This difference is particularly important in genetic engineering. Even if the target base is changed precisely, the corresponding gene may not be expressed, alternative pathways may compensate, proteins may misfold, or edited cells may selectively disappear from the cell population. If editing success rates and functional success rates are reported as a single figure, the owners of the failures become invisible.

> The boundary between interpretation and prediction separates reading possible proteins from sequences from matching functional amounts in actual cells. The latter is a prediction only when verified under new conditions.

## Research Content and Validation Results

## DNA: Information Storage, Coding Lower Bounds, and Renderer Dependence

In a general triplet genetic code, n sense codons and one stop codon are required to specify a peptide of n residues including the start amino acid. The grammatical coding lower bounds, excluding regulatory sequences, non-translation regions, and cloning handles, are as follows.

L\_coding,min(n) = 3n + 3 nucleotides (10)

L\_cassette = 3n + 3 + R\_executor (11)

The R\_executor is not a fixed universal constant. The promoter depends on which polymerase recognizes it, the ribosome, temperature, salt, and RNA structure under which the RBS operates, and the mechanism used for termination. Therefore, the question of "shortest expressed DNA" is a misdefined question unless the executer is fixed.

| **peptide residue n** | **Coding lower bound (nt)** | **Sequence selection information (bit, n log₂20)** | **High-loss boundary P\_full** |
| --------------------- | --------------------------- | -------------------------------------------------- | ------------------------------ |
| 5                     | 18                          | 21.6                                               | 0.936                          |
| 10                    | 33                          | 43.2                                               | 0.876                          |
| 20                    | 63                          | 86.4                                               | 0.767                          |
| 50                    | 153                         | 216.1                                              | 0.515                          |
| 100                   | 303                         | 432.2                                              | 0.265                          |
| 300                   | 903                         | 1296.6                                             | 0.019                          |

Table 6. Coding Length and Simple Process Loss Scenarios.

### Why DNA Does Not Execute by Itself

Y\_protein(t) = Φ(D, E, X₀, t) (12)

E = ∅ ⇒ Y\_protein(t) = 0 (ordinary DNA-directed translation) (13)

D is DNA, and E is an executer including polymerase, ribosomes, tRNA, aminoacyl-tRNA synthetase, initiation/elongation/termination factors, and the energy recovery system. Even though DNA encodes these proteins, an executer is required to read them at the initial moment. This is the DNA-only bootstrap problem. The RNA catalysis hypothesis shifts the executer boundaries, but it still requires specifying replication chemistry, substrates, energy, compartments, and heredity.

### Mutations and Information Budget

P\_intact(L | f) = fᴸ (14)

When replication fidelity f is constant, the probability that L independent positions are copied without errors that destroy function is fᴸ. Longer genetic information requires higher fidelity, repair, and redundancy. Although this equation is a baseline that omits actual error correlations, neutral mutations, and sequence-specific tolerances, it clearly demonstrates the genetic engineering trade-off that “increasing the genome size increases possible functions but also increases the cost of errors.”

## The Actual Execution Sequence of DNA Replication

DNA replication is not a symbolic operation that copies a sequence, but a material process in which various enzymes and structures combine in chronological order. The replication origin opens, helicase separates the two strands, and topoisomerase reduces the forward torsional stress. The exposed single strand is stabilized by SSB proteins or eukaryotic RPA. If any of these steps are delayed, the subsequent polymerization reaction cannot begin.

DNA polymerase synthesizes new strands only in the 5′ to 3′ direction. Since the two template strands are antiparallel, one becomes the leading strand, which is synthesized continuously along the direction of the replication fork, while the other becomes the lagging strand, which is synthesized by splitting into short Okazaki fragments. Primase provides RNA primers, and in bacteria, DNA polymerase III primarily performs elongation. In eukaryotic cells, polymerase α is involved in primer formation, while polymerases ε and δ share the responsibility of leading and lagging strand synthesis. The specific division of labor may vary depending on the biological species and organelles.

Even after elongation is complete, the new DNA is not finished. RNA primers must be removed, the empty spaces filled with DNA, and ligase must close the phosphodiester bonds between the fragments. In bacteria, DNA polymerase I and RNase H are involved in primer removal, while in eukaryotic cells, RNase H and FEN1 perform this function. Finally, the termination of the replication fork, the separation of entangled DNA, and the distribution of chromosomes or plasmids follow. Semi-conservative replication and discontinuous synthesis of the lagging strand were established by experiments of Meselson, Stahl, Okazaki, and others, respectively \[56,57].

Table 6A. Execution stages and failure points of DNA replication.

| **Execution step**         | **Representative components**                 | **The state remaining when failing**                                         |
| -------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------- |
| initiation                 | Replication origin, DNA or ORC·MCM            | Replication does not start or origin is used redundantly                     |
| release                    | helicase, topoisomerase, SSB·RPA              | Branch stop, single-strand damage, twist accumulation                        |
| primer formation           | primase, polymerase α                         | polymerase fails to start synthesis                                          |
| height                     | Bacteria Pol III, Eukaryotes Pol ε·δ          | Incomplete replication, errors, and fork collapse                            |
| primer removal             | Pol I, RNase H, FEN1                          | RNA residue or empty space                                                   |
| connection                 | DNA ligase                                    | Nick duration between Okazaki segments                                       |
| Termination and separation | topoisomerase, chromosome distribution device | Replication is complete, but it could not be delivered to the daughter cells |

## DNA Repair Maintains Information Closure

Replication errors and DNA damage are not the same thing. Replication errors originate from incorrectly inserted bases during polymerization, whereas DNA damage can occur at any time before or after replication due to ultraviolet radiation, oxidation, alkylation, hydrolysis, radiation, or metabolic byproducts. If damaged bases are repaired before replication, sequence information can be restored. Conversely, if the damage transforms into fixed base substitutions, insertions, or deletions, that state becomes the source for the next generation.

Direct repair reverses damaged chemical bonds. Base excision repair (BER) cleaves the AP site created by DNA glycosylase removing the damaged base, and polymerase and ligase fill the empty space. Uracil-DNA glycosylase isolated by Lindahl is a classic example demonstrating this principle \[58]. Nucleotide excision repair (NER) removes short oligonucleotides by cleaving both ends of a region that significantly distorts the helical structure, such as a UV dimer. Bacterial UvrABC excinuclease directly demonstrated a mechanism of cleaving both ends of the damaged site \[59].

Mismatch repair MMR finds incorrect base pairs and small insertion/deletion loops remaining immediately after replication and corrects the new strand. In the purified system of Escherichia coli, it was reconstructed as a reaction involving MutS, MutL, MutH, helicase, exonuclease, polymerase, and ligase \[60]. Double-strand breaks are more dangerous. Homologous recombination HR is relatively accurate because it restores information using homologous templates such as sister chromatids, but there are limitations on the cell cycles and templates that can be used. Non-homologous end ligation NHEJ directly connects severed ends, which is fast but can leave small insertions or deletions.

Table 6B. Ownership and Limitations of Major DNA Repair Routes.

| **Repair route** | **Main targets**                                         | **Execution logic and remaining risks**                                  |
| ---------------- | -------------------------------------------------------- | ------------------------------------------------------------------------ |
| Direct recovery  | Specific alkylation and photodamage                      | Directly reverses damage bonding but is limited to applicable damage     |
| BER              | Individual base damage such as oxidation and deamination | Synthesize one or two nucleotides again after removing a base            |
| NER              | UV dimer and bulky adduct                                | Cut out the entire distorted section and re-synthesize                   |
| MMR              | Mismatch and small loop after duplication                | New strands must be identified, and if they fail, the mutation is fixed. |
| HR               | Double-strand breakage and collapsed fork                | High-accuracy restoration using identical molds                          |
| NHEJ             | double strand cut                                        | Directly connects the ends but may leave small sequence changes          |

In WRRA, replication and repair are separate from the source and act as a renderer. Even for the same sequence, the probability of preservation varies depending on the replication enzyme, nucleotide pool, damage burden, checkpoint, and repair inventory. Therefore, f in Equation (14) represents not only the accuracy of the polymerase itself but also effective fidelity, which combines proofreading, damage occurrence, repair success, and pre-replication selection. If these values are not distinguished, the owner of the mutation is incorrectly attributed to the DNA itself.

The pathways of replication and repair at the boundary between interpretation and prediction are established biological processes. However, predicting which damage will lead to which mutation in a specific cell can only be achieved by measuring the damage amount, cell cycle, enzyme inventory, template availability, apoptosis, and selection together.

## Next Step

The next chapter covers the process by which conserved DNA is converted into actual function through transcription, RNA processing, translation, and protein quality control.

### DOIs for This Chapter

> DOI 10.5281/zenodo.22290829 · Executable Genetic Expression in WRRA
>
> One sentence from this chapter: DNA is maintained as a source across generations only when it is replicated and repaired. Sequence information and the execution unit that preserves that information are different layers.

**WRRA BIOLOGY**
