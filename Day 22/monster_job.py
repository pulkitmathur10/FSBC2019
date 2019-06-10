# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

dataset = pd.read_csv('monster_com-job_sample.csv')

od = dataset['organization'].value_counts()

od1 = od.drop(labels = ['Dallas, TX', 'Chicago, IL', 'Cincinnati, OH', 'Houston, TX', 'Redmond, WA', 'Plano, TX', 'San Jose, CA 95134', 'Atlanta, GA', 'Abbott Park, IL 60064', 'San Francisco, CA', 'Northbrook, IL 60062', 'Warren, IL 60064', 'Irving, TX', ])

ld = dataset['location'].value_counts()

def reg_l(loc):
    re.findall(r'^[A-Za-z]*\,{1}\s[A-Z]{2}', loc)
df1=pd.DataFrame()    
dataset['location_clean'] = dataset['location'].apply(lambda x: reg_l(x))
dataset1 = dataset.drop(labels = data)