import pymongo
from pymongo import MongoClient

client = MongoClient()
# Параметры подключения к базе
client = MongoClient('localhost', 27017)

# Or use the MongoDB URI format:
# client = MongoClient('mongodb://localhost:27017/')

# Подключаемся к базе
# db = client.test

# If your database name is such that using attribute style access won’t work (like test-database),
# you can use dictionary style access instead:
# Данные по БД
db = client['test']
print(db)

# A collection is a group of documents stored in MongoDB, and can be thought of as roughly the equivalent of a table in a relational database. Getting a collection in PyMongo works the same as getting a database:
#
collection = db.test_collection
# or (using dictionary style access):
# collection = db['test-collection']


# Documents
# Data in MongoDB is represented (and stored) using JSON-style documents. In PyMongo we use dictionaries
# to represent documents. As an example, the following dictionary might be used to represent a blog post:
#
import datetime

# данные для записи в БД
# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}
# Note that documents can contain native Python types (like datetime.datetime instances) which will be
# automatically converted to and from the appropriate BSON types.
#
# Inserting a Document
# To insert a document into a collection we can use the insert_one() method:
#
# Для доступа к таблицам
posts = db.posts
users = db.users

# Записываем данные в таблицу
# post_id = posts.insert_one(post).inserted_id
# print(post_id)

# ObjectId('...')
# When a document is inserted a special key, "_id", is automatically added if the document doesn’t
# already contain an "_id" key. The value of "_id" must be unique across the collection. insert_one()
# returns an instance of InsertOneResult. For more information on "_id", see the documentation on _id.
#
# After inserting the first document, the posts collection has actually been created on the server.
# We can verify this by listing all of the collections in our database:
#
# Показывает какие таблицы есть
# db.list_collection_names()
# print(db.list_collection_names())

# Вытягиваем одну запись
print((posts.find_one({"author": "Mike"})))

# Вытягиваем много записей
for post in users.find():
    print(post)

# Количество записей
print(posts.count_documents({}))

# или только тех документов, которые соответствуют определенному запросу:
print(posts.count_documents({"author": "Mike"}))
#
# Запросы диапазона
# MongoDB поддерживает множество различных типов сложных запросов . В качестве примера давайте выполним
# запрос, в котором мы ограничиваем результаты сообщениями старше определенной даты, но также сортируем результаты по автору:


# for post in posts.find({"author": "Mike"}).sort("author"):
#     print(post)

# # только уникальные строки ?????????????????????????
# print(db.posts.create_index([('id', pymongo.ASCENDING)], unique=True))

#
# # Удалить БД, если она существует
# connection.drop_database("test_database")
#
# # Удалить коллекцию
#  db.final.drop()
#
# # Добавление документов в колекцию 'users'

# users.insert_one({'name': 'user 6', 'level': 1}).inserted_id

#
# # Полное имя колекции
# print (db.users.full_name)
# #

# # Получить все документы
# for user in db.users.find():
#     print(user)
# #
# лимит
# for data in db.users.find().limit(2):
#     print(data)
#
# Выбрать конкретные атрибуты
#
# print(db.users.find({},{ 'level':1, 'name':'user 1' }))
#
# # Получить один документ по условию
# print(db.users.find_one({'name':'user 1'}))

# # Сохранить документ
# db.users.save(user)
#
# # Удалить документ
# db.users.remove(user)
#
# # Установить значение в документе
# db.users.update_one({ 'name':'user 2' }, { "$set": { 'level':5 } })
#
# # Кол-во документов
# print('Count',db.users.estimated_document_count())
# print('Count lvl=3',db.users.find({'level':3}).count())
#
# # Сортировка
# for user in db.users.find().sort('level'):
#     print(user)
# # в обратном порядке: .sort('level',pymongo.DESCENDING)
#
# Сортировка по нескольким атрибутам
# for user in db.users.find({}).sort( [('name',1),('level',-1)] ):
#         print(user)
# #
# # Ограничение выборки, пропустить один документ и выбрать не более двух
# for user in db.users.find().skip(1).limit(2):
#     print(user)
#
# # Условия
# for user in db.users.find().where('this.name == "user 2" || this.level>3'):
#     print(user)
#
# # Выбрать неповторяющиеся записи
# for user in db.users.distinct('level'):
#     print(user)
#
# # Поиск регулярным выражением
# import re
# regex = re.compile('^us', re.I | re.U)
# result = db.collection.find({ 'name':regex })
#
# # вставка даты и время
# import datetime
# db["11111"].insert({'date': datetime.datetime.utcnow()})
# x = db["11111"].find_one()
# print(x)
# # вставка измененной даты и время
# # год, месяц, день, часы, минуты, секунды, мл-секунды
# x = datetime.datetime(2015, 7, 8, 18, 17, 28, 324000)
# #или так
# x = datetime.datetime(2015, 7, 8)
# print(x)
#
# # получить записи с конца
# # выбираем все и сортируем по _id
# x = db["ru"].find({}).sort("_id", -1).limit(3)
# print(x)
# # выбираем по условию и сортируем по last_modified
# x = db["ru"].find({"flag":"y"}).sort("last_modified", -1).limit(3)
# for s in x:
#     print(s["ip"])
