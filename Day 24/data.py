# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data.csv')

df1 = dataset.dropna(subset=['Country'])

df2 = df1['Country'].str.split("|", n=0, expand=True)

df3 = df2[0]

lst0 = list(df2[0])
lst1 = list(df2[1])
lst2 = list(df2[2])

lst1 = [i for i in lst1 if i] 
lst2 = [i for i in lst2 if i]

lst = lst0 + lst1 + lst2

pdata = pd.Series(lst)
x = np.array(pdata.value_counts().index)

#x.plot.pie(y=x.index,
#           shadow=False,
#           startangle=90,
#           autopct='%1.1f%%', labeldistance=1.2)
#
#plt.axis('equal')
#plt.tight_layout()
#plt.show()

y = np.array(pdata.value_counts())
porcent = 100.*y/y.sum()

patches, texts = plt.pie(y, startangle=90, radius=1.2)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]

sort_legend = True
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
                                          key=lambda x: x[2],
                                          reverse=True))

plt.legend(patches, labels, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)

plt.savefig('piechart.png', bbox_inches='tight')
plt.axis('equal')
plt.tight_layout()
plt.show()

#fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
#def func(pct, allvals):
#    absolute = int(pct/100.*np.sum(allvals))
#    return "{:.1f}%\n({:d} g)".format(pct, absolute)
#
#
#wedges, texts, autotexts = ax.pie(y, autopct=lambda pct: func(pct, y),
#                                  textprops=dict(color="w"))
#
#ax.legend(wedges, x,
#          title="Ingredients",
#          loc="center left",
#          bbox_to_anchor=(1, 0, 0.5, 1))
#
#plt.setp(autotexts, size=8, weight="bold")
#
#ax.set_title("Matplotlib bakery: A pie")
#
#plt.show()