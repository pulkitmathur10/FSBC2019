# Normally Distributed Random Data

import numpy as np
import matplotlib.pyplot as plt

rd = np.random.normal(150.0, 20.0, 1000)
plt.hist(rd, bins=100)
print(np.std(rd))
print(np.var(rd))
