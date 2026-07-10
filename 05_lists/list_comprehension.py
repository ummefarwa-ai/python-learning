# ==========================================
# List Comprehension in Python
# ==========================================

# Squares of numbers

squares = [x ** 2 for x in range(1, 11)]

print("Squares:")
print(squares)

print("----------------------------------")

# Even numbers

even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print("Even Numbers:")
print(even_numbers)

print("----------------------------------")

# Convert to uppercase

names = ["farwa", "ali", "ahmed"]

upper_names = [name.upper() for name in names]

print(upper_names)

print("----------------------------------")

# String lengths

words = ["Python", "NumPy", "Pandas", "Machine Learning"]

lengths = [len(word) for word in words]

print(lengths)