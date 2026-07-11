# ==========================================
# Pandas GroupBy
# ==========================================

import pandas as pd

# Create a sample DataFrame
data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT"],
    "Employee": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal", "Usman", "Fatima"],
    "Salary": [50000, 45000, 60000, 70000, 48000, 75000, 55000],
    "Experience": [2, 3, 5, 7, 4, 8, 3]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# --------------------------
# Group by Department
# --------------------------

group = df.groupby("Department")

# Mean Salary
print("\nAverage Salary by Department:")
print(group["Salary"].mean())

# Maximum Salary
print("\nMaximum Salary by Department:")
print(group["Salary"].max())

# Minimum Salary
print("\nMinimum Salary by Department:")
print(group["Salary"].min())

# Employee Count
print("\nNumber of Employees in Each Department:")
print(group["Employee"].count())

# Multiple Aggregations
print("\nSalary Statistics:")
print(group["Salary"].agg(["mean", "min", "max", "sum"]))

# Mean Experience
print("\nAverage Experience by Department:")
print(group["Experience"].mean())