# ==========================================
# Lists in Python
# ==========================================

# Creating a list

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)

print("----------------------------------")

# Accessing elements

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

print("----------------------------------")

# Slicing

print(fruits[1:3])

print("----------------------------------")

# Updating an element

fruits[1] = "Grapes"
print(fruits)

print("----------------------------------")

# Iterating through a list

for fruit in fruits:
    print(fruit)

print("----------------------------------")

# List length

print("Length:", len(fruits))