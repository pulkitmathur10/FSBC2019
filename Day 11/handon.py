#Mean, Median and Mode

import numpy as np


lst = [13, 18, 13, 14, 13, 16, 14, 21, 13]

val = np.array(lst)

print("Mean:", np.mean(val))
print("Median:" , np.median(val))
print("Mode:", np.bincount(val).argmax())
r = np.ptp(val, axis = 0)
print("Range:", r)
        
#temp={}
#for i in val:
#    if i in temp:
#        temp[i]+=1
#    else:
#        temp[i]=1
#       
#print("Mode:" ,max(temp, key=temp.get))

