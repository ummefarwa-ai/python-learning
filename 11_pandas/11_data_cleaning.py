# ==========================================
# Pandas Data Cleaning
# ==========================================
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ali", "Bilal"],
    "Age": [21, np.nan, 20, 21, 24],
    "City": ["Lahore", "Karachi", "Lahore", "Lahore", np.nan],
    "Marks": [85, 90, 78, 85, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# --------------------------
# Check Missing Values
# --------------------------

print("\nMissing Values:")
print(df.isna().sum())

# --------------------------
# Fill Missing Values
# --------------------------

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Unknown")

print("\nAfter Filling Missing Values:")
print(df)

# --------------------------
# Remove Duplicate Rows
# --------------------------

print("\nAfter Removing Duplicates:")
print(df.drop_duplicates())

# --------------------------
# Rename Columns
# --------------------------

df = df.rename(columns={"Marks": "Score"})

print("\nAfter Renaming Column:")
print(df)

# --------------------------
# Unique Values
# --------------------------

print("\nUnique Cities:")
print(df["City"].unique())

# --------------------------
# Number of Unique Values
# --------------------------

print("\nNumber of Unique Cities:")
print(df["City"].nunique())