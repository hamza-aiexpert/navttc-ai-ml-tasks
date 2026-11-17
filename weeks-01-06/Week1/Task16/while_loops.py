# Task 16 - while loops

# 1. Counting
count = 1
while count <= 5:
    print("count =", count)
    count += 1

# 2. Sum of digits
n, s = 98765, 0
while n > 0:
    s += n % 10
    n //= 10
print("Sum of digits of 98765 =", s)

# 3. Fibonacci numbers below 100
a, b, fib = 0, 1, []
while a < 100:
    fib.append(a)
    a, b = b, a + b
print("Fibonacci:", fib)

# 4. Collatz sequence
x, steps = 27, 0
while x != 1:
    x = x // 2 if x % 2 == 0 else 3 * x + 1
    steps += 1
print("Collatz steps for 27:", steps)

# 5. Countdown with while-else
t = 3
while t > 0:
    print("T-minus", t)
    t -= 1
else:
    print("Lift off!")

# 6. Reverse a number
num, rev = 12345, 0
while num:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed 12345 =", rev)
