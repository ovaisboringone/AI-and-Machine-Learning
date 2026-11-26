import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(42)

keywords = np.random.randint(0, 10, 100)

spam_prob = 1 / (1 + np.exp(-(keywords - 5)))

is_spam = (np.random.rand(100) < spam_prob).astype(int)

df = pd.DataFrame({
    'NumSuspiciousKeywords': keywords,
    'IsSpam': is_spam
})

X = df[['NumSuspiciousKeywords']]
y = df['IsSpam']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Training data:")
print(X_train.head())

print("\nSpam target:")
print(y_train.head())

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)