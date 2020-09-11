import numpy as np
import pandas as pd
import json
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
# df = pd.read_excel('C:/Users/王凯/Desktop/data4.xlsx', header=None, names=['a', 'b', 'c'])
# print(df)
# print('----------------')
# print(df.loc[:1, ['a', 'b']])
# df = pd.read_excel('C:/Users/王凯/Desktop/data4.xlsx', header=None)
# new_df = df.loc[0:2]
# print(df)
# print(type(new_df))
# new_df.to_excel('C:/Users/王凯/Desktop/data4.xlsx', sheet_name='Sheet3')
# obj = """
# {"name": "Wes",
#     "places_lived": ["United States", "Spain", "Germany"],
#     "pet": null,
#     "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
#                  {"name": "Katie", "age": 38, "pets": ["Sixes", "Stache", "Cisco"]}]
# }
# """
# print(type(obj))
# result = json.loads(obj)
# print(type(result), result)
# print('-------------')
# change = json.dumps(result)
# print(type(change), change)
# print('-------------')
# df = pd.DataFrame(result['siblings'], columns=['name', 'age', 'pets'])
# print(df)
# df.to_json('test.json')
# df = pd.read_json('test.json')
# print(df)
