# Task 38 - NumPy searching arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
print("where == 4 ->", np.where(arr == 4)[0])
print("where even ->", np.where(arr % 2 == 0)[0])
print("where with replacement:", np.where(arr > 3, 1, 0))

# searchsorted works on SORTED arrays
sorted_arr = np.array([6, 7, 8, 9])
print("searchsorted(7):", np.searchsorted(sorted_arr, 7))
print("searchsorted(7, side='right'):", np.searchsorted(sorted_arr, 7, side="right"))
print("searchsorted multiple:", np.searchsorted(sorted_arr, [2, 7, 10]))

print("argmax:", arr.argmax(), "| argmin:", arr.argmin())
print("any > 4:", (arr > 4).any(), "| all > 0:", (arr > 0).all())
print("nonzero:", np.nonzero(np.array([0, 3, 0, 5]))[0])
print("isin:", np.isin(arr, [2, 5]))
