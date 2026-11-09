import numpy as np
arr=np.array([1,2,3,3,5,6,7,8,9])
# print(np.split(arr,3))  # Splitting the array into 3 equal parts
arr2=np.array([[1,2,3,4],[5,6,7,8]])
print(np.hsplit(arr2,2))  # Splitting the 2D array into 2 parts along columns (axis=1pr
print(np.vsplit(arr2,2))  # Splitting the 2D array into 2 parts along rows (axis=0)