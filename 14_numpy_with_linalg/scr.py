import numpy as np

A = np.array([
    [3, 2, 1],
    [1, 6, 2],
    [4, 1, 5]
])

b = np.array([360, 300, 675])
x = np.linalg.solve(A, b)
answer = np.round(x)
print(answer)