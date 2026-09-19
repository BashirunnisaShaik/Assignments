class Car:
    def start(self):
        print("Car starts")
class Bike:
    def start(self):
        print("Bike starts")
def start(x):
    x.start()
c=Car()
b=Bike()
start(c)
start(b)