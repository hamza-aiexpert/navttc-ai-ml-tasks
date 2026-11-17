# Task 36 - NumPy joining arrays
import numpy as np

a = np.array([1, 2, 3]); b = np.array([4, 5, 6])
print("concatenate 1-D:", np.concatenate((a, b)))

A = np.array([[1, 2], [3, 4]]); B = np.array([[5, 6], [7, 8]])
print("concatenate axis=0 (rows):\n", np.concatenate((A, B), axis=0))
print("concatenate axis=1 (columns):\n", np.concatenate((A, B), axis=1))

print("stack axis=1:\n", np.stack((a, b), axis=1))
print("stack axis=0:\n", np.stack((a, b), axis=0))
print("hstack:", np.hstack((a, b)))
print("vstack:\n", np.vstack((a, b)))
print("dstack shape:", np.dstack((a, b)).shape)
print("append:", np.append(a, [7, 8]))
