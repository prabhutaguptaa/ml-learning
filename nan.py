import numpy as np
arr=np.array([1,2,3,np.nan,5,6,7,8,np.nan,9])
print(np.isnan(arr))  # Checking for NaN values in the array
print(np.nanmean(arr))  # Calculating the mean of the array, ignoring NaN values

# replacing nan values
print(np.nan_to_num(arr, nan=6))  # Replacing NaN values with 6