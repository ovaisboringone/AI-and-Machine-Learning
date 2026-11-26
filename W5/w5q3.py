import pandas as pd
import numpy as np

np.random.seed(43)

temp_data = pd.DataFrame({
    "CityName": ["London", "Paris", "New York", "Tokyo",
                 "Berlin", "Rome", "Sydney", "Cairo"],
    "AvgTempC": np.random.uniform(10, 30, 8).round(1),
    "Humidity": np.random.uniform(50, 90, 8).round(1)
})

city_data = pd.DataFrame({
    "City": ["London", "Paris", "New York", "Tokyo",
            "Sydney", "Dubai", "Beijing"],
    "Country": ["UK", "France", "USA", "Japan",
                "Australia", "UAE", "China"],
    "PopulationMillions": [9, 2.1, 8.4, 14, 5.3, 3.1, 21.5]
})

result = pd.merge(
    temp_data,
    city_data,
    left_on="CityName",
    right_on="City",
    how="inner"
)

print(result)