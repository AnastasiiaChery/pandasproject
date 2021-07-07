import numpy as np

import pandas as pd

import pickle

filename = 'heart.csv'
#
# df = pd.read_csv(filename)
# df.head()
# print(df)
#
#
# #
# # data = np.loadtxt(filename, delimiter=',', skiprows=1)
# # print(data)
# # print(data.dtype)
#
#
# def load_file(filename):
#     with open(filename, encoding='utf-8-sig') as f:
#         data, cols = [], []
#         for i, line in enumerate(f.read().splitlines()):
#             if i == 0:
#                 cols += line.split(",")
#             else:
#                 data.append([float(x) for x in line.split(",")])
#         df = pd.DataFrame(data, columns=cols)
#     return df
#
#
# # print(load_file(filename).head(4))
# # print(load_file(filename))
#
# df2 = df[["age", "sex", "cp"]]
# data2 = df2.to_numpy()
# data2[3, 2] = 100
# print(df2)
#
# df.age.to_numpy()[0] = 100
# print(df)
#
# print(df['age'].mean())
# print(df['age'].to_numpy().mean())
# print(df['age'].to_numpy().reshape(3, -1))
#
# # Creating dataframe
# # 1
# data = np.random.random(size=(5, 3))
# df = pd.DataFrame(data=data, columns=['A', 'B', 'C'])
# print(df)
#
# # 2
# df = pd.DataFrame(data={'A': [1, 2, 3], "B": ["Sam", "Alex", "John"]})
# print(df)
#
# # 3
# dtype = [('A', np.int_), ('B', (np.str_, 20))]
# data=np.array([(1, "Sam"), (2, "Alex"), (3, "John")], dtype=dtype)
# df=pd.DataFrame(data)
# print(df)
#
# # 4
# data=[{"A":1, "B":"Sam"}, {"A":2, "B":"Sam2"},{"A":3, "B":"Sam3"},]
# df=pd.DataFrame(data)
# print(df)


# Saving and Serialising a dataframe

#
# df=pd.DataFrame(np.random.random(size=(100000, 4)), columns=['A', 'B', 'C', 'D'])
# print(df)
#
# df.to_csv('save.csv', index=False, float_format="%0.4f")
#
# df.to_pickle('save.pkl')


# Inspecting dataframe
# df=pd.read_csv('astronauts.csv')
# print(df.head())
#
# # fron end
# print(df.tail(1))
#
# # random
# print(df.sample(3))
# print(df.info())
#
# # count, mean, min, max .....
# print(df.describe())
#
# # cuont rov , column
# print(df.shape)
#
# # corelation
# print(df.corr())
#
# # counts
# print(df["Year"].value_counts())
