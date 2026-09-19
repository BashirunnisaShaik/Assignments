class UPI:
    def pay(self):
        print("UPI payment")
class Card:
    def pay(self):
        print("Card payment")
class Cash:
    def pay(self):
        print("Cash payment")
def pay(x):
    x.pay()
u=UPI()
c=Card()
h=Cash()
pay(u)
pay(c)
pay(h)