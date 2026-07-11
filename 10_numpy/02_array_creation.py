# ==========================================
# NumPy Array Creation
# ==========================================

import numpy as np

# Creating arrays from Python lists
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1)

# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr2)

# Array of zeros
zeros = np.zeros((2, 3))
print("\nZeros Array:")
print(zeros)

# Array of ones
ones = np.ones((3, 2))
print("\nOnes Array:")
print(ones)

# Identity matrix
identity = np.eye(3)
print("\nIdentity Matrix:")
print(identity)

# Array with a range of values
arr_range = np.arange(0, 10, 2)
print("\nUsing arange():")
print(arr_range)

# Evenly spaced values
linspace = np.linspace(0, 1, 5)
print("\nUsing linspace():")
print(linspace)

# Array filled with a specific value
full = np.full((2, 2), 7)
print("\nUsing full():")
print(full)

# Empty array (contains uninitialized values)
empty = np.empty((2, 2))
print("\nUsing empty():")
print(empty)