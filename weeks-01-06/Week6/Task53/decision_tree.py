# Task 53 - Decision Tree classification
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target
print("Dataset:", X.shape, "| classes:", [str(c) for c in data.target_names])

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

# Unrestricted tree (likely to overfit)
full = DecisionTreeClassifier(random_state=1).fit(Xtr, ytr)
print("\nFull tree  -> depth:", full.get_depth(), "| train acc:", round(full.score(Xtr, ytr), 4), "| test acc:", round(full.score(Xte, yte), 4))

# Pruned tree (max_depth) and entropy criterion
tree = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=1).fit(Xtr, ytr)
pred = tree.predict(Xte)
print("Depth-3 tree -> train acc:", round(tree.score(Xtr, ytr), 4), "| test acc:", round(accuracy_score(yte, pred), 4))
print("\nConfusion matrix:\n", confusion_matrix(yte, pred))
print(classification_report(yte, pred, target_names=data.target_names))

# Effect of depth
print("Depth vs test accuracy:")
for d in range(1, 9):
    m = DecisionTreeClassifier(max_depth=d, random_state=1).fit(Xtr, ytr)
    print(f"  max_depth={d}: {m.score(Xte, yte):.4f} (5-fold CV: {cross_val_score(m, X, y, cv=5).mean():.4f})")

# Feature importance
imp = pd.Series(tree.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nTop features:\n", imp.head(5).round(4).to_string())

# Text rules + picture
print("\nTree rules:\n", export_text(tree, feature_names=list(X.columns)))
plt.figure(figsize=(16, 8))
plot_tree(tree, feature_names=X.columns, class_names=data.target_names, filled=True, fontsize=8)
plt.tight_layout(); plt.savefig("decision_tree.png", dpi=110)
print("Saved decision_tree.png")
