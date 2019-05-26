#Telecom Churn Analysis

import pandas as pd
#import matplotlib.pyplot as plt

df2 = pd.read_csv('Telecom_churn.csv')

churned_df = df2[df2['churn'] == True]


df21 = df2[(df2['international plan'] == 'yes') & (df2['voice mail plan'] == 'yes') & (df2['churn'] == True) ]
df2_a = df21['state'].shape
print(df2_a)
df2_sum = df2['total intl charge'].sum()
print(df2_sum)

df221_sum = float(churned_df['total intl charge'].sum())
df222_sum = float(df2[df2['churn'] == False][['total intl charge']].sum())
intl_chrge = pd.DataFrame({'intl calls':['Churned', 'Not Churned'], 'val':[df221_sum, df222_sum]})
xpl=intl_chrge.plot.bar(x='intl calls', y='val', rot=0)


df23 = churned_df[['total night minutes', 'state']]
dfm = float(df23['total night minutes'].max())
df23_state = df23[df23['total night minutes'] == dfm][['state']]


call_pop=churned_df.iloc[:, 7:19].sum().sort_index()
call_pop.plot.bar()

churn_acc = churned_df['account length'].max()
nchurn_acc = df2[df2['churn']== False]['account length'].max()

if(churn_acc>nchurn_acc):
    print("Churned Customers have maximum acc length")
else:
    print("Non Churned Customers have maximum acc length")    


cust_calls = churned_df['customer service calls'].value_counts()
ypl=cust_calls.plot.bar(rot=0)

#df24 = df2.groupby('area code')['international plan'].value_counts()




temp1 = df2[df2['international plan'] == 'yes']['area code'].value_counts()
temp1 = pd.DataFrame(temp1)
temp1.reset_index(level=0, inplace=True)
y=temp1['area code'].max()
area_intl = temp1[temp1['area code']==y]['index'][0]
print("Area code with most international calls:", area_intl)


