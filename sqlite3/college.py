import sqlite3

a=sqlite3.connect('college.db')

c=a.cursor()
c.execute("DROP TABLE IF EXISTS student")

 
c.execute('''CREATE TABLE student
(id INTEGER primary key,
name TEXT,
age INTEGER,
course TEXT,
marks INTEGER)''')



a.commit()
a.close()