"""
LINEAR SYSTEM OF EQUATIONS

Author:  Joe Stowers

Date:    October 16, 2025

Background:
-----------
Solve A𝐱 = 𝐛

where:

  A:  N x N matrix of coefficients
  
  b:  input vector

  x:  solution vector (unknowns)

Problem Statement:
------------------
Use python and numpy to solve this 2 x 2 linear
system of equations.

    2x +  y = 5
     x + 3y = 7
"""

import numpy as np

A = np.array([[2, 1], [1, 3]])
b = np.array([5,7])

x = np.linalg.solve(A,b)
print("x =", x) # x = [1.6 1.8]
