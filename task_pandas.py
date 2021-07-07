import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')


# # 1. Напишите программу Pandas для чтения CSV-файла из указанного источника и печати первых 5 строк
# #
# print(diamonds.head(3))
# #
# # 2. Напишите программу Pandas для чтения набора данных из бриллианта DataFrame, изменения значений столбцов по умолчанию и печати первых 6 строк
# #
# user_cols = ['carat', 'cut', 'x', 'y', 'z']
# diam=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv').head(6)
# print(diam[user_cols])
#
# # 3. Напишите программу Pandas, чтобы выбрать серию из бриллиантов DataFrame. Распечатайте содержание серии
# #
# # print(diamonds.sample(frac=0.05))
# print(diamonds['carat'])
# # 4. Напишите программу Pandas для создания новой серии «Качество? Цвет» (используйте обозначение в скобках для определения имени серии) бриллианта DataFrame
#
# diamonds['Quality–color'] = diamonds.cut + ', ' + diamonds.color
# print(diamonds.head())
# #
# # 5. Напишите программу Pandas, чтобы найти количество строк и столбцов и тип данных для каждого столбца алмазов
# #
# diamonds.info()
# print(diamonds.shape)
# print(diamonds.dtypes)
# #
# # 6. Напишите программу Pandas для суммирования только столбцов «объект» в бриллианте Dataframe
# print(diamonds.describe(include=['object']))
# #
# # 7. Напишите программу Pandas для переименования двух столбцов бриллианта в Dataframe
# #
# diamonds.rename(columns={'color':'diamond_color', 'clarity':'dimaond_clarity'}, inplace=True)
# print(diamonds.head())
# #
# 8. Напишите программу Pandas, чтобы переименовать все столбцы бриллианта в Dataframe
#
# diamonds_cols = ['new_carat', 'new_cut', 'new_color', 'new_clarity', 'new_depth', 'new_table', 'new_price', 'new_x', 'new_y', 'new_z']
# diamonds.columns = diamonds_cols
# print(diamonds.head())
# #
# # 9. Напишите программу Pandas для удаления второго столбца алмаза Dataframe
#
# print(diamonds.drop(['new_cut'], axis=1))
#
# #
# # 10. Напишите программу Pandas для одновременного удаления нескольких столбцов из блока данных
# #
# print(diamonds.drop(['new_cut','new_color', 'new_clarity' ], axis=1))
# #
# # 11. Напишите программу Pandas для одновременного удаления нескольких строк (ось = 0 относится к строкам) из фрейма данных diamonds
#
# diamonds.drop([2, 4, 5], axis=0, inplace=True)
# print(diamonds.head())
# 
# 
# # 12. Напишите программу Pandas для сортировки «отрезанной» серии в порядке возрастания (возвращает серию) алмазов в Dataframe
# #
# print(diamonds[3:7].sort_index(ascending=True))
# #
# # 13. Напишите программу Pandas для сортировки Серии цен в порядке убывания (возвращает Серии) бриллиантов Датафрейм
# print(diamonds['price'].sort_values(ascending=False))
# #
# # 14. Напишите программу Pandas, чтобы отсортировать весь DataFrame бриллиантов по серии «Карат» в порядке возрастания и убывания
# #
# print(diamonds.sort_values(['carat'],ascending=False).head())
# print(diamonds.sort_values(['carat'],ascending=True).head())
# # 15. Напишите программу Pandas, чтобы отфильтровать строки DataFrame так, чтобы вес в каратах составлял не менее 0,3
# #
# print(diamonds[diamonds['carat']>0.3])
# 
# # 16. Напишите программу Pandas для преобразования списка питонов в серии Pandas.
# #
# list=[1, 2, 3, 4, 5, 6, 7, 7, 9]
# result=pd.Series(list)
# print(result)
# # 17. Напишите программу Pandas, чтобы найти детали бриллиантов, где длина> 5, ширина> 5 и глубина> 5
# #
# result= diamonds[(diamonds.x >5) & (diamonds.y >5) & (diamonds.z >5)]
# print(result)
# #
# # 18. Напишите программу Pandas, чтобы найти бриллианты премиум-класса или идеальные
# #
# res = diamonds[(diamonds.cut =='Premium') | (diamonds.cut == 'Ideal') ]
# print(res)
# #
# # 19. Напишите программу Pandas, чтобы найти бриллианты, которые имеют оценку Fair, Good или Premium.
# #
# mark = diamonds[(diamonds.cut =='Premium') | (diamonds.cut == 'Good')| (diamonds.cut == 'Fair')  ]
# print(mark)
# #
# 20. Напишите программу Pandas для отображения всех меток столбцов бриллиантов DataFrame
# print(diamonds.columns)
# 
# 21. Напишите программу Pandas, которая будет читать только подмножество из 3 строк из DataFrame с бриллиантами
#
# result = pd.read_csv('http://bit.ly/uforeports', nrows=3)
# print(result.head())
# 
# 22. Напишите программу Pandas для перебора бриллиантов в DataFrame
#
# def funct(list):
#     for index, row in list.iterrows():
#         print(index, row)
# funct(diamonds.head())
#
# # 26. Напишите программу Pandas для расчета среднего значения каждого числового столбца алмазов в DataFrame
# print(diamonds.describe())
# print(diamonds.mean())
# #
# # 27. Напишите программу Pandas для расчета среднего значения каждого ряда алмазов в DataFrame
# #
# print(diamonds.mean(axis=1).head())
# #
# # 28. Напишите программу Pandas для расчета среднего значения цены для каждого бриллианта DataFrame
# #
# print(diamonds.groupby('cut').price.mean())
# #
# # 29. Напишите программу Pandas для расчета количества, минимальной, максимальной цены на каждый бриллиант DataFrame
# #
# print(diamonds.groupby('cut').price.min())
# print(diamonds.groupby('cut').price.max())
# 
# 30. Напишите программу Pandas для создания линейного линейчатого графика бриллианта DataFrame
#
# diamonds.groupby('cut').mean().plot(kind='bar')
# plt.show()
# 
# # 31. Напишите программу Pandas, чтобы подсчитать, сколько раз встречается каждое значение в серии ограненных бриллиантов DataFrame
# #
# print(diamonds.cut.value_counts())
#
# # 32. Напишите программу Pandas для отображения процентов каждого значения серии огранки, встречающейся в бриллиантах в DataFrame
# #
# print(diamonds.cut.value_counts(normalize=True))
# #
# # 33. Напишите программу Pandas для отображения уникальных значений в бриллиантах ограненной серии DataFrame
# #
# print(diamonds.cut.unique())
# #
# # 34. Напишите программу Pandas для подсчета количества уникальных значений в ограненной серии бриллиантов DataFrame
#
# print(diamonds.cut.nunique())
# 
# # 35. Напишите программу Pandas для расчета кросс-табуляции двух серий в бриллиантах DataFrame
# print(pd.crosstab(diamonds.cut, diamonds.price))
# 
# 
# # 36. Напишите программу Pandas для расчета различных сводных статистических данных о бриллиантах серии огранки DataFrame
# #
# print(diamonds.describe())
# 
# # 37. Напишите программу Pandas для создания гистограммы из серии «Карат» (распределение числовой переменной) бриллиантов DataFrame
# #
# diamonds.carat.plot(kind='hist')
# plt.show()
# 
# 38. Напишите программу Pandas для создания гистограммы «value_counts» для «ограненной» серии бриллиантов DataFrame
#
# diamonds.cut.value_counts().plot(kind='bar')
# plt.show()
# 
# # 39. Напишите программу Pandas для создания DataFrame с логическими значениями (True, если отсутствует, False, если не отсутствует) из алмазов DataFrame
# #
# print(diamonds.isnull().head(20))
# 
# # 40. Напишите программу Pandas для подсчета количества пропущенных значений в каждой серии бриллиантов DataFrame
# #
# print(diamonds.isnull().sum())
# 
# # 41. Напишите программу Pandas, чтобы проверить количество строк и столбцов и отбросьте эти строки, если в строке DataFrame «строки» отсутствуют значения «any»
# #
# print(diamonds.dropna(how='any').shape)
# 

# # 43. Напишите программу Pandas, чтобы установить существующий столбец в качестве индекса алмазов DataFrame
# #
# diamonds.set_index('color', inplace=True)
# print(diamonds.head())

# # 45. Напишите программу Pandas для доступа к указанному индексу Series и значениям Series для алмазов DataFrame
# #
# print(diamonds.carat.value_counts().index)
# print(diamonds.carat.value_counts().values)
# 
# # 46. Напишите программу Pandas для сортировки Серии по ее значениям и индексу алмазов в DataFrame
# #
# print(diamonds.cut.value_counts().sort_values())
# print(diamonds.cut.value_counts().sort_index())
# #
# # 47. Напишите программу Pandas для расчета умножения длины, ширины и глубины на каждый бриллиант DataFrame
# #
# print((diamonds.x*diamonds.y*diamonds.z).head())
# 
# # 48. Напишите программу Pandas для объединения DataFrame с бриллиантами в «цветную» серию
# #
# print(pd.concat([diamonds, diamonds.color], axis=1).head())
# 
# # 49. Напишите программу Pandas для чтения указанных строк и всех столбцов алмазов DataFrame
# #
# print(diamonds.head(7))
# print(diamonds.loc[0, :])
# #
# # 50. Напишите программу Pandas для чтения строк 0, 5, 7 и всех столбцов алмазов в DataFrame
# #
# print(diamonds.loc[[0, 5, 7], :])

# # 51. Напишите программу Pandas для чтения строк со 2 по 5 и всех столбцов алмазов в DataFrame
# #
# print(diamonds.loc[[2, 5], :])
# 
# # 52. Напишите программу Pandas для чтения строк с 0 по 2 (включительно), столбцов «цвет» и «цена» алмазов в DataFrame
# #
# print(diamonds.loc[0:2, ['color', 'price']])
# 
# # 53. Напишите программу Pandas для чтения строк с 0 по 2 (включительно), столбцы «цвет» - «цена» (включительно) бриллиантов DataFrame
# #
# print(diamonds.loc[0:2, 'color':'price'])
# 
# # 54. Напишите программу Pandas для чтения строк, в которых «огранка» - это «Премиум», колонка «цвет» алмазов DataFrame
# #
# print(diamonds.loc[diamonds.cut=='Premium', 'color'])
# 
# # 55. Напишите программу Pandas для чтения строк в позициях 0 и 1, столбцов в позициях 0 и 3 ромбов DataFrame
# #
# print(diamonds.iloc[[0, 1], [0, 3]])
# #
# # 56. Напишите программу Pandas для чтения строк в позициях с 0 по 4, столбцов в позициях с 1 по 4 в ромбах DataFrame
# #
# print(diamonds.iloc[0:4, 1:4])
# #
# # 57. Напишите программу Pandas для чтения строк в позициях от 0 до 4 (исключая) и всех столбцов алмазов в DataFrame
# #
# print(diamonds.iloc[5:])
# print(diamonds.iloc[0:5, :])
# #
# # 58. Напишите программу Pandas для чтения строк с 2 по 5 (включительно), столбцов в позициях с 0 по 2 (без учета) бриллиантов в DataFrame
# #
# print(diamonds.iloc[2:6, 3:])
# 
# # 59. Напишите программу Pandas для печати краткого описания бриллиантов DataFrame
# #
# print(diamonds.info())
# 
# # 60. Напишите программу Pandas, чтобы получить истинное использование памяти бриллиантами DataFrame
# #
# print(diamonds.info(memory_usage='deep'))
# 
# # 61. Напишите программу Pandas для расчета использования памяти для каждой серии (в байтах) бриллиантов DataFrame
# #
# print(diamonds.memory_usage(deep=True))
# #
# # 62. Напишите программу Pandas для случайной выборки строк из бриллиантов в DataFrame
# #
# print(diamonds.sample(frac=0.3))
# #
# # 63. Напишите программу Pandas, чтобы получить образец 75% строк в DataFrame с бриллиантами без замены и сохранить оставшиеся 25% строк в другом DataFrame
# #
# result = diamonds.sample(frac=0.75, random_state=99)
# print(result)
# print(diamonds.loc[~diamonds.index.isin(result.index), :])
# 
# # 64. Напишите программу Pandas для чтения бриллиантов DataFrame и определения дублирующего цвета
# # Примечание: функция duplicated () возвращает логическую серию, обозначающую дублирующиеся строки, опционально только с учетом определенных столбцов.
# #
# print(diamonds.shape)
# print(diamonds.clarity.duplicated().sum())
# #
# # 65. Напишите программу Pandas для подсчета повторяющихся рядов алмазов в DataFrame.
# #
# print(diamonds.shape)
# print(diamonds.duplicated().sum())