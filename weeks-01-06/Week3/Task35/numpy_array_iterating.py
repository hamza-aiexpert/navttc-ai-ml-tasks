# Task 35 - NumPy array iterating
import numpy as np

arr1 = np.array([1, 2, 3])
for x in arr1:
    print("1-D element:", x)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Iterating rows of a 2-D array:")
for row in arr2:
    print("  row:", row)
print("Iterating every scalar:")
for row in arr2:
    for x in row:
        print(x, end=" ")
print()

# nditer - iterate every element of any dimension
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("nditer:", [int(x) for x in np.nditer(arr3)])

# Iterating with a different data type
for x in np.nditer(np.array([1, 2, 3]), flags=["buffered"], op_dtypes=["S"]):
    print("as bytes:", x)

# ndenumerate - index + value
for idx, x in np.ndenumerate(arr2):
    print(idx, "->", x)
