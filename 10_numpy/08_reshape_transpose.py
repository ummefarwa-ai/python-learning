# ==========================================
# NumPy Reshape and Transpose
# ==========================================

import numpy as np

# Create a 1D array
arr = np.arange(1, 13)

print("Original Array:")
print(arr)

# --------------------------
# Reshape
# --------------------------

reshape_2x6 = arr.reshape(2, 6)
print("\nReshape to 2 x 6:")
print(reshape_2x6)

reshape_3x4 = arr.reshape(3, 4)
print("\nReshape to 3 x 4:")
print(reshape_3x4)

reshape_4x3 = arr.reshape(4, 3)
print("\nReshape to 4 x 3:")
print(reshape_4x3)

# --------------------------
# Flatten
# --------------------------

flattened = reshape_3x4.flatten()

print("\nFlattened Array:")
print(flattened)

# --------------------------
# Transpose
# --------------------------

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nOriginal Matrix:")
print(matrix)

print("\nTranspose using .T:")
print(matrix.T)

print("\nTranspose using np.transpose():")
print(np.transpose(matrix))

# --------------------------
# Shape Comparison
# --------------------------

print("\nOriginal Shape:")
print(matrix.shape)

print("\nTransposed Shape:")
print(matrix.T.shape)