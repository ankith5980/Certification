# predict the weight of a fish from its length and height

# importing necessar libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Loading the dataset
df = pd.read_csv("Practice/Q4/Fish.csv")
print(df.head())
print(df.info())
print(df.describe())

# Checking for null values
print(df.isnull().sum())

# Features and Target
x = df[['Length1', 'Length2', 'Length3', 'Height']]
y = df['Weight']
print(x.head())

# Encoding categorical variable 'Species' using one-hot encoding
x = pd.get_dummies(x, drop_first=True)
print(x.head())

# Drop 'Species' column if it was included in features
x = x.drop(columns=['Species'], errors='ignore')
print(x.shape)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape)

# Training the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
print("\nModel trained successfully")

# Making predictions
y_pred = model.predict(X_test)
print(y_pred[:5])

# Evaluating the model
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("R² Score:", r2)
print("RMSE:", rmse)

# Visualizing Actual vs Predicted weights
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Weight")
plt.ylabel("Predicted Weight")
plt.title("Actual vs Predicted Weight")
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--')
plt.show()
