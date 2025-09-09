import pandas as pd

# Exploratory data analysis
data = pd.read_csv("Day7/MISSING_DATASET_HANDLING.csv", encoding = "latin1")
print(data.isnull().sum())