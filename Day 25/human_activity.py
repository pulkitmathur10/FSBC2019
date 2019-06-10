#Human Activity Recognition with Smartphones

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset_train = pd.read_csv('train.csv')
dataset_test = pd.read_csv('test.csv')

dataset_train.isnull().any().any()
#temp = dataset_train.iloc[:, -2:]

features_train = dataset_train.iloc[:, :-2].values
label_train = dataset_train.iloc[:, -1].values

features_test = dataset_test.iloc[:, :-2].values
label_test = dataset_test.iloc[:, -1].values

accuracy=[]
import statsmodels.api as sm

features_train1 = sm.add_constant(features_train)

list1 = []
list2 = range(562)
while True:
    features_opt = features_train1.iloc[:, list1]
    regressor_OLS = sm.OLS(endog = label_train, exog = features_opt.values).fit()
    list2 = regressor_OLS.pvalues
    list2 = list2[0]
    temp = np.max(list2)
    temp2 = list2.argmax()
    if temp>0.08:
        list1.pop(temp2)
    else:
        break
list1.pop(0)
list_ = np.array(list1)
list_=list_-1
feas_train = features_train[:, list_]
feas_test = features_test[:, list_]






from sklearn.tree import DecisionTreeClassifier  
classifier_dt = DecisionTreeClassifier()  
classifier_dt.fit(features_train, label_train)

labels_pred_dt = classifier_dt.predict(features_test) 

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(label_test, labels_pred_dt))  

classifier_dt.score(features_train, label_train)
classifier_dt.score(features_test, label_test)
accuracy.append(classifier_dt.score(features_test, label_test))


from sklearn.ensemble import RandomForestClassifier

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
label_traine = labelencoder.fit_transform(label_train)
label_teste = labelencoder.transform(label_test)


classifier_rf = RandomForestClassifier(n_estimators=30, random_state=0)  
classifier_rf.fit(features_train, label_traine)  
labels_pred_rf = classifier_rf.predict(features_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(label_test,labels_pred_rf))  
print(classification_report(label_test,labels_pred_rf))  
print(accuracy_score(label_test, labels_pred_rf))

classifier_rf.score(features_train, label_traine)
classifier_rf.score(features_test, label_teste)
accuracy.append(classifier_rf.score(features_test, label_teste))

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, label_train)

probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(label_test, labels_pred)

classifier.score(features_train, label_train)
classifier.score(features_test, label_test)
accuracy.append(classifier.score(features_test, label_test))

from sklearn.neighbors import KNeighborsClassifier
classifier_knn = KNeighborsClassifier(n_neighbors = 5, p = 2)
classifier_knn.fit(features_train, label_train)

classifier_knn.score(features_train, label_train)
classifier_knn.score(features_test, label_test)
accuracy.append(classifier_knn.score(features_test, label_test))

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
labels = ['DecisionTree', 'RandomForest', 'LogisticRegression', 'kNN']

plt.bar(labels, accuracy)
plt.xlabel('Algorithm Used', fontsize=25)
plt.ylabel('Accuracy', fontsize=5)
plt.xticks(labels, fontsize=15, rotation=90)
plt.show()