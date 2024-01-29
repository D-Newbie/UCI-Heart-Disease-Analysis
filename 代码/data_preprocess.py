"""
该部分内容为数据预处理
在这一部分完成了数据清洗，删除了303个样本中有缺失值的6个样本,并将样本的变量名称转换为更易理解的中文名称。
除此之外，还将一些特定得到数据类型，由整型转换为字符串，表示其真正的意义。
最后将得到的数据集保存下来，用于后续的分析。
"""
import warnings
warnings.filterwarnings("ignore")
import pandas as pd

# 读入数据，并删除有空值的样本
data0 = pd.read_csv('D:\编程文件夹\《大数据处理课程设计》\Heart-Disease-Analysis\数据集\heart_disease.csv')

print(data0.head())  # 预览数据集的前五行，可见我们的数据集已经读取成功了,这里若去掉()则会读取前五行和后五行

print(data0.shape)  # 得出的结果为（303，14），可见该数据集有303行，14列

data = data0.dropna(axis=0, how='any')  # 删除有缺失值的行
data1 = data0.dropna(axis=0, how='any')  # 删除有缺失值的行

print(data.shape)  # 得出的结果为（297,14），由此可见，六行数据有缺失值

print(data.dtypes)  # 由此了解各列数据的数据类型

# 还原定类数据的真正含义，方便理解
data.sex[data.sex == 0] = '女'
data.sex[data.sex == 1] = '男'
data1.sex[data1.sex == 0] = '女'
data1.sex[data1.sex == 1] = '男'

data.cp[data.cp == 1] = '典型心绞痛'
data.cp[data.cp == 2] = '非典型心绞痛'
data.cp[data.cp == 3] = '无心绞痛'
data.cp[data.cp == 4] = '渐进式疼痛'
data1.cp[data1.cp == 1] = '典型心绞痛'
data1.cp[data1.cp == 2] = '非典型心绞痛'
data1.cp[data1.cp == 3] = '无心绞痛'
data1.cp[data1.cp == 4] = '渐进式疼痛'

data.fbs[data.fbs == 0] = '小于等于120mg/dl'
data.fbs[data.fbs == 1] = '大于120mg/dl'
data1.fbs[data1.fbs == 0] = '小于等于120mg/dl'
data1.fbs[data1.fbs == 1] = '大于120mg/dl'

data.restecg[data.restecg == 0] = '正常'
data.restecg[data.restecg == 1] = '患有ST-T波异常'
data.restecg[data.restecg == 2] = '左心室肥大'
data1.restecg[data1.restecg == 0] = '正常'
data1.restecg[data1.restecg == 1] = '患有ST-T波异常'
data1.restecg[data1.restecg == 2] = '左心室肥大'

data.exang[data.exang == 0] = '否'
data.exang[data.exang == 1] = '是'
data1.exang[data1.exang == 0] = '否'
data1.exang[data1.exang == 1] = '是'

data.slope[data.slope == 1] = '抬高'
data.slope[data.slope == 2] = '平缓'
data.slope[data.slope == 3] = '下降'
data1.slope[data1.slope == 1] = '抬高'
data1.slope[data1.slope == 2] = '平缓'
data1.slope[data1.slope == 3] = '下降'

data.thal[data.thal == 3] = '正常'
data.thal[data.thal == 6] = '固定缺陷'
data.thal[data.thal == 7] = '可逆缺陷'
data1.thal[data1.thal == 3] = '正常'
data1.thal[data1.thal == 6] = '固定缺陷'
data1.thal[data1.thal == 7] = '可逆缺陷'

data.target[data.target != 0] = '患病'  # 患病
data.target[data.target == 0] = '健康'  # 健康

print(data.dtypes)  # 检查各列数据类型是否发生了预期的改变，注：在pandas中，离散的定类特征数据为object型
print(data.head())

# 更改列名
data.columns = ['年龄', '性别', '胸痛类型', '静息血压', '血清总胆固醇', '空腹血糖', '静息心电图结果', '最大心率',
                '运动诱发的心绞痛',
                'ST段下降', '运动高峰ST段', '主要血管数', '地中海贫血', '诊断结果']

data1.columns = ['年龄', '性别', '胸痛类型', '静息血压', '血清总胆固醇', '空腹血糖', '静息心电图结果', '最大心率',
                 '运动诱发的心绞痛',
                 'ST段下降', '运动高峰ST段', '主要血管数', '地中海贫血', '诊断结果']

data1 = pd.get_dummies(data1)  # 将object类的定类变量转变为独热编码
print(data1.head())  # 可见转换完后的数据集变成了27列
print(data1.iloc[0])

# 导出为csv数据
data.to_csv('D:\编程文件夹\《大数据处理课程设计》\Heart-Disease-Analysis\数据集\heart_disease_preprocessed.csv',
            index=False)
#  index= False 为不要索引0.1.2....，只保留数据集本身

data1.to_csv('D:\编程文件夹\《大数据处理课程设计》\Heart-Disease-Analysis\数据集\heart_disease_preprocessed1.csv',
             index=False)
