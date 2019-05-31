# Food Truck Profit Prediction Tool

import pandas as pd  
#import numpy as np
from sklearn.linear_model import LinearRegression
#from sklearn.model_selection import train_test_split 

dataset = pd.read_csv('Foodtruck.csv')

features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 

#features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(features, labels)


#labels_pred = regressor.predict(features_test) 

#df = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})

profit = regressor.predict(3.5)
print(profit[0])