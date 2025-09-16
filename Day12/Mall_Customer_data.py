import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns



data = pd.read_csv("Day12/Mall_Customers.csv")
print(data.head())
data.shape

print(data.info())
print(data.describe())
print(data.isnull().sum())

x = data.iloc[:,[3,4]].values
print(x)

wcss = []
for i in range(1,11):
   
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

#elbow method
sns.set()
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')

plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

Clusters = 5
kmeans = KMeans(n_clusters=Clusters, init='k-means++', random_state=0)
y = kmeans.fit_predict(x)
print(y)

plt.figure(figsize=(8,8))
plt.scatter(x[y==0,0], x[y==0,1], s=50, c='blue', label='Cluster 1')
plt.scatter(x[y==1,0], x[y==1,1], s=50, c='green', label='Cluster 2')
plt.scatter(x[y==2,0], x[y==2,1], s=50, c='pink', label='Cluster 3')
plt.scatter(x[y==3,0], x[y==3,1], s=50, c='black', label='Cluster 4')
plt.scatter(x[y==4,0], x[y==4,1], s=50, c='gray', label='Cluster 5')

# Centroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='red', label='Centroids')
plt.title('Customer Groups')
plt.xlabel('Annual Income')
plt.show()
