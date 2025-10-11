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
