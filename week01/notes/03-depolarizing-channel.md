# Depolarizing Channel on the Bloch Sphere

Monday, September 29, 2025

Prof. Peter Shor, MIT

---

## Noise Channels

Noise channels are the different noise mechanisms and the means by which they affect a quantum system.

Three simple noise channels:

1. depolarization

2. amplitude damping

3. dephasing


## Depolarization

The depolarizing channel represents a process where, with some probability, the quantum state is _depolarized_, meaning it's driven toward the __maximally mixed state__.  

This mixed state is completely random and carries no information.  It is represented as ${I/2}$

### Symmetric Noise

The depolarizing channel is symmetric because it treats all directions in the Bloch sphere _equally_.  It __shrinks__ the Bloch sphere uniformly.

### Purpose

The depolarizing channel is often used to model errors in quantum gates or storage due to environmental interactions.

We model these errors using three different quantum gates:

  1. X-gate

  2. Y-gate

  3. Z-gate

The depolarization probability is ${p}$.

We assume that each gate is equally likely with probability ${p/3}$.  In this way, the depolarization channel models errors as bit flips and phase flips.


## Mathematical Definition

With $(1-p)$, you do nothing.

With ${p/3}$, you apply each of the three __Pauli matrices__:


## Computing the Density Matrix

1. Define the input density matrix, ${\rho}$.

    - it can be a pure state or a mixed state

    - it must be a 2 x 2 Hermitian matrix, positive semi-definite, with trace 1

2. Choose the noise parameter, ${p}$.

3. Apply the channel formula

4. Verify the output