class Rectangle:
    def area(self):
        length=10
        breadth=5
        print("Rectangle area:",length*breadth)
class Circle:
    def area(self):
        radius=5
        print("Circle area:",3.14*radius*radius)
r=Rectangle()
c=Circle()
r.area()
c.area()