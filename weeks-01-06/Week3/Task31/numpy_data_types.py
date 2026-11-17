# Task 31 - NumPy data types
import numpy as np

arr = np.array([1, 2, 3, 4])
print("int array dtype:", arr.dtype)
print("float array dtype:", np.array([1.5, 2.5]).dtype)
print("string array dtype:", np.array(["apple", "banana"]).dtype)
print("bool array dtype:", np.array([True, False]).dtype)

# Creating arrays with a defined dtype
print("dtype 'S':", np.array([1, 2, 3, 4], dtype="S"))
print("dtype 'i4':", np.array([1, 2, 3, 4], dtype="i4").dtype)
print("dtype float32:", np.array([1, 2, 3], dtype=np.float32).dtype)

# Converting the type with astype()
f = np.array([1.1, 2.1, 3.1])
print("float -> int:", f.astype("i"), "| float -> bool:", np.array([0, 1, 2.5]).astype(bool))
print("int -> str:", np.array([1, 2, 3]).astype(str))

# Errors when conversion is impossible
try:
    np.array(["a", "b"]).astype(int)
except ValueError as e:
    print("ValueError:", e)

# Size in memory
for dt in (np.int8, np.int32, np.int64, np.float64):
    print(dt.__name__, "uses", np.dtype(dt).itemsize, "bytes per element")
