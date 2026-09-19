class Shape:
    def area(self):
        print("Shape area")
class Rectangle(Shape):
    def area(self):
        print("Rectangle area:",10*5)
class Circle(Shape):
    def area(self):
        print("Circle area:",3.14*5*5)
class Triangle(Shape):
    def area(self):
        print("Triangle area:",0.5*10*5)
Rectangle().area()
Circle().area()
Triangle().area()