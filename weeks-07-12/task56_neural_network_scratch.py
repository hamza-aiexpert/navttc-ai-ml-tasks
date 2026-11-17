"""Task 56 - Demonstration of Neural Networks from scratch (NumPy only).
A 2-layer network learns the XOR problem, which a single neuron cannot solve."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.random.seed(42)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)

sigmoid = lambda z: 1 / (1 + np.exp(-z))
d_sigmoid = lambda a: a * (1 - a)

n_hidden, lr, epochs = 4, 1.0, 10000
W1 = np.random.randn(2, n_hidden); b1 = np.zeros((1, n_hidden))
W2 = np.random.randn(n_hidden, 1); b2 = np.zeros((1, 1))

losses = []
for epoch in range(epochs):
    # forward pass
    a1 = sigmoid(X @ W1 + b1)
    a2 = sigmoid(a1 @ W2 + b2)
    loss = np.mean((y - a2) ** 2)
    losses.append(loss)
    # backward pass (chain rule)
    d2 = (a2 - y) * d_sigmoid(a2)
    d1 = (d2 @ W2.T) * d_sigmoid(a1)
    W2 -= lr * a1.T @ d2; b2 -= lr * d2.sum(0, keepdims=True)
    W1 -= lr * X.T @ d1;  b1 -= lr * d1.sum(0, keepdims=True)
    if epoch % 2000 == 0:
        print(f"epoch {epoch:5d}  loss {loss:.5f}")

print("\nPredictions after training:")
for xi, pi in zip(X, a2):
    print(xi, "->", round(float(pi[0]), 3), "=>", int(pi[0] > 0.5))

plt.plot(losses); plt.xlabel("Epoch"); plt.ylabel("MSE loss")
plt.title("Task 56: XOR neural network training loss")
plt.savefig("outputs/task56_loss_curve.png", dpi=120, bbox_inches="tight")
