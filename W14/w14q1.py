import numpy as np
from sklearn.metrics import precision_score, recall_score

y_true_disease = np.array([
    0, 0, 1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 0, 1, 1, 0, 1, 0, 1, 0
])

y_pred_disease = np.array([
    0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
    1, 0, 0, 1, 0, 0, 1, 0, 1, 0
])

precision = precision_score(y_true_disease, y_pred_disease)
recall = recall_score(y_true_disease, y_pred_disease)

print("Precision:", precision)
print("Recall:", recall)