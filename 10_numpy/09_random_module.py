# ==========================================
# NumPy Random Module
# ==========================================

import numpy as np

# Set a seed for reproducible results
np.random.seed(42)

# --------------------------
# Random Float Values
# --------------------------

print("Random Floats:")
print(np.random.rand(5))

# Random 2D array
print("\nRandom 2D Array:")
print(np.random.rand(3, 3))

# --------------------------
# Random Integers
# --------------------------

print("\nRandom Integers (1 to 9):")
print(np.random.randint(1, 10, size=5))

print("\nRandom Integer Matrix:")
print(np.random.randint(10, 100, size=(3, 4)))

# --------------------------
# Random Choice
# --------------------------

colors = ["Red", "Green", "Blue", "Yellow"]

print("\nRandom Color:")
print(np.random.choice(colors))

print("\nRandom Colors:")
print(np.random.choice(colors, size=3))

# --------------------------
# Shuffle
# --------------------------

numbers = np.array([1, 2, 3, 4, 5])

print("\nOriginal Array:")
print(numbers)

np.random.shuffle(numbers)

print("Shuffled Array:")
print(numbers)

# --------------------------
# Random Normal Distribution
# --------------------------

print("\nRandom Numbers (Normal Distribution):")
print(np.random.randn(5))