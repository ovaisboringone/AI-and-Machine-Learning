from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_true_spam, y_pred_spam)

print("\nConfusion Matrix:")
print(cm)

tn, fp, fn, tp = cm.ravel()

print("True Positives:", tp)
print("True Negatives:", tn)
print("False Positives:", fp)
print("False Negatives:", fn)