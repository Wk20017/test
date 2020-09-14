import numpy as np
import pandas as pd

#axis=1: 按列计算    axis=0： 按行计算

# df = pd.DataFrame(np.random.randn(10, 6))
# df.iloc[:4, 1] = None
# df.iloc[:2, 4:6] = None
# df.iloc[6, 3:5] = None
# df.iloc[8, 0:2] = None
#
# print(df)
# print('---------------')
# print(df.dropna(thresh=4)) #保留至少有4个非空值的行
# print('---------------')
# print(df.dropna(subset=[2, 4]))
# print('---------------')
# info = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5} #用指定值填充指定列的NaN，如用0填充第0列
# print(df.fillna(value=info))
# result = df.isnull()
# print(result)
# result = df.isnull().any()
# print(result)
# result = df[df.isnull().values == True].drop_duplicates()  #去掉重复行
# print('------------------')
# print(result)

# df = pd.DataFrame({'k1': ['one', 'two']*3 + ['two']*2, 'k2': [1, 2, 3, 4, 5, 6, 7, 8]})
# print(df)
# print('-------------------------')
# print(df.duplicated(keep=False))
# print(df.duplicated(subset='k1', keep=False))
# print('--------------------------')
# print(df.drop_duplicates(subset='k1'))

# df = pd.DataFrame(np.random.randn(1000, 4))
# print(df.describe())
# col = df[2]
# print(df[(np.abs(df)>3).any(1)])

# x = (lambda a= 'fee', b= 'bee', c= 'aee' : a+b+c)
# print(type(x))
# print(x('my'))

# key = 'got'
# a = {
#     'already': (lambda : 2 + 2),
#     'got': (lambda : 2 * 4),
#     'one': (lambda : 2 ** 6)
# }[key]()
# print(a)

# action = (lambda x: (lambda y: x+y))
# act = action(99)
# print(act(3))

df = pd.read_csv('data1.csv')
print(df)
print('----------------')
new_df = df.loc[:, 'a']
print(new_df)
print('----------------')
print(pd.get_dummies(new_df))
