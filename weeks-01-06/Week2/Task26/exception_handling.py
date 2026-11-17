# Task 26 - Exception handling in Python

# 1. try / except
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Caught ZeroDivisionError:", e)

# 2. Multiple except blocks
def convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"  ValueError: {value!r} is not a number")
    except TypeError:
        print(f"  TypeError: cannot convert {type(value).__name__}")
for v in ["42", "abc", None]:
    print("convert", repr(v), "->", convert(v))

# 3. try / except / else / finally
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  cannot divide by zero")
    else:
        print("  success, result =", result)
        return result
    finally:
        print("  finally: always runs")
divide(10, 2); divide(1, 0)

# 4. Handling IndexError / KeyError
for action in (lambda: [1, 2, 3][5], lambda: {"a": 1}["b"]):
    try:
        action()
    except (IndexError, KeyError) as e:
        print("Caught", type(e).__name__, "->", e)

# 5. File handling with exceptions
try:
    with open("does_not_exist.txt") as f:
        f.read()
except FileNotFoundError as e:
    print("File error:", e)

# 6. raise and assert
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
try:
    set_age(-5)
except ValueError as e:
    print("Raised:", e)
try:
    assert 1 + 1 == 3, "math is broken"
except AssertionError as e:
    print("AssertionError:", e)

# 7. Writing then reading a file safely
with open("demo.txt", "w") as f:
    f.write("Hello file handling\nSecond line\n")
with open("demo.txt") as f:
    print("File content:", f.read().splitlines())
