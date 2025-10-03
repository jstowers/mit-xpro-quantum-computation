# Noise Processes

Tuesday, September 30, 2025

## Impact of Noise

Noise impacts nearly every aspect of quantum information.

Simple examples:

- __Quantum communication__

  - photon loss in a long optical fiber

  - measurement error in a photo detector

- __Quantum computing__

  - qubit decoherence

  - control errors in implementing a qubit gate

  - both of these reduce _gate fidelity_

Noise is ubiquitous.  And it's a problem because it causes _errors_.

## Categories of Noise

Noise can be categorized into two primary types:

1. __Systematic__

  - Noise arising from a process that can be traced back to a _systematic error_.

  - Example:

    - A control field isn't tuned properly and the X-gate does not rotate the qubit 180 degrees.  
  
    - The underlying error is the same and it produces noise every time an experiment is run.  The qubit measurement may not be the same, but once the control field is fixed, the noise goes away.

2. __Stochastic__

  - The random fluctuation of a _parameter_ that is coupled to the qubit.

  - Example:

    - A 50 ohm resistor will have voltage and current fluctuations called Johnson noise (thermal noise).

    - An oscillator used to create an X-pulse has _amplitude_ fluctuations.

  - Any randomly fluctuating parameter that couples to a qubit can cuase _decoherence_.


## Rabi Oscillation

In a Bloch sphere, apply a control field resonant iwht the qubit along the x-axis.  Leave the control field on.

The Bloch vector rotates around this field from north pole to south pole, over and over.  This oscillation is plotted as a cosine curve.  This is called _Rabi oscillation_.

The Rabi frequency is proportional to amplitude.  Fluctuations in the control field amplitude cuase fluctuations in the Rabi frequency.

__Result:__

Rabi oscillations decay over time due to the frequency fluctuations which are caused by the ampltitude noise of the control field.



