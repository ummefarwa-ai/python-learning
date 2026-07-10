# ==========================================
# Sets in Python
# ==========================================

# Creating a set

fruits = {"Apple", "Banana", "Mango", "Orange"}

print(fruits)

print("----------------------------------")

# Adding an element

fruits.add("Grapes")
print("After add():", fruits)

print("----------------------------------")

# Removing an element

fruits.remove("Banana")
print("After remove():", fruits)

print("----------------------------------")

# Discard an element

fruits.discard("Pineapple")   # No error if element doesn't exist
print("After discard():", fruits)

print("----------------------------------")

# Loop through a set

for fruit in fruits:
    print(fruit)

print("----------------------------------")

# Membership operator

if "Apple" in fruits:
    print("Apple is present in the set.")

print("----------------------------------")

# Length of a set

print("Length:", len(fruits))