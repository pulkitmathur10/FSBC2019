# -*- coding: utf-8 -*-

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

colnames = ["mpg", "cylinders", "displacement", "horsepower","weight","acceleration", "model year", "origin", "car name"]
dataset_auto = pd.read_csv("Auto_mpg.txt", delimiter="\s+", names=colnames)  
dataset_auto = dataset_auto.replace(to_replace="?", value=float(dataset_auto.horsepower.mode()[0]))

df = dataset_auto[dataset_auto['mpg']== dataset_auto.mpg.max()][['car name']]
print("The Car Name with highest miles per gallon is:", df.values[0][0])

#dataset_auto['horsepower']= dataset_auto['horsepower'].astype(np.float64)
label = dataset_auto['mpg']
features = dataset_auto.drop(['mpg', 'car name'] , axis=1)
features = features.astype(np.float64)                 
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, label, test_size=0.10)  

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  


from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
compare=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
 
from sklearn.ensemble import RandomForestRegressor

regressor1 = RandomForestRegressor(n_estimators=80, random_state=0)  
regressor1.fit(features_train, labels_train)  
labels_pred_tree = regressor.predict(features_test)

compare_t = pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred_tree})


x = np.array([[6,215,100,2630,22.2,80,3]])
x=x.reshape(1,-1)
x1 = sc.transform(x)
print("MPG value of the given car using a single Decision Tree is:", regressor.predict(x1))
print("MPG value of the given car using Random Forest Regressor is:",regressor1.predict(x1))