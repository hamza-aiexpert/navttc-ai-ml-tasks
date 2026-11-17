"""Task 59 - Neural network loss functions implemented in NumPy and plotted."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

eps = 1e-12
def mse(y, p):  return np.mean((y - p) ** 2)
def mae(y, p):  return np.mean(np.abs(y - p))
def huber(y, p, d=1.0):
    e = np.abs(y - p)
    return np.mean(np.where(e <= d, 0.5 * e**2, d * (e - 0.5 * d)))
def binary_cross_entropy(y, p):
    p = np.clip(p, eps, 1 - eps); return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))
def categorical_cross_entropy(Y, P):
    P = np.clip(P, eps, 1); return -np.mean(np.sum(Y * np.log(P), axis=1))
def hinge(y, s):  # y in {-1,+1}
    return np.mean(np.maximum(0, 1 - y * s))

y_reg = np.array([3.0, -0.5, 2.0, 7.0]); p_reg = np.array([2.5, 0.0, 2.0, 8.0])
print("Regression  MSE:", mse(y_reg, p_reg), " MAE:", mae(y_reg, p_reg), " Huber:", huber(y_reg, p_reg))

y_b = np.array([1, 0, 1, 1, 0]); p_b = np.array([0.9, 0.2, 0.7, 0.6, 0.1])
print("Binary cross-entropy:", round(binary_cross_entropy(y_b, p_b), 4))

Y = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
P = np.array([[0.8, 0.1, 0.1], [0.2, 0.7, 0.1], [0.1, 0.3, 0.6]])
print("Categorical cross-entropy:", round(categorical_cross_entropy(Y, P), 4))
print("Hinge:", hinge(np.array([1, -1, 1]), np.array([0.8, -0.3, -0.5])))

# Plot loss vs prediction error
e = np.linspace(-3, 3, 400)
plt.figure(figsize=(7, 4))
plt.plot(e, e**2, label="MSE"); plt.plot(e, np.abs(e), label="MAE")
plt.plot(e, np.where(np.abs(e) <= 1, 0.5 * e**2, np.abs(e) - 0.5), label="Huber")
plt.xlabel("prediction error"); plt.ylabel("loss"); plt.legend(); plt.title("Task 59: regression loss functions")
plt.savefig("outputs/task59_losses.png", dpi=120, bbox_inches="tight")
