import sqlite3

a=sqlite3.connect('college.db')

c=a.cursor()



data=[(1, 'Bashir', 20, 'cme', 98),
      (2, 'rukku', 22, 'cse', 90),
        (3, 'naziya', 21, 'diploma', 72),
        (4, 'pooja', 23, 'AIML', 92),
        (5, 'siri', 20, 'Mpc', 88)
]

c.executemany("INSERT INTO student VALUES (?, ?, ?, ?, ?)", data)

a.commit()

a.close()