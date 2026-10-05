import sqlite3

a = sqlite3.connect('example.db')
c = a.cursor()
c.execute("DROP TABLE IF EXISTS emp")

c.execute('''CREATE TABLE emp
(id INTEGER primary key,
name TEXT,
phone INTEGER)''')

data=[(1, 'abc', 1234567890),
      (2, 'def', 9876543210),
      (3, 'ghi', 4567891230)
      ] 

c.executemany("INSERT INTO emp VALUES (?, ?, ?)", data)

c.execute("update emp set name='xyz' where id=2")

c.execute("select name ,count(*) from emp group by name")

a.commit()
p=c.execute("SELECT * FROM emp")
print(p.fetchone())
print(p.fetchmany())


a.close()
