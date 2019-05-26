#E-commerce Data Exploration

import numpy as np
import matplotlib.pyplot as plt
 
 
incomes = np.random.normal(100.0, 20.0, 10000)
plt.hist(incomes, bins=50)
print(np.mean(incomes))
print(np.median(incomes))
outliers= np.random.randint(950, 1000, 100)
incomes=np.append(incomes, outliers)

plt.hist(incomes, bins=50)
print(np.mean(incomes))
print(np.median(incomes))