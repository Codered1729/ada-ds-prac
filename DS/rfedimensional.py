import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load dataset
data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print("Original dataset shape:", X.shape)
print(X.head())

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Standardize data
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model before RFE
model = LogisticRegression(max_iter=500)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

before_accuracy = accuracy_score(y_test, y_pred)
before_precision = precision_score(y_test, y_pred)
before_recall = recall_score(y_test, y_pred)
before_f1 = f1_score(y_test, y_pred)

print("\nBefore RFE")
print("Accuracy:", before_accuracy)
print("Precision:", before_precision)
print("Recall:", before_recall)
print("F1 Score:", before_f1)

# Apply RFE
rfe = RFE(
    estimator=LogisticRegression(max_iter=500),
    n_features_to_select=10
)

X_train_rfe = rfe.fit_transform(X_train_scaled, y_train)
X_test_rfe = rfe.transform(X_test_scaled)

# Train model after RFE
model_rfe = LogisticRegression(max_iter=500)
model_rfe.fit(X_train_rfe, y_train)

y_pred_rfe = model_rfe.predict(X_test_rfe)

after_accuracy = accuracy_score(y_test, y_pred_rfe)
after_precision = precision_score(y_test, y_pred_rfe)
after_recall = recall_score(y_test, y_pred_rfe)
after_f1 = f1_score(y_test, y_pred_rfe)

print("\nAfter RFE")
print("Accuracy:", after_accuracy)
print("Precision:", after_precision)
print("Recall:", after_recall)
print("F1 Score:", after_f1)

# Display selected features
selected_features = X.columns[rfe.support_]

print("\nSelected Features:")
print(selected_features)
