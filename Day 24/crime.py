# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder

dataset = pd.read_csv('crime_data.csv')

features = dataset.iloc[:, [1,2,4]]
#label = dataset.iloc[:, []]


from sklearn.cross_validation import train_test_split
features_train, features_test = train_test_split(features, test_size = 0.1, random_state = 0)
features_traind = pd.DataFrame(features_train)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)
explained_variance = pca.explained_variance_ratio_

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features_train)
#le = LabelEncoder()
#label = le.fit_transform(label)

plt.scatter(features_train[pred_cluster == 0, 0], features_train[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features_train[pred_cluster == 1, 0], features_train[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features_train[pred_cluster == 2, 0], features_train[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()

#df_pca =  pd.DataFrame(pca.components_,columns=features_traind.columns,index = ['PC-1','PC-2', 'PC-3'])

