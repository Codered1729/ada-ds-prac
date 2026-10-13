import pandas as pd
from sklearn.datasets import load_breast_cancer, make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_selection import RFE

# --- Baseline Model (Breast Cancer) ---
ata = load_breast_cancer()
X = pd.DataFrame(ata.data, columns=ata.feature_names)
y = ata.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.transform(X_test)

model = LogisticRegression(max_iter=500)
model.fit(X_train_sc, y_train)
y_pred = model.predict(X_test_sc)

print("Baseline Breast Cancer Performance:")
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print(f"Precision: {precision_score(y_test, y_pred) * 100:.2f}%")

# --- RFE Model (Breast Cancer) ---
rfe = RFE(estimator=model, n_features_to_select=3)
X_train_rfe = rfe.fit_transform(X_train_sc, y_train)
X_test_rfe = rfe.transform(X_test_sc)

model.fit(X_train_rfe, y_train)
Y_pred = model.predict(X_test_rfe)

print("\nRFE (3 Features) Breast Cancer Performance:")
print(f"Accuracy: {accuracy_score(y_test, Y_pred) * 100:.2f}%")
