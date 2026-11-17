# Task 47 - Pandas: data cleaning techniques
import numpy as np
import pandas as pd

raw = pd.DataFrame({
    "Name":     ["Ali", "Sara", "Hamza", "Sara", "Zoya", "Bilal", "Ayesha"],
    "Date":     ["2026/01/05", "2026/01/06", "20260107", "2026/01/06", None, "2026/01/09", "2026/01/10"],
    "Duration": [60, 45, np.nan, 45, 50, 450, 55],     # NaN and an outlier (450)
    "Calories": [409.1, 479.0, 340.0, 479.0, 282.4, np.nan, 300.0],
})
print("RAW DATA\n", raw)
print("\nMissing values:\n", raw.isna().sum())

df = raw.copy()
# 1. Fix wrong format (dates)
df["Date"] = pd.to_datetime(df["Date"], format="mixed", errors="coerce")
# 2. Remove rows with empty cells in critical columns
df = df.dropna(subset=["Date"])
# 3. Fill empty values (mean / median)
df["Duration"] = df["Duration"].fillna(df["Duration"].median())
df["Calories"] = df["Calories"].fillna(df["Calories"].mean().round(1))
# 4. Fix wrong values (outlier replaced)
df.loc[df["Duration"] > 120, "Duration"] = 120
# 5. Remove duplicates
print("\nDuplicated rows:", df.duplicated().sum())
df = df.drop_duplicates().reset_index(drop=True)

print("\nCLEAN DATA\n", df)
print("\nDtypes:\n", df.dtypes)
print("\nMissing values after cleaning:", int(df.isna().sum().sum()))
