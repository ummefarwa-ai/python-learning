# ==========================================
# Pandas Data Selection
# ==========================================

import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"],
    "Age": [21, 22, 20, 23, 24],
    "City": ["Lahore", "Karachi", "Islamabad", "Multan", "Faisalabad"],
    "Marks": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# --------------------------
# Select a Single Column
# --------------------------

print("\nName Column:")
print(df["Name"])

# --------------------------
# Select Multiple Columns
# --------------------------

print("\nName and Marks:")
print(df[["Name", "Marks"]])

# --------------------------
# Select a Row using loc
# --------------------------

print("\nFirst Row using loc:")
print(df.loc[0])

# --------------------------
# Select Multiple Rows using loc
# --------------------------

print("\nRows 1 to 3 using loc:")
print(df.loc[1:3])

# --------------------------
# Select Specific Rows and Columns using loc
# --------------------------

print("\nName and Marks of Rows 1 to 3:")
print(df.loc[1:3, ["Name", "Marks"]])

# --------------------------
# Select a Row using iloc
# --------------------------

print("\nSecond Row using iloc:")
print(df.iloc[1])

# --------------------------
# Select Multiple Rows and Columns using iloc
# --------------------------

print("\nRows 0 to 2 and Columns 0 to 2:")
print(df.iloc[0:3, 0:3])

# --------------------------
# Select a Single Value
# --------------------------

print("\nMarks of Ahmed:")
print(df.loc[2, "Marks"])