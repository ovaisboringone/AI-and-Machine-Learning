import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_true_prices = np.array([
    200, 250, 300, 350, 400, 220, 280, 330, 380, 420
])

y_pred_prices = np.array([
    210, 240, 310, 360, 390, 230, 270, 340, 370, 430
])

print("True Prices:")
print(y_true_prices)

print("\nPredicted Prices:")
print(y_pred_prices)

mae = mean_absolute_error(y_true_prices, y_pred_prices)

mse = mean_squared_error(y_true_prices, y_pred_prices)

rmse = np.sqrt(mse)

r2 = r2_score(y_true_prices, y_pred_prices)

print("\nMAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)