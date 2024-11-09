# 随机森林分类
import time
import pandas as pd
# 导入sklearn库的RandomForestClassifier函数
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics  # 分类结果评价函数
data1 = pd.read_csv('train_after_he8_2.csv')
feature_names = data1.columns[:-1]  # 特征名，最后一列是标签
# print(feature_names)
data = pd.read_csv('./train_after_he8_2.csv',
                   index_col=False, encoding='gb18030')
feature_names = data.columns[:-1]  # 特征名，最后一列是标签
# x = data[['f2', 'f3', 'f4', 'f6', 'f7']]  # 特征
x = data[['Atomic_radius', 'Atomic_number', 'Atomic_weight', 'Dipole_polarizability',
          'Electron_affinity', 'Nvalence', 'Magnetic_moment']]
y = data['Tc']  # 标签
# 划分数据集
x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=0, train_size=0.70)
#print('训练集和测试集 shape', x_train.shape, x_test.shape)
print('训练集和测试集 shape:', x_train.shape,
      y_train.shape, x_test.shape, y_test.shape)
model = RandomForestClassifier()  # 实例化模型RandomForestClassifier
model.fit(x_train, y_train)  # 在训练集上训练模型
# print(model)  # 输出模型RandomForestClassifier
# 在测试集上测试模型
rfc = RandomForestClassifier(random_state=2)
rfc.fit(x_train, y_train)
expected = y_test  # 测试样本的期望输出
predicted = model.predict(x_test)  # 测试样本预测
# 输出结果 微平均 micro avg: 不区分样本类别，计算整体的 精准、召回和F1  ,,加权平均 weighted avg：是对宏平均的一种改进，考虑了每个类别样本数量在总样本中占比
print(metrics.classification_report(expected, predicted))  # 输出结果，精确度、召回率、f-1分数
print(metrics.confusion_matrix(expected, predicted))  # 混淆矩阵
auc = metrics.roc_auc_score(y_test, predicted)
accuracy = metrics.accuracy_score(y_test, predicted)  # 求精度
print("Accuracy: %.2f%%" % (accuracy * 100.0))
fileout = open('Before.txt', 'a+')
a = str([sorted(zip(feature_names, map(lambda x: round(x, 17),
                                       rfc.feature_importances_)), key=lambda x: x[1], reverse=True)])
timestar = '\n\n\n--****-- 本次训练时间：' + time.strftime('%Y-%m-%d %H:%M:%S',
                                                    time.localtime(time.time()))+'\n'
fileout.writelines(a+'\n'+timestar)
fileout.close()
# print('\n\n\n-- 本次训练时间：' + time.strftime('%Y-%m-%d %H:%M:%S',
#      time.localtime(time.time())))
