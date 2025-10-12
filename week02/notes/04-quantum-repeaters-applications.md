# Quantum Repeaters:  Applications

Saturday, October 11, 2025

Jason Orcutt

Research Staff Member, IBM

## Introduction

The __no-cloning theorem__ has been leveraged for very useful secure communication in quantum key distribution (QKD) systems, but the theorem presents a fundamental complication to _long-distance_ quantum communication.

To date, QKD systems have been limited to a practical distance of 100 km (62 mi) in optical fiber.  This is far below the global reach of today's classical internet.

## The Quantum Internet

The vision of a quantum internet was spelled out in a 2008 _Nature Review_ article by Jeff Kimble.

## Quantum Repeater Constraints

A photon (light) loses 0.2 db of optical power per kilometer of current optical fiber.  This signal loss is called __attenuation__.

The formula for power loss in dB is:

  $Loss(dB) = 10 \cdot log_{10}  \left(\frac{P_{out}}{P_{in}}\right)$

where $P_{in}$ is the inpute power and $P_{out}$ is the output power after traveling some distance.

Optical power (measured in watts) is proportional to the __number of photons per second__ arriving at a detector.

Each photon carries energy, $E = hv$, where $h$ is Planck's constant and $v$ is the speed of light.

For a stream of photons, power is:

  $P = N \cdot hv$

where $N$ is the photon flux (photons per second)