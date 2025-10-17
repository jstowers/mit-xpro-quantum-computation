"""
LINEAR SYSTEM OF EQUATIONS

Solve A𝐱 = 𝐛

where:

  A:  N x N matrix of coefficients
  
  b:  input vector

  x:  solution vector (unknowns)

Author:  Joe Stowers

Date:    October 15, 2025
"""

import numpy as np

# use python and numpy to solve this
# 2x2 linear system of equations:
# 2x +  y = 5
#  x + 3y = 7

A = np.array([[2, 1], [1, 3]]) # coefficients
b = np.array([5,7]) # right-hand vector, b

x = np.linalg.solve(A,b)
print("x =", x) # x = [1.6 1.8]
