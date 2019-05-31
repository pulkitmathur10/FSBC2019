#Mushrooms

import sklearn as sk  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

mush = pd.read_csv('mushrooms.csv')  

label_m = mush.iloc[:,0].values 
features_m = mush.iloc[:,[5,-2,-1]].values
#le_obj=[]
#for m in range(3):
enc1 = LabelEncoder()
enc2 = LabelEncoder()
enc3 = LabelEncoder()

features_m[:, 0] = enc1.fit_transform(features_m[:, 0])
features_m[:, 1] = enc2.fit_transform(features_m[:, 1])
features_m[:, 2] = enc3.fit_transform(features_m[:, 2])
#le_obj.append(labelencoder)

onehotencoder = OneHotEncoder(categorical_features=[[0,1,2]])
features_m = onehotencoder.fit_transform(features_m).toarray()


cols_feat=[5,-2,-1]
total_col, indexes = 0, []
for col in cols_feat:
    unique_val_count = len(mush.iloc[:,col].value_counts())
    total_col += unique_val_count
    indexes.append(total_col - unique_val_count)
    
    
features_m = np.delete(features_m, indexes, axis=1)


from sklearn.model_selection import train_test_split
features_train_m, features_test_m, label_train_m, label_test_m = train_test_split(features_m, label_m, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train_m = sc.fit_transform(features_train_m)
features_test_m = sc.transform(features_test_m)



from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train_m, label_train_m)

label_pred_m = classifier.predict(features_test_m)

from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(label_test_m, label_pred_m)

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  
