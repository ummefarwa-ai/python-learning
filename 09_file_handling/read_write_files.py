# ==========================================
# Reading and Writing Files in Python
# ==========================================

# Writing to a file

file = open("sample.txt", "w")

file.write("Welcome to Python File Handling.\n")
file.write("This is the second line.")

file.close()

print("Data written successfully.")

print("----------------------------------")

# Reading a file

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()

print("----------------------------------")

# Appending to a file

file = open("sample.txt", "a")

file.write("\nThis line was appended.")

file.close()

print("Data appended successfully.")