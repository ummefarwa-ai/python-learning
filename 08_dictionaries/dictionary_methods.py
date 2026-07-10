# ==========================================
# Dictionary Methods in Python
# ==========================================

student = {
    "name": "Umme Farwa",
    "age": 27,
    "country": "Pakistan"
}

print(student)

print("----------------------------------")

# get()

print(student.get("name"))

print("----------------------------------")

# keys()

print(student.keys())

print("----------------------------------")

# values()

print(student.values())

print("----------------------------------")

# items()

print(student.items())

print("----------------------------------")

# update()

student.update({"age": 28})

print(student)

print("----------------------------------")

# pop()

student.pop("country")

print(student)

print("----------------------------------")

# popitem()

student.popitem()

print(student)

print("----------------------------------")

# copy()

new_student = student.copy()

print(new_student)

print("----------------------------------")

# clear()

new_student.clear()

print(new_student)