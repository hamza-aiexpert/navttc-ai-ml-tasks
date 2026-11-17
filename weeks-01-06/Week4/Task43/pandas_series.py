# Task 43 - Pandas Series
import pandas as pd

a = [1, 7, 2]
s = pd.Series(a)
print(s, "\nfirst value:", s[0])

s2 = pd.Series(a, index=["x", "y", "z"])
print("\nCustom labels:\n", s2, "\ns2['y'] =", s2["y"])

# From a dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}
s3 = pd.Series(calories)
print("\nFrom dict:\n", s3)
print("\nOnly day1 and day2:\n", pd.Series(calories, index=["day1", "day2"]))

# Operations
print("\nsum/mean/max:", s3.sum(), round(s3.mean(), 2), s3.max())
print("filter > 385:\n", s3[s3 > 385])
print("vectorized math (x*2):\n", s3 * 2)
print("idxmax:", s3.idxmax(), "| sort:\n", s3.sort_values())
print("\napply:\n", s3.apply(lambda v: "high" if v > 400 else "normal"))
