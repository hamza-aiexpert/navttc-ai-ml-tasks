# Task 24 - Set data type
s = {1, 2, 3, 3, 2, 1}
print("Duplicates removed:", s, "| length:", len(s))
empty = set()          # {} would create a dict
print("empty set:", empty, type(empty).__name__)

s.add(4); s.update([5, 6]); s.discard(10); s.remove(6)
print("After add/update/discard/remove:", s)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}
print("union:", a | b, a.union(b))
print("intersection:", a & b)
print("difference a-b:", a - b, "| b-a:", b - a)
print("symmetric difference:", a ^ b)
print("subset/superset/disjoint:", {1, 2} <= a, a >= {1, 2}, a.isdisjoint({9}))

# Remove duplicates from a list (order not preserved)
data = [3, 1, 3, 2, 1, 5]
print("unique:", sorted(set(data)))

# Set comprehension and frozenset
print({x % 3 for x in range(10)})
fs = frozenset([1, 2, 3])
print("frozenset:", fs, "(immutable, hashable)")

# Common letters
print("common letters:", set("python") & set("typhoon"))
