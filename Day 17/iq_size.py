#IQ Size

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#from sklearn.preprocessing import PolynomialFeatures
#from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


iq_dataset = pd.read_csv('iq_size.csv')

features_iq = iq_dataset.iloc[:, 1:].values
iq = iq_dataset.iloc[:, 0].values

features_iq = sm.add_constant(features_iq)


regressor_iq = sm.OLS(endog = iq, exog = features_iq).fit()
print(regressor_iq.summary())
print("\nWeight is not much significant here.")

features_opt = features_iq[:, [0, 1, 2]]
regressor_iq = sm.OLS(endog = iq, exog = features_opt).fit()
print(regressor_iq.summary())

x = np.array([1,90,70])
x = x.reshape(1, -1)
iq = regressor_iq.predict(x)
print("The IQ of the given person is:", iq)
