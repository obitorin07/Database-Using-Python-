from dotenv import dotenv_values
import mysql.connector

secret_code =dotenv_values('.secret_code')

database_name=secret_code['DATABASE_NAME']
host_name =secret_code['USER_HOST']
user_password=secret_code['USER_PASSWORD']
user_name=secret_code['USER_NAME']

connect = mysql.connector.connect(user =user_name ,host=host_name,password=user_password,database=database_name)
print("Contents of secret_code:", secret_code)
#creating cursor
cursor =connect.cursor()

#now excecuting for create table 
table_name ='CREATE TABLE STUDENT(NAME VARCHAR(255),ROLL_NO INT);'
cursor.execute(table_name)

connect.close()

"""
use LEARN_MYSQL;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-----------------------+
| Tables_in_LEARN_MYSQL |
+-----------------------+
| STUDENT               |
+-----------------------+
1 row in set (0.00 sec)

"""

