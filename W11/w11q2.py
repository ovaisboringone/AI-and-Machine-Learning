import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

X_linear, y_linear = make_classification(
    n_samples=100,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=1,
    random_state=4,
    class_sep=1.5
)

plt.scatter(
    X_linear[:, 0],
    X_linear[:, 1],
    c=y_linear,
    cmap="viridis",
    s=50
)

plt.title("Linearly Separable Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

model = LogisticRegression()
model.fit(X_linear, y_linear)

print("Accuracy:", model.score(X_linear, y_linear))