# ==========================================
# Pandas Series
# ==========================================

import pandas as pd

# Creating a Series from a list
numbers = pd.Series([10, 20, 30, 40, 50])

print("Series:")
print(numbers)

# Display index
print("\nIndex:")
print(numbers.index)

# Display values
print("\nValues:")
print(numbers.values)

# Access elements
print("\nFirst Element:")
print(numbers[0])

print("\nLast Element:")
print(numbers[4])

# Creating a Series with custom index
students = pd.Series(
    [85, 90, 78],
    index=["Ali", "Sara", "Ahmed"]
)

print("\nSeries with Custom Index:")
print(students)

# Accessing data using labels
print("\nMarks of Sara:")
print(students["Sara"])

# Series from a dictionary
employee = {
    "Name": "John",
    "Age": 25,
    "City": "Berlin"
}

employee_series = pd.Series(employee)

print("\nSeries from Dictionary:")
print(employee_series)

# Basic statistics
print("\nMaximum Value:")
print(numbers.max())

print("\nMinimum Value:")
print(numbers.min())

print("\nMean:")
print(numbers.mean())

print("\nSum:")
print(numbers.sum())