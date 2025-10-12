# QKD:  Practical Issues and Challenges

Saturday, October 11, 2025

Prof. Jeffrey Shapiro

Electrcal Engineering, MIT

## Quantum Key Distribution (QKD)

Randomness is a valuable resource.

Shared randomness is of great value for secure communication.

Quantum computers running Shor's factoring algorithm could break the RSA public key infrastructure on which internet commerce relies.

QKD systems are now commercially available and have been demonstrated in the United States, Europe, and Japan.  Another

Without quantum repeaters, __only 10%__ of BB84 light survives a 50 km fiber optic cable.  For a 100 km fiber, the survival fraction drops to __1 %__.

## Floodlight QKD (FL-QKD)

Introudced in 2015-16 as a paradigm shift from traditional single-photon QKD schemes, FL-QKD "floods" the quantum channel with many photons per encoding

  - Alice transmits many photons per bit.

  - Bob uses an optical amplifier.

Floodlight QKD, unlike BB84, is a __two-way__ protocol.

## Implementation Challenges

Catherine Lee

Technical Staff, MIT Lincoln Laboratory

### Goal of QKD

- Establish a shared list of _random_ numbers that can be used for encryption.

- The list of random numbers is called a __key__.

- After a successful QKD session, Alice and Bob should have identical copies of the key, while eavesdropper Eve should have no information about the random numbers in the key.

### Secret Key Rate

How quickly are the secret random numbers shared?

Units:  bits / sec

The secret key rate depends ons:

  1. encryption algorithm

  2. desired rate of secured communication

### Holy Grail: One Time Pad Encyrption

The One-Time Pad (OTP) encryption algorithm has been mathematically proven to be secure.

But it has limitations:

  1. it consumes one bit of the secret key for each bit of the message to be encrypted

  2. the secret keys cannot be reused

Gilbert Vernam (AT&T) and Joseph Mauborgne (U.S. Army cryptologist) developed OTP between 1917-19 using telegraph equipment.  

They created a system that combined a message with a random key.  As long as the key is perfectly random, used only once, and kept secret, OTP is an unbreakable, perfect cipher.



