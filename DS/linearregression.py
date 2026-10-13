import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Load dataset
df = pd.read_csv("Pune-House-Rent.csv")

print(df.head())

# Select input and output features
X = df[["BHK", "Size", "Bathroom"]]
y = df["Rent"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict rent
y_pred = model.predict(X_test)

# Evaluate the model
r2 = r2_score(y_test, y_pred)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

mae = mean_absolute_error(y_test, y_pred)

n = len(y_test)
p = X_test.shape[1]

adjusted_r2 = 1 - ((1 - r2) * (n - 1) / (n - p - 1))

print("\nModel Evaluation")
print("R2 Score:", r2)
print("Adjusted R2:", adjusted_r2)
print("RMSE:", rmse)
print("MAE:", mae)

# Predict rent for a new house
new_house = [[2, 1000, 2]]

predicted_rent = model.predict(new_house)

print("\nPredicted Rent:", predicted_rent[0])
