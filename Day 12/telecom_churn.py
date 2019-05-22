#Telecom Churn Analysis

import pandas as pd
import matplotlib.pyplot as plt

df2 = pd.read_csv('Telecom_churn.csv')

df21 = df2[(df2['international plan'] == 'yes') & (df2['voice mail plan'] == 'yes') & (df2['churn'] == True) ]
df2_a = df21['state'].shape

df2_sum = df2['total intl charge'].sum()
df221 = df2[df2['churn'] == True][['total intl charge']]
df221_sum = float(df221.sum())
df222 = df2[df2['churn'] == False][['total intl charge']]
df222_sum = float(df222.sum())
sizes = [df221_sum, df222_sum]
labels = 'Churned', 'Non Churned'
colors = ['gold', 'yellowgreen']
explode = (0.1, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)


df23 = df2[df2['churn'] == True][['total night minutes', 'state']]
dfm = float(df23['total night minutes'].max())
df23_state = df23[df23['total night minutes'] == dfm][['state']]


df24 = df2[df2['churn']==True][['total day calls', 'total eve calls', 'total night calls']]

temp = df24.max()
print(temp[1])

sizes = [float(temp[0]), float(temp[1]), float(temp[2])]
labels = 'Day Calls', 'Evening Calls', 'Night Calls'
colors = ['gold', 'yellowgreen', 'blue']
explode = (0, 0.1, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)
