import numpy as np
oneD_ARRAY = np.array([1, 2, 3, 4, 5])
twoD_ARRAY = np.array([[1, 2, 3], [4, 5, 6]])
threeD_ARRAY = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[5, 6], [7, 8]]])
print("1D Array:", oneD_ARRAY.ndim)
print("2D Array:", twoD_ARRAY.ndim)
print("3D Array:", threeD_ARRAY.ndim)
print(threeD_ARRAY)
