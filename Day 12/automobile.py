#Exploratory Data Analysis - Automobile

import pandas as pd
import numpy as np

df1 = pd.read_csv('automobile.csv')

#Handling NaN price values
df1['price'] = df1['price'].fillna(df1['price'].mean())

data = np.array(df1['price'])

print(data.mean())
print(data.min())
print(data.max())
