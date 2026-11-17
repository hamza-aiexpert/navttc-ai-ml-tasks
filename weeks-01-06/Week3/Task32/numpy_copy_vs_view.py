# Task 32 - NumPy array copy vs view
import numpy as np

# COPY - owns its data, changes do not affect original
arr = np.array([1, 2, 3, 4, 5])
c = arr.copy()
arr[0] = 42
print("original:", arr, "| copy:", c)

# VIEW - shares data, changes DO affect the original
arr = np.array([1, 2, 3, 4, 5])
v = arr.view()
arr[0] = 42
print("original:", arr, "| view:", v)
v[1] = 77
print("after changing view -> original:", arr)

# Checking who owns the data with .base
print("copy.base is None:", c.base is None)
print("view.base is arr:", v.base is arr)

# Slices return views; fancy indexing returns copies
a = np.arange(6)
sl = a[1:4]; fancy = a[[1, 2, 3]]
a[2] = 100
print("slice sees change:", sl, "| fancy index does not:", fancy)
