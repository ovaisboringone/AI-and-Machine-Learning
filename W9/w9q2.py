import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_shapes = np.array([
    [4, 1.0],
    [4, 1.05],
    [4, 0.95],
    [0, 1.0],
    [0, 1.1],
    [0, 0.9],
    [4, 0.5],
    [0, 2.0]
])

y_shapes = np.array([0, 0, 0, 1, 1, 1, 0, 1])

X_train, X_test, y_train, y_test = train_test_split(
    X_shapes, y_shapes, test_size=0.3, random_state=42
)

print("Training data:")
print(X_train)

model = MLPClassifier(
    hidden_layer_sizes=(5,),
    max_iter=500,
    random_state=42,
    solver="adam"
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)