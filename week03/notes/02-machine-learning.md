# Quantum Advantage in Machine Learning

Monday, October 13, 2025

## Lecturer

Diego Ristè

Scientist, Quantum Engineering and Computing

Raytheon BBN Technologies

## Learning Parity with Noise (LPN) Experiment

Raytheon, in collaboration with IBM Research, demonstrated a clear quantum advantage using only a few highly noisy qubits.

The __oracle__ is a device with an unknown string, $k$, encoded on it.

### Goal

Learn what $k$ is by observing the effect of the oracle on _random_ input bit.

### What is a parity function?

In mathematics, a parity function checks whether the sum of a set of binary values (0s and 1s) is even or odd.

### How is a parity function calculated?

Take a string of bits, say $x = [x_1, x_2, ..., x_n]$, where each $x_i$ is either 0 or 1.  The parity function computs the sum of these bits and uses modulo 2 arithmetic to determine if the sum is even or odd:

  - 0 => the number of 1s is even (even parity)

  - 1 => the number of 1s is odd (odd parity)

### Example

Input: x = [1, 0, 1, 1]

Sum of bits: 1 + 0 + 1 + 1 = 3

Parity: 3 mod 2 = 1 (odd => output is 1)

### How are parity functions used?

Parity functions are used in computer science and cryptography to __detect errors__ in data transmission, verify data integrity, or define certain computational problems like the Learning Parity with Noise (LPN) problem.
