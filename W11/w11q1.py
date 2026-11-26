import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

np.random.seed(0)

X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.normal(0, 0.5, 80)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

plt.scatter(X_train, y_train, label="Training Data")
plt.scatter(X_test, y_test, label="Testing Data")
plt.title("Original Data")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

# Underfitting
model1 = LinearRegression()
model1.fit(X_train, y_train)

y_pred1 = model1.predict(X_test)

plt.scatter(X, y)
plt.plot(X, model1.predict(X), color="red")
plt.title("Underfitting - Linear Regression")
plt.show()

# Overfitting
model2 = make_pipeline(
    PolynomialFeatures(degree=20),
    LinearRegression()
)

model2.fit(X_train, y_train)

y_pred2 = model2.predict(X_test)

plt.scatter(X, y)
plt.plot(X, model2.predict(X), color="red")
plt.title("Overfitting - Polynomial Regression")
plt.show()