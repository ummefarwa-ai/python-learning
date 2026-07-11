# ==========================================
# Pandas Statistical Functions
# ==========================================

import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"],
    "Age": [21, 22, 20, 23, 24],
    "Marks": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# --------------------------
# Statistical Summary
# --------------------------

print("\nStatistical Summary:")
print(df.describe())

# --------------------------
# Mean
# --------------------------

print("\nMean Age:")
print(df["Age"].mean())

print("\nMean Marks:")
print(df["Marks"].mean())

# --------------------------
# Median
# --------------------------

print("\nMedian Marks:")
print(df["Marks"].median())

# --------------------------
# Maximum & Minimum
# --------------------------

print("\nMaximum Marks:")
print(df["Marks"].max())

print("\nMinimum Marks:")
print(df["Marks"].min())

# --------------------------
# Standard Deviation
# --------------------------

print("\nStandard Deviation:")
print(df["Marks"].std())

# --------------------------
# Variance
# --------------------------

print("\nVariance:")
print(df["Marks"].var())

# --------------------------
# Count
# --------------------------

print("\nCount:")
print(df["Marks"].count())

# --------------------------
# Sum
# --------------------------

print("\nTotal Marks:")
print(df["Marks"].sum())

# --------------------------
# Value Counts
# --------------------------

city_data = pd.Series([
    "Lahore",
    "Karachi",
    "Lahore",
    "Multan",
    "Karachi",
    "Lahore"
])

print("\nCity Frequency:")
print(city_data.value_counts())