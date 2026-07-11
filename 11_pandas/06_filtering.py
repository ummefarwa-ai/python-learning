# ==========================================
# Pandas Data Filtering
# ==========================================

import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"],
    "Age": [21, 22, 20, 23, 24],
    "City": ["Lahore", "Karachi", "Islamabad", "Multan", "Lahore"],
    "Marks": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# --------------------------
# Filter by Marks
# --------------------------

print("\nStudents with Marks greater than 85:")
print(df[df["Marks"] > 85])

# --------------------------
# Filter by Age
# --------------------------

print("\nStudents whose Age is less than 22:")
print(df[df["Age"] < 22])

# --------------------------
# Filter by City
# --------------------------

print("\nStudents from Lahore:")
print(df[df["City"] == "Lahore"])

# --------------------------
# Multiple Conditions (AND)
# --------------------------

print("\nStudents with Marks > 80 and Age > 21:")
print(df[(df["Marks"] > 80) & (df["Age"] > 21)])

# --------------------------
# Multiple Conditions (OR)
# --------------------------

print("\nStudents from Lahore or Karachi:")
print(df[(df["City"] == "Lahore") | (df["City"] == "Karachi")])

# --------------------------
# Using isin()
# --------------------------

print("\nStudents from Lahore or Multan:")
print(df[df["City"].isin(["Lahore", "Multan"])])

# --------------------------
# Using between()
# --------------------------

print("\nStudents with Marks between 80 and 90:")
print(df[df["Marks"].between(80, 90)])