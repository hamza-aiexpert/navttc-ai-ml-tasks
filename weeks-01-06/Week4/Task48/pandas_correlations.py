# Task 48 - Pandas: data correlations
import numpy as np
import pandas as pd

rng = np.random.default_rng(3)
n = 100
duration = rng.integers(20, 120, n)
df = pd.DataFrame({
    "Duration": duration,
    "Calories": duration * 3 + rng.normal(0, 25, n),          # strongly related to duration
    "Pulse": 100 + duration * 0.1 + rng.normal(0, 8, n),       # weakly related
    "Shoe_size": rng.integers(36, 46, n),                      # unrelated
})
df["Lazy_index"] = -df["Duration"] + rng.normal(0, 10, n)      # negative relation

corr = df.corr().round(3)
print("Correlation matrix:\n", corr)
print("\nDuration vs Calories:", round(df["Duration"].corr(df["Calories"]), 3), "(strong positive)")
print("Duration vs Lazy_index:", round(df["Duration"].corr(df["Lazy_index"]), 3), "(strong negative)")
print("Duration vs Shoe_size:", round(df["Duration"].corr(df["Shoe_size"]), 3), "(about 0, no relation)")

# Rules of thumb: |r| > 0.7 strong, 0.3-0.7 moderate, < 0.3 weak
pairs = corr.where(np.triu(np.ones(corr.shape, dtype=bool), 1)).stack()
print("\nStrongest pairs:\n", pairs.reindex(pairs.abs().sort_values(ascending=False).index).head(4))

# Heatmap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_xticks(range(len(corr))); ax.set_xticklabels(corr.columns, rotation=45, ha="right")
ax.set_yticks(range(len(corr))); ax.set_yticklabels(corr.columns)
for i in range(len(corr)):
    for j in range(len(corr)):
        ax.text(j, i, corr.iloc[i, j], ha="center", va="center", fontsize=8)
fig.colorbar(im); ax.set_title("Correlation matrix")
plt.tight_layout(); plt.savefig("correlation_heatmap.png", dpi=120)
print("\nSaved correlation_heatmap.png")
