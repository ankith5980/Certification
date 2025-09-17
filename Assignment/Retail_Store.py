# Forecasting Demand for a Retail Store

# Import ncessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Loading dataset
df = pd.read_csv("Assignment/retail_store_inventory.csv")
print(df.head())

# Showing available columns
print("Columns in dataset:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

# Identifying features and target
target_col = 'Demand Forecast'

# Label Encoding categorical features
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = le.fit_transform(df[col].astype(str))
print("\nTransformed Data:\n", df.head())

X = df.drop(target_col, axis=1)
y = df[target_col]

# Putting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Creation and Training - Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("\nThe Linear Regression Model has been trained successfully.")

# Evaluating the model
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)
print("R² Score:", model.score(X_test, y_test))
print("Predictions on Test Set:", y_pred)
print("Actual values:", y_test.values)
print("Mean Absolute Error:", np.mean(np.abs(y_test - y_pred)))

# Graphical representation of Actual vs Predicted
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Demand")
plt.ylabel("Predicted Demand")
plt.title("Actual vs Predicted Demand")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.show()

# This model has an R² score of 0.9937, That is it has 99.37% accuracy
