# ==========================================
# Pandas Handling Missing Values
# ==========================================

import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"],
    "Age": [21, np.nan, 20, 23, np.nan],
    "Marks": [85, 90, np.nan, 88, 95],
    "City": ["Lahore", "Karachi", np.nan, "Multan", "Lahore"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# --------------------------
# Check Missing Values
# --------------------------

print("\nMissing Values:")
print(df.isna())

print("\nCount of Missing Values:")
print(df.isna().sum())

# --------------------------
# Fill Missing Values
# --------------------------

filled_df = df.fillna(0)

print("\nDataFrame after fillna(0):")
print(filled_df)

# Fill missing values in a specific column
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nAge Column after Filling with Mean:")
print(df)

# --------------------------
# Drop Missing Values
# --------------------------

drop_df = df.dropna()

print("\nDataFrame after dropna():")
print(drop_df)

# Drop rows with fewer than 3 non-missing values
thresh_df = df.dropna(thresh=3)

print("\nDataFrame after dropna(thresh=3):")
print(thresh_df)