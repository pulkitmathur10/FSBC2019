# -*- coding: utf-8 -*-
import pandas as pd
import re

df = pd.read_csv('amazon_cells_labelled.txt', delimiter='\t', header=None)
df.columns = ['Review', 'Liked']

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer

corpus=[]
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', df['Review'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = df.iloc[:, 1].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_nb = confusion_matrix(labels_test, labels_pred)

classifier.score(features_test, labels_test)


from sklearn.svm import SVC
classifier1 = SVC(kernel = 'rbf', random_state = 0)
classifier1.fit(features_train, labels_train)


labels_pred1 = classifier1.predict(features_test)


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred1)


score = classifier1.score(features_test,labels_test)
corpus1 = []
inp = 'Amazing sound quality, great experience.'

review1 = re.sub('[^a-zA-Z]', ' ', inp)
review1 = review1.lower()
review1 = review1.split()
review1 = [word for word in review1 if not word in set(stopwords.words('english'))]

ps = PorterStemmer()
review1 = [ps.stem(word) for word in review1]
review1 = ' '.join(review1)
corpus1.append(review1)
