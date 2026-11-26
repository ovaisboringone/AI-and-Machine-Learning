import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

np.random.seed(0)

churn_data = pd.DataFrame({
    'MonthlyCharges': np.random.uniform(20, 100, 200),
    'DataUsageGB': np.random.uniform(10, 80, 200),
    'ContractYears': np.random.randint(1, 4, 200),
    'Churn': np.random.choice([0, 1], 200, p=[0.7, 0.3])
})

X = churn_data.drop('Churn', axis=1)
y = churn_data['Churn']

model = LogisticRegression()

kf = KFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')

print("Accuracy of each fold:")
print(scores)

print("\nAverage Accuracy:")
print(scores.mean())