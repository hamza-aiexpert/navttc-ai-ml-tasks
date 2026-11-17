# Task 39 - NumPy sorting arrays
import numpy as np

arr = np.array([3, 2, 0, 1])
print("sorted:", np.sort(arr), "| original unchanged:", arr)
print("strings:", np.sort(np.array(["banana", "cherry", "apple"])))
print("booleans:", np.sort(np.array([True, False, True])))

arr2 = np.array([[3, 2, 4], [5, 0, 1]])
print("2-D sort (per row):\n", np.sort(arr2))
print("2-D sort (per column):\n", np.sort(arr2, axis=0))

# Descending order
print("descending:", np.sort(arr)[::-1])

# argsort - indices that would sort the array
scores = np.array([88, 92, 75, 96])
names = np.array(["Ali", "Sara", "Hamza", "Zoya"])
order = np.argsort(-scores)
print("ranking:", list(zip(names[order], scores[order])))
arr.sort()          # in-place
print("in-place sort:", arr)
