import sqlite3

a = sqlite3.connect('college.db')
c = a.cursor()

c.execute("SELECT COUNT(*) FROM student")

print(c.fetchall())

a.close()