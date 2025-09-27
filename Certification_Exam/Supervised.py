# Linear Regression model to predict salary based on years of experience, education level, and job role. Evaluate R² score.

# importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Loading Dataset
df = pd.read_csv("Certification_Exam/Salary_Data.csv")
print(df.head())
print(df.info())
print(df.describe())

# Checking for null values
print(df.isnull().sum())

# Removing null values
df = df.dropna()
print("After removing null values:")
print(df.isnull().sum())

# Checking for duplicates
print("Duplicates :: ", df.duplicated().sum())

# Dropping duplicates
df = df.drop_duplicates()
print("After removing duplicates:")
print(df.duplicated().sum())

# Dropping irrelevant columns
df = df.drop(columns=["Age", "Gender"])
print(df.head())

# Feature and Target Splitting
X = df[["Years of Experience", "Education Level", "Job Title"]]
y = df["Salary"]
print(X.head())
print(y.head())

# One-hot encoding categorical variables
ct = ColumnTransformer(
    transformers=[("encoder", OneHotEncoder(drop='first'), ["Education Level", "Job Title"])],
    remainder='passthrough'
)
X = ct.fit_transform(X)
print(X[:5])
print(y[:5])

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# Training the model --> Here, Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)
print("\n Model trained successfully")

# Making predictions
y_pred = model.predict(X_test)
print("Predictions:", y_pred[:5])

# Evaluating the model
r2 = r2_score(y_test, y_pred)
print("R² Score:", r2)

# Accuracy interpretation
accuracy_percentage = r2 * 100
print(f"Model Accuracy: {accuracy_percentage:.2f}%")