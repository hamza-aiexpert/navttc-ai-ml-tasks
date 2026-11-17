"""Task 57 - Multi-Layer Perceptron (MLP) exercise.
Trains an MLP on the handwritten digits dataset (scikit-learn, bundled offline)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

X, y = load_digits(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
sc = StandardScaler().fit(Xtr); Xtr, Xte = sc.transform(Xtr), sc.transform(Xte)

mlp = MLPClassifier(hidden_layer_sizes=(64, 32), activation="relu", solver="adam",
                    alpha=1e-3, max_iter=300, random_state=42)
mlp.fit(Xtr, ytr)
pred = mlp.predict(Xte)
print("Test accuracy:", round(accuracy_score(yte, pred), 4))
print(classification_report(yte, pred))

# Compare activation functions
for act in ["relu", "tanh", "logistic"]:
    m = MLPClassifier(hidden_layer_sizes=(64, 32), activation=act, max_iter=300, random_state=42).fit(Xtr, ytr)
    print(f"activation={act:9s} test acc={m.score(Xte, yte):.4f}")

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(mlp.loss_curve_); ax[0].set_title("MLP training loss"); ax[0].set_xlabel("Iteration")
ConfusionMatrixDisplay.from_predictions(yte, pred, ax=ax[1], colorbar=False)
ax[1].set_title("Confusion matrix")
plt.savefig("outputs/task57_mlp.png", dpi=120, bbox_inches="tight")
