# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
house = pd.read_csv('kc_house_data.csv')

features = house.drop('price',axis = 1)
label = house['price']

features.isnull().any()

features['sqft_above'] = features['sqft_above'].fillna(features['sqft_above'].mode()[0])
features['date']=features.date.str.split("T", expand=True)
features['date'] = features['date'].astype(np.float64)

features = features.astype(np.float64)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train,labels_test	=	train_test_split(features, label, test_size=0.3, random_state=1)

from sklearn.linear_model import LinearRegression 
lr = LinearRegression()
lr.fit(features_train, labels_train)

print (lr.score(features_test, labels_test))
print (lr.score(features_train, labels_train))

labels_pred = lr.predict(features_test)


df1 = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})  
print ( df1 )

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
lr_lasso = Lasso() 
lr_ridge =  Ridge() 
lr_elastic_net = ElasticNet()

lr_lasso.fit(features_train, labels_train)
lr_ridge.fit(features_train, labels_train)
lr_elastic_net.fit(features_train, labels_train)

print (lr_lasso.score(features_test, labels_test))
print (lr_lasso.score(features_train, labels_train))

print (lr_ridge.score(features_test, labels_test))
print (lr_ridge.score(features_train, labels_train))

print (lr_elastic_net.score(features_test, labels_test))
print (lr_elastic_net.score(features_train, labels_train))
