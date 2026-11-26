import numpy as np

X_and = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y_and = np.array([0, 0, 0, 1])

weights = np.random.rand(2) * 0.1
bias = np.random.rand(1)[0] * 0.1

def step_function(z):
    if z >= 0:
        return 1
    else:
        return 0

learning_rate = 0.1
epochs = 20

for epoch in range(epochs):
    for x, y_true in zip(X_and, y_and):
        z = np.dot(x, weights) + bias

        prediction = step_function(z)

        error = y_true - prediction

        weights = weights + learning_rate * error * x
        bias = bias + learning_rate * error

print("AND Gate Predictions:")

for x in X_and:
    z = np.dot(x, weights) + bias
    prediction = step_function(z)
    print(x, "=", prediction)