# ==========================================
# NumPy Practice Exercises
# ==========================================

import numpy as np

# --------------------------
# Practice 1: Create a 1D array
# --------------------------

arr1 = np.array([10, 20, 30, 40, 50])
print("Practice 1:")
print(arr1)

# --------------------------
# Practice 2: Create a 3x3 matrix of zeros
# --------------------------

zeros = np.zeros((3, 3))
print("\nPractice 2:")
print(zeros)

# --------------------------
# Practice 3: Create a 4x4 matrix of ones
# --------------------------

ones = np.ones((4, 4))
print("\nPractice 3:")
print(ones)

# --------------------------
# Practice 4: Create numbers from 1 to 20
# --------------------------

arr2 = np.arange(1, 21)
print("\nPractice 4:")
print(arr2)

# --------------------------
# Practice 5: Reshape the array
# --------------------------

reshape = arr2.reshape(4, 5)
print("\nPractice 5:")
print(reshape)

# --------------------------
# Practice 6: Slice the first row
# --------------------------

print("\nPractice 6:")
print(reshape[0])

# --------------------------
# Practice 7: Slice the last column
# --------------------------

print("\nPractice 7:")
print(reshape[:, -1])

# --------------------------
# Practice 8: Multiply every element by 10
# --------------------------

print("\nPractice 8:")
print(arr2 * 10)

# --------------------------
# Practice 9: Calculate statistics
# --------------------------

print("\nPractice 9:")
print("Sum:", np.sum(arr2))
print("Mean:", np.mean(arr2))
print("Maximum:", np.max(arr2))
print("Minimum:", np.min(arr2))

# --------------------------
# Practice 10: Generate random integers
# --------------------------

random_numbers = np.random.randint(1, 101, size=10)
print("\nPractice 10:")
print(random_numbers)

# --------------------------
# Practice 11: Sort the random numbers
# --------------------------

print("\nPractice 11:")
print(np.sort(random_numbers))

# --------------------------
# Practice 12: Find unique values
# --------------------------

duplicate_array = np.array([1, 2, 2, 3, 4, 4, 5, 5, 6])

print("\nPractice 12:")
print(np.unique(duplicate_array))