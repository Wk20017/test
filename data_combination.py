import numpy as np
import pandas as pd
# df = pd.DataFrame(np.random.randn(12).reshape(4, 3),
#                   index=[['a', 'a', 'b', 'c'], ['1', '2', '1', '2']], columns=[['A', 'A', 'B'], ['1', '2', '3']])
# df = pd.DataFrame(np.random.randn(16).reshape(4, 4), pd.MultiIndex.from_product([['a', 'b'], [1, 2]], names=['k1', 'k2']),
#                  columns=pd.MultiIndex.from_product([['A', 'B'], [1, 2]], names=['n1', 'n2']))
# print(df)
# print('--------------------')
# df.set_index(['A', 'B'])
# df.reset_index()
# print(df)
# print('----------------')
# new_df = df.swaplevel('k1', 'k2')
# print(new_df)
# print('----------------')
# new_df1 = df.swaplevel('k1', 'k2').sort_index(level=0)
# print(new_df1)
# print('----------------')
# new_df2 = df.swaplevel('k1', 'k2')
# print(new_df2)
# df1 = pd.DataFrame({'A': ['A1', 'A2', 'A3'], 'B': ['B1', 'B2', 'B3']})
# df2 = pd.DataFrame({'A': [0, 1, 2], 'B': [4, 5, 6]})
# df3 = pd.DataFrame({'A': [0, 1, 2, 4], 'B': [4, 5, 6, 10], 'D': [10, 20, 30, 5]})
# print(pd.concat([df1, df2], axis=1))
# print(pd.concat([df1, df3], axis=1, join='inner'))
# df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
#                     'data': range(7)})
# df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
#                     'data': range(3)})
# print(df1)
# print(df2)
# print(pd.merge(df1, df2, on='key'))
# df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
#                     'data1': range(7)})
# df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
#                     'data2': range(3)})
# print(df3)
# print(df4)
# print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))
# print(pd.merge(df3, df4, how='outer'))
df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],
                    'b': [np.nan, 2., np.nan, 6.],
                    'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5, 4., np.nan, 3., 7.],
                    'b': [np.nan, 3., 4., 6., 8.]})
print(df1)
print(df2)
print(df1.combine_first(df2))
print(df2.combine_first(df1))

