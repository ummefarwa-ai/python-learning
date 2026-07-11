# ==========================================
# Pandas Read and Write Files
# ==========================================

import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [21, 22, 23],
    "City": ["Lahore", "Karachi", "Islamabad"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# --------------------------
# Save DataFrame to CSV
# --------------------------

df.to_csv("students.csv", index=False)

print("\nData has been saved to 'students.csv'.")

# --------------------------
# Read Data from CSV
# --------------------------

new_df = pd.read_csv("students.csv")

print("\nData Read from CSV:")
print(new_df)

# --------------------------
# Display First Rows
# --------------------------

print("\nFirst 2 Rows:")
print(new_df.head(2))

# --------------------------
# Display Last Rows
# --------------------------

print("\nLast 2 Rows:")
print(new_df.tail(2))