import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.linear_model import LogisticRegression

X_nonlinear, y_nonlinear = make_circles(
    n_samples=100,
    noise=0.1,
    factor=0.5,
    random_state=1
)

plt.scatter(
    X_nonlinear[:, 0],
    X_nonlinear[:, 1],
    c=y_nonlinear,
    cmap="plasma",
    s=50
)

plt.title("Non-linearly Separable Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

model = LogisticRegression()
model.fit(X_nonlinear, y_nonlinear)

print("Accuracy:", model.score(X_nonlinear, y_nonlinear))