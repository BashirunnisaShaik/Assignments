import sqlite3

a=sqlite3.connect('college.db')

c=a.cursor()
c.execute("update student set marks=98 where id=1")

c.execute("select * from student ")
print(c.fetchall())

a.commit()
a.close()
