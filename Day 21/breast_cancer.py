# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cancer = pd.read_csv('breast_cancer.csv')
cancer.isnull()
cancer['G'] = cancer['G'].fillna(cancer['G'].mode()[0])

cancer["K"]=np.where(cancer["K"]==2,0,1)
features = cancer.drop('A', axis=1)
features = features.drop('K', axis=1).values
label = cancer['K']


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, label, test_size = 0.3, random_state = 0)

from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)


labels_pred = classifier.predict(features_test)


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

score = classifier.score(features_test,labels_test)
score1 = classifier.score(features_train,labels_train)
print(score, score1)
x = np.array([[6,2,5,3,9,4,7,2,2]])
result = classifier.predict(x)
print(result[0])

#x_min, x_max = features_train[:, 0].min() - 1, features_train[:, 0].max() + 1
#y_min, y_max = features_train[:, 1].min() - 1, features_train[:, 1].max() + 1
#
#xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
#                     np.arange(y_min, y_max, 0.1))
## Obtain labels for each point in mesh using the model.
## ravel() is equivalent to flatten method.
## data dimension must match training data dimension, hence using ravel
#Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
#
## Plot the points
#plt.plot(features_test[labels_test == 0, 0], features_test[labels_test == 0, 1], 'ro', label='Class 1')
#plt.plot(features_test[labels_test == 1, 0], features_test[labels_test == 1, 1], 'bo', label='Class 2')
##plot the decision boundary
#plt.contourf(xx, yy, Z, alpha=1.0)
#
#plt.show()
