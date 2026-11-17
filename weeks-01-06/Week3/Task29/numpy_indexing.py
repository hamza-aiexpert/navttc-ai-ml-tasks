# Task 29 - NumPy array indexing
import numpy as np

arr = np.array([1, 2, 3, 4])
print("arr[0] =", arr[0], "| arr[1] + arr[2] =", arr[1] + arr[2])

arr2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2-D arr[0, 1] =", arr2d[0, 1], "| arr[1, -1] =", arr2d[1, -1])

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3-D arr[0, 1, 2] =", arr3d[0, 1, 2])

# Negative indexing
print("last element of row 1:", arr2d[1, -1])

# Boolean / logical selection
print("elements > 5:", arr2d[arr2d > 5])
mask = arr % 2 == 0
print("mask:", mask, "->", arr[mask])

# Fancy indexing
print("fancy:", arr[[0, 3]])
print("rows 0 and 1, columns 1 and 3:", arr2d[[0, 1], [1, 3]])
