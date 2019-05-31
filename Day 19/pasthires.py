# -*- coding: utf-8 -*-

import pandas as pd  
import numpy as np  
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


dataset = pd.read_csv("PastHires.csv")

label_h = dataset.iloc[:, -1]
features_h = dataset.iloc[:, :-1]

enc1 = LabelEncoder()
enc2 = LabelEncoder()

features_h['Employed?'] = enc1.fit_transform(features_h['Employed?'])
features_h['Top-tier school'] = enc1.fit_transform(features_h['Top-tier school'])
features_h['Interned'] = enc1.fit_transform(features_h['Interned'])
features_h['Level of Education'] = enc2.fit_transform(features_h['Level of Education'])

#onehotencoder = OneHotEncoder(categorical_features=[[1,3,4,5]])
#features_h = onehotencoder.fit_transform(features_h).toarray()
#
#cols_feat=[1,3,4,5]
#total_col, indexes = 0, []
#for col in cols_feat:
#    unique_val_count = len(dataset.iloc[:,col].value_counts())
#    total_col += unique_val_count
#    indexes.append(total_col - unique_val_count)
#    
#features_h = np.delete(features_h, indexes, axis=1)

from sklearn.model_selection import train_test_split  
features_train_h, features_test_h, labels_train_h, labels_test_h = train_test_split(features_h, label_h, test_size=0.20)  


from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train_h, labels_train_h)

labels_pred = classifier.predict(features_test_h) 

from sklearn.metrics import confusion_matrix  
print("CM matrix for a single Decision Tree: ", confusion_matrix(labels_test_h, labels_pred))  


from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features_train_h, labels_train_h)  

labels_predt = classifier.predict(features_test_h)

print("CM matrix for using Random Forest: ", confusion_matrix(labels_test_h, labels_predt))

x = np.array([[10, 'N', 4, 'MS', 'N', 'Y']])

x[:, 1] = enc1.transform(x[:, 1])
x[:, 3] = enc2.transform(x[:, 3])
x[:, 4] = enc1.transform(x[:, 4])
x[:, 5] = enc1.transform(x[:, 5])

#x= onehotencoder.transform(x).toarray()
#
#cols_feat1=[1,3,4,5]
#total_col1, indexes1 = 0, []
#for col1 in cols_feat1:
#    unique_val_count1 = len(dataset.iloc[:,col1].value_counts())
#    total_col1 += unique_val_count1
#    indexes1.append(total_col1 - unique_val_count1)
#    
#x = np.delete(x, indexes1, axis=1)

approval = classifier.predict(x)
if(approval[0]=='Y'):
    print("The given candidate is hired.")
else:
    print("The given candidate is not hired.")