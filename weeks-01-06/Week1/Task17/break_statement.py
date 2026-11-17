# Task 17 - break statement

# 1. Stop at first match
for ch in "geeksforgeeks":
    if ch == "e":
        print("Found 'e', breaking out")
        break
    print("current letter:", ch)

# 2. First number divisible by 7 and 5 above 100
n = 100
while True:
    n += 1
    if n % 7 == 0 and n % 5 == 0:
        print("First number > 100 divisible by 5 and 7:", n)
        break

# 3. Prime check using break/else
for num in [2, 15, 17, 21, 29]:
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            print(num, "is not prime (divisible by", d, ")")
            break
    else:
        print(num, "is prime")

# 4. Search in a list
data = [4, 8, 15, 16, 23, 42]
target = 16
for idx, v in enumerate(data):
    if v == target:
        print(f"{target} found at index {idx}")
        break
else:
    print("not found")
