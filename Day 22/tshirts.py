# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

shirts = pd.read_csv('tshirts.csv')
sizes = shirts.iloc[:, [1, 2]].values

plt.scatter(sizes[:,0], sizes[:,1])
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_size = kmeans.fit_predict(sizes)

plt.scatter(sizes[pred_size == 0, 0], sizes[pred_size == 0, 1], c = 'blue', label = 'medium')
plt.scatter(sizes[pred_size == 1, 0], sizes[pred_size == 1, 1], c = 'red', label = 'large')
plt.scatter(sizes[pred_size == 2, 0], sizes[pred_size == 2, 1], c = 'green', label = 'small')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
plt.show()

