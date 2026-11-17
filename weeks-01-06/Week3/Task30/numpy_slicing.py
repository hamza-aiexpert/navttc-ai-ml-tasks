# Task 30 - NumPy array slicing
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("arr[1:5]  =", arr[1:5])
print("arr[4:]   =", arr[4:])
print("arr[:4]   =", arr[:4])
print("arr[-3:-1]=", arr[-3:-1])
print("arr[1:5:2]=", arr[1:5:2])
print("arr[::2]  =", arr[::2])
print("reversed  =", arr[::-1])

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2-D arr[1, 1:4] =", arr2[1, 1:4])
print("2-D arr[0:2, 2] =", arr2[0:2, 2])
print("2-D arr[0:2, 1:4] =\n", arr2[0:2, 1:4])
print("first column:", arr2[:, 0], "| last row:", arr2[-1])

# Slices are views: changing the view changes the original
view = arr[1:3]
view[0] = 99
print("original after editing view:", arr)
