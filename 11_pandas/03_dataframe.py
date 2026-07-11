# ==========================================
# Pandas DataFrame
# ==========================================

import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha"],
    "Age": [21, 22, 20, 23],
    "City": ["Lahore", "Karachi", "Islamabad", "Multan"],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# --------------------------
# Display first rows
# --------------------------

print("\nFirst 3 Rows:")
print(df.head(3))

# --------------------------
# Display last rows
# --------------------------

print("\nLast 2 Rows:")
print(df.tail(2))

# --------------------------
# Shape
# --------------------------

print("\nShape:")
print(df.shape)

# --------------------------
# Column Names
# --------------------------

print("\nColumns:")
print(df.columns)

# --------------------------
# Data Types
# --------------------------

print("\nData Types:")
print(df.dtypes)

# --------------------------
# Summary Information
# --------------------------

print("\nInformation:")
df.info()

# --------------------------
# Statistical Summary
# --------------------------

print("\nStatistical Summary:")
print(df.describe())

# --------------------------
# Access a Single Column
# --------------------------

print("\nNames:")
print(df["Name"])

# --------------------------
# Access Multiple Columns
# --------------------------

print("\nName and Marks:")
print(df[["Name", "Marks"]])