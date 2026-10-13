import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, r2_score

try:
    # --- Before PCA ---
    df2 = pd.read_csv("/content/sdperform.csv")

    std_indep = df2.drop(columns=['GradeClass', 'StudentID', 'GPA'])
    std_dep = df2['GPA']

    std_indep_train, std_indep_test, std_dep_train, std_dep_test = train_test_split(
        std_indep, std_dep, test_size=0.2, random_state=42
    )

    scaler_perf = StandardScaler()
    std_indep_train_sc = scaler_perf.fit_transform(std_indep_train)
    std_indep_test_sc = scaler_perf.transform(std_indep_test)

    model1 = LinearRegression()
    model1.fit(std_indep_train_sc, std_dep_train)

    std_dep_pred = model1.predict(std_indep_test_sc)
    print("Before PCA Performance:")
    print(f"Mean Squared Error: {mean_squared_error(std_dep_test, std_dep_pred):.4f}")
    print(f"R-squared: {r2_score(std_dep_test, std_dep_pred):.4f}")

    # --- After PCA ---
    pca_perf = PCA(n_components=10)
    std_indep_train_pca = pca_perf.fit_transform(std_indep_train_sc)
    std_indep_test_pca = pca_perf.transform(std_indep_test_sc)

    model2 = LinearRegression()
    model2.fit(std_indep_train_pca, std_dep_train)

    std_dep_pred2 = model2.predict(std_indep_test_pca)
    print("\nAfter PCA (10 Components) Performance:")
    print(f"Mean Squared Error: {mean_squared_error(std_dep_test, std_dep_pred2):.4f}")
    print(f"R-squared: {r2_score(std_dep_test, std_dep_pred2):.4f}")
except FileNotFoundError:
    print("Error: /content/sdperform.csv not found. Please place the file in the proper path.")
