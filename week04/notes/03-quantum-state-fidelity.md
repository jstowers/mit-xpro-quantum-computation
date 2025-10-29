# Quantum State Fidelity

Sunday, October 19, 2025

## Introduction

For pure quantum states, __fidelity__ answers the question:

How well does one state, $\ket{\psi}$, represent another state, $\ket{\phi}$?

Fidelity, ${F}$, is given by the absolute value of the overlap between two states:

  $F(\ket{\psi}, \ket{\phi}) = |\bra{\phi}\ket{\phi}|$

Since both states can be represented as unit vectors, $F$ can be interpreted as the projection of $\psi$ onto $\phi$, or vice versa.

Fidelity is <= 1

    Low fidelity:  F near 0

    High fidelity: F near 1


## Fidelity Extended to Noisy Quantum States

How well does a density matrix, $\rho$, represent some state $\ket{\phi}$?

