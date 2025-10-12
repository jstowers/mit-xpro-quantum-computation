# EPR Pair Violation

Friday, October 9, 2025

## Introduction

1. Alice and Bob share the following quantum-entangled Bell state: 

    ${\Phi^+ = \frac{1}{\sqrt{2}}}(\ket{00}+\ket{11})$

    -  Alice and Bob each have one qubit.  
    
    -  Each qubit is a two-level quantum system that can be in states $\ket{0}$, $\ket{1}$, or a superposition of both.

    -  State $\ket{00}$ means Alice's qubit is in $\ket{0}$ and Bob's qubit is in $\ket{0}$.
  
    -  Similarly, $\ket{11}$ means both qubits are in $\ket{1}$.

    -  The notation above describes a __superposition__ of the two states.  There is equal probability for each state:

        ${|\frac{1}{\sqrt{2}}|^2} = \frac{1}{2}$

    - The coefficient $(\frac{1}{\sqrt{2}})$ ensures the state is normalized (the probabilities sum to 1).

    - This Bell state is often called the __maximally entangled state__ for two qubits.  The state of one qubit is _directly_ tied to the state of the other, no matter how far apart they are.

2. Alice and Bob make the same measurement, ${M}$, on the Bloch sphere:

    $M = \alpha\sigma_x + \beta\sigma_z$

    - Alice and Bob get the same outcome.  Their measurement outcomes are __perfectly correlated__.

    - The probability of each correlated outcome is ${\frac{1}{2}}$

    - Two calculations are required:

        1. find the __eigenvalues__ of the operator.  The eignvalues are the _possible_ measurement outcomes.

        2. project thte state onto the __eigenstates__ corresponding to those eigenvalues, with probabilities determined by the state.

    - If they measure with the observable, ${\sigma_y}$, they get _opposite_ outcomes.


## Example

Alice measures $\ket{0}$.

Bob has qubit $\ket{0}$ and measures it with $\frac{\sigma_x + \sigma_z}{\sqrt{2}}$

What is the probability that Bob gets the eigenvector +1?

- The expectation of Bob's value is:

    $\bra{0}(\frac{\sigma_x + \sigma_z}{\sqrt{2}})\ket{0}$


## EPR Paradox

The Einstein, Podolsky, Rosen (EPR) paradox presents a thought experiment on quantum weirdness.

Imagine two, distant entangled particles.  For example, two polarization-entangled photons, one in Alice's lab and one in Bob's lab.  The labs are separated by a very large distance.

If Alice and Bob measure in the _same_ measurement basis, they will have correlated measurement results.

 - If Alice measures $H$ polarization, then Bob will measure $V$ polarization.

But if Alice and Bob measure in _different_ measurement bases, the result may change.

Einstein called this "spooky action at a distance." He believed there were "hidden variables" that were not captured in the quantum theory that predetermine the measurement result.  In other worlds, quantum theory was incomplete.


## Polarization of Light with Nonlinear Crystals

In most materials, the polarization (displacement of electric charges) induced by light is linear.  The polarization is proportional to the electric field:

  $P \propto E$


But in __nonlinear crystals__, the polarization includes higher-order terms:

  $P \propto E + \chi^{(2)} E^2 + \chi^{(3)} E^3 + ...

Common nonlinear crystals include Beta-Barium Borate (BBO) and Potassium Titanyl Phosphate (KTP).