# predict wine quality score based on chemical properties

# import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np

# load dataset
df = pd.read_csv("Practice/Q5/wine.csv")
print(df.head())
print(df.info())
print(df.describe())

# Features and targets
x = df[[]]