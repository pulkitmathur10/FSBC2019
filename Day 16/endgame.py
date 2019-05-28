#Endgame Box Office
import matplotlib.pyplot as plt
import pandas as pd  
#import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 

E = pd.read_csv('endgame.csv')

E['Gross'] = E['Gross'].str.replace('$', '')
E['Gross'] = E['Gross'].str.replace(',', '')
E['Gross'] = E['Gross'].astype(int)

E['Gross-to-Date'] = E['Gross-to-Date'].str.replace('$', '')
E['Gross-to-Date'] = E['Gross-to-Date'].str.replace(',', '')
E['Gross-to-Date'] = E['Gross-to-Date'].astype(int)

E['Avg_Theatre'] = E['Avg_Theatre'].str.replace('$', '')
E['Avg/Theatre'] = E['Avg/Theatre'].str.replace(',', '')
E['Avg/Theatre'] = E['Avg/Theatre'].astype(int)



#day = E.iloc[:,-1].values
#gross = E.iloc[:, -2].values
da = E.iloc[:,2:-2].values
gross = E.iloc[:, -2:-1].values

import statsmodels.api as sm

daym = sm.add_constant(day)

day_opt = day[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = gross, exog = day_opt).fit()
regressor_OLS.summary()






















features_train_e, features_test_e, labels_train_e, labels_test_e = train_test_split(day, gross, test_size=0.0001, random_state=0)

regressor_E = LinearRegression()  
regressor_E.fit(day, gross)

labels_pred_e = regressor_E.predict(features_test_e)
df_e = pd.DataFrame({'Actual': labels_test_e, 'Predicted': labels_pred_e})

plt.scatter(day, gross)

estimated_collection = regressor_E.predict(60)
