import sqlite3

a = sqlite3.connect('college.db')
c = a.cursor()

c.execute("SELECT course,count(*) FROM student GROUP BY course")

print(c.fetchall())

a.close()