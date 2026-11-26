import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

np.random.seed(42)

small_animals = np.random.normal(
    loc=[5, 20], scale=[1, 5], size=(20, 2)
)

medium_animals = np.random.normal(
    loc=[50, 80], scale=[10, 15], size=(20, 2)
)

large_animals = np.random.normal(
    loc=[300, 150], scale=[50, 25], size=(20, 2)
)

X_animals = pd.DataFrame(
    np.vstack([small_animals, medium_animals, large_animals]),
    columns=["Weight_kg", "Height_cm"]
)

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X_animals)

X_scaled_df = pd.DataFrame(
    X_scaled, columns=X_animals.columns
)

print("Scaled data:")
print(X_scaled_df.head())

model = KMeans(n_clusters=3, random_state=42, n_init=10)

model.fit(X_scaled_df)

X_animals["Cluster"] = model.labels_

print("\nClustered data:")
print(X_animals.head())

centroids = scaler.inverse_transform(model.cluster_centers_)

plt.scatter(
    X_animals["Weight_kg"],
    X_animals["Height_cm"],
    c=X_animals["Cluster"]
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="X",
    s=200
)

plt.xlabel("Weight (kg)")
plt.ylabel("Height (cm)")
plt.title("Animal Grouping using K-Means")

plt.show()