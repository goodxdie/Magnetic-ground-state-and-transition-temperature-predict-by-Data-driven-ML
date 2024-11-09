import sys
import csv
import numpy as np
# 系数矩阵
matrix = np.array([[3, 1], [-3, 1]])
with open('Te.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过表头
    data = np.array([[float(row[3]), float(row[4])] for row in reader])
    # print(data)
# 循环矩阵运算
with open('Te.csv', 'r') as file:
    reader = csv.reader(file)
    # 读取第一行，即表头，作为每一列的名称
    headers = next(reader)
    # 要读取的列的名称
    col_names = ['A', 'B', 'X']
    # 初始化列表，用于存储每一列的数据
    data_name = [[] for _ in range(len(col_names))]
    # 记录每个要读取的列的编号
    col_indices = [headers.index(name) for name in col_names]
    # 读取每一行的数据，将要读取的列的值添加到对应的列表中
    for row in reader:
        for i, index in enumerate(col_indices):
            data_name[i].append(row[index])
ABX = ["".join(x) for x in zip(data_name[0], data_name[1], data_name[2])]
J1 = []
Tc1 = []
for row in data:
    result = np.linalg.solve(matrix, row)
    #print(f"x'={result[0]}, y'={result[1]}")
    ABX = ["".join(x) for x in zip(data_name[0], data_name[1], data_name[2])]
    J = {result[0]*1000/2.25}
    Tc = {-result[0]*1000/2.25*11.6087*0.95}
    J1.append(J)
    Tc1.append(Tc)
FM_AFM = []
for i in data:
    if i[0] > i[1]:
        FM_AFM.append('AFM')
    else:
        FM_AFM.append('FM')
flee2 = open('J_Tc666.csv', 'w')
for i, j, k, p in zip(ABX, J1, Tc1, FM_AFM):
    print('ABX:', i, '---', '磁态:', p, '---',
          'J:', j, 'meV', '---', 'Tc:', k, 'K')
    a = str(['ABX:', i, '---', '磁态:', p, '---',
             'J:', j, 'meV', '---', 'Tc:', k, 'K'])+'\n'
    flee2.writelines(a)
flee2.close()
