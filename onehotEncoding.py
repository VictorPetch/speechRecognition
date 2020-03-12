###For now it receives a dictionary, tokenize it and one hot encodes it###
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import csv
corpus = [
          'Can you bring me a coke please',
          'bring me a coke please',
          'I want some coke ',
          'Can I have a coke',
          'I want a coke',
          'Can you bring me a pepsi please',
          'bring me a pepsi please',
          'I want some pepsi',
          'I want a pepsi',
          'I would like a pepsi please',
          'I would like a coke please',
         ]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
header = np.asarray([vectorizer.get_feature_names()])
#print(vectorizer.get_feature_names())
X = X.toarray()
data = np.append(header,X,axis = 0)
destination = 'wordsTokens.csv'
with open(destination, mode='a') as f_file:
    f_file = csv.writer(f_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        f_file.writerow(row)
