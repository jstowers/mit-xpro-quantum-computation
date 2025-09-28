# Density Matrices:  Introduction

Monday, September 22, 2025

Prof. Isaac Chuang, MIT

---

## Lecture 1: Density Matrices: 

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

## Single Qubit Hilbert Space

The basis states are:

${\ket{0}} = \begin{pmatrix}1\\0\\\end{pmatrix}$

${\ket{1}} = \begin{pmatrix}0\\1\\\end{pmatrix}$

### Orthogonality

These two states are mutually orthogonal.  Orthogonality is essential for quantum mechanics because:

  1. when the quantum system is measured, it collapses into one of the eigenstates (basis states) corresponding to the observable being measured.

  2. zero probability of overlap between state ${\ket{a}}$ and state ${\ket{b}}$.

  3. perfect distinguishability between the states.  If a measurement finds the system in state ${\ket{a}}$, it definitively was not in state ${\ket{b}}$.


### Proof of Orthogonality

1. Calculate the inner product of the two basis states, ${\ket{\psi}}$ and ${\ket{\phi}}$

  - The inner product is formed by multiplying the complex conjugate of ${\psi}$ by ${\phi}$

2. Evaluate the inner product:


### Normalization

These states are normalized.

  - If you take the inner product of one state by itself, you get get 1.


## Quantum Error Correction (QEC)

For QEC, we need more than just the Four Postulates.  We also need _classical statistics_.

### Example

A qubit is a two-state quantum system.  

How do you describe a two-state quantum system, $\ket{\psi}$ and $\ket{\phi}$?

-  It is not a single quantum state, but rather a _statistical_ combination of two possible states with equal probability.

-  The _density matrix_ uses the outer product ($\otimes$) to combine two individual density matrices:

    $\rho = {\rho_1} \otimes {\rho_2}$


### What is the Outer Product ($\otimes$)?

The outer product, or _matrix product_, is the multiplication of two vectors to form a matrix.  It is also called the projection operator.

-  The "ket" vector, $\ket{\psi}$, represents a vector in the complex vector space called a Hilbert space.  It is a column vector with dimension n x 1.

-  The "bra" vector, $\bra{\psi}$, represents a linear functional and is a row vector.  It is the _conjugate transpose_ of the ket and has a dimension 1 x n.

$\ket{\psi}\bra{\psi} = \begin{pmatrix}1\\0\\\end{pmatrix} \begin{pmatrix}1 & 0\end{pmatrix}$


### Pure States

A quantum system in a pure state means it is not entangled with its environment or any other system.

A pure state, $\ket{\psi}$, is represented mathematically as a single state vector.  

Here are examples of two pure states, $\ket{0}$ and $\ket{1}$:

  $\ket{\psi} = \ket{0} = \begin{pmatrix}1\\0\\\end{pmatrix}$

  $\ket{\psi} = \ket{1} = \begin{pmatrix}0\\1\\\end{pmatrix}$

Note that a coherent superposition of pure states is also a pure state:

  $\alpha\ket{0} + \beta\ket{1}$

### Why do Density Matrices Matter?

The density matrix formulation is designed to compute the _expectation value_ of any observable, $\hat{A}$, in a quantum system.

#### Key Observables

Key observables in a quantum system include:

1. Position ($\hat{x}$)

2. Momentum ($\hat{p}$)

3. Spin ($\hat{S}$)

4. Angular momentum ($\hat{L}$)

5. Hamiltonian (total energy of system) ($\hat{H}$)


### Density Matrix of a Pure State

The density matrix representation, $\rho$, of a pure state is the _outer product_ of the pure state with itself.

The __outer product__ represents a complete, unambiguous description of the pure state with no classical uncertainty.


The __outer product__ is found by multiplying the pure state vector, $\ket{\psi}$, with its conjugate transpose, $\bra{\psi}$.

  $\rho = \ket{\psi}\bra{\psi}$

Example:

For the pure state, $\ket{0}$, the density matrix is:

  $\rho = \ket{0}\bra{0}$

  $\rho = \begin{pmatrix}1\\0\\\end{pmatrix} \begin{pmatrix}1 & 0\end{pmatrix}$

  $\rho = \begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix}$

For the pure state, $\ket{1}$, the density matrix is:

  $\rho = \ket{1}\bra{1}$

  $\rho = \begin{pmatrix}0\\1\\\end{pmatrix} \begin{pmatrix}0 & 1\end{pmatrix}$

  $\rho = \begin{pmatrix} 0 & 0 \\ 0 & 1\end{pmatrix}$


### Density Matrix of a Mixed State

The density matrix, $\rho$, of a mixed state is a statistical mixture of  pure states with individual weights or probabilities:

  $\rho = \displaystyle\sum_{i} p_i\ket{\psi_i}\bra{\psi_i}$

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

  - The state of A will be a _statistical combination_ depending on B's measurement result.

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

---

## Lecture 2:  Density Matrix Properties

A matrix, ${\rho}$, is a density matrix if and only if:

1. the trace, ${Tr}$, of ${\rho}$ must equal 1.

2. ${\rho}$ must be real and greater than or equal to 0.


### Trace of a Square Matrix

The trace of a _square_ matrix is the sum of its diagonal elements.

For a square matrix, ${A}$, the trace with elements ${a_{ij}}$ will be:

  ${Tr(A) = a_{11}} + a_{22} + a_{33} + ... + a_{nn}$ 


A density matrix can be made from the _probabalistic_ combination of pure states:

### Spectral Decomposition

The spectral decomposition (or _eigendecomposition_) of a _diagonalizable_ matrix A is a factorization of the matrix into the product of its eigenvectors and eigenvalues.

Here is the formula for matrix, ${A}$:

  ${A} = {P} {DP^{-1}} $

where ${P}$ is the matrix formed by the eigenvectors and ${D}$ is a diagonal matrix containing the corresponding eigenvalues.


### State Vector

A state vector is a mathematical object represented as a vector in a _complex vector space_ called a Hilbert space.

### Pure State

A pure quantum state, $\ket{\psi}$, is represented mathematically as a single state vector.

For state 0, the vector notation is:

  $\ket{\psi} = \ket{0} = \begin{pmatrix} 1 \\ 0 \\ \end{pmatrix}$

For state 1, the vector notation is:

  $\ket{\psi} = \ket{1} = \begin{pmatrix} 0 \\ 1 \\ \end{pmatrix}$






### Infinite Unravelings

The concept of infinite unravelings and the interpretation of density matrices in purified forms will be key ideas in understanding the intuition of QEC.


## Single Qubit System

A single qubit exists in a two-dimensional Hilber space.


## Two Qubit System

In a two qubit syste, two single qubit systems combine into one larger system.

The combined system is a four-dimensional Hilbert space.

The system requires 4 orthonormal basis vectors to form the computational basis.

To compute the computational basis, you must calculate the four tensor products from the two single qubit states:

1. $\ket{0}\ket{0} = \ket{00} = \ket{0} \otimes \ket{0}$

2. $\ket{0}\ket{1} = \ket{01} = \ket{0} \otimes \ket{1}$

3. $\ket{1}\ket{0} = \ket{10} = \ket{1} \otimes \ket{0}$

4. $\ket{1}\ket{1} = \ket{11} = \ket{1} \otimes \ket{1}$

## Tensor Product Calculation

Consider two generic column vectors $\begin{pmatrix} a_0 \\ a_1 \\ \end{pmatrix}$ and $\begin{pmatrix} b_0 \\ b_1 \\ \end{pmatrix}$.

To calculate the tensor product (${\otimes}$) of these two vectors:

$\begin{pmatrix} a_0 \\ a_1 \\ \end{pmatrix} \otimes \begin{pmatrix} b_0 \\ b_1 \\ \end{pmatrix}$

Place the second column vector inside the first column vector.  The first column vector values will scale (multiply) the second column vector values:

$\begin{pmatrix} a_0 begin{pmatrix} b_0 \\ b_1 \\ \end \\ \end$

## Quantum Tensor Product

For a quantum system, each column vector represents a single qubit.

## Generalization 

Any two-qubit system can be described as a linear combination of the four computational basis vectors:

$\ket{\psi} = \alpha_{00}{\ket{00}} + \alpha_{01}{\ket{01}} + \alpha_{10}{\ket{10}} + \alpha_{11}{\ket{11}}$

How do you find the different coefficients, $\alpha$?

- Take the inner product of $\ket{\psi}$.  That will cancel out all the basis vectors because they are orthogonal.


