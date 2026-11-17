# Task 19 - various looping techniques

# 1. enumerate()
for i, color in enumerate(["red", "green", "blue"], start=1):
    print(i, color)

# 2. zip() - loop over two sequences together
names = ["Ali", "Sara", "Hamza"]
ages = [20, 22, 21]
for n, a in zip(names, ages):
    print(f"{n} is {a}")

# 3. sorted() and reversed()
nums = [5, 1, 4, 2, 3]
print("sorted:", [x for x in sorted(nums)])
print("reversed:", [x for x in reversed(nums)])
for x in sorted(set("balloon")):
    print(x, end=" ")
print()

# 4. dict.items(), keys(), values()
d = {"a": 1, "b": 2, "c": 3}
for k, v in d.items():
    print(k, "->", v)

# 5. Loop with index via range(len())
for i in range(len(nums)):
    print(f"nums[{i}] = {nums[i]}")

# 6. List comprehension and nested loops
print([x * x for x in range(1, 6)])
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()

# 7. Iterator protocol
it = iter([10, 20, 30])
print(next(it), next(it), next(it))

# 8. itertools-style with zip(*)
pairs = [(1, "one"), (2, "two")]
numbers, words = zip(*pairs)
print(numbers, words)
