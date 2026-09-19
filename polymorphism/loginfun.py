class Student:
    def login(self):
        print("Student logged in")
class Admin:
    def login(self):
        print("Admin logged in")
class User:
    def login(self):
        print("User logged in")
def login(x):
    x.login()
s=Student()
a=Admin()
u=User()
login(s)
login(a)
login(u)