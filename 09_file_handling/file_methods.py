# ==========================================
# File Methods in Python
# ==========================================

# read()

with open("sample.txt", "r") as file:
    print(file.read())

print("----------------------------------")

# readline()

with open("sample.txt", "r") as file:
    print(file.readline())

print("----------------------------------")

# readlines()

with open("sample.txt", "r") as file:
    print(file.readlines())

print("----------------------------------")

# Writing using with

with open("sample.txt", "w") as file:
    file.write("Learning Python File Handling.")

print("File updated successfully.")