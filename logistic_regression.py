import pandas as pd
import numpy as np
import random
from sklearn import utils
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn import metrics
import csv

#Reading all the data and training model

clf = LogisticRegression()
train_all = pd.DataFrame()
test_all = pd.DataFrame()

#positions
for i in range(1, 2):
    for j in range(1, 6):
        train = pd.read_csv(str('data/position' + str(i) + '/subject' + str(j) + '/train.csv'), header = None)
        train_all = train_all.append(train)
        test = pd.read_csv(str('data/position' + str(i) + '/subject' + str(j) + '/test.csv'), header = None)
        test_all = test_all.append(test)
        try:
            exec('train_p' + str(i) + '_s' + str(j) + ' = train')
            #Train the data
            exec('train_p' + str(i) + '_s' + str(j) + '= utils.shuffle(train)')
            exec('clf.fit(train_p' + str(i) + '_s' + str(j) + '.iloc[:,1:], train_p' + str(i) + '_s' + str(j) + '.iloc[:,0])')
            exec('test_p' + str(i) + '_s' + str(j) + ' = test')
        except IOError:
            print("IOError occurred at ", i, j)
joblib.dump(clf, 'activity_recognizer_model.pkl')

#print(train_all.shape)
#print(test_all.shape)

sample_test = pd.DataFrame()
for i in range(1, 2):
    for j in range(6, 7):
        test_sample = pd.read_csv(str('data/position' + str(i) + '/subject' + str(j) + '/test.csv'), header = None)
        sample_test = sample_test.append(test_sample)

predicted_out = pd.DataFrame(clf.predict(sample_test.iloc[:, 1:]))
test_sample['predicted_output'] = predicted_out
test_sample.to_csv('temp.csv', index=False)
score = metrics.accuracy_score(predicted_out, sample_test.iloc[:, 0])
print("accuracy:   %0.3f" % score)

# predicted = pd.DataFrame(clf.predict(test_all.iloc[:,1:]))
# score = metrics.accuracy_score(predicted, test_all.iloc[:, 0])
# print("accuracy:   %0.3f" % score)


