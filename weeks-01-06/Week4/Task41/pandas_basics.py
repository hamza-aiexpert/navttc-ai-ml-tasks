# Task 41 - Pandas basics
import pandas as pd

print("pandas version:", pd.__version__)
mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
df = pd.DataFrame(mydataset)
print(df)

# Core ideas: Series (1-D) and DataFrame (2-D table)
s = pd.Series([10, 20, 30], index=["a", "b", "c"], name="values")
print("\nSeries:\n", s)
print("\nBasic info:")
print("shape:", df.shape, "| columns:", list(df.columns), "| dtypes:", df.dtypes.to_dict())
print(df.describe())
print("\nSelect a column:\n", df["cars"])
print("\nFilter rows (passings > 2):\n", df[df["passings"] > 2])
df["is_german"] = df["cars"].isin(["BMW"])
print("\nNew column:\n", df)
