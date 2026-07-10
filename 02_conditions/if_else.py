# ==========================================
# If-Else Statements in Python
# ==========================================

# ------------------------------------------
# Program 1: Even or Odd
# ------------------------------------------

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")

print("----------------------------------")


# ------------------------------------------
# Program 2: Positive, Negative or Zero
# ------------------------------------------

number = int(input("Enter another number: "))

if number > 0:
    print(f"{number} is Positive.")
elif number < 0:
    print(f"{number} is Negative.")
else:
    print("The number is Zero.")

print("----------------------------------")