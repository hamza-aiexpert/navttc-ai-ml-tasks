# Task 34 - NumPy array reshaping
import numpy as np

arr = np.arange(1, 13)
print("original:", arr, arr.shape)

print("reshape(4, 3):\n", arr.reshape(4, 3))
print("reshape(2, 3, 2):\n", arr.reshape(2, 3, 2))

# Unknown dimension with -1
print("reshape(2, -1) shape:", arr.reshape(2, -1).shape)
print("reshape(-1, 4) shape:", arr.reshape(-1, 4).shape)

# Reshape returns a view when possible
r = arr.reshape(3, 4)
print("reshape returns a view:", r.base is arr)

# Flattening
print("flatten 2-D:", r.flatten())
print("reshape(-1):", r.reshape(-1))
print("ravel:", r.ravel())

# Invalid reshape
try:
    arr.reshape(5, 3)
except ValueError as e:
    print("ValueError:", e)

# Adding/removing dimensions
print("expand_dims:", np.expand_dims(arr, 0).shape, "| squeeze:", np.squeeze(np.expand_dims(arr, 0)).shape)
