import numpy as np
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array2 = np.delete(array1, 2,axis=1)  # Deleting the element at index 2
print(array2)