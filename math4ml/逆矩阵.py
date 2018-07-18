import numpy as np

A = [[1, 1, 3],
     [1, 2, 4],
     [1, 1, 2]]
Ainv = np.linalg.inv(A)


B = [[4, 6, 2],
     [3, 4, 1],
     [2, 8, 13]]

s = [9, 7, 2]

r = np.linalg.solve(B, s)
