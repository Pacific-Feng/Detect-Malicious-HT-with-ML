import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('CHIP_Feather_File.csv')
#df.shape:(173102, 8)
#df.size:1384816
#df.count():To count each different column of row
#df['Trojan_Flag'].value_counts() :To get the specific numberof member of that label 
df.head()

TF_NET_df = df[df['Trojan_Flag']==0][0:200]
TI_NET_df = df[df['Trojan_Flag']==1][0:200]

axes = TI_NET_df.plot(kind='scatter' , x='LGFI' , y='FFi' , color='r' , label = 'TI')
TF_NET_df.plot(kind='scatter' , x='LGFI' , y='FFi' , color='b' , label = 'TF' , ax = axes)

df.dtypes # Module_Name is object

#df.columns
Feature_df = df[['LGFI', 'FFi', 'FFo', 'PI', 'PO']]

#independent variable
X = np.asarray(Feature_df)

#dependent variable
y = np.asarray(df['Trojan_Flag'])

#x[0:5]
Feature_df.head()

#import sklearn
from sklearn.model_selection import train_test_split

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.3 , random_state=0)
#X_train.shape:(138481, 5)
#y_train.shape:(138481,1)
#X_test.shape:(34621, 5)
#y_test.shape:(34621, 1)

from sklearn import svm
from sklearn.model_selection import GridSearchCV 


parameter = {'kernel':('linear','rbf'),'C':[0.001,0.01,1,10,100],'gamma':[0.001,0.01,1,10,100]}
clf = svm.SVC(random_state=0)
grid = GridSearchCV(clf,parameter)
#clf = svm.SVC(kernel='rbf' , gamma ='auto' , C=1)
grid_result = grid.fit(X_train,y_train)
y_predict = grid.predict(X_test)
#print(y_predict)
# 評估，打分數
print(f"最佳準確率: {grid_result.best_score_}，最佳參數組合：{grid_result.best_params_}")
# 取得 cross validation 的平均準確率及標準差
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print(f"平均準確率: {mean}, 標準差: {stdev}, 參數組合: {param}")

from sklearn.metrics import classification_report

print(classification_report(y_test,y_predict))