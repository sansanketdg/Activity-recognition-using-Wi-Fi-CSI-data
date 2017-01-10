import pandas as pd
from sklearn.svm import SVC
from sklearn import metrics

## READ DATA

#load training-set
train_path = 'data_2/position1/subject1/SVM/SVM.csv'

with open(train_path, 'r') as f:
    data_buffer1 = pd.read_csv(f, header=None, skiprows=0)

labels = data_buffer1[0]
features = data_buffer1.iloc[:,1:78]
#print(features)

X = features.values.tolist()
Y = labels.values.tolist()

'''
#load training-set
train_path = 'data_2/position1/subject2/SVM/SVM.csv'
train_path_2 = 'data_2/position1/subject1/SVM/SVM.csv'
#train_path_3 = 'data_2/position2/subject1/SVM/SVM.csv'
train_path_4 = 'data_2/position3/subject1/SVM/SVM.csv'
train_path_4 = 'data_2/position4/subject1/SVM/SVM.csv'
train_path_5 = 'data_2/position5/subject1/SVM/SVM.csv'

with open(train_path, 'r') as f:
    data_buffer1 = pd.read_csv(f, header=None, skiprows=0)

labels = data_buffer1[0]
features = data_buffer1.iloc[:,1:78]

temp_X = features.values.tolist()
temp_Y = labels.values.tolist()

X.extend(temp_X)
Y.extend(temp_Y)

with open(train_path_2, 'r') as f:
    data_buffer2 = pd.read_csv(f, header=None, skiprows=0)

labels = data_buffer2[0]
features = data_buffer2.iloc[:,1:78]

temp_X = features.values.tolist()
temp_Y = labels.values.tolist()

X.extend(temp_X)
Y.extend(temp_Y)

# with open(train_path_3, 'r') as f:
#     data_buffer3 = pd.read_csv(f, header=None, skiprows=0)
#
# labels = data_buffer3[0]
# features = data_buffer3.iloc[:,1:78]
#
# temp_X = features.values.tolist()
# temp_Y = labels.values.tolist()
#
# X.extend(temp_X)
# Y.extend(temp_Y)

with open(train_path_4, 'r') as f:
    data_buffer4 = pd.read_csv(f, header=None, skiprows=0)

labels = data_buffer4[0]
features = data_buffer4.iloc[:,1:78]

temp_X = features.values.tolist()
temp_Y = labels.values.tolist()

X.extend(temp_X)
Y.extend(temp_Y)

with open(train_path_5, 'r') as f:
    data_buffer5 = pd.read_csv(f, header=None, skiprows=0)

labels = data_buffer5[0]
features = data_buffer5.iloc[:,1:78]

temp_X = features.values.tolist()
temp_Y = labels.values.tolist()

X.extend(temp_X)
Y.extend(temp_Y)
'''

clf = SVC()
clf.fit(X, Y)

#load test-set
test_path = 'data_2/position1/subject2/SVM/SVM.csv'

with open(test_path, 'r') as f:
    data_buffer2 = pd.read_csv(f, header=None, skiprows=0)

labels_test = data_buffer2[0]
features_test = data_buffer2.iloc[:, 1:78]

X_test = features_test.values.tolist()
Y_test = labels_test.values.tolist()

Y_predicted = clf.predict(X_test)

score = metrics.accuracy_score(Y_predicted, Y_test)
print("accuracy:   %0.3f" % score)

# print(Y_test)
# print(Y_predicted)

# print(labels_test[0:5])
# print(features_test[0:5])

# print(labels[1:10])
# print(labels_predicted[1:10])