#Automobile

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Automobile.csv")

series = df["make"].value_counts()

explode = (0.1,0,0,0,0,0,0,0,0,0,0)

plt.pie(series.values[0:11], explode = explode, labels=series.index[0:11], autopct='%2.2f%%')
plt.axis('equal')

plt.show()


