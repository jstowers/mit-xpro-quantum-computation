# Noise Characterization and Noise Power Spectral Density

Thursday, October 2, 2025

## Example 1 - Temporal Statistics

- We have a __single system__ with a noisy parameter, ${x}$.

- We set up a detector to measure ${x}$ and record how it varies with time.

- We can measure the noise, but we don't know the explict probability density function of the noise processes that underlie the fluctuations in ${x}$.

- This should be a straightforward measurement because there is only one system.

- If we measure for a long time, we can find a time average and get a reasonable estimate for the statistics of ${x}$.

- Used to study __time-correlated noise__, like 1/f noise in superconducting qubits.

## Example 2 - Ensemble Statistics

- We set up an ensemble of ${n}$ identical systems and record one sample of ${x}$ from each of them at the same time.

- We calculate the _ensemble average_ across many identical systems at a fixed time (spatial position).

## Autocorrelation Function

The autocorrelation function is a mathematical tool that quantifies how a noise signal is correlated with itself at different points in time.

It measures the _similarity_ between a signal at time ${t}$ and the same signal at a later time ${t + \tau}$, where ${\tau}$ is the time lag.


### Why correlate a noise signal to itself?

- White Noise: the autocorrelation function is a delta function, indicating no correlation between noise at different times.

- 1/f Noise: common in superconducting qubits, it has a slowly decaying autocorrelation function, indicating long-term correlations

## Ergodic Ensembles

When time averaging is equivalent to ensemble averaging, the statistics are called _ergodic_.

If the statistics calculated from a time trace are _independent_ of time, then the noise is statistically stationary.

While ergodicty implies stationarity, the opposite is not always true.

## Weak Stationarity ("Wide Sense")

The mean value is constant in time.

The autocorrelation function only depends on the time difference ${\tau}$

## Power Spectral Density (PSD)

The Wiener-Khinchine theorem posits that the autocorrelation function and power spectral density (PSD) are __Fourier transform pairs__.

This is critical because PSD describes how noise power is distributed across frequencies, affecting qubit coherence.




## Summary

If you can characterize the type of noise in the system, you can implement noise mitigation strategies or inform coherence times ${T_1, T_2}$ by linking noise correlations to dephasing or relaxation rates.

