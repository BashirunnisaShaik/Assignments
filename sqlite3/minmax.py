import sqlite3

a = sqlite3.connect('college.db')
c = a.cursor()

c.execute("SELECT min(marks) FROM student")
c.execute("SELECT max(marks) FROM student")

print(c.fetchall())

a.close()