# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('election.csv')

df1 = dataset.groupby('State')['Constituency', 'Party', '%' ]

df2 = df1.groupby('Constituency')['Party', '%']

#df= dataset[['State','Constituency', 'Party', '%']]

x=pd.DataFrame([dataset['State'].value_counts()])

y=dataset[dataset['State']== 'Rajasthan'][['Constituency', '%', 'Party']]
y1 = y.groupby('Constituency')['Party', '%', 'Constituency']
z =pd.DataFrame([y['Constituency'].value_counts()])

par = []
per=[]
con=[]
for cons in z.columns:
    temp = y1.get_group(cons)
    m = temp['%'].max()
    o=temp[temp['%'] == m][['Party', 'Constituency']]
    o.index= range(1)
    par.append(o['Party'][0])
    per.append(m)
    con.append(cons)
    
raj_win = pd.DataFrame(zip(con, par, per))
raj_win.columns = ['Constituency','Party','%']

index = list(raj_win.index)
plt.bar(index, per)
plt.xticks(index, con, fontsize=10, rotation=90)
plt.show()




sum1 = raj_win[raj_win['Party'] == 'Bharatiya Janata Party']['%']
sum1 = sum1.sum()
sum2 = raj_win[raj_win['Party'] == 'Rashtriya Loktantrik Party']['%'].sum()

plt.pie([sum1,sum2], labels=['BJP', 'RLP'], colors = ['orange', 'blue'])