# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('Dating_Data.csv', encoding = 'windows 1252')

df1 = df.dropna(subset=['attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1'])

df1m = df1[df1['gender']==1][['attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1']]
df1f = df1[df1['gender']==0][['attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1']]

attr = df1f['attr1_1'].mean()
sinc = df1f['sinc1_1'].mean()
intel =df1f['intel1_1'].mean()
fun = df1f['fun1_1'].mean()
amb = df1f['amb1_1'].mean()
shar = df1f['shar1_1'].mean()


import matplotlib.pyplot as plt

labelm = ['attr', 'sinc', 'intel', 'fun', 'amb', 'shar']
val = [attr, sinc, intel, fun, amb, shar]
val = [float(x) for x in val]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange', 'red']
explode = (0, 0, 0, 0, 0, 0)
plt.pie(val, explode=explode, labels=labelm, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


df2 = df.dropna(subset=['attr2_1', 'sinc2_1', 'intel2_1', 'fun2_1', 'amb2_1', 'shar2_1'])

df2f = df2[df2['gender']==0][['attr2_1', 'sinc2_1', 'intel2_1', 'fun2_1', 'amb2_1', 'shar2_1']]