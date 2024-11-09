import numpy as np
import pandas as pd
# 系数矩阵
data = pd.read_csv('Te.csv')
FM = data.row[2]
print(FM)
A = np.array([[6, 12, 6, 1],
              [-6, 12, -6, 1],
              [-2, -4, 6, 1],
              [2, -4, -6, 1]])
b = np.array([-94.81369644, -94.61409716, -94.69504487, -94.75941092])
x = 1000*np.linalg.solve(A, b)/2.25
x = x[0:3]
Tc = (x[0]+4*x[1]+3*x[2])*11.6087*0.95
# print('交换耦合系数为：\n', x, 'meV')
# print('Tc值为:\n', Tc, 'K')
