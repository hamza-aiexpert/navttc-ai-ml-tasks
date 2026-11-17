# Task 54 - Support Vector Machine (linear + kernel SVM)
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer, load_iris, make_moons
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ---------- Part A: linear SVM on a real dataset ----------
cancer = load_breast_cancer()
Xtr, Xte, ytr, yte = train_test_split(cancer.data, cancer.target, test_size=0.25, random_state=0, stratify=cancer.target)
svm = make_pipeline(StandardScaler(), SVC(kernel="linear", C=1.0)).fit(Xtr, ytr)
pred = svm.predict(Xte)
print("Linear SVM accuracy (breast cancer):", round(accuracy_score(yte, pred), 4))
print(confusion_matrix(yte, pred))
print(classification_report(yte, pred, target_names=cancer.target_names))

# ---------- Part B: kernel SVM comparison on iris ----------
iris = load_iris()
Xi_tr, Xi_te, yi_tr, yi_te = train_test_split(iris.data, iris.target, test_size=0.3, random_state=2, stratify=iris.target)
print("Kernel comparison on iris (3-class):")
for kernel in ["linear", "poly", "rbf", "sigmoid"]:
    m = make_pipeline(StandardScaler(), SVC(kernel=kernel)).fit(Xi_tr, yi_tr)
    print(f"  {kernel:8s} accuracy = {m.score(Xi_te, yi_te):.4f}")

# ---------- Part C: non-linear data and decision boundaries ----------
Xm, ym = make_moons(n_samples=300, noise=0.2, random_state=0)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, kernel in zip(axes, ["linear", "rbf"]):
    clf = make_pipeline(StandardScaler(), SVC(kernel=kernel, C=1.0, gamma="scale")).fit(Xm, ym)
    xx, yy = np.meshgrid(np.linspace(Xm[:, 0].min() - .5, Xm[:, 0].max() + .5, 300),
                         np.linspace(Xm[:, 1].min() - .5, Xm[:, 1].max() + .5, 300))
    zz = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, zz, alpha=0.3, cmap="coolwarm")
    ax.scatter(Xm[:, 0], Xm[:, 1], c=ym, cmap="coolwarm", edgecolor="k", s=20)
    ax.set_title(f"{kernel} kernel (accuracy {clf.score(Xm, ym):.2f})")
plt.tight_layout(); plt.savefig("svm_kernels_moons.png", dpi=120)
print("\nMoons dataset: linear vs RBF kernel saved to svm_kernels_moons.png")

# ---------- Part D: hyper-parameter tuning ----------
grid = GridSearchCV(make_pipeline(StandardScaler(), SVC()),
                    {"svc__C": [0.1, 1, 10, 100], "svc__gamma": ["scale", 0.01, 0.1], "svc__kernel": ["rbf"]}, cv=5)
grid.fit(Xtr, ytr)
print("\nBest params:", grid.best_params_, "| CV score:", round(grid.best_score_, 4), "| test acc:", round(grid.score(Xte, yte), 4))
