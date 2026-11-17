# Task 20 - User defined functions in Python

# 1. Basic function with return value
def add(a, b):
    return a + b
print("add(3, 4) =", add(3, 4))

# 2. Default and keyword arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Ali"), greet("Sara", greeting="Salam"))

# 3. *args and **kwargs
def total(*numbers):
    return sum(numbers)
def describe(**info):
    return ", ".join(f"{k}={v}" for k, v in info.items())
print("total:", total(1, 2, 3, 4), "|", describe(name="Ali", city="Lahore"))

# 4. Returning multiple values
def min_max(values):
    return min(values), max(values)
lo, hi = min_max([4, 9, 1, 7])
print("min, max:", lo, hi)

# 5. Recursion
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print("5! =", factorial(5), "| fib(10) =", fib(10))

# 6. Variable scope (local / global)
x = "global"
def show_scope():
    x = "local"
    return x
def change_global():
    global x
    x = "changed"
print(show_scope(), x); change_global(); print(x)

# 7. Lambda, map, filter
square = lambda n: n * n
nums = [1, 2, 3, 4, 5, 6]
print("lambda:", square(9))
print("map:", list(map(lambda n: n * 2, nums)))
print("filter:", list(filter(lambda n: n % 2 == 0, nums)))

# 8. Inner (nested) function and closure
def make_multiplier(k):
    def multiply(n):
        return n * k
    return multiply
triple = make_multiplier(3)
print("triple(7) =", triple(7))

# 9. Docstring and function that takes a function
def apply_twice(func, value):
    """Apply func two times to value."""
    return func(func(value))
print(apply_twice(lambda n: n + 5, 1), "|", apply_twice.__doc__)

# 10. Prime checker
def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, int(n ** 0.5) + 1))
print("primes < 30:", [n for n in range(30) if is_prime(n)])
