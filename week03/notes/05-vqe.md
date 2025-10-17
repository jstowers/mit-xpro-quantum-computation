# Practical Quantum Simulation: Contemporary VQE

Tuesday, October 14, 2025

## Electronic Structure Problems in Chemistry

How can we develop a quantum algorithm?

From quantum mechanics, an electron is a __fermion__.

  - it obeys symmetry rules

  - it is indistinguishable from other electrons

### Haber-Bosch Nitrogen Fixation Process

Ammonia is used to make fertilizer which feeds 50% of the world.

__Haber-Bosch__ is the current industrial process to take atmospheric N2 and H2 and make ammonia (NH3).  It produces NH3 in high yield, but requires 400-500 C and 200-300 atm pressure.  This is a massive energy input that consumes abgout 1-2% of global energy.

In nature, the __nitrogenase enzyme__ can "fix" nitrogen at room temperature and atomospheric pressure, meaning that it can break down the triple bond between N2 atoms and get H atoms to attach.  This process requires no huge energy investment, but the ammonia yield is very low.

But _how_ this enzyme can break N2's triple bond remains elusive due to its quantum complexity.

Quantum computers can "solve" this problem by accurately simulating the enzyme's quantum behavior, potentially revealing the full reaction pathway.

## Variational Quantum Eigensolver (VQE)

### Background

Variational Quantum Eigensolver (VQE) is a hybrid __quantum-classical algorithm__ designed to approximate the __lowest eigenvalue (ground state energy)__ of a quantum system's Hamiltonian operator.

VQE is particularly useful for Noisy Intermediate-Scale Quantum (NISQ) devices where noise exists and qubits are limited.

### Theory

VQE is based on the __variational principle__ of quantum mechanics.  

For any trial wavefunction, $|\psi\rangle$, the expectation value of the Hamiltonian, $H$, satisfies:

$\langle \psi | H | \psi \rangle \geq E_0$

where $E_0$ is the true ground state energy.

### Why determine the ground state energy?

In quantum mechanics, most physical systems naturally settle into their lowest energy state at absolute zero temperature or under an equilibrium condition.

This ground state dictates all __stable properties__ of the system:

    • shape

    • reactivity

    • conductivity

    • magnetism

    • etc.

Finding the ground state energy (and its wavefunction) of a system is like unlocking the "default configuration" of matter.


### Process

1. parameterize the quantum state

1. set the knobs to an experimental value

1. compute the terms in the Hamiltonian

1. turn the control knobs until a minimum is found

### Key Questions

1. Will sources of error _scale_ in a way that does not require large resources for error correction?

1. Will the quantum processor be stable over the time needed to make all the correlator measurements?


