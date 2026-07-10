# ==========================================
# Functions in Python
# ==========================================

# Function without parameters

def greet():
    print("Welcome to Python!")

greet()

print("----------------------------------")

# Function with parameters

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Umme Farwa")

print("----------------------------------")

# Function with return value

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)

print("----------------------------------")

# Function with default parameter

def country(name, country="Pakistan"):
    print(f"{name} lives in {country}.")

country("Farwa")
country("Ali", "Germany")

print("----------------------------------")

# Function returning multiple values

def calculate(a, b):
    return a + b, a - b

sum_result, difference = calculate(15, 5)

print("Sum:", sum_result)
print("Difference:", difference)