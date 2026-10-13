from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

rent=pd.read_csv("/content/sample_data/Pune_rent.csv")
for col in ['bedroom', 'bathroom', 'area']:
    rent[col] = pd.to_numeric(rent[col].astype(str).str.replace('Grfloor', '0'), errors='coerce')
    rent[col] = rent[col].fillna(0) 

x=rent[['bedroom','bathroom','area']]
y= rent['price'].str.replace(',', '').astype(float).astype(int)

scaler=StandardScaler()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
x_train_sc=scaler.fit_transform(x_train)
x_test_sc=scaler.transform(x_test)

model=LinearRegression()
model.fit(x_train_sc,y_train)

y_pred=model.predict(x_test_sc)
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


import matplotlib.pyplot as plt
plt.scatter(y_test,y_pred)
plt.xlabel("Actual Age")
plt.ylabel("Predicted Age")
plt.title("Actual vs Predicted Age")
plt.show()
