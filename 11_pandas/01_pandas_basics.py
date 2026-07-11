# ==========================================
# Pandas Basics
# ==========================================

# Importing the Pandas library
import pandas as pd

# Display Pandas version
print("Pandas Version:")
print(pd.__version__)

# Creating a simple Series
series = pd.Series([10, 20, 30, 40, 50])

print("\nSeries:")
print(series)

# Creating a simple DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [21, 22, 23],
    "City": ["Lahore", "Karachi", "Islamabad"]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# Display DataFrame information
print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nSummary Information:")
print(df.info())