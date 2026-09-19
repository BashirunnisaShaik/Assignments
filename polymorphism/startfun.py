class Car:
    def start(self):
        print("Car starts")
class Bike:
    def start(self):
        print("Bike starts")
class Bus:
    def start(self):
        print("Bus starts")
def start(x):
    x.start()
c=Car()
b=Bike()
u=Bus()
start(c)
start(b)
start(u)