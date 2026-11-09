import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.concatenate((a, b), axis=1)  # Concatenating along columns (axis=1)
print(c)  # Output: [[1 2 5 6] [3 4 7 8]]
d = np.concatenate((a, b), axis=0)  # Concatenating along rows (axis=0)
print(d)  # Output: [[1 2] [3 4] [5