# Task 51 - Linear Regression with scikit-learn
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.datasets import load_diabetes

# ---------- Part A: simple (univariate) linear regression ----------
rng = np.random.default_rng(42)
experience = rng.uniform(0, 15, 120)
salary = 30000 + 4500 * experience + rng.normal(0, 6000, 120)      # true slope 4500, intercept 30000
df = pd.DataFrame({"YearsExperience": experience.round(2), "Salary": salary.round(0)})
print(df.head(), "\n")

X = df[["YearsExperience"]]
y = df["Salary"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)
print("Intercept:", round(model.intercept_, 2), "| Slope:", round(model.coef_[0], 2))
print("MAE :", round(mean_absolute_error(y_test, pred), 2))
print("MSE :", round(mean_squared_error(y_test, pred), 2))
print("RMSE:", round(float(np.sqrt(mean_squared_error(y_test, pred))), 2))
print("R^2 :", round(r2_score(y_test, pred), 4))
print("Predicted salary for 10 years of experience:", round(float(model.predict(pd.DataFrame({"YearsExperience": [10]}))[0]), 2))

plt.figure(figsize=(7, 4.5))
plt.scatter(X_train, y_train, alpha=0.6, label="train")
plt.scatter(X_test, y_test, color="orange", label="test")
xs = np.linspace(0, 15, 50).reshape(-1, 1)
plt.plot(xs, model.predict(pd.DataFrame(xs, columns=["YearsExperience"])), color="red", label="fitted line")
plt.xlabel("Years of experience"); plt.ylabel("Salary"); plt.title("Simple linear regression")
plt.legend(); plt.tight_layout(); plt.savefig("simple_linear_regression.png", dpi=120)

# ---------- Part B: multiple linear regression (diabetes dataset) ----------
data = load_diabetes(as_frame=True)
Xd, yd = data.data, data.target
Xtr, Xte, ytr, yte = train_test_split(Xd, yd, test_size=0.2, random_state=1)
mlr = LinearRegression().fit(Xtr, ytr)
p = mlr.predict(Xte)
print("\n--- Multiple linear regression (diabetes, 10 features) ---")
print("R^2 :", round(r2_score(yte, p), 4), "| RMSE:", round(float(np.sqrt(mean_squared_error(yte, p))), 2))
print("Coefficients:\n", pd.Series(mlr.coef_, index=Xd.columns).round(1).to_string())

plt.figure(figsize=(5, 5))
plt.scatter(yte, p, alpha=0.7); plt.plot([yte.min(), yte.max()], [yte.min(), yte.max()], "r--")
plt.xlabel("Actual"); plt.ylabel("Predicted"); plt.title("Actual vs predicted (diabetes)")
plt.tight_layout(); plt.savefig("multiple_regression_actual_vs_pred.png", dpi=120)
print("\nSaved: simple_linear_regression.png, multiple_regression_actual_vs_pred.png")
