# ==========================================
# Pandas Sorting
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

print("Original DataFrame:")
print(df)

# --------------------------
# Sort by Age (Ascending)
# --------------------------

print("\nSort by Age (Ascending):")
print(df.sort_values(by="Age"))

# --------------------------
# Sort by Marks (Descending)
# --------------------------

print("\nSort by Marks (Descending):")
print(df.sort_values(by="Marks", ascending=False))

# --------------------------
# Sort by Multiple Columns
# --------------------------

print("\nSort by City and Marks:")
print(df.sort_values(by=["City", "Marks"]))

# --------------------------
# Sort by Index
# --------------------------

print("\nSort by Index:")
print(df.sort_index())

# --------------------------
# Reset Index
# --------------------------

sorted_df = df.sort_values(by="Marks", ascending=False).reset_index(drop=True)

print("\nSorted DataFrame with Reset Index:")
print(sorted_df)