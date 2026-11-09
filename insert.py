# np.insert(arra,idx,values,axis=None) is used to insert values along the given axis before the given indices of array.
# If axis is None, the input array is flattened first.
# if axis=0, values are inserted as new rows, and if axis=1, values are inserted as new columns.
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.insert(a, 1, [7, 8]))  # Inserting values as new rows
print()
b = np.insert(a, 2, [7, 8], axis=1)
print(b)