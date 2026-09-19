class Person:
    def role(self):
        print("Person")
class Student(Person):
    def role(self):
        print("Student")
class Teacher(Person):
    def role(self):
        print("Teacher")
class Doctor(Person):
    def role(self):
        print("Doctor")
Student().role()
Teacher().role()
Doctor().role()