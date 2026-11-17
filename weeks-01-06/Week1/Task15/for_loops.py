# Task 15 - for loops

# 1. Iterate over a list
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print("Fruit:", f)

# 2. range(start, stop, step)
print("Even numbers 0-10:", [i for i in range(0, 11, 2)])

# 3. Iterate over a string and a dictionary
for ch in "Python":
    print(ch, end=" ")
print()
marks = {"Ali": 82, "Sara": 91, "Hamza": 76}
for name, score in marks.items():
    print(f"{name} scored {score}")

# 4. Multiplication table
n = 7
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 5. Sum of 1..100 and factorial of 6
total = 0
for i in range(1, 101):
    total += i
fact = 1
for i in range(1, 7):
    fact *= i
print("Sum 1..100 =", total, "| 6! =", fact)

# 6. for-else
for i in range(3):
    print("loop", i)
else:
    print("for loop finished without break")
