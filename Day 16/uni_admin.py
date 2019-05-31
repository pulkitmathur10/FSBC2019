#University Admission Prediction Tool

import pandas as pd  
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
#from sklearn.model_selection import train_test_split 

uni_dataset = pd.read_csv('University_data.csv')
features_uni = uni_dataset.iloc[:, 0:6].values
chance = uni_dataset.iloc[:, -1].values

labelencoder = LabelEncoder()
features_uni[:, 0] = labelencoder.fit_transform(features_uni[:, 0])

onehotencoder = OneHotEncoder(categorical_features = [0])
features_uni = onehotencoder.fit_transform(features_uni).toarray()
features_uni = features_uni[:, 1:]

#features_train_uni, features_test_uni, chance_train_uni, chance_test_uni = train_test_split(features_uni, chance, test_size = 0.2, random_state = 0)

regressor_uni = LinearRegression()
regressor_uni.fit(features_uni, chance)

#Predu = regressor_uni.predict(features_test_uni)
#
#print (pd.DataFrame(Predu, chance_test_uni))


x = ['Beaver', 316, 3, 3.5, 8, 1]
x = np.array(x)
x = x.reshape(1, -1)
x[:, 0] = labelencoder.transform(x[:, 0])

#onehotencoder = OneHotEncoder(categorical_features=[0])
x = onehotencoder.transform(x).toarray()
x = x[:, 1:]



adm_chance = regressor_uni.predict(x)
print(adm_chance[0]*100)
