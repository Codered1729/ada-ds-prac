import pandas as pd

# Load dataset
df = pd.read_csv('iris-data.csv')

print("Data frame head:\n", df.head())
print("Data frame info:\n")
print(df.info())

# Encode categorical class column
df_encoded = pd.get_dummies(
    df, columns=['class'], drop_first=True
)

print("Encoded head:\n", df_encoded.head())

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X = df_encoded.drop(columns=['Id'])

X_scaled = scaler.fit_transform(X)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

df_pca = pd.DataFrame(
    data=X_pca,
    columns=['principal component-1',
             'principal component-2']
)

df_pca['class'] = df['class']

print("PCA dataframe head:\n", df_pca.head())

import seaborn as sns
import matplotlib.pyplot as plt

# Plot original data
sns.scatterplot(
    x='Sepal length',
    y='Sepal width',
    hue='class',
    data=df
)

plt.title('Original data: Sepal length vs Sepal width')
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal width (cm)')
plt.show()

# Plot PCA-transformed data
sns.scatterplot(
    x='principal component-1',
    y='principal component-2',
    hue='class',
    data=df_pca
)

plt.title('Principal Component-1 vs Principal Component-2')
plt.xlabel('Principal Component-1')
plt.ylabel('Principal Component-2')
plt.show()
