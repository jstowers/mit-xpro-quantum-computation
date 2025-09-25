# Density Matrices:  Introduction

Monday, September 22, 2025

Prof. Isaac Chuang, MIT

---

## Four Postulates of Quantum Mechanics

1. __Wavefunction__

A mathematical object called a _wavefunction_ describes the state of a quantum system.

The wavefunction contains all the accessible physical information about the system in that particular state.

2. __Operators__

An _observable_ is a measurable physical property of a quantum system.  Observables include position, momentum, and energy.

Every observable is represented by a corresponding mathematical _operator_ that acts on the wavefunction.

3. __Measurement and Collapse__

When a physical property is measured, the possible outcomes are restricted to the _eigenvalues_ of the corresponding operator.

After measurement, the quantum state instantaneously _collapses_ into the specific state (eigenvector) associated with the measured eigenvalue.

4. __Time Evolution__

_Schrödinger's equation_ governs how the state of a quantum system changes over time.

This equation describes the continuous and deterministic evolution of the wavefunction, showing how the system progresses from one state to another.

## Quantum Error Correction (QEC)

For QEC, we need more than just the Four Postulates.  We also need _classical statistics_.

### Example

A qubit is a two-state quantum system.  

How do you describe a two-state quantum system, $\ket{\psi}$ and $\ket{\phi}$?

-  It is not a single quantum state, but rather a _statistical_ combination of two possible states with equal probability.

-  The _density matrix_ uses the outer product ($\otimes$) to combine two individual density matrices:

    $\rho = {\rho_1} \otimes {\rho_2}$


### What is the Outer Product ($\otimes$)?

The outer product, or _matrix product_, is the multiplication of two vectors to form a matrix.

-  The "ket" vector, $\ket{\psi}$, represents a vector in the complex vector space called a Hilbert space.  It is a column vector with dimension n x 1.

-  The "bra" vector, $\bra{\psi}$, represents a linear functional and is a row vector.  It is the _conjugate transpose_ of the ket and has a dimension 1 x n.

$\ket{\psi}\bra{\psi} = [1] x [0, 1] =  [1x0  1x1] =  [0 1]$
                        [0]             [0x0  0x1]    [0 0]



### Density Matrix

The sum of two outer product vectors yields the density matrix, ${\rho}$:

  ${\rho} = \frac{1}{2} \ket{\psi}\bra{\psi} + \frac{1}{2} \ket{\phi}\bra{\phi}$

${\rho}$ represents the statistical combination of two different pure states, $\ket{\psi}$ and $\ket{\phi}$.

### Stochastic Combinations of Quantum States

A mixed state arises when a physical system is not in one definite, pure state.  The uncertainty is _statistical_ or "stochastic" in nature.  Mixed states can arise in two main ways:

1. __Imperfect knowledge:__ the physicist may not be aware of the specific pure state the system is in.

2. __Interaction with an environment:__ when a quantum system interacts with its environment (_decoherence_), the system loses its phase coherence and becomes entangled with the environment.  When an observer measures only _part_ of the total entangled state, the subsystem is in a mixed state.

### Example 1

Consider the two-part state, $\ket{\psi_{AB}}$.  We draw the state as a quantum circuit originating from a single place.

If B measures its part of the quantum state, how do we describe part A?

  - The state of A will be a statistical combination depending on B's measurement result.

  - If B measures 0, then A is 0.

  - If B measures 1, then A is 1.


### Example 2

In this scenario, B measures in a different _basis_, not the 0 or 1 shown above.

Before measurement, B performs a Hadamard transform (H).

  -  The Hadamard transform turns a single qubit from a definite state (0 or 1) into a perfect 50/50 superposition of both.

  -  Applying a Hadamard gate to a qubit in state ${\ket{0}}$ yields:

      ${{\frac{1}{\sqrt{2}}}({\ket{0} + \bra{1}})}$

  -  This transform allows quantum computers to process multiple possibilities at once, enabling _quantum parallelism_.

The state of B before measurement is a superposition.  What about A?











