# Quantum Repeaters

Saturday, October 11, 2025

## Practical Concern

Over long distances, how do we ensure that __photons__ and their quantum information traverse the communication channel without getting lost along the way?

Based on the __no-cloning theorem__, quantum states _cannot_ be amplified in the way we amplify classical signals.

  - A single photon cannot be copied into more than one photon carrying the same quantum information.

We need a _clever_ solution for quantum mechanics. What quantum takes away with one hand, it gives back with the other.

## Example

Alice and Bob want to establish a secure communication link using a Quantum Key Distribution (QKD) protocol.

Consider:

  - They live in different cities over 500 km (310 mi) apart.

  - They each have photon sources and detectors.

  - Between them is a large mountain range which prevents any free space (air) communication.

  - A fiber optic cable connects them.  It is a flexible, transparent glass fiber designed to guide and transmit _light_ over long distances.

Issue:

  - Optical fiber does not perfectly transmit light.

  - There exists a small, but non-negligible probability that a photon gets lost along the way.

  - Usually caused from glass inhomogeneity:

    1. incoherent scattering

    2. photon absorption

  - For typical optical fibers, the losses are remarkably low:

    1. 0.2 dB / kilometer

    2. For a 1 km length of fiber, that represents a __5% chance__ of photon loss

  - But photon loss scales exponentially for every kilometer.

  - At 500 km, the probability of a _single_ photon arriving successfully is 1 / 10 billion (0.0000000001%)!

## Entanglement to the Rescue!

Entanglement __swapping__ can be used to _teleport_ the state of one qubit onto another qubit without the two qubits directly interacting.

Each node is called a _quantum repeater_ and it uses a Bell state to swap entanglement from Alice's original photon to the photon coming from the quantum repeater.

- With each repeater, the average distance a photon needs to travel decreases _linearly_.

- In turn, this _exponentially_ decreases the probability of a photon getting lost in the fiber.

The generation of entangled photons is _stochastic_.  So entangled photons won't arrive at each node simulataenously.

We need a means to _store_ quantum information, effectively, a quantum memory.

## Summary

Quantum repeaters will enable long-distance entanglement distribution in quantum communication.

A linear increase in resources causes an exponential decrease in the loss of quantum information over long distances.