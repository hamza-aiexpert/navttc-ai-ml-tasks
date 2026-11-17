# Task 33 - NumPy array shape
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("shape:", arr.shape, "| ndim:", arr.ndim, "| size:", arr.size, "| dtype:", arr.dtype)

arr5 = np.array([1, 2, 3, 4], ndmin=5)
print("ndmin=5 array:", arr5, "shape:", arr5.shape)
print("each dimension size ->", [f"axis {i}: {n}" for i, n in enumerate(arr5.shape)])

# Shape of other structures
print("3-D shape:", np.zeros((2, 3, 4)).shape)
print("itemsize:", arr.itemsize, "| total bytes:", arr.nbytes)
print("transpose shape:", arr.T.shape)
