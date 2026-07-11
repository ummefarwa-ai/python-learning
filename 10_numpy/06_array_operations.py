# ==========================================
# NumPy Array Operations
# ==========================================

import numpy as np

# Create two arrays
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

# --------------------------
# Arithmetic Operations
# --------------------------

print("\nAddition:")
print(arr1 + arr2)

print("\nSubtraction:")
print(arr1 - arr2)

print("\nMultiplication:")
print(arr1 * arr2)

print("\nDivision:")
print(arr1 / arr2)

print("\nFloor Division:")
print(arr1 // arr2)

print("\nModulus:")
print(arr1 % arr2)

print("\nPower:")
print(arr2 ** 2)

# --------------------------
# Universal Functions (ufuncs)
# --------------------------

print("\nSquare Root:")
print(np.sqrt(arr1))

print("\nSquare:")
print(np.square(arr2))

print("\nExponential:")
print(np.exp(arr2))

print("\nNatural Logarithm:")
print(np.log(arr2))

print("\nAbsolute Values:")
print(np.abs(np.array([-5, -10, 15, -20])))

# --------------------------
# Comparison Operations
# --------------------------

print("\nGreater Than 20:")
print(arr1 > 20)

print("\nEqual To:")
print(arr1 == arr2)

# --------------------------
# Aggregate Functions
# --------------------------

print("\nSum:")
print(np.sum(arr1))

print("\nMean:")
print(np.mean(arr1))

print("\nMaximum:")
print(np.max(arr1))

print("\nMinimum:")
print(np.min(arr1))