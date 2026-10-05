import sqlite3

a=sqlite3.connect('college.db')

c=a.cursor()

p=c.execute("SELECT * FROM student where id=3")
print(p.fetchall())
a.commit()
a.close()