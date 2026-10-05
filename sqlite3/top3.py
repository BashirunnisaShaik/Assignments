import sqlite3

a = sqlite3.connect('college.db')
c = a.cursor()

c.execute("SELECT * FROM student order by marks desc limit 3 ")
print(c.fetchall())

a.close()