"""Task 1

Create a table

Create a table of your choice inside the sample
SQLite database, rename it,
and add a new column. Insert a couple rows inside
your table. Also, perform UPDATE and DELETE statements
on inserted rows.

As a solution to this task, create a file named: task1.sql,
with all the SQL statements you have used
to accomplish this task"""

import sqlite3

db = sqlite3.connect('task0111.sql')
sql = db.cursor()

#создание табл
sql.execute("""CREATE TABLE IF NOT EXISTS users(userid INT PRIMARY KEY, 
first_name TEXT, lastname TEXT);
""")
db.commit()

#переименование табл
sql.execute("""
ALTER TABLE users RENAME TO usersdb
""")
db.commit()

#добавление новой колоны
sql.execute("""
ALTER TABLE usersdb ADD COLUMN 'nickname''TEXT'
""")
db.commit()


#добавление данных
sql.execute("""
INSERT INTO usersdb VALUES (1,"Igor","Ivanov","kokshka");
""")
db.commit()

sql.execute("""
INSERT INTO usersdb VALUES (2,"Oleg","Petrov","Frider");
""")
db.commit()

sql.execute("""
INSERT INTO usersdb VALUES (3,"John","Malkovic","NEO");
""")
db.commit()

#удаление записи
sql.execute("""
DELETE FROM usersdb WHERE userid = '1'
""")
db.commit()

#редактирование
sql.execute("""
UPDATE usersdb SET first_name = 'Ira' WHERE userid = '2'
""")
db.commit()




for value in db.execute("SELECT * FROM usersdb"):
    print(value)