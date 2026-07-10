# ==========================================
# Set Operations in Python
# ==========================================

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

print("----------------------------------")

# Union

print("Union:")
print(set1.union(set2))

print("----------------------------------")

# Intersection

print("Intersection:")
print(set1.intersection(set2))

print("----------------------------------")

# Difference

print("Difference (set1 - set2):")
print(set1.difference(set2))

print("----------------------------------")

# Symmetric Difference

print("Symmetric Difference:")
print(set1.symmetric_difference(set2))

print("----------------------------------")

# Subset

print("Is {1,2} a subset of set1?")
print({1, 2}.issubset(set1))

print("----------------------------------")

# Superset

print("Is set1 a superset of {1,2}?")
print(set1.issuperset({1, 2}))

print("----------------------------------")

# Disjoint

print("Are set1 and {10,11} disjoint?")
print(set1.isdisjoint({10, 11}))