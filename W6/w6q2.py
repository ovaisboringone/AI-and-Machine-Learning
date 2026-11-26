from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)

df = iris.frame

print(df.head())



normalized = df[features].copy()

for column in features:
    minimum = normalized[column].min()
    maximum = normalized[column].max()

    normalized[column] = (
        normalized[column] - minimum
    ) / (maximum - minimum)

print("Normalized data:")
print(normalized.head())





standardized = df[features].copy()

for column in features:
    mean = standardized[column].mean()
    std = standardized[column].std()

    standardized[column] = (
        standardized[column] - mean
    ) / std

print("\nStandardized data:")
print(standardized.head())