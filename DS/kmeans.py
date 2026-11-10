import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score

df = pd.read_csv("Iris.csv")

print(df.head())

X = df.drop(["Id", "Species"], axis=1)
y = df["Species"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

labels = kmeans.fit_predict(X_scaled)

ari = adjusted_rand_score(y, labels)
silhouette = silhouette_score(X_scaled, labels)

print("\nCluster Centers:")
print(kmeans.cluster_centers_)

print("\nPerformance Measures:")
print("Adjusted Rand Index:", ari)
print("Silhouette Score:", silhouette)
