# ==========================================
# Pandas Practice Exercises
# ==========================================

import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"],
    "Age": [21, 22, 20, 23, 24],
    "Marks": [85, 90, 78, 88, 95],
    "City": ["Lahore", "Karachi", "Islamabad", "Multan", "Lahore"]
}

df = pd.DataFrame(data)

# --------------------------
# Practice 1: Display the DataFrame
# --------------------------

print("Practice 1:")
print(df)

# --------------------------
# Practice 2: Display the first 3 rows
# --------------------------

print("\nPractice 2:")
print(df.head(3))

# --------------------------
# Practice 3: Select the Name column
# --------------------------

print("\nPractice 3:")
print(df["Name"])

# --------------------------
# Practice 4: Students with Marks greater than 85
# --------------------------

print("\nPractice 4:")
print(df[df["Marks"] > 85])

# --------------------------
# Practice 5: Sort by Marks (Descending)
# --------------------------

print("\nPractice 5:")
print(df.sort_values(by="Marks", ascending=False))

# --------------------------
# Practice 6: Average Marks
# --------------------------

print("\nPractice 6:")
print(df["Marks"].mean())

# --------------------------
# Practice 7: Maximum Marks
# --------------------------

print("\nPractice 7:")
print(df["Marks"].max())

# --------------------------
# Practice 8: Value Counts of City
# --------------------------

print("\nPractice 8:")
print(df["City"].value_counts())

# --------------------------
# Practice 9: Unique Cities
# --------------------------

print("\nPractice 9:")
print(df["City"].unique())

# --------------------------
# Practice 10: DataFrame Information
# --------------------------

print("\nPractice 10:")
df.info()

# --------------------------
# Practice 11: Statistical Summary
# --------------------------

print("\nPractice 11:")
print(df.describe())

# --------------------------
# Practice 12: Select Name and Marks Columns
# --------------------------

print("\nPractice 12:")
print(df[["Name", "Marks"]])