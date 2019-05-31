# Female Stat Students

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt
import statsmodels.api as sm



dataset_female = pd.read_csv('Female_Stats.csv')  

features = dataset_female.iloc[:, 1:].values
labels = dataset_female.iloc[:, 0].values

features = sm.add_constant(features)


regressor_OLS = sm.OLS(endog = labels, exog = features).fit()

p = regressor_OLS.params

m = p[1]
f=p[2]
print("Increase in height for an inch increase in mother's height, when father's height is constant:" , m)
print("Increase in height for an inch increase in father's height, when mother's height is constant:" , f)