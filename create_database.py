from dotenv import dotenv_values
import mysql.connector

secret =dotenv_values('.secret_code')

user_name=secret['USER_NAME']
user_pass=secret['USER_PASSWORD']
user_host=secret['USER_HOST']

mydb =mysql.connector.connect(user=user_name,password=user_pass,host=user_host)

#creating cursor

cursor =mydb.cursor()

cursor.execute('CREATE DATABASE LEARN_MYSQL')

mydb.close()
cursor.close()

"""
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| LEARN_MYSQL        |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
"""

