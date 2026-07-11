# ==========================================
# NumPy Array Indexing
# ==========================================

import numpy as np

# Create a 1D array
arr1 = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(arr1)

# Accessing elements
print("\nFirst Element:")
print(arr1[0])

print("\nThird Element:")
print(arr1[2])

print("\nLast Element:")
print(arr1[-1])


# Create a 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print("\n2D Array:")
print(arr2)

# Accessing elements in a 2D array
print("\nElement at Row 1, Column 2:")
print(arr2[0, 1])

print("\nElement at Row 2, Column 3:")
print(arr2[1, 2])

print("\nElement at Row 3, Column 1:")
print(arr2[2, 0])


# Create a 3D array
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("\n3D Array:")
print(arr3)

# Accessing an element in a 3D array
print("\nElement at [1, 0, 1]:")
print(arr3[1, 0, 1])