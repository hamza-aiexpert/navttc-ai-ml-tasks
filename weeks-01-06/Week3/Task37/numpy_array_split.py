# Task 37 - NumPy splitting arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print("array_split(3):", np.array_split(arr, 3))
print("array_split(4) (uneven allowed):", np.array_split(arr, 4))

parts = np.array_split(arr, 3)
print("first part:", parts[0], "| second part:", parts[1])

arr2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print("2-D split into 3 (rows):", [p.tolist() for p in np.array_split(arr2, 3)])
print("2-D split along axis=1:", [p.tolist() for p in np.array_split(arr2, 2, axis=1)])

print("hsplit:", np.hsplit(np.arange(6), 3))
print("vsplit:", [p.tolist() for p in np.vsplit(np.arange(8).reshape(4, 2), 2)])
print("split at indices [2, 4]:", np.split(arr, [2, 4]))
