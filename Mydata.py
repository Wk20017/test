import numpy as np
import pandas as pd
# df = pd.read_csv('data1.csv')
# df = pd.read_csv('data1.csv', header=None)
# df = pd.read_csv('data1.csv', names=['a', 'b', 'c', 'd', 'info'])
# df = pd.read_table('data1.csv', sep=',')
# name = ['A1', 'A2', 'A3', 'A4', 'info']
# df = pd.read_csv('data2.csv')
# print(df)
# df.to_csv('data3.csv', na_rep='Null', header=False, index=False)
# df1 = pd.read_csv('data3.csv')
# print(df1)
df = pd.read_excel('C:/Users/王凯/Desktop/data4.xlsx', header=None, names=['a', 'b', 'c'])
print(df)
