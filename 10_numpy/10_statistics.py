# ==========================================
# NumPy Statistical Functions
# ==========================================

import numpy as np

# Create a sample array
arr = np.array([12, 25, 18, 30, 45, 22, 28])

print("Array:")
print(arr)

# --------------------------
# Basic Statistics
# --------------------------

print("\nSum:")
print(np.sum(arr))

print("\nMean:")
print(np.mean(arr))

print("\nMedian:")
print(np.median(arr))

print("\nMinimum:")
print(np.min(arr))

print("\nMaximum:")
print(np.max(arr))

# --------------------------
# Measures of Spread
# --------------------------

print("\nRange:")
print(np.ptp(arr))   # Max - Min

print("\nStandard Deviation:")
print(np.std(arr))

print("\nVariance:")
print(np.var(arr))

# --------------------------
# Position Statistics
# --------------------------

print("\n25th Percentile:")
print(np.percentile(arr, 25))

print("\n50th Percentile (Median):")
print(np.percentile(arr, 50))

print("\n75th Percentile:")
print(np.percentile(arr, 75))

# --------------------------
# Cumulative Functions
# --------------------------

print("\nCumulative Sum:")
print(np.cumsum(arr))

print("\nCumulative Product:")
print(np.cumprod(arr))