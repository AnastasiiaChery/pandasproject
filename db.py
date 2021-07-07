import mysql
import pandas as pd

# import MySQLdb
import mysql.connector
from mysql import connector
from mysql.connector import Error, cursor
#
# def create_connection(host_name, user_name, user_password, db_name):
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host=host_name,
#             user=user_name,
#             passwd=user_password,
#             database=db_name
#         )
#         print("Connection to MySQL DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#     return connection
# connection = create_connection("localhost", "newuser", "password", "test")
#
# def execute_query(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#
# create_table = """
# CREATE TABLE IF NOT EXISTS stock (
#   id INT AUTO_INCREMENT,
#   name TEXT NOT NULL,
#   age FLOAT,
#   PRIMARY KEY (id)
#
# ) ENGINE = InnoDB
# """
#
# execute_query(connection, create_table)


db_connection = mysql.connector.connect(host="localhost", user="newuser", passwd="password", database="test")
db_cursor = db_connection.cursor()
db_cursor.execute('SELECT * FROM stock')

table_rows = db_cursor.fetchall()

df = pd.DataFrame(table_rows)
diamonds_cols = ['id', 'name', 'age']
df.columns = diamonds_cols
print(df)


diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')


