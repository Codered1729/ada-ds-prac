import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('Iris.csv')

# Display first 5 rows
print("Data Frame Head:\n")
print(df.head())

# Display dataset info
print("\n DataFrame Info:")
print(df.info())

print(df.describe())  # Statistical information

# Check for missing values
print("\n Missing values in each column:")
print(df.isnull().sum())

# Fill the missing values with column mean (for numerical columns)
numeric_columns = df.select_dtypes(include=[np.number]).columns

df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].mean()
)

# Fill missing values of categorical columns with the mode
categorical_columns = df.select_dtypes(
    exclude=[np.number]
).columns

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Display the dataset after handling missing values
print("\n DataFrame after handling missing values:")
print(df.head())

# Check missing values again
print("\n Missing values after filling:")
print(df.isnull().sum())
