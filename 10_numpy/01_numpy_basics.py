# ==========================================
# NumPy Basics
# ==========================================

# Importing NumPy library
import numpy as np

# Creating a simple NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Display the array
print("Array:")
print(arr)

# Type of object
print("\nType:")
print(type(arr))

# Array data type
print("\nData Type:")
print(arr.dtype)

# Number of dimensions
print("\nDimensions:")
print(arr.ndim)

# Shape of array
print("\nShape:")
print(arr.shape)

# Total number of elements
print("\nSize:")
print(arr.size)

# Memory used by each element (in bytes)
print("\nItem Size:")
print(arr.itemsize)

# Total memory occupied by the array
print("\nTotal Bytes:")
print(arr.nbytes)