"""Task 58 - Feed Forward Neural Network (NumPy class with configurable layers).
Shows forward pass, backpropagation, ReLU hidden layers and softmax + cross-entropy output."""
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

class FeedForwardNN:
    def __init__(self, sizes, lr=0.1, seed=0):
        rng = np.random.default_rng(seed)
        self.lr = lr
        self.W = [rng.standard_normal((a, b)) * np.sqrt(2 / a) for a, b in zip(sizes[:-1], sizes[1:])]
        self.b = [np.zeros((1, b)) for b in sizes[1:]]

    @staticmethod
    def softmax(z):
        e = np.exp(z - z.max(1, keepdims=True)); return e / e.sum(1, keepdims=True)

    def forward(self, X):
        self.acts = [X]
        for i, (W, b) in enumerate(zip(self.W, self.b)):
            z = self.acts[-1] @ W + b
            self.acts.append(self.softmax(z) if i == len(self.W) - 1 else np.maximum(0, z))
        return self.acts[-1]

    def backward(self, Y):
        m = Y.shape[0]
        delta = (self.acts[-1] - Y) / m            # softmax + cross-entropy gradient
        for i in reversed(range(len(self.W))):
            gW = self.acts[i].T @ delta; gb = delta.sum(0, keepdims=True)
            if i > 0:
                delta = (delta @ self.W[i].T) * (self.acts[i] > 0)
            self.W[i] -= self.lr * gW; self.b[i] -= self.lr * gb

    def fit(self, X, y, epochs=200, n_classes=10):
        Y = np.eye(n_classes)[y]
        for ep in range(epochs):
            p = self.forward(X)
            loss = -np.mean(np.sum(Y * np.log(p + 1e-12), axis=1))
            self.backward(Y)
            if ep % 40 == 0: print(f"epoch {ep:3d} cross-entropy {loss:.4f}")

    def predict(self, X): return self.forward(X).argmax(1)

X, y = load_digits(return_X_y=True); X = X / 16.0
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)
net = FeedForwardNN([64, 64, 32, 10], lr=0.5)
net.fit(Xtr, ytr, epochs=300)
print("Train accuracy:", (net.predict(Xtr) == ytr).mean().round(4))
print("Test accuracy :", (net.predict(Xte) == yte).mean().round(4))
