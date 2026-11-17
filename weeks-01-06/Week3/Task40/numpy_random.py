# Task 40 - NumPy random numbers
import numpy as np
from numpy import random

random.seed(42)                      # reproducible results
print("randint(100):", random.randint(100))
print("randint array:", random.randint(100, size=5))
print("2-D randint:\n", random.randint(100, size=(2, 3)))
print("rand float:", round(random.rand(), 4), "| rand array:", random.rand(3).round(3))
print("choice:", random.choice([3, 5, 7, 9]), "| choice array:", random.choice([3, 5, 7, 9], size=(2, 3)).tolist())

# Probabilities for choice
print("weighted choice:", random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=10))

# Shuffle and permutation
arr = np.arange(1, 8)
random.shuffle(arr);  print("shuffle:", arr)
print("permutation:", random.permutation(np.arange(1, 8)))

# Distributions
x = random.normal(loc=50, scale=10, size=10000)
print("normal mean ~", x.mean().round(2), "| std ~", x.std().round(2))
print("binomial:", random.binomial(n=10, p=0.5, size=5))
print("uniform:", random.uniform(0, 1, 3).round(3))
print("poisson:", random.poisson(lam=3, size=5))
