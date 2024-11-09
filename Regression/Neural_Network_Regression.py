import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# 读取数据
data = pd.read_csv('Tc.csv')
X = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values

# 划分训练集和测试集
test_size = 0.4  # 测试集比例
random_state = 42  # 随机种子
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=random_state)

# 特征缩放
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 构建神经网络回归模型
mlp = MLPRegressor(hidden_layer_sizes=(100, 50),
                   activation='relu', solver='adam', max_iter=500)
mlp.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = mlp.predict(X_test)

# 输出模型评估指标
print('R2 score:', r2_score(y_test, y_pred))
print('MAE:', mean_absolute_error(y_test, y_pred))
print('MSE:', mean_squared_error(y_test, y_pred))

# # 输出真实值和预测值进行对比
# df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
# print(df)
