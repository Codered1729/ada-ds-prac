import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder, StandardScaler
from sklearn.decomposition import PCA

try:
    # Load and preview
    df = pd.read_csv("/content/Iris.csv")
    print("Dataset successfully loaded.")
    
    # Handle Missing Values
    num_col = df.select_dtypes(include=[np.number]).columns
    df[num_col] = df[num_col].fillna(df[num_col].mean())

    cat_col = df.select_dtypes(exclude=[np.number]).columns
    for cat in cat_col:
        df[cat] = df[cat].fillna(df[cat].mode()[0])

    df = df.round(1)
    df.to_csv("123Iris123.csv", index=False)
    print("Missing values handled and file saved to 123Iris123.csv.")

    # Categorical Encoding
    encoder = OneHotEncoder()
    enc_data = encoder.fit_transform(df[['Species']]).toarray()
    enc_df = pd.DataFrame(enc_data, columns=encoder.get_feature_names_out(['Species']))
    df_final = pd.concat([df.drop(columns=['Species']), enc_df], axis=1)

    le = LabelEncoder()
    df['LabelEncoded'] = le.fit_transform(df['Species'])

    order = ['Iris-versicolor', 'Iris-setosa', 'Iris-virginica']
    Ore = OrdinalEncoder(categories=[order])
    df["OrdinalEncoded"] = Ore.fit_transform(df[['Species']])
    print("Encoding completed.")

    # Scaling
    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled[['SepalLengthCm']] = scaler.fit_transform(df[['SepalLengthCm']])
    
    # Plot heatmaps & scatterplots
    plt.figure(figsize=(6, 4))
    sns.scatterplot(y='SepalWidthCm', x='SepalLengthCm', hue='Species', data=df)
    plt.title("Sepal Dimensions")
    plt.savefig("task1_scatter.png")
    plt.close()
    print("Visualizations saved to disk.")
except FileNotFoundError:
    print("Error: /content/Iris.csv not found. Please upload the dataset to run the pipeline.")
