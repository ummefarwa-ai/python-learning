# ==========================================
# Recursion in Python
# ==========================================

# Factorial using recursion

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print("Factorial of 5 =", factorial(5))

print("----------------------------------")

# Sum of natural numbers

def sum_numbers(n):

    if n == 1:
        return 1

    return n + sum_numbers(n - 1)

print("Sum =", sum_numbers(5))

print("----------------------------------")

# Fibonacci using recursion

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")