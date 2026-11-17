# Task 52 - Logistic Regression (digit recognition, MNIST-style, + binary classification)
# Uses scikit-learn's bundled 8x8 digits dataset so it works offline (same idea as MNIST).
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

# ---------- Part A: multiclass (digits 0-9) ----------
digits = load_digits()
print("Images:", digits.images.shape, "| flattened:", digits.data.shape, "| classes:", len(set(digits.target)))

fig, axes = plt.subplots(1, 8, figsize=(10, 1.6))
for ax, img, lab in zip(axes, digits.images, digits.target):
    ax.imshow(img, cmap="gray_r"); ax.set_title(lab); ax.axis("off")
plt.tight_layout(); plt.savefig("sample_digits.png", dpi=120); plt.close()

Xtr, Xte, ytr, yte = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0, stratify=digits.target)
clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000))
clf.fit(Xtr, ytr)
pred = clf.predict(Xte)
print("\nMulticlass accuracy:", round(accuracy_score(yte, pred), 4))
print(classification_report(yte, pred))
ConfusionMatrixDisplay(confusion_matrix(yte, pred)).plot(cmap="Blues", colorbar=False)
plt.title("Digits - confusion matrix"); plt.tight_layout(); plt.savefig("digits_confusion_matrix.png", dpi=120); plt.close()

# predicted probabilities for one test image
proba = clf.predict_proba(Xte[:1])[0]
print("True label:", yte[0], "| predicted:", pred[0], "| probability:", round(float(proba.max()), 3))

# ---------- Part B: binary classification (breast cancer) ----------
cancer = load_breast_cancer()
Xb_tr, Xb_te, yb_tr, yb_te = train_test_split(cancer.data, cancer.target, test_size=0.25, random_state=0, stratify=cancer.target)
bin_clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000)).fit(Xb_tr, yb_tr)
pb = bin_clf.predict(Xb_te)
print("\nBinary accuracy (breast cancer):", round(accuracy_score(yb_te, pb), 4))
print("Confusion matrix [[TN FP] [FN TP]]:\n", confusion_matrix(yb_te, pb))

# Sigmoid illustration
z = np.linspace(-8, 8, 200)
plt.figure(figsize=(5, 3.5)); plt.plot(z, 1 / (1 + np.exp(-z)))
plt.axhline(0.5, color="gray", ls="--"); plt.title("Sigmoid function"); plt.xlabel("z"); plt.ylabel("sigma(z)")
plt.tight_layout(); plt.savefig("sigmoid.png", dpi=120)
print("\nSaved: sample_digits.png, digits_confusion_matrix.png, sigmoid.png")
