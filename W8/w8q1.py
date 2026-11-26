import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(42)

data = {
    'Age': np.random.randint(20, 60, 100),
    'PurchaseFrequency': np.random.uniform(0.5, 5, 100).round(1),
    'RespondedToCampaign': np.random.choice([0, 1], 100, p=[0.6, 0.4])
}

for i in range(100):
    if data['Age'][i] < 35 and data['PurchaseFrequency'][i] > 3:
        data['RespondedToCampaign'][i] = 1
    elif data['Age'][i] > 50 and data['PurchaseFrequency'][i] < 1.5:
        data['RespondedToCampaign'][i] = 0

df = pd.DataFrame(data)

X = df[['Age', 'PurchaseFrequency']]
y = df['RespondedToCampaign']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Training data:")
print(X_train.head())

print("\nTarget values:")
print(y_train.head())

model = DecisionTreeClassifier(max_depth=3)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)