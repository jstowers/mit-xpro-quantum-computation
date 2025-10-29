# Benchmarking Quantum States

Sunday, October 19, 2025

## Noisy Intermediate Scale Quauntum (NISQ) Computers

- Smaller-scale quantum computers

    - 50 - 100 qubits

    - up to a few thousand qubitss

- Not error-corrected

- Utility limited by:

    1. intrinsic gate fidelity enabled by the hardware
    
    2. depth they can support

- Quantum Volume metric developed to measure different modalities and architectures

- Implement small, application-specific algorithms

## Introduction

- For large-scale commercialization, quantum computers will require __error-protected__ qubits peforming computations with __large circuit depth__.

- How do we benchmark quantum states in quantum gates?

- How well can we prepare, operate, and even measure a quantum system?

- __tomography__ - process of _reconstructing_ a complete description of a quantum state by taking "slices" (measurements) from multiple angles.

_ __state tomography__ - benchmark quantum gates

- Theories

    1. Fault-tolerant error correction

    2. Threshold theorem

