#Space Separated Data

import numpy as np

inp=input("Enter the space separated numbers").split()
lst1=[]
for val in inp:
    val = int(val)
    lst1.append(val)
x = np.array( lst1 ) 
x = x.reshape(3,3)
print (x)

