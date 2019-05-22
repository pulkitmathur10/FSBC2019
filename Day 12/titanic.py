#Titanic Analysis

import pandas as pd
import numpy as np

df = pd.read_csv('training_titanic.csv')
#Survivors
surv_lst = df['Survived'].value_counts().tolist()
print("No of survivors:" , surv_lst[1])

#Deaths
print("No of deaths:" , surv_lst[0])

#Percentage Death(0) and Survival(1)
print(df['Survived'].value_counts(normalize = True))

#Males passed away vs Survived

df_males = df[df['Sex'] == 'male' ][['Survived']]
surv_male = df_males['Survived'].value_counts().tolist()
print("No of male survivors:" , surv_male[1])
print("No of male deaths:" , surv_male[0])
print(df_males['Survived'].value_counts(normalize = True).tolist())

#Females passed away vs Females Survived

df_females = df[df['Sex'] == 'female' ][['Survived']]
surv_females = df_females['Survived'].value_counts().tolist()
print("No of female survivors:" , surv_females[1])
print("No of female deaths:" , surv_females[0])

print(df_females['Survived'].value_counts(normalize = True))


def age_div(x):  
    if (x >= 18) :
        return 0
    elif (x<18) :
        return 1   


df["Child"] = df["Age"].apply(age_div)
df_child = df[df['Child'] == 1 ][['Survived']]
surv_age = df_child['Survived'].value_counts().tolist()
print("No of child survivors:" , surv_age[1])
print("No of child deaths:" , surv_age[0])
