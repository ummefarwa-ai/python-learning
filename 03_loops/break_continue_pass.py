# ==========================================
# break, continue and pass
# ==========================================

# -------- break --------

print("Break Example")

for number in range(1, 11):

    if number == 6:
        break

    print(number)

print("----------------------------------")

# -------- continue --------

print("Continue Example")

for number in range(1, 11):

    if number == 6:
        continue

    print(number)

print("----------------------------------")

# -------- pass --------

print("Pass Example")

for number in range(1, 6):

    if number == 3:
        pass

    print(number)