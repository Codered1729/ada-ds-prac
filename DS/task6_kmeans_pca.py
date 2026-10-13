import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, adjusted_rand_score

# Load Data
iris = load_iris()
x_iris = iris.data
y_iris = iris.target

scaler_iris = StandardScaler()
x_iris_scaled = scaler_iris.fit_transform(x_iris)

# K-Means Before PCA
kmeans_full = KMeans(n_clusters=3, random_state=42)
k_labels_full = kmeans_full.fit_predict(x_iris_scaled)
sil_full = silhouette_score(x_iris_scaled, k_labels_full)
ari_full = adjusted_rand_score(y_iris, k_labels_full)

# K-Means After PCA
pca_iris = PCA(n_components=2, random_state=42)
x_iris_pca = pca_iris.fit_transform(x_iris_scaled)

kmeans_pca = KMeans(n_clusters=3, random_state=42)
k_labels_pca = kmeans_pca.fit_predict(x_iris_pca)
sil_pca = silhouette_score(x_iris_pca, k_labels_pca)
ari_pca = adjusted_rand_score(y_iris, k_labels_pca)

print(f"Before PCA -> Silhouette Score: {sil_full:.4f} | Adjusted Rand Index: {ari_full:.4f}")
print(f"After PCA  -> Silhouette Score: {sil_pca:.4f}  | Adjusted Rand Index: {ari_pca:.4f}")
