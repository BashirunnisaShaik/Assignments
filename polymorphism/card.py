class DebitCard:
    def pay(self):
        print("Debit Card payment")
class CreditCard:
    def pay(self):
        print("Credit Card payment")
def pay(x):
    x.pay()
d=DebitCard()
c=CreditCard()
pay(d)
pay(c)