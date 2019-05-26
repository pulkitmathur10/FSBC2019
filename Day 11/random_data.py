#Random Data

import numpy as np 
from collections import Counter

random_nos =np.random.randint(5, 15, 40)
count_freq=Counter(random_nos)
print(count_freq.most_common()[0][0])

#With Numpy
most_freq = np.bincount(random_nos).argmax()
print("Most Frequent using Numpy:", most_freq)