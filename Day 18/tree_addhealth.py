#Classification Code Challenge
  
import pandas as pd


health = pd.read_csv('tree_addhealth.csv') 

for colname in health:
    health[colname] = health[colname].fillna(health[colname].mode()[0])


feat = health[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
           'DEP1','ESTEEM1']].values
label = health["TREG1"].values


from sklearn.model_selection import train_test_split
ftrain,ftest,ltrain,ltest = train_test_split(feat, label, test_size = 0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
ftrain = sc.fit_transform(ftrain)
ftest = sc.transform(ftest)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2)
classifier.fit(ftrain, ltrain)

probability = classifier.predict_proba(ftest)
labels_pred = classifier.predict(ftest)


from sklearn.metrics import confusion_matrix
cmat = confusion_matrix(ltest, labels_pred)

