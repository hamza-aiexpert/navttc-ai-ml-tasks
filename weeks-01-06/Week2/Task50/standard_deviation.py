# Task 50 - Standard deviation (and variance)
import numpy as np

speed = [86, 87, 88, 86, 87, 85, 86]
print("Data (low spread): ", speed)
print("std:", round(float(np.std(speed)), 4), "| variance:", round(float(np.var(speed)), 4))

speed2 = [32, 111, 138, 28, 59, 77, 97]
print("Data (high spread):", speed2)
print("std:", round(float(np.std(speed2)), 4), "| variance:", round(float(np.var(speed2)), 4))

# Manual calculation to show how it works
def manual_std(data, sample=False):
    n = len(data)
    mean = sum(data) / n
    var = sum((x - mean) ** 2 for x in data) / (n - 1 if sample else n)
    return var, var ** 0.5

var, std = manual_std(speed2)
print("\nManual population: variance =", round(var, 4), " std =", round(std, 4))
var_s, std_s = manual_std(speed2, sample=True)
print("Manual sample:     variance =", round(var_s, 4), " std =", round(std_s, 4))
print("numpy ddof=1 check:", round(float(np.std(speed2, ddof=1)), 4))

# Coefficient of variation and 1-std range
mean = np.mean(speed2)
print("Mean:", round(float(mean), 3), "| CV:", round(float(np.std(speed2) / mean), 3))
print("68% range (mean +- 1 std):", round(float(mean - np.std(speed2)), 2), "to", round(float(mean + np.std(speed2)), 2))
