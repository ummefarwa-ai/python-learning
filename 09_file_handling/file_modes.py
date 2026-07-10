# ==========================================
# File Modes in Python
# ==========================================

print("r  -> Read")
print("w  -> Write")
print("a  -> Append")
print("x  -> Create")
print("r+ -> Read and Write")
print("w+ -> Write and Read")
print("a+ -> Append and Read")

print("----------------------------------")

# Creating a file

with open("new_file.txt", "x") as file:
    file.write("New file created successfully.")

print("File created.")