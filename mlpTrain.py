###TRAINING MLP TO COMPREEND TEXT MEANING###
import numpy as np 
import pandas as pd 

dataset = pd.read_csv('wordsTokens.csv')
print('dataset shape: ', dataset.shape)
