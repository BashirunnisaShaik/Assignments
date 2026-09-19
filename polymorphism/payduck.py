class UPIPayment:
    def pay(self):
        print("UPI payment")
class CardPayment:
    def pay(self):
        print("Card payment")
def pay(x):
    x.pay()
u=UPIPayment()
c=CardPayment()
pay(u)
pay(c)