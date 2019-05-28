# Bluegill Fish

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


dataset_fish = pd.read_csv('bluegills.csv')

age = dataset_fish.iloc[:, 0:1].values
length = dataset_fish.iloc[:, 1].values

poly_object = PolynomialFeatures(degree = 5)
age_poly = poly_object.fit_transform(age)


lin_reg_h = LinearRegression()
lin_reg_h.fit(age_poly, length)


plt.scatter(age, length, color = 'red')
plt.plot(age, lin_reg_h.predict(poly_object.fit_transform(age)), color = 'blue')
plt.title('Fish Length')
plt.xlabel('age')
plt.ylabel('length')
plt.show()

x = np.array([5])
x = x.reshape(1, -1)

x_poly = poly_object.transform(x)

lin_reg_h.predict(x_poly)










#plt.scatter(age, length, color = 'red')
#plt.plot(age, length, color = 'blue')
#plt.title('Linear Regression')
#plt.xlabel('Age')
#plt.ylabel('Length')
#plt.show()