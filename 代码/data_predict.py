import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

"""
该部分为预测模型,此处选择的是随机森林分类模型,期望构建的机器学习模型在学习过训练集后，能很好的完成对测试集的预测
"""

df = pd.read_csv('D:\编程文件夹\《大数据处理课程设计》\Heart-Disease-Analysis\数据集\heart_disease_preprocessed1.csv')

print(df.shape)
print(df.dtypes)

X = df.drop('诊断结果', axis=1)
print(X.shape)

y = df['诊断结果']
print(y.shape)

#  五分之一作为测试集，五分之四作为训练集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

print(X_train.shape)
print(X_test.shape)

model = RandomForestClassifier(max_depth=5, n_estimators=100, random_state=5)  # 100棵决策树
model.fit(X_train, y_train)

# 单个个体预测
print(X_test.iloc[2])
test_sample = X_test.iloc[2]
print(test_sample.shape)
test_sample = np.array(test_sample).reshape(1, -1)

print(test_sample)

# 预测是否会患有心脏病，给出一个结果
print(model.predict(test_sample))

# 分别预测不患心脏病的概率和患心脏病的概率
print(model.predict_proba(test_sample))

#  多个案例同时预测
print(model.predict(X_test))
print(model.predict_proba(X_test))
