class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
class Cow:
    def sound(self):
        print("Cow moos")
def sound(x):
    x.sound()
d=Dog()
c=Cat()
w=Cow()
sound(d)
sound(c)
sound(w)