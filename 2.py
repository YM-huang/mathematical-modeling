import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score,classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

pd.set_option('display.max_columns',None)
#导入数据

data_train1 = pd.read_csv('数据.csv', encoding='utf8', engine='python')
data_label1 = pd.read_csv('train_label.csv', encoding='utf8', engine='python')
data_train = pd.merge(data_train1,data_label1,how = 'right',on='ID')

# data_train.head()

data_train.drop(['H','I','J','K','L','M','N','O','P'],axis=1,inplace=True)
#构建新字段：近三月平均语音超套金额A1、近三月平均流量超套金额A2、近三月平均流量饱和度A3
data_train['A1'] = data_train[['T','U','V']].mean(axis=1)
data_train['A2'] = data_train[['W','X','Y']].mean(axis=1)
data_train['A3'] = data_train[['AJ','AK','AL']].mean(axis=1)
#删除原字段
data_train.drop(['T','U','V','W','X','Y','AJ','AK','AL'],axis=1,inplace=True)
#删除用户号码和宽带信息
data_train.drop(['NUM','Z','AA','AB','AC'],axis=1,inplace=True)
# 无重复值
data_train[data_train.duplicated()]
data_train.info()
#查看缺失值信息
data_train[pd.isna(data_train['XJ'])]
#查看缺失值的X4字段信息
data_train[pd.isna(data_train['XJ'])]['YEAR'].describe()
#X3字段缺失值填充为0
data_train['XJ'].fillna(0,inplace=True)
#分组查看各用户类别数量
data_train[['ID','TYPE']].groupby('TYPE').count()
#填充缺失值为众数
data_train['TYPE'].fillna('大众用户',inplace=True)
data_train['AN'].fillna(0,inplace=True)

#查看剩余缺失值的数据分布
data_train[['Q','R','S','AD','AE','AF','AG','AH','AI','A1','A2','A3']].describe()

#根据各字段的数据分布填充缺失值为均值、中位数或众数
mean_cols = ['Q','R','S','A1']
median_cols = ['AD','AE','AF','AG','A2','A3','AH','AI']
mode_cols = ['AH','AI']
for col in mean_cols:
    data_train[col].fillna(data_train[col].mean(),inplace=True)
for col in median_cols:
    data_train[col].fillna(data_train[col].median(),inplace=True)
# for col in mode_cols:
#     data_train[col].fillna(data_train[col].mode(),inplace=True)

# data_train.info()
# print(data_train)


label = LabelEncoder()
data_train['SEX'] = label.fit_transform(data_train['SEX'])
data_train['TYPE'] = label.fit_transform(data_train['TYPE'])

data_train.head()

del data_train['AI']
#独热编码
data_train = data_train.join(pd.get_dummies(data_train['SEX'], prefix='SEX_'))
data_train = data_train.join(pd.get_dummies(data_train['TYPE'], prefix='TYPE_'))
#删除原特征列
del data_train['SEX']
del data_train['TYPE']


#标准化转换器
transfer = StandardScaler()
a = transfer.fit_transform(data_train[['Q','R','S','AH','AN','A1','A2','A3']])
data_train = pd.concat([data_train,pd.DataFrame(a,columns=['Q_s','R_s','S_s','AH_s','AN_s','A1_s','A2_s','A3_s'])],axis=1)
data_train.head()
#删除原有列
data_train.drop(['Q','R','S','AH','AN','A1','A2','A3'],axis=1,inplace=True)

data_train.info()

#划分数据集
x_train,x_test,y_train,y_test = train_test_split(data_train.iloc[:,-1:],data_train['label'],test_size=0.3,random_state=6)

# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

# #逻辑回归模型训练
# estimator_log = LogisticRegression()
# estimator_log.fit(x_train, y_train)
# #模型评估
# score_log = estimator_log.score(x_test, y_test)
# y_pred = estimator_log.predict(x_test)
# report_log = classification_report(y_test,y_pred, labels=[0, 1], target_names=['not 5Ger', '5Ger'])
# auc_log = roc_auc_score(y_test, y_pred)
# print('逻辑回归的准确率为%.4f' % score_log,
#      '\n精确率、召回率及F1-score为：\n',report_log,
#      '\nAUC指标为%.4f' % auc_log)



#决策树模型
estimator_tree = DecisionTreeClassifier()
estimator_tree.fit(x_train,y_train)
#模型评估
score_tree = estimator_tree.score(x_test,y_test)
y_pred = estimator_tree.predict(x_test)
report_tree = classification_report(y_test,y_pred,labels=[0,1],target_names=['不是5G用户','是5G用户'])
auc_tree = roc_auc_score(y_test,y_pred)
print('决策树模型的准确率为%.4f' % score_tree,
     '\n精确率、召回率及F1-score为：\n',report_tree,
     '\nAUC指标为%.4f' % auc_tree)


# #决策树参数优化
# estimator_tree = DecisionTreeClassifier()
# param_dict_tree = {'max_depth':range(1,11)}
# estimator_tree = GridSearchCV(estimator_tree,param_grid=param_dict_tree,cv=10)
# estimator_tree.fit(x_train,y_train)
# score_tree = estimator_tree.score(x_test,y_test)
# y_pred = estimator_tree.predict(x_test)
# report_tree = classification_report(y_test,y_pred,labels=[0,1],target_names=['不是5G用户','是5G用户'])
# auc_tree = roc_auc_score(y_test,y_pred)
# print('决策树模型的最优参数为：',estimator_tree.best_params_,
#      '\n决策树模型优化后的准确率为%.4f' % score_tree,
#      '\n精确率、召回率及F1-score为：\n',report_tree,
#      '\nAUC指标为%.4f' % auc_tree)

