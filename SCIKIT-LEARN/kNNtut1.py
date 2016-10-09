import numpy as np 
import pandas as pd 
from sklearn.preprocessing import scale
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('BreastCancer.txt')
df.replace('?', -99999, inplace = True)
df.drop(['id'],1, inplace = True)

feature_set = np.array(df.drop(['class'],1))
label_set   = np.array(df['class'])

x_train, x_test, y_train, y_test = train_test_split(feature_set, label_set,test_size = 0.2)

clf = KNeighborsClassifier()
clf.fit(x_train, y_train)

accuracy = clf.score(x_test, y_test)
print(accuracy)