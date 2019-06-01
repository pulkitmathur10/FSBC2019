import numpy as np
import pandas as pd

from sklearn import datasets 
iris = datasets.load_iris()

iris_df	= pd.DataFrame (iris.data, columns= iris.feature_names )
label_iris = pd.DataFrame (iris.target)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(iris_df, label_iris, test_size = 0.3, random_state = 0)

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
