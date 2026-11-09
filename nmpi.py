# for only large data sets use numpy
python_list=[1,2,3,4,5]
print("Python List:", python_list)

import numpy as np
numpy_array=np.array([1,2,3,4,5])
numpy_array=np.array(python_list)

print("NumPy Array:", numpy_array)  

twod_array=np.array([[1,2,3],[4,5,6]])
print("2D NumPy Array:\n", twod_array)

