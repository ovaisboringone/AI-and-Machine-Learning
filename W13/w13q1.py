import numpy as np
from sklearn.metrics import accuracy_score

y_true_spam = np.array([
    0, 0, 1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 0, 1, 1, 0, 1, 0, 1, 0
])

y_pred_spam = np.array([
    0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
    1, 0, 0, 1, 0, 0, 1, 0, 1, 0
])

print("True Labels:")
print(y_true_spam)

print("\nPredicted Labels:")
print(y_pred_spam)

accuracy = accuracy_score(y_true_spam, y_pred_spam)

print("\nAccuracy:", accuracy)