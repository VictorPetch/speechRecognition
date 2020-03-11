###One Hot Encoding the csv###
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder
import numpy as np
enc = OneHotEncoder(handle_unknown='ignore')
#print(np.asarray(X).shape)
X = [['bring', 'me','a','coke','please'],['coke', 'please','can','i','have'],['i', 'would','like','a','coke']]
#X = X.reshape(-1,1)
#print(X.shape)
enc.fit(X)
print(enc.categories_[1])
print(enc.transform(X).toarray())