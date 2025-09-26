# predict student marks based on the number of study hours

# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load dataset
df = pd.read_csv("Practice/Q2/student_exam_scores.csv")
print(df.head())
print(df.info())
print(df.describe())

# Checking for null values
print(df.isnull().sum())

# Features and Target
X = df[["hours_studied"]] #Core feature --> Based on what we want to predict
y = df["exam_score"] #Target --> What we want to predict
print(X.shape, y.shape)

# Performing One-Hot Encoding
# X = pd.get_dummies(X, drop_first=True) # No categorical variable here
# print(X.head())
# print(X.shape)
# Since there aren't any categorical variables, we skip one-hot encoding

# Performing Standardization/Normalization
scaler = StandardScaler()
X[['hours_studied']] = scaler.fit_transform(X[['hours_studied']])
print(X.head())
print(X.describe())
# Since there's only one feature, scaling is not strictly necessary here

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
print("\n Model trained successfully")

# Predictions
y_pred = model.predict(X_test)
print(y_pred)
print(y_test.values)

# Evaluation
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("R² Score:", r2)
print("MSE:", mse)
print("RMSE:", rmse)

