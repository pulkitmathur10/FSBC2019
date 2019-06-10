# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('deliveryfleet.csv')
features = dataset.iloc[:, [1, 2]].values

plt.scatter(features[:,0], features[:,1])
plt.show()

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Rural')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Urban')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance')
plt.ylabel('Speeding')
plt.legend()
plt.show()

kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster1 = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster1 == 0, 0], features[pred_cluster1 == 0, 1], c = 'blue', label = 'Rural Non-Speeding')
plt.scatter(features[pred_cluster1 == 1, 0], features[pred_cluster1 == 1, 1], c = 'red', label = 'Urban Non-Speeding')
plt.scatter(features[pred_cluster1 == 2, 0], features[pred_cluster1 == 2, 1], c = 'green', label = 'Urban Speeding')
plt.scatter(features[pred_cluster1 == 3, 0], features[pred_cluster1 == 3, 1], c = 'black', label = 'Urban Non-Speeding')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance')
plt.ylabel('Speeding')
plt.legend()
plt.show()
