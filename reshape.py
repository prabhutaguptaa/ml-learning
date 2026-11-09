# reshape(rows,colomn) specify new shape if dimensions matches
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
print(b)  # Reshaping the array to 3 rows and 2 columns