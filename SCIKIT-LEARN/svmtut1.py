import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import cross_validation
from sklearn import preprocessing
from sklearn import svm

# df = pd.read_csv('BreastCancer.txt')
# df.replace('?',-99999,inplace = True)
# df.drop(['id'],1,inplace = True)
# feature_set = np.array(df.drop(['class'],1))
# label_set = np.array(df['class'])

# df = pd.read_csv('~/DevCode/AI/ML/Datasets/Fisher.csv')
# feature_set = np.array(df.drop(['Type'],1))
# label_set = np.array(df['Type'])

x_train, x_test, y_train, y_test = cross_validation.train_test_split(feature_set, label_set, test_size = 0.2)

clf = svm.SVC()
clf.fit(x_train, y_train)

accuracy = clf.score(x_test, y_test)
print(accuracy)