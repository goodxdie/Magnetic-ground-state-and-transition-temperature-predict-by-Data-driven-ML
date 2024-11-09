import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.kernel_ridge import KernelRidge
from sklearn.metrics import mean_squared_error, r2_score

# 读取数据文件
data = pd.read_csv('train_Tc.csv', index_col=0)

# 将标签分离
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

# 训练模型
model = KernelRidge(alpha=0.1, kernel='rbf')
model.fit(X_train, y_train)

# 预测测试集
y_pred = model.predict(X_test)

# 输出对比结果和评价指标
for i in range(len(y_test)):
    print(
        f"{y_test.index[i]}: Real = {y_test.iloc[i]}, Predicted = {y_pred[i]}")

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse}")
print(f"R2 Score: {r2}")
