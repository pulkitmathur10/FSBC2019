#BreadBasket_DMS

import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt
# Data Preprocessing
dataset = pd.read_csv('BreadBasket_DMS.csv')
dataset1 = dataset[dataset.Item != 'NONE']
item_freq = dataset1.Item.value_counts()

top15 = item_freq.head(15)


top15.plot.pie(y=top15.index,
           shadow=False, 
           startangle=90,
           autopct='%1.1f%%')

plt.axis('equal')
plt.tight_layout()
plt.show()

def cart(items):
    tmp_cart = list(set(items))
    return tmp_cart

df = list(dataset1.groupby('Transaction')['Item'].apply(cart))

rules = apriori(df, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)
results = list(rules)

for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
