# ==========================================
# NumPy Array Slicing
# ==========================================

import numpy as np

# Create a 1D array
arr1 = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("Original 1D Array:")
print(arr1)

# Slicing examples
print("\nElements from index 1 to 4:")
print(arr1[1:5])

print("\nElements from the beginning to index 3:")
print(arr1[:4])

print("\nElements from index 4 to the end:")
print(arr1[4:])

print("\nEvery second element:")
print(arr1[::2])

print("\nReverse the array:")
print(arr1[::-1])


# Create a 2D array
arr2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("\n2D Array:")
print(arr2)

# Slicing rows
print("\nFirst two rows:")
print(arr2[:2])

# Slicing columns
print("\nFirst two columns:")
print(arr2[:, :2])

# Slicing rows and columns together
print("\nFirst two rows and first three columns:")
print(arr2[:2, :3])

# Last column
print("\nLast column:")
print(arr2[:, -1])

# Last row
print("\nLast row:")
print(arr2[-1])