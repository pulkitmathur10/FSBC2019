#SSA Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


main_df = pd.DataFrame()

for i in range(1880, 2011):
    temp1 = pd.read_csv('yob' + str(i) +'.txt', header=None)
    temp1.columns= ['Name', 'Gender', 'Number']
    temp1['Year'] = i
    main_df = pd.concat([main_df, temp1])

df_males = main_df[(main_df['Gender'] == 'M')  & (main_df['Year']==2010) ][['Name']]
df_males['Name'].value_counts().head(5)

df_females = main_df[(main_df['Gender'] == 'F')  & (main_df['Year']==2010)][['Name']]
df_females['Name'].value_counts().head(5)

temp3 = main_df[(main_df['Gender'] == 'M') ][['Number']]
sum_m=temp3.sum()
print("Total male births" , sum_m[0])

temp4 = main_df[(main_df['Gender'] == 'F')][['Number']]
sum_f=temp4.sum()
print("Total female births" , sum_f[0])

fig, ax = plt.subplots()
main_df.groupby('Gender').plot(x='Year', y='Number', ax=ax, legend=False)
main_df.plot(x='Year', y='Number')

