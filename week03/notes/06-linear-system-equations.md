# Solving Linear Systems of Equations

Wednesday, October 15, 2025

## Lecturer

Prof. Aram Harrow

MIT, Physics

## What is a system of linear equations?

A linear system takes the form:

$A\mathbf{x} = \mathbf{b}$

where $\mathbf{x}$ and $\mathbf{b}$ are vectors.

We have a vector of unknowns that we want to find:

$x_1, x_2, x_3, ..., x_n$

## Parameterization

1. size of the vector

    - dimension ${N}$ = length of vector $\mathbf{x}$

2. size of the matrix

    - size of ${A}$ = $N x N$

3. sparcity, $S$

    - most of the entries of the matrix are 0
    
    - makes algorithms more efficient
  
4. condition number, $\kappa$


## Reference

[Quantum algorithm for linear systems of equations](https://arxiv.org/pdf/0811.3171) by Aram Harrow, Avinatan Hassidim, and Seth Lloyd, 2009.

Solving linear systems of equations is a common problem that arises both on its own and as a subroutine in more complex problems.


## Quantum Algorithm Theory

The quantum algorithm will solve a linear system of equations where the input and output are __amplitudes__ of a quantum state, not just a list of numbers stored in memory.

This is very similar to the quantum Fourier transform.

### Building Blocks

1. Hamiltonian simulation

2. Phase estimation

3. Filtering

State will evolve linearly, but not necessarily unitary.

Like light going through a filter.

### Condition Number

The condition number, $\kappa$, measures how far $A$ is from a unitary matrix.

It is calculated based on the larged and smallest eigenvalues of $A$:

  $\kappa = \frac{\lambda_{max}}{\lambda_{min}}$

where both $\lambda_{max}$ and $\lambda_{min} > 0$

The condition number plays several key roles:

1. bounds eigenvalue inversion and ensures numerical stability

2. controls QPE precision

3. governs success probability

4. determines runtime

### Key Conditions

When $\kappa = 1$, the matrix is invertible.


