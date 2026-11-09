import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])
print([x + y for x, y in zip(array1, array2)])  # Element-wise addition, arrays

# fast method
sum=array1 + array2  # Element-wise addition using NumPy
print(sum)

product=array1 * array2  # Element-wise multiplication using NumPy
print(product)

prod_3=array1 * 3  # Element-wise multiplication with a scalar
print(prod_3)