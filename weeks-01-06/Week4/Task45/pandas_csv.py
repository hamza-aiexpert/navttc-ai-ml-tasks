# Task 45 - Pandas: working with CSV files
import numpy as np
import pandas as pd

# Create a sample CSV (so the exercise works offline)
rng = np.random.default_rng(1)
n = 40
sample = pd.DataFrame({
    "Duration": rng.integers(20, 120, n),
    "Pulse": rng.integers(90, 130, n),
    "Maxpulse": rng.integers(110, 175, n),
    "Calories": rng.normal(300, 80, n).round(1),
})
sample.to_csv("data.csv", index=False)
print("Created data.csv with", len(sample), "rows")

# 1. Load the CSV
df = pd.read_csv("data.csv")
print("\nhead():\n", df.head())
print("\ntail(3):\n", df.tail(3))

# 2. Printing the whole frame vs. options
print("\nmax rows option:", pd.options.display.max_rows)

# 3. Useful read_csv parameters
part = pd.read_csv("data.csv", usecols=["Duration", "Calories"], nrows=5)
print("\nusecols + nrows:\n", part)

# 4. Save modified data
df["Calories_per_min"] = (df["Calories"] / df["Duration"]).round(2)
df.to_csv("data_with_ratio.csv", index=False)
print("\nSaved data_with_ratio.csv ->", pd.read_csv("data_with_ratio.csv").columns.tolist())
