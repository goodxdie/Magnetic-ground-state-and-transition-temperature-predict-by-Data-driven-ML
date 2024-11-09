import pandas
data = pandas.read_csv('./train_after_add.csv')
a = str(data['f8'].corr(data['f8']))
print(a)
fileout = open('guanliandu8.txt', 'a+')
fileout.writelines(a + '\n')
fileout.close()
