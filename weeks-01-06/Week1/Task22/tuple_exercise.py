# Task 22 - Tuple data type
t = (1, 2, 3, "four", 5.0)
print("Tuple:", t, "| type:", type(t).__name__, "| length:", len(t))
print("Indexing/slicing:", t[0], t[-1], t[1:3])

single = (42,)          # comma makes it a tuple
print("Single-element tuple:", single, type(single).__name__)

# Immutability
try:
    t[0] = 100
except TypeError as e:
    print("Cannot modify a tuple ->", e)

# Packing / unpacking
point = (3, 4)
x, y = point
print("Unpacked x, y:", x, y)
first, *rest = (1, 2, 3, 4)
print("Star unpacking:", first, rest)

# Methods and operations
nums = (1, 2, 2, 3, 2)
print("count(2) =", nums.count(2), "| index(3) =", nums.index(3))
print("Concatenate:", (1, 2) + (3, 4), "| Repeat:", (0,) * 3)
print("Membership:", 3 in nums)

# Swapping variables with tuples
a, b = 1, 2
a, b = b, a
print("Swapped:", a, b)

# Tuple as dictionary key
locations = {(31.5497, 74.3436): "Lahore", (33.6844, 73.0479): "Islamabad"}
print(locations[(31.5497, 74.3436)])
print("Convert:", tuple([1, 2, 3]), list((4, 5, 6)))
