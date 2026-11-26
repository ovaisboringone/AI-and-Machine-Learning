import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

temp = np.array([10, 15, 20, 25, 30, 12, 18, 23, 28, 32]).reshape(-1, 1)

kwh = np.array([50, 60, 75, 90, 105, 55, 70, 85, 95, 110])

X_train, X_test, y_train, y_test = train_test_split(
    temp, kwh, test_size=0.3, random_state=42
)

print("Training temperatures:")
print(X_train)

print("\nTraining electricity consumption:")
print(y_train)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)

mse = mean_squared_error(y_test, y_pred)

print("\nMean Squared Error:", mse)

plt.scatter(X_train, y_train)
plt.plot(X_train, model.predict(X_train))

plt.xlabel("Temperature (°C)")
plt.ylabel("Electricity Consumption (kWh)")
plt.title("Temperature vs Electricity Consumption")

plt.show()