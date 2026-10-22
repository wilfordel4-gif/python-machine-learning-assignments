from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]
customer_data = [ [1000, 2], [1500, 3], [20000, 2], [5000, 6], [6000, 7], [5500, 5], [12000, 12], [15000, 12], [13000, 11], [3000, 4] ]
scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_data)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(scaled_data)
cluster_labels = kmeans.predict(scaled_data)
for i, cluster in enumerate(cluster_labels):
 print(f"Customer {i+1} belongs to cluster {cluster}")
print("\n---cluster Summary---")
for cluster in range(3):
 count = np.sum(cluster_labels == cluster)
 print(f"Cluster {cluster}: {count} customers")
spending = [data[0] for data in customer_data]
visits = [data[1] for data in customer_data]
plt.figure(figsize=(8, 6))
scatter =plt.scatter(spending, visits, c=cluster_labels, cmap='viridis')
for i,(x,y) in enumerate(zip(spending, visits),start=1):
 plt.text(x+200, y, f'Customer {i}')
plt.title('Customer Segmentation using K-Means Clustering')
plt.xlabel('Annual Spending (kes)')
plt.ylabel('Monthly Visits')
plt.grid(True, linestyle='--', alpha=0.6)
plt.colorbar(scatter, label='Cluster ID', ticks=[0, 1, 2])
plt.show()
