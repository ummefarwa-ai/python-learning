# ==========================================
# List Methods in Python
# ==========================================

numbers = [10, 20, 30]

print(numbers)

print("----------------------------------")

# append()

numbers.append(40)
print("append():", numbers)

# insert()

numbers.insert(1, 15)
print("insert():", numbers)

# extend()

numbers.extend([50, 60])
print("extend():", numbers)

print("----------------------------------")

# remove()

numbers.remove(20)
print("remove():", numbers)

# pop()

numbers.pop()
print("pop():", numbers)

print("----------------------------------")

# sort()

numbers.sort()
print("sort():", numbers)

# reverse()

numbers.reverse()
print("reverse():", numbers)

print("----------------------------------")

# index()

print("Index of 30:", numbers.index(30))

# count()

numbers.append(30)
print("Count of 30:", numbers.count(30))

print("----------------------------------")

# copy()

new_list = numbers.copy()

print("Copied list:", new_list)

print("----------------------------------")

# clear()

new_list.clear()

print("After clear():", new_list)