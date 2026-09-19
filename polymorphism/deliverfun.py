class Food:
    def deliver(self):
        print("Food delivered")
class Parcel:
    def deliver(self):
        print("Parcel delivered")
class Medicine:
    def deliver(self):
        print("Medicine delivered")
def deliver(x):
    x.deliver()
f=Food()
p=Parcel()
m=Medicine()
deliver(f)
deliver(p)
deliver(m)