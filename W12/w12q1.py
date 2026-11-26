import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(0)

churn_data = pd.DataFrame({
    'MonthlyCharges': np.random.uniform(20, 100, 200),
    'DataUsageGB': np.random.uniform(10, 80, 200),
    'ContractYears': np.random.randint(1, 4, 200),
    'Churn': np.random.choice([0, 1], 200, p=[0.7, 0.3])
})

X = churn_data.drop('Churn', axis=1)
y = churn_data['Churn']

print("Original Data:")
print(churn_data.head())

# Train-Test Split (70%-30%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("\nTrain-Test Split:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)

# Train-Validation-Test Split (60%-20%-20%)
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.4, random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

print("\nTrain-Validation-Test Split:")
print("Training:", X_train.shape)
print("Validation:", X_val.shape)
print("Testing:", X_test.shape)