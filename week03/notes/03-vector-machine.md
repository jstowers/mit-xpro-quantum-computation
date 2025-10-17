# Quantum Support Vector Machine (QSVM)

Monday, October 13, 2025

## Lecturer

Antonio Corcoles

Research Staff Member, IBM

## What is a kernel matrix?

A __kernel matrix__ ${K}$ is an $N \times N$ square matrix used in Support Vector Machines (SVMs) to represent the similarity betweeen pairs of data points in a dataset.

If states are normalized, diagonal entries are typically 1 in QSVMs.

Off-diagonal entries measure how similar $x_i$ and $x_j$ are in the quantum feature space.

In SVMs, the kernel matrix is used to find the _optimal hyperplane_ that separates classes.

The ability of a quantum computer to compute a kernel function and capture complex patterns in data potentially offers a computing advantage over classical methods.


## Support Vector Machine

Place __cutting hyperplane__ as far as possible from any data point in the training set.

The data points closet to the cutting hyperplane will be more difficult to classify.

These data points are called the support vectors.  Once you know the support vectors, you know the cutting hyperplane.

### Inner Product

A tool to help determine how close two points are in a given space.

### Kernel

The information that gives you the inner product between two points in a feature space.

Onc you know the kernel, you know the distance between each of the points.  From there, you can find the support vectors.

### Support Vector

Estimate support vectors outside of the quantum computer.  Easy to do if you know the kernel.



## CZ Gate

The __Controlled-Z gate__ is a two-qubit gate that operates on a control qubit and a target qubit.

It applies a Pauli-Z gate to the target qubit conditioned on the control qubit being in the $\ket{1}$ state.

The term "controlled" means that the action on the target qubit depends on the state of the control qubit.

  - For CZ and CNOT gates, the action on the target only happends when the control qubit is in a specific state, typically $\ket{1}$.

  - This convention aligns with classical computing control logic.  For instance, a controlled operation might depend on a bit being 1.

### Matrix Representation

In the computational basis ${\ket{00}, \ket{01}, \ket{10}, \ket{11}}, the CZ gate is represented by a 4x4 matrix:


## Computational Basis

In a single qubit system, the computational basis consists of the states $\ket{0}$ and $\ket{1}$.

These states are the _eigenvectors_ of the Pauli-Z operator:

$Z\ket{0} = \ket{0}$

$Z\ket{1} = -\ket{1}$

It is called "computational" because they are the standard reference basis for quantum computations, where qubits are measured to yield classical outcomes (0 or 1).

Quantum states are often expressed as _superpositions_ of these basis states.

Quantum gates (like CZ) _transform_ these basis states.


