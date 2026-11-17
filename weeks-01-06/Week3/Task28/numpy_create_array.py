# Task 28 - Creating NumPy arrays
import numpy as np
print("NumPy version:", np.__version__)

a0 = np.array(42);                       print("0-D:", a0, "ndim =", a0.ndim)
a1 = np.array([1, 2, 3, 4, 5]);          print("1-D:", a1, "ndim =", a1.ndim)
a2 = np.array([[1, 2, 3], [4, 5, 6]]);   print("2-D:\n", a2, "ndim =", a2.ndim)
a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]); print("3-D shape:", a3.shape, "ndim =", a3.ndim)
print("Higher dimension:", np.array([1, 2, 3, 4], ndmin=5).shape)

# From built-in methods
print("zeros:", np.zeros((2, 3)).tolist())
print("ones:", np.ones(4))
print("full:", np.full((2, 2), 7))
print("eye:\n", np.eye(3))
print("arange:", np.arange(0, 20, 5))
print("linspace:", np.linspace(0, 1, 5))

# From random
np.random.seed(0)
print("rand:", np.random.rand(3).round(3))
print("randint:", np.random.randint(0, 10, 5))
print("randn:", np.random.randn(3).round(3))
