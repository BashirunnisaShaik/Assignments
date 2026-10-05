import sqlite3

a = sqlite3.connect('college.db')
c = a.cursor()

d=[(11, 'bashir', 20, 'python', 85),
   (12, 'jyothi', 22, 'java', 90),
   (13, 'kusi', 19, 'c++', 75),
   (14, 'siri', 21, 'python', 80),
   (15, 'ruksana', 23, 'java', 95),
   (6, 'pooja', 20, 'c++', 70),
   (7, 'sweety', 22, 'python', 88),
   (8, 'sirisha', 19, 'java', 92),
   (9, 'sushu', 21, 'c++', 78),
   (10, 'teja', 23, 'python', 84)
]

c.executemany("INSERT INTO student VALUES (?, ?, ?, ?, ?)", d)

c.execute("select * from student ")
print(c.fetchall())

a.commit()
a.close()