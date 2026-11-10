import pandas as pd
import numpy as np

df = pd.read_csv('Iris.csv')

print("Data Frame Head:\n")
print(df.head())

print("\n DataFrame Info:")
print(df.info())

print(df.describe())

print("\n Missing values in each column:")
print(df.isnull().sum())

numeric_columns = df.select_dtypes(include=[np.number]).columns

df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].mean()
)

categorical_columns = df.select_dtypes(
    exclude=[np.number]
).columns

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\n DataFrame after handling missing values:")
print(df.head())

print("\n Missing values after filling:")
print(df.isnull().sum())
