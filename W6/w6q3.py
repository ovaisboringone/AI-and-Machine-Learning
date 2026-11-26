import pandas as pd

columns = [
    "age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race",
    "sex", "capital-gain", "capital-loss", "hours-per-week",
    "native-country", "income"
]

df = pd.read_csv(
    "adult.data",
    header=None,
    names=columns,
    skipinitialspace=True
)

bins = [17, 30, 45, 60, df["age"].max()]
labels = ["Young Adult", "Middle-Aged", "Senior Adult", "Elderly"]

df["age_group"] = pd.cut(
    df["age"],
    bins=bins,
    labels=labels
)

print(df[["age", "age_group"]].head())

print("\nAge groups:")
print(df["age_group"].value_counts())