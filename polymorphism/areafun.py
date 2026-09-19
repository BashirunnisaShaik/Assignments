class Rectangle:
    def area(self):
        print("Rectangle area")
class Circle:
    def area(self):
        print("Circle area")
class Triangle:
    def area(self):
        print("Triangle area")
def area(x):
    x.area()
r=Rectangle()
c=Circle()
t=Triangle()
area(r)
area(c)
area(t)