import pandas as pd

df = pd.read_csv("train.csv")

print("Missing values:")
print(df.isnull().sum())

df = df.drop("Cabin", axis=1)

df["Age"] = df["Age"].fillna(df["Age"].median())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())