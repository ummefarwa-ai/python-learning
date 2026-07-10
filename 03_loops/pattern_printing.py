# ==========================================
# Pattern Printing
# ==========================================

# Triangle Pattern

rows = 5

for i in range(1, rows + 1):
    print("*" * i)

print("----------------------------------")

# Reverse Triangle

for i in range(rows, 0, -1):
    print("*" * i)