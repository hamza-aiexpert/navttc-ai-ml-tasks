# Task 55 - Time Series Analysis with pandas
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Synthetic daily sales data for 3 years: trend + yearly seasonality + weekly pattern + noise
rng = np.random.default_rng(11)
idx = pd.date_range("2023-01-01", "2025-12-31", freq="D")
t = np.arange(len(idx))
sales = (200 + 0.15 * t
         + 40 * np.sin(2 * np.pi * idx.dayofyear / 365.25)
         + np.where(idx.dayofweek >= 5, 35, 0)
         + rng.normal(0, 12, len(idx)))
ts = pd.Series(sales.round(1), index=idx, name="sales")
print("Series head:\n", ts.head())
print("\nIndex type:", type(ts.index).__name__, "| freq:", ts.index.freq, "| length:", len(ts))

# 1. Date-based selection
print("\nMarch 2024 mean:", round(ts["2024-03"].mean(), 2))
print("Slice 2025-06-01..2025-06-05:\n", ts["2025-06-01":"2025-06-05"])

# 2. Resampling
monthly = ts.resample("ME").mean()
quarterly = ts.resample("QE").sum()
print("\nMonthly mean (first 6):\n", monthly.head(6).round(1))
print("\nQuarterly total:\n", quarterly.round(0))

# 3. Rolling windows / smoothing
roll7 = ts.rolling(7).mean()
roll30 = ts.rolling(30).mean()
print("\n7-day rolling mean (last 3):\n", roll7.tail(3).round(2))

# 4. Shifting, differencing, growth
print("\nDay-over-day change (first 3):\n", ts.diff().head(4).round(2).dropna())
print("Year-over-year % change of monthly mean (last 3):\n", (monthly.pct_change(12) * 100).dropna().tail(3).round(2))

# 5. Seasonality: average by weekday and month
print("\nAverage sales by weekday (0=Mon):\n", ts.groupby(ts.index.dayofweek).mean().round(1))
print("\nAverage by month:\n", ts.groupby(ts.index.month).mean().round(1))

# 6. Simple decomposition (trend via 365-day centered rolling mean)
trend = ts.rolling(365, center=True).mean()
detrended = ts - trend
seasonal = detrended.groupby(ts.index.dayofyear).transform("mean")
resid = detrended - seasonal
print("\nResidual std:", round(float(resid.std()), 2))

# 7. Autocorrelation
print("\nAutocorrelation at lag 1, 7, 30:", [round(float(ts.autocorr(l)), 3) for l in (1, 7, 30)])

# 8. Stationarity check by differencing
print("Std of series:", round(float(ts.std()), 2), "| std after 1st difference:", round(float(ts.diff().std()), 2))

# 9. Naive forecast evaluation (last 30 days predicted by same days of previous year)
train, test = ts[:-30], ts[-30:]
forecast = ts.shift(365)[-30:]
mape = float((abs(test - forecast) / test).mean() * 100)
print("\nSeasonal-naive forecast MAPE for last 30 days:", round(mape, 2), "%")

# Plots
fig, axes = plt.subplots(3, 1, figsize=(10, 9))
ts.plot(ax=axes[0], alpha=0.4, label="daily"); roll30.plot(ax=axes[0], color="red", label="30-day mean")
trend.plot(ax=axes[0], color="black", label="365-day trend"); axes[0].legend(); axes[0].set_title("Daily sales")
monthly.plot(ax=axes[1], marker="o"); axes[1].set_title("Monthly average")
seasonal.iloc[:365].plot(ax=axes[2]); axes[2].set_title("Estimated yearly seasonal component")
plt.tight_layout(); plt.savefig("time_series.png", dpi=110)
print("Saved time_series.png")
