# Unsupervised Learning
#  Cluster policyholders based on age, premium paid, and claim history.
# Suggest how the company can use these clusters for targeted insurance plans.

# importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Loading Dataset
df = pd.read_csv("Certification_Exam/InsurancePrediction.csv")
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
print(df.head())

# Convert FrequentFlyer and TravelInsurance to numeric BEFORE one-hot encoding
if df['FrequentFlyer'].dtype == 'object':
    df['FrequentFlyer'] = df['FrequentFlyer'].map({'Yes': 1, 'No': 0})
if df['TravelInsurance'].dtype == 'object':
    df['TravelInsurance'] = df['TravelInsurance'].map({'Yes': 1, 'No': 0})

# One-hot encoding categorical variables
df = pd.get_dummies(df, columns=['GraduateOrNot', 'Employment Type', 'ChronicDiseases', 'EverTravelledAbroad'], drop_first=True)
print(df.head())

# Selecting features for clustering
# Using FrequentFlyer as claim history indicator
# Using TravelInsurance as Premium paid indicator
X = df[['Age', 'FrequentFlyer', 'TravelInsurance']]
print(X.head())

# Scalling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)

# Number of clusters using Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Elbow Method plot
sns.set()
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Optimal number of clusters
optimal_clusters = 3

# Applying KMeans Clustering
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X_scaled)
print(y_kmeans)

# Labelling
df['Cluster'] = y_kmeans
print(df.head())

# clusters
plt.figure(figsize=(8, 8))
plt.scatter(X_scaled[y_kmeans == 0, 0], X_scaled[y_kmeans == 0, 1], s=50, c='blue', label='Cluster 1')
plt.scatter(X_scaled[y_kmeans == 1, 0], X_scaled[y_kmeans == 1, 1], s=50, c='green', label='Cluster 2')
plt.scatter(X_scaled[y_kmeans == 2, 0], X_scaled[y_kmeans == 2, 1], s=50, c='pink', label='Cluster 3')

# Centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='red', label='Centroids')
plt.title('Policyholder Clusters')
plt.xlabel('Age')
plt.ylabel('Frequent Flyer')
plt.legend()
plt.show()

# Looking into clusters
for i in range(optimal_clusters):
    print(f"\nCluster {i} details:")
    print(df[df['Cluster'] == i].describe())


# Suggestions with respect to clusters
print("\nTargeted Insurance Plan Suggestions")
for i in range(optimal_clusters):
    cluster_data = df[df['Cluster'] == i]
    avg_age = cluster_data['Age'].mean()
    freq_flyer_rate = cluster_data['FrequentFlyer'].mean()
    travel_insurance_rate = cluster_data['TravelInsurance'].mean()
    print(f"\nCluster {i}:")
    print(f"Average Age: {avg_age:.2f}")
    print(f"Frequent Flyer Rate: {freq_flyer_rate:.2f}")
    print(f"Travel Insurance Rate: {travel_insurance_rate:.2f}")
    if travel_insurance_rate < 0.5:
        print("Suggestion: Offer discounted travel insurance plans to increase uptake.")
    else:
        print("Suggestion: Maintain current insurance offerings, consider loyalty rewards for frequent flyers.")

