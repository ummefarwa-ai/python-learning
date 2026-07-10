# ==========================================
# Tuples in Python
# ==========================================

# Creating tuples

fruits = ("Apple", "Banana", "Mango", "Orange")

print(fruits)

print("----------------------------------")

# Accessing elements

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

print("----------------------------------")

# Slicing

print("Sliced tuple:", fruits[1:3])

print("----------------------------------")

# Length of tuple

print("Length:", len(fruits))

print("----------------------------------")

# Loop through a tuple

for fruit in fruits:
    print(fruit)

print("----------------------------------")

# Tuple packing

student = ("Umme Farwa", 27, "Pakistan")

print(student)

print("----------------------------------")

# Tuple unpacking

name, age, country = student

print("Name:", name)
print("Age:", age)
print("Country:", country)

print("----------------------------------")

# count()

numbers = (10, 20, 30, 20, 40, 20)

print("Count of 20:", numbers.count(20))

print("----------------------------------")

# index()

print("Index of 30:", numbers.index(30))

print("----------------------------------")

# Nested tuple

coordinates = ((10, 20), (30, 40), (50, 60))

print(coordinates)

print("----------------------------------")

# Membership operator

if "Apple" in fruits:
    print("Apple is present in the tuple.")