# ==========================================
# Strings in Python
# ==========================================

# Creating strings
first_name = "Umme"
last_name = "Farwa"

print(first_name)
print(last_name)

print("----------------------------------")

# String concatenation
full_name = first_name + " " + last_name
print("Full Name:", full_name)

print("----------------------------------")

# String repetition
print(first_name * 3)

print("----------------------------------")

# Indexing
text = "Machine Learning"

print("First character:", text[0])
print("Second character:", text[1])
print("Last character:", text[-1])

print("----------------------------------")

# Slicing
print("First 7 characters:", text[:7])
print("Last 8 characters:", text[8:])
print("Characters 2 to 6:", text[2:7])

print("----------------------------------")

# Negative indexing
print(text[-1])
print(text[-2])
print(text[-5])

print("----------------------------------")

# String methods

name = "umme farwa"

# Capitalize
print(name.capitalize())

# Uppercase
print(name.upper())

# Lowercase
print(name.lower())

print("----------------------------------")

sentence = "I am learning Python"

# Endswith
print(sentence.endswith("Python"))
print(sentence.endswith("Java"))

print("----------------------------------")

# Replace
new_sentence = sentence.replace("Python", "Machine Learning")
print(new_sentence)

print("----------------------------------")

# Find
print(sentence.find("learning"))
print(sentence.find("Java"))

print("----------------------------------")

# Count
message = "Python is easy. Python is powerful."

print(message.count("Python"))
print(message.count("is"))

print("----------------------------------")

# Length of string
print("Length:", len(sentence))