import pandas as pd

# Exploratory data analysis
data = pd.read_csv("Day7/MISSING_DATASET_HANDLING.csv", encoding = "latin1")
print(data.isnull().sum())

print("\n")

# Dropping column with more than 50% missing values
data = data.drop(columns = ["ADDRESSLINE2"])
print(data.isnull().sum())

print("\n")

# Drops rows with any missing values
# If missing values are very less, we can drop those rows
data = data.dropna(subset = ["ORDERDATE", "PRODUCTLINE"])
print(data.isnull().sum())

print("\n")

# Fill missing values (imputation)
# Numerical columns (MSRP, YEAR_ID)
# Use mean mean/median/mode based on distribution
data["MSRP"] = data["MSRP"].fillna(data["MSRP"].median())
data["YEAR_ID"] = data["YEAR_ID"].fillna(data["YEAR_ID"].mode()[0])
print(data.isnull().sum())

print("\n")

# Categorial columns (STATUS, PRODUCTLINE, CUSTOMERNAME)
# Use mode (Most frequent value)
data["STATUS"].fillna(data["STATUS"].mode()[0], inplace = True)
print(data.isnull().sum())

print("\n")

# Phone numbers or addresses (PHONE, ADDRESSLINE1))
data["PHONE"].fillna("Unknown",inplace=True)
print(data.isnull().sum())

print("\n")