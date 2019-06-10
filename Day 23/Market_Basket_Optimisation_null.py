# -*- coding: utf-8 -*-

import pandas as pd
from apyori import apriori
import numpy as np
# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv')


def cart(items):
    tmp_cart = list(set(items))
    if np.nan in tmp_cart:
        tmp_cart.remove(np.nan)
    return tmp_cart

transactions = list(dataset.apply(cart, axis=1))

rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
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








