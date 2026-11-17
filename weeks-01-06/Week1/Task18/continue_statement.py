# Task 18 - continue statement

# 1. Skip a letter
for ch in "geeksforgeeks":
    if ch in ("e", "s"):
        continue
    print(ch, end="")
print()

# 2. Print only odd numbers 1..10
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# 3. Sum of numbers 1..20 skipping multiples of 3
total = 0
for i in range(1, 21):
    if i % 3 == 0:
        continue
    total += i
print("Sum skipping multiples of 3:", total)

# 4. continue in a while loop
i = 0
while i < 8:
    i += 1
    if i == 5:
        continue
    print("i =", i)

# 5. Skip invalid data
readings = [21.5, None, 22.0, -999, 23.1]
valid = []
for r in readings:
    if r is None or r == -999:
        continue
    valid.append(r)
print("valid readings:", valid)
