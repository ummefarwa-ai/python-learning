# ==========================================
# Lambda Functions in Python
# ==========================================

# Lambda for addition

add = lambda a, b: a + b

print(add(10, 20))

print("----------------------------------")

# Lambda for square

square = lambda x: x ** 2

print(square(5))

print("----------------------------------")

# Lambda with map()

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)

print("----------------------------------")

# Lambda with filter()

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)