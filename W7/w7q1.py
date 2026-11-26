import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = {
    'Size_cm': [7, 7.5, 6.8, 18, 19, 17.5, 8.5, 9, 8.2, 7.2],
    'Color_Intensity': [0.8, 0.75, 0.82, 0.6, 0.58, 0.62, 0.9, 0.88, 0.92, 0.78],
    'FruitType': ['Apple', 'Apple', 'Apple', 'Banana', 'Banana',
                  'Banana', 'Orange', 'Orange', 'Orange', 'Apple']
}

df = pd.DataFrame(data)

X = df[['Size_cm', 'Color_Intensity']]
y = df['FruitType']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Training data:")
print(X_train.head())

print("\nFruit types:")
print(y_train.head())

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)