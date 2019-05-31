#Simple Linear Regression

import pandas as pd  
#import numpy as np
from sklearn.linear_model import LinearRegression
#from sklearn.model_selection import train_test_split 

movie_dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')

features_movie = movie_dataset.iloc[:, 0:1].values 
labels_movie = movie_dataset.iloc[:, 1:].values 

#features_train_m, features_test_m, labels_train_m, labels_test_m = train_test_split(features_movie, labels_movie, test_size=0.00001, random_state=0)

regressor_m = LinearRegression()  
regressor_m.fit(features_movie, labels_movie)
#labels_pred_m = regressor.predict(features_test_m)
#df_m = pd.DataFrame({'Actual': labels_test_m[0], 'Predicted': labels_pred_m[0]})

print(regressor_m.predict(10))

