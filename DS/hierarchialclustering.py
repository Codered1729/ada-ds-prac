import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage

# Load dataset
df = pd.read_csv("weather.csv")

print(df.head())

# Select features
X = df[
    [
        "Data.precipitation",
        "Data.Temperature.Avg.Temp",
        "Data.Temperature.Max.Temp",
        "Data.Temperature.Min.Temp",
        "Data.Wind Direction",
        "Data.Wind Speed"
    ]
]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create linkage matrix using Ward's method
linked = linkage(X_scaled, method="ward")

# Plot dendrogram
plt.figure(figsize=(10, 6))
dendrogram(linked)

plt.title("Hierarchical Clustering Using Ward's Method")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()

# Apply Agglomerative Clustering
model = AgglomerativeClustering(
    n_clusters=3,
    linkage="ward"
)

labels = model.fit_predict(X_scaled)

print("\nCluster Labels:")
print(labels)

# Calculate Silhouette Score
silhouette = silhouette_score(X_scaled, labels)

print("\nPerformance Measure:")
print("Silhouette Score:", silhouette)
