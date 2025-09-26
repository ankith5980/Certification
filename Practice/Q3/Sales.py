# predict sales from advertising budget (TV, Radio, Newspaper)

# importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings("ignore")

# Load dataset
df = pd.read_csv("Practice/Q3/Advertising Budget and Sales.csv")
print(df.head())
print(df.info())
print(df.describe())

# Checking for null values
print(df.isnull().sum())


# Features & Target
x = df[['TV Ad Budget ($)', 'Radio Ad Budget ($)', 'Newspaper Ad Budget ($)']]
y = df['Sales ($)']
print(x.shape)
print(y.shape)


# Encode categorical variables if any
# (In this dataset, there are no categorical variables to encode)


# Splitting into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# Training the Linear Regression model
model = LinearRegression()
model.fit(x_train, y_train)
print("\n Model trained successfully")

# Predictions
y_pred = model.predict(x_test)
print(y_pred)
print(y_test.values)

# Evaluation
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("R² Score:", r2)
print("MSE:", mse)
print("RMSE:", rmse)

# Visualizing Actual vs Predicted Sales
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2, color='red')
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.title('Actual vs Predicted Sales')
plt.show()
