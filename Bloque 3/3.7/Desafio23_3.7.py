import numpy as np 

A = np.array([[1, 0, 1],
              [4, -1, 4],
              [5, 6, 7]])

inversa = np.linalg.inv(A)
print(inversa)

traza = np.trace(inversa)
print(round(traza, 2))
