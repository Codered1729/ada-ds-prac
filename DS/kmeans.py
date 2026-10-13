import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score

# Load dataset
df = pd.read_csv("Iris.csv")

print(df.head())

# Select features and actual species labels
X = df.drop(["Id", "Species"], axis=1)
y = df["Species"]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means clustering
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

labels = kmeans.fit_predict(X_scaled)

# Evaluate clustering performance
ari = adjusted_rand_score(y, labels)
silhouette = silhouette_score(X_scaled, labels)

# Display cluster centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# Display performance measures
print("\nPerformance Measures:")
print("Adjusted Rand Index:", ari)
print("Silhouette Score:", silhouette)
