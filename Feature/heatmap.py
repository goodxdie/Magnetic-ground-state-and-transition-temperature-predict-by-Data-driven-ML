# -*- coding: utf-8 -*-


from numpy import array
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df_base = pd.read_csv('./train_after_add.csv',)
plt.figure(figsize=(16, 12))
pf = pd.get_dummies(df_base['f1'])
df = pd.concat([df_base, pf], axis=1)
df.drop(['f1'], axis=1, inplace=True)
print(df)
sns.heatmap(df.corr(), annot=True, fmt=".2f")
df.drop(['f3'], axis=1, inplace=True)
df.to_csv('result.csv')
plt.show()
