# Task 49 - Mean, Median and Mode
import numpy as np
from collections import Counter
from statistics import mode, multimode

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
print("Data:", speed)

# Using numpy
print("Mean   (numpy):", round(float(np.mean(speed)), 3))
print("Median (numpy):", float(np.median(speed)))

# Mode with the statistics module
print("Mode   (statistics):", mode(speed), "| all modes:", multimode(speed))

# Manual computation (to show the logic)
n = len(speed)
manual_mean = sum(speed) / n
s = sorted(speed)
manual_median = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
counts = Counter(speed)
manual_mode = [k for k, v in counts.items() if v == max(counts.values())]
print("Manual mean:", round(manual_mean, 3), "| median:", manual_median, "| mode:", manual_mode)

# Even-length example for the median
even = [1, 3, 5, 7]
print("Median of", even, "=", np.median(even))

# Using pandas as well
import pandas as pd
ser = pd.Series(speed)
print("pandas  mean/median/mode:", round(ser.mean(), 3), ser.median(), ser.mode().tolist())
