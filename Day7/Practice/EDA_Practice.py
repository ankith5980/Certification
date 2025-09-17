# Typical EDA Steps ::
# Summarize: Look at shapes, column names, missing values.
# Describe: Mean, median, min, max, std for each feature.
# Visualize: Histograms, boxplots, scatterplots, heatmaps.
# Check correlations: Which features move together?
# Check balance: Are classes or categories evenly distributed?

# Import ncessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings("ignore")

# Load Dataset
df = pd.read_csv("Day7/MISSING_DATASET_HANDLING.csv")
print(df.head())
print(df.shape) # check number of rows and columns
print(df.columns) # check column names

# Check for missing values
print(df.isnull().sum())

# Descriding using mean, median, min, max, std for each feature
print(df.describe())
print(df.info())

# Check for duplicate rows
print("Duplicates :: ", df.duplicated().sum())
# Drop duplicate rows
df = df.drop_duplicates()

# Visualizations
# Histograms
df.hist(bins=30, figsize=(15,10))
plt.tight_layout()
plt.show()

# Boxplots
plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.xticks(rotation=45)
plt.show()

# Scatterplot matrix
sns.pairplot(df)
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.show()

# Check balance of categorical features
categorical_cols = df.select_dtypes(include=['object', 'category']).columns
for col in categorical_cols:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())
    sns.countplot(y=col, data=df)
    plt.show()

# Handling missing values (example strategies)
# For numerical columns, fill missing values with mean/median
numerical_cols = df.select_dtypes(include=[np.number]).columns
for col in numerical_cols:
    df[col].fillna(df[col].median(), inplace=True)

# For categorical columns, fill missing values with mode
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)
print("\nAfter handling missing values:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("Day7/CLEANED_EDA_DATASET.csv", index=False)
print("\nCleaned dataset saved as 'CLEANED_EDA_DATASET.csv'")

