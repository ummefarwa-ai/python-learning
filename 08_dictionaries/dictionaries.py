# ==========================================
# Dictionaries in Python
# ==========================================

# Creating a dictionary

student = {
    "name": "Umme Farwa",
    "age": 27,
    "country": "Pakistan"
}

print(student)

print("----------------------------------")

# Accessing values

print("Name:", student["name"])
print("Age:", student["age"])

print("----------------------------------")

# Adding a new key-value pair

student["course"] = "Artificial Intelligence"

print(student)

print("----------------------------------")

# Updating a value

student["age"] = 28

print(student)

print("----------------------------------")

# Looping through a dictionary

for key, value in student.items():
    print(f"{key}: {value}")

print("----------------------------------")

# Dictionary length

print("Length:", len(student))