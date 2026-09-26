# **Chapter 24**

Extending WRRA to the Nervous System and Behavior

> Just because genetic information creates a cell does not mean that behavior is output directly from DNA. Neural connections, current activities, sensory inputs, the body's state, and the environment form a closed loop.

## Established Scientific Starting Point

C. elegans has a known connectivity map of 302 neurons and has accumulated calcium imaging and behavioral data, making it a testing ground for the whole nervous system-body-environment model.

## WRRA Reconstruction

WRRA-Worm 0.1 constructed a sensorimotor loop of 23 nodes and 57 relationships. It passed AVA and AVB removal, same-current restart, and resource ledger internal inspection.

## Comparative Reading

The connectome provides part of the source or law of behavior, but it does not fix the actual trajectory. Even with the same connections, behavior changes if neuromodulators, sensory inputs, body posture, and feedback from muscles and the environment differ. Reading the nervous system solely as a wiring diagram is the same kind of abbreviation as reading DNA solely as a sequence.

The next step of WRRA-Worm is to connect the 23-node toy circuit with actual 302-neuron data. It must simultaneously predict calcium activity and behavior, and make predictions in experiments involving neuronal ablation and the absence of sensory stimulation. Closed-loop external validation is a stronger threshold than open-loop fitting with the body and environment removed.

> The boundary between interpretation and prediction is not an independent biological discovery, but rather a PASS for the internal consistency of the toy circuit. The closed-loop external verification of the formal connectome, actual calcium kinetics, and behavior is OPEN.

## Research Content and Validation Results

## WRRA-Worm: Extending Relations and Behavior beyond Genetic Information

Life does not end with gene expression. WRRA-Worm 0.1 implements the sensory–neuromotor loop of C. elegans with 23 nodes and 57 relationships. This model places neurons as information sources, chemical synapses and electrical connections as relationships, senses, muscles, the body, and the environment as boundaries, and adaptive states and resources as current residue.

vₖ₊₁=tanh{0.72vₖ+qₖ⊙\[W\[vₖ\]₊+GΔvₖ+0.85uₖ−0.62aₖ\]} (37)

aₖ₊₁=clip(0.94aₖ+0.06\|vₖ₊₁\|,0,1) (38)

| **Internal inspection**        | **result** | **margin**                                 |
|--------------------------------|------------|--------------------------------------------|
| Reversal after forward contact | 0.071587   | Design path operation                      |
| AVA Reversal                   | 0          | Wired dependency                           |
| Forward after rear contact     | 0.021224   | Design path operation                      |
| AVB removal forward            | 0          | Wired dependency                           |
| Same current restart error     | 0          | Verification of determinism implementation |
| Initial/Final Resource Ledger  | 23/23      | Dimensionless internal preservation        |

Table 18. WRRA-Worm 0.1 Internal Results.

This case illustrates an upper renderer layer where cellular components generated from genes lead to behavioral phenotypes through network-state-environment loops. However, the full 302-neuron model, polarity and weight measurements, calcium imaging, muscle-body-environment closed loops, and holdout excision verification are open.

## Next Step

Now, the research results are translated into audit procedures for actual gene editing and cell design.

> One sentence from this chapter: Just because genetic information creates a cell does not mean that behavior is output directly from DNA. Neural connections, current activity, sensory input, the state of the body, and the environment form a closed loop.
