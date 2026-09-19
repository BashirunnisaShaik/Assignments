class MySQL:
    def connect(self):
        print("Connected to MySQL")
class Oracle:
    def connect(self):
        print("Connected to Oracle")
class MongoDB:
    def connect(self):
        print("Connected to MongoDB")
def connect(x):
    x.connect()
m=MySQL()
o=Oracle()
d=MongoDB()
connect(m)
connect(o)
connect(d)