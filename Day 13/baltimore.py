# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv('Baltimore_City_Employee_Salaries_FY2014.csv',header=0)


df['AnnualSalary'] = df['AnnualSalary'].astype(str)

df['AnnualSalary'] = df['AnnualSalary'].str.replace('$', ' ')

df['AnnualSalary'] = df['AnnualSalary'].astype(float)




group = df.groupby(['JobTitle'])['AnnualSalary']
aggr = group.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])


output = df.sort_values(['AnnualSalary'],ascending=0)
print (str(output.iloc[0,0])+" get the highest salary")


group = df.groupby(['JobTitle'])
group = group.keys().sort()


df['JobTitle'].value_counts()[0:10].plot('bar')
aggr.sort_values(['sum'],ascending=0,inplace=True)
print (str(aggr.index[0])+" job title spends the most")

aggr['sum'][0:10].plot('bar')

# List All the Agency ID and Agency Name
agency_name_id = df[['Agency','AgencyID']]
agency_name_id.drop_duplicates(inplace=True)

# Find all the missing Gross data in the dataset
df['GrossPay'].isnull().sum()
