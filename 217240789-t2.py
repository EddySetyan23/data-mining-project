import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.metrics import silhouette_score
import warnings


os.environ['OMP_NUM_THREADS'] = '1'


# Read data from the CSV file
data = pd.read_csv('C:\\Data Mining Project\\Data Mining Task 3\\217240789.csv')

# Drop the 'Date' column
data = data.drop(['Date'], axis=1)

# Prepare the data for clustering
X = data.values

# Normalize the data
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# Calculate SSE for k=5 and k=7
def calculate_sse(data, k_values):
    sse_values = []
    for k in k_values:
        warnings.filterwarnings('ignore', category=UserWarning)
        kmeans = MiniBatchKMeans(n_clusters=k, batch_size=3072, n_init=10)
        kmeans.fit(data)
        sse_values.append(kmeans.inertia_)
    return sse_values

k_values = [5, 7]
sse_values = calculate_sse(X_normalized, k_values)

# Print SSE values
for k, sse in zip(k_values, sse_values):
    print(f"SSE for k={k}: {sse}")

# Perform k-means clustering with the number of classes from Phase 2 Task 6
k = 2  
warnings.filterwarnings('ignore', category=UserWarning)
kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
kmeans.fit(X_normalized)
y_pred = kmeans.labels_

# Compute silhouette score assuming we don't have true labels
silhouette = silhouette_score(X_normalized, y_pred)
print(f"Silhouette Score: {silhouette}")
