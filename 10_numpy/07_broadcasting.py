# ==========================================
# NumPy Broadcasting
# ==========================================

import numpy as np

# --------------------------
# Broadcasting with a Scalar
# --------------------------

arr = np.array([10, 20, 30, 40])

print("Original Array:")
print(arr)

print("\nAdd 5:")
print(arr + 5)

print("\nMultiply by 2:")
print(arr * 2)

# --------------------------
# Broadcasting Between Arrays
# --------------------------

arr1 = np.array([[1], [2], [3]])
arr2 = np.array([10, 20, 30])

print("\nArray 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

print("\nBroadcasted Addition:")
print(arr1 + arr2)

# --------------------------
# Another Example
# --------------------------

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

vector = np.array([100, 200, 300])

print("\nMatrix:")
print(matrix)

print("\nVector:")
print(vector)

print("\nMatrix + Vector:")
print(matrix + vector)

# --------------------------
# Broadcasting Rules
# --------------------------

print("\nShapes:")
print("Matrix Shape:", matrix.shape)
print("Vector Shape:", vector.shape)

print("\nNumPy automatically expands the smaller array")
print("to match the larger array when possible.")