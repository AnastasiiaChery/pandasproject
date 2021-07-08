import json

import pymongo
from pymongo import MongoClient

# Подключение к БД и таблице
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['test']
users_list= db.users_list

# Запись данных в файл
# with open('users.json', 'r', encoding='utf-8') as f:
#     text = json.load(f)
# print(text)
# for i in text:
#     users_list.insert_one(i).inserted_id

# Вывести все данные

for user in


# Вывести честь данных
# Фильтровать
# Сортировать

