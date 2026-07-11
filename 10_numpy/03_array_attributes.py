# ==========================================
# NumPy Array Attributes
# ==========================================

import numpy as np

# Create a sample array
arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print("Array:")
print(arr)

# Number of dimensions
print("\nNumber of Dimensions (ndim):")
print(arr.ndim)

# Shape of the array (rows, columns)
print("\nShape:")
print(arr.shape)

# Total number of elements
print("\nSize:")
print(arr.size)

# Data type of array elements
print("\nData Type (dtype):")
print(arr.dtype)

# Size of each element in bytes
print("\nItem Size:")
print(arr.itemsize)

# Total memory occupied by the array
print("\nTotal Bytes:")
print(arr.nbytes)

# Array type
print("\nArray Type:")
print(type(arr))