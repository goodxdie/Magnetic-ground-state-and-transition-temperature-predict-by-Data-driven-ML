from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

# 创建一个管道（Pipeline）实例，里面包含标准化方法和随机森林模型
pipeline = make_pipeline(
    StandardScaler(), RandomForestClassifier(n_estimators=100, max_depth=4))
# 创建一个用于得到不同训练集和测试集样本的索引的StratifiedKFold实例，折数为10
data = pd.read_csv('./train_after_he8_2.csv',
                   index_col=False, encoding='gb18030')
feature_names = data.columns[:-1]  # 特征名，最后一列是标签
x = data[['Atomic_radius', 'Atomic_number', 'Atomic_weight', 'Dipole_polarizability',
          'Electron_affinity', 'Nvalence', 'Magnetic_moment', 'Charge']]
y = data['y']  # 标签
X_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=0, train_size=0.70)
strtfdKFold = StratifiedKFold(n_splits=10)
# 把特征和标签传递给StratifiedKFold实例
kfold = strtfdKFold.split(X_train, y_train)
# 循环迭代，（K-1）份用于训练，1份用于验证，把每次模型的性能记录下来。
scores = []
for k, (train, test) in enumerate(kfold):
    pipeline.fit(X_train.iloc[train, :], y_train.iloc[train])
    score = pipeline.score(X_train.iloc[test, :], y_train.iloc[test])
    scores.append(score)
    print('Fold: %2d, Training/Test Split Distribution: %s, Accuracy: %.3f' %
          (k+1, np.bincount(y_train.iloc[train]), score))
print('\n\nCross-Validation accuracy: %.3f +/- %.3f' %
      (np.mean(scores), np.std(scores)))
