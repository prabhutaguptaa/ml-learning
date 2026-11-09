import numpy as np
array1 = np.array([10, 20, 30, 40, 50,90,88])
print(array1[1:6:2])  # Slicing from index 1 to 6 with a step of 2
print(array1[::3])  # Slicing with a step of 3
print(array1[::-2])  # Reversing the array