# -*- coding: utf-8 -*-

import pandas as pd
from collections import Counter
import re
#import nltk
from collections import OrderedDict
#nltk.download('stopwords')
from nltk.corpus import stopwords

""" Using read/storing file in buffer string"""

with open('mercy.txt') as book:
    c= book.read()
c = re.sub('[^a-zA-Z]', ' ', c)
c=c.lower()
c=c.split()
c = [word for word in c 
      if not word 
      in set(stopwords.words('english'))]
count = Counter(c)
print(count)
k=sorted(count.items() , reverse=True,  key=lambda x: x[1])
print(k)

""" Using loop/readlines()"""

with open('mercy.txt') as theon:
    f = theon.readlines()
  
f = pd.DataFrame(f)

coun= OrderedDict()  
for i in range(0, 1457):
    review = re.sub('[^a-zA-Z]', ' ', f[0][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    for word in review:
        if word in coun:
            coun[word] +=1
        else:
            coun[word] = 1

print("Without Counter class", coun)    
kc=sorted(coun.items() , reverse=True,  key=lambda y: y[1])
print(kc)
        