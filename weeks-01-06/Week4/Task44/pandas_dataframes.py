# Task 44 - Pandas DataFrames
import pandas as pd

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
df = pd.DataFrame(data)
print(df)

print("\nRow 0 (loc):\n", df.loc[0])
print("\nRows 0 and 1:\n", df.loc[[0, 1]])

# Named index
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print("\nNamed index:\n", df)
print("\nloc['day2']:\n", df.loc["day2"])
print("iloc[0, 1] =", df.iloc[0, 1])

# Adding / dropping
df["rating"] = [4.5, 3.9, 4.1]
df.loc["day4"] = [400, 42, 4.0]
print("\nAfter adding column and row:\n", df)
print("\nDrop column 'rating':\n", df.drop(columns="rating"))

# Attributes
print("\nshape:", df.shape, "| columns:", df.columns.tolist(), "| index:", df.index.tolist())
print("\ndf.T:\n", df.T)
print("\nsorted by duration:\n", df.sort_values("duration"))
print("\nquery calories>390:\n", df.query("calories > 390"))
