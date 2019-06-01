import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

cancer = pd.read_csv('breast_cancer.csv')
cancer.isnull()
cancer['G'] = cancer['G'].fillna(cancer['G'].mode()[0])

cancer["K"]=np.where(cancer["K"]==2,0,1)
features = cancer.drop('A', axis=1)
features = features.drop('K', axis=1)
label = cancer['K']


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, label, test_size = 0.3, random_state = 0)

gnb = GaussianNB()
gnb.fit(features_train, labels_train)

labels_pred1 = gnb.predict(features_test)



from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(labels_test, labels_pred1)
print(cm1)

score2 = gnb.score(features_test,labels_test)
score3 = gnb.score(features_train,labels_train)
print(score2, score3)