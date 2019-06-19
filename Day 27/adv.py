# -*- coding: utf-8 -*-

import json
import pandas as pd
import requests
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import re
#import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

url1 = 'http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json'
response1 = requests.get(url1).text
train = pd.read_json(response1, lines = True)

url2 = 'http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json'
response2 = requests.get(url2).text
test = pd.read_json(response2, lines = True)

features_train = train.iloc[:, 1:].values
features_train1 = train.iloc[:, 1:]
label_train = train['category'].values

features_test = test.iloc[:,:]
features_test1 = test.iloc[:,:]
corpus=[]
for i in range(0, 20217):
    review = re.sub('[^a-zA-Z]', ' ', features_train['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features_train['heading'] = cv.fit_transform(corpus).toarray()

features_train = features_train.values

ls = [0,1]
list1=[]
for ob in ls:
    labelencoder = LabelEncoder()
    features_train[:,0] = labelencoder.fit_transform(features_train[:, 0])
    features_train[:,2] = labelencoder.fit_transform(features_train[:, 2])
    list1.append(labelencoder)
onehotencoder = OneHotEncoder(categorical_features = [0,2])
features_train = onehotencoder.fit_transform(features_train).toarray()

cols_feat=[0,2]
total_col, indexes = 0, []
for col in cols_feat:
    unique_val_count = len(features_train1.iloc[:,col].value_counts())
    total_col += unique_val_count
    indexes.append(total_col - unique_val_count)
features_train = np.delete(features_train, indexes, axis=1)


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, label_train)


corpus1=[]
for j in range(0, 15370):
    review1 = re.sub('[^a-zA-Z]', ' ', features_test['heading'][j])
    review1 = review1.lower()
    review1 = review1.split()
    review1 = [word for word in review1 if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review1 = [ps.stem(word) for word in review1]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review1 = ' '.join(review1)
    corpus1.append(review1)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features_test['heading'] = cv.transform(corpus1).toarray()

features_test = features_test.values
labelencoder1 = LabelEncoder()
labelencoder2 = LabelEncoder()
features_test[:,0] = labelencoder1.fit_transform(features_test[:, 0])
features_test[:,2] = labelencoder2.fit_transform(features_test[:, 2])

onehotencoder = OneHotEncoder(categorical_features = [0,2])
features_test = onehotencoder.transform(features_test).toarray()

cols_feat=[0,2]
total_col1, indexes = 0, []
for col in cols_feat:
    unique_val_count1 = len(features_test1.iloc[:,col].value_counts())
    total_col1 += unique_val_count
    indexes.append(total_col1 - unique_val_count)
features_test = np.delete(features_test, indexes, axis=1)






label_pred = pd.DataFrame(classifier.predict(features_test))
from sklearn.metrics import confusion_matrix

classifier.score(features_train, label_train)


