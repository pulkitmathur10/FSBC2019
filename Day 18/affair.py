# Affair
 
import pandas as pd
import numpy as np


affair = pd.read_csv('affairs.csv')  

label = affair.iloc[:,-1].values 
features = affair.iloc[:,:-1].values

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[[6,7]])
features = onehotencoder.fit_transform(features).toarray()

cols_feat=[6,7]
total_col, indexes = 0, []
for col in cols_feat:
    unique_val_count = len(affair.iloc[:,col].value_counts())
    total_col += unique_val_count
    indexes.append(total_col - unique_val_count)
features = np.delete(features, indexes, axis=1)

from sklearn.model_selection import train_test_split
features_train, features_test, label_train, label_test = train_test_split(features, label, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, label_train)

label_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(label_test, label_pred)

per = (cm[1].sum()/cm.sum())*100

print("Percentage of women having an affair:" , per.round())

sample = np.array([3,25,3,1,4,16,4,2])
sample = sample.reshape(1,-1)


sample = onehotencoder.transform(sample).toarray()
sample = sample[:, 1:]
sample = np.delete(sample, 5, axis=1)

m=classifier.predict(sample)
if m[0]==0:
    print("The woman might not have an affair.")
else:
    print("The woman may have an affair.")    
