# Task 46 - Pandas: analyzing data
import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
n = 60
df = pd.DataFrame({
    "Duration": rng.integers(20, 120, n),
    "Pulse": rng.integers(90, 130, n),
    "Calories": rng.normal(300, 80, n).round(1),
    "Group": rng.choice(["A", "B", "C"], n),
})

print("head(5):\n", df.head())
print("\ntail(3):\n", df.tail(3))
print("\ninfo():")
df.info()
print("\ndescribe():\n", df.describe())
print("\nshape:", df.shape)
print("\nvalue_counts of Group:\n", df["Group"].value_counts())
print("\nunique groups:", df["Group"].unique())
print("\nmean per group:\n", df.groupby("Group")[["Duration", "Calories"]].mean().round(2))
print("\nTop 3 calories:\n", df.nlargest(3, "Calories"))
print("\nnull values per column:\n", df.isnull().sum())
