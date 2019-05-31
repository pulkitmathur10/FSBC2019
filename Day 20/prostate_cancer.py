#Prostate Cancer

import pandas as pd
import sklearn
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

df = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter=' ')

features_p = df.drop('lpsa',axis = 1)
label_p = df['lpsa']


features_train_p, features_test_p, labels_train_p,labels_test_p = train_test_split(features_p, label_p, test_size=0.3, random_state=1)

sc = StandardScaler()
features_train_p = sc.fit_transform(features_train_p)
features_test_p = sc.transform(features_test_p)

lm = LinearRegression()
lm.fit(features_train_p, labels_train_p)

print (lm.score(features_test_p, labels_test_p))
print (lm.score(features_train_p, labels_train_p))

labels_pred = lm.predict(features_test_p)


df1 = pd.DataFrame({'Actual': labels_test_p, 'Predicted': labels_pred})  
print ( df1 )

from sklearn import metrics

print(metrics.mean_squared_error(labels_test_p, labels_pred))

lm_lasso = Lasso() 
lm_ridge =  Ridge() 


lm_lasso.fit(features_train_p, labels_train_p)
lm_ridge.fit(features_train_p, labels_train_p)

print (lm_lasso.score(features_test_p, labels_test_p))
print (lm_lasso.score(features_train_p, labels_train_p))

print (lm_ridge.score(features_test_p, labels_test_p))
print (lm_ridge.score(features_train_p, labels_train_p))

mean_lpsa = df.lpsa.mean()

label_pc = pd.DataFrame()
label_pc['lpsa'] = pd.Series(map(lambda x: 1 if x>=mean_lpsa else 0, label_pc['lpsa']))

features_train_p, features_test_p, labels_train_p,labels_test_p = train_test_split(features_p, label_pc, test_size=0.3, random_state=1)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train_p, labels_train_p)

labels_pred = classifier.predict(features_test_p)


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test_p, labels_pred)

from sklearn.metrics import accuracy_score 
 
print (accuracy_score(labels_test_p, labels_pred))

from sklearn.metrics import f1_score

print (f1_score(labels_test_p, labels_pred, pos_label=0)  )
print (f1_score(labels_test_p, labels_pred, pos_label=1)  )

