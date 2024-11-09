import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# 读取数据
data = pd.read_csv('train_Tc.csv')
X = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values

# 划分训练集和测试集
test_size = 0.25  # 测试集比例
random_state = 42  # 随机种子
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=random_state)
# 构建梯度提升回归模型
gbdt = GradientBoostingRegressor()
gbdt.fit(X_train, y_train)
# 在测试集上进行预测
y_pred = gbdt.predict(X_test)
# # 输出真实值和预测值进行对比
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)
# 输出模型评估指标
print('R2 score:', r2_score(y_test, y_pred))
print('MAE:', mean_absolute_error(y_test, y_pred))
