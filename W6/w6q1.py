from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)

df = housing.frame

print("Original data:")
print(df.head())

print("\nOriginal columns:")
print(df.columns)

selected = df[
    ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population"]
]

print("\nSelected features:")
print(selected.head())

print("\nSelected columns:")
print(selected.columns)