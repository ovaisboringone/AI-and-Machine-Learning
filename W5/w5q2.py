import pandas as pd
import numpy as np

np.random.seed(42)

scores = np.random.normal(75, 10, 100)

scores[10] = 150
scores[25] = -20
scores[50] = 5

df = pd.DataFrame({
    "EmployeeID": range(1, 101),
    "PerformanceScore": scores.round(0)
})

print(df.head())

q1 = df["PerformanceScore"].quantile(0.25)
q3 = df["PerformanceScore"].quantile(0.75)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = df[
    (df["PerformanceScore"] < lower) |
    (df["PerformanceScore"] > upper)
]

print("\nOutliers:")
print(outliers)

df.loc[df["PerformanceScore"] < lower, "PerformanceScore"] = lower
df.loc[df["PerformanceScore"] > upper, "PerformanceScore"] = upper

print("\nAfter capping:")
print(df.head())