import numpy as np
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array2=np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
# print(np.stack((array1, array2), axis=0))  # Stacking along a new axis (axis=0)
# print(np.stack((array1, array2), axis=1))  # Stacking along a new axis (axis=1)
# print(np.stack((array1, array2), axis=2))  # Stacking along a new axis (axis=2)
print(np.vstack((array1, array2)))  # Vertical stacking
print(np.hstack((array1, array2)))  # Horizontal stacking
