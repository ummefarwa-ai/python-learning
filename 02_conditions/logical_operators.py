# ==========================================
# Logical Operators
# ==========================================

age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ").lower()

# AND
if age >= 18 and citizen == "yes":
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

print("----------------------------------")

marks = int(input("Enter your marks: "))

# OR
if marks >= 90 or marks == 89:
    print("Excellent!")
else:
    print("Keep improving.")

print("----------------------------------")

# NOT
logged_in = False

if not logged_in:
    print("Please log in first.")