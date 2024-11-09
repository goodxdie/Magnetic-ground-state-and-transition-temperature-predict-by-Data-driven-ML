import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# 读取数据
data = pd.read_csv("train_RFC.csv")

# 拆分特征和标签
features = data.iloc[:, 1:-1].values
labels = data.iloc[:, -1].values

# 自定义训练集和测试集的比例
train_size = 0.65  # 训练集比例
test_size = 0.35  # 测试集比例

# 根据指定的比例分割数据集
train_num = int(len(features) * train_size)
train_features = features[:train_num]
train_labels = labels[:train_num]
test_features = features[train_num:]
test_labels = labels[train_num:]

# 创建随机森林分类器
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# 拟合模型
clf.fit(train_features, train_labels)

# 预测结果
pred_labels = clf.predict(test_features)

# 输出真实标签和预测标签
for i in range(len(test_labels)):
    print(
        f"{data.iloc[train_num+i, 0]}  Real:{test_labels[i]}  Pred:{pred_labels[i]}")

# 计算准确率和混淆矩阵
acc = accuracy_score(test_labels, pred_labels)
cm = confusion_matrix(test_labels, pred_labels)

print("Accuracy:", acc)
print("Confusion Matrix:\n", cm)
