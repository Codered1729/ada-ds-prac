import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create Synthetic Dataset
np.random.seed(42)
n_samples = 500
age = np.random.uniform(18, 80, n_samples)
systolic_bp = 90 + (0.7 * age) + np.random.normal(0, 8, n_samples)
cholesterol = 140 + (1.5 * age) + np.random.normal(0, 15, n_samples)
screen_time = np.maximum(0.5, 9.0 - (0.08 * age) + np.random.normal(0, 1.2, n_samples))

df11 = pd.DataFrame({
    'systolic_bp': np.round(systolic_bp, 1),
    'cholesterol_mg_dl': np.round(cholesterol, 1),
    'daily_screen_time_hrs': np.round(screen_time, 1),
    'age': np.round(age, 1)
})

# Prepare Regression Data
dep = df11.drop(columns=['age'])
indep = df11['age']

dep_train, dep_test, indep_train, indep_test = train_test_split(dep, indep, test_size=0.2, random_state=42)

scaler_reg = StandardScaler()
dep_train_sc = scaler_reg.fit_transform(dep_train)
dep_test_sc = scaler_reg.transform(dep_test)

# Fit and Evaluate Linear Regression
model_reg = LinearRegression()
model_reg.fit(dep_train_sc, indep_train)

indep_pred = model_reg.predict(dep_test_sc)
mse = mean_squared_error(indep_test, indep_pred)
r2 = r2_score(indep_test, indep_pred)

print(f"Mean Squared Error: {mse:.4f}")
print(f"R-squared: {r2:.4f}")
