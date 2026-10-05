import sqlite3

a=sqlite3.connect('college.db')

c=a.cursor()

c.execute("delete from student where id=3")
c.execute("select * from student ")
print(c.fetchall())
a.commit()
a.close()
