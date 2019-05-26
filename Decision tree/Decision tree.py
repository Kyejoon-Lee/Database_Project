import csv
import numpy as np
import pandas as pd
from sklearn.tree import export_graphviz
import matplotlib.pylab as plt
from IPython.display import display
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
name = []
def data_load(dana_name, tr_te):
    y = []
    x = []
    if dana_name == 'data':
        if(tr_te == 'Spam_train'):
            file = './data/spam_train.csv'
        elif(tr_te == 'Spam_test'):
            file = './data/Spam_test.csv'

        with open(file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            num =0
            for row in csv_reader:
                if num ==0:
                    name.append(row)
                    num = num+1
                else:
                    y.append(int(row[57]))
                    feature = []
                    feature += list(map(float, row[0:57]))
                    x.append(feature)

    return np.array(x), np.array(y)

X,Y = data_load('data','Spam_train')
X_t, Y_t = data_load('data','Spam_test')
X_train = pd.DataFrame(X)
Y_train = pd.DataFrame(Y)
X_test = pd.DataFrame(X_t)
Y_test = pd.DataFrame(Y_t)
Y_test.columns = ['real']

from sklearn import tree
from sklearn.metrics import precision_score, f1_score, recall_score

clf = tree.DecisionTreeClassifier(max_depth=100,max_leaf_nodes=50)
clf = clf.fit(X_train,Y_train)
predict = pd.DataFrame(clf.predict(X_test))
predict.columns = ['predict']
export_graphviz(clf, out_file="tree1.dot", class_names=["ham", "spam"],
                impurity=False, filled=True)

import graphviz

with open("tree1.dot") as f:
    dot_graph = f.read()
dot = graphviz.Source(dot_graph)
dot.format ='png'
dot.render(filename='tree.png')

ct = pd.crosstab(Y_test['real'],predict['predict'])
print("특성 중요도:\n{}".format(clf.feature_importances_))
'''
f = open('result.csv','w')
wr = csv.writer(f)
wr.writerow(clf.feature_importances_)

f.close()
'''
print(ct)
prec = precision_score(Y_test['real'],predict['predict'])
print(prec)
rec = recall_score(Y_test['real'],predict['predict'])
print(rec)
f1 = f1_score(Y_test['real'],predict['predict'])
print(f1)
'''
n_features = name
plt.barh(range(57), clf.feature_importances_, align='center')
plt.yticks(range(57), name[0])
plt.xlabel("Importance of attribute")
plt.ylabel("Attribute")
plt.ylim(-1)
plt.show()
'''