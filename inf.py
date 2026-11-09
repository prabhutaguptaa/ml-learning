import numpy as np
arr=np.array([1,2,np.inf,4,5,-np.inf,7,8,9])
print(np.isinf(arr))  # Checking for infinite values in the array
print(np.nan_to_num(arr, posinf=10, neginf=-10))  #