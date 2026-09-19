class Payment:
    def pay(self):
        print("Payment")
class UPI(Payment):
    def pay(self):
        print("Payment through UPI")
class CreditCard(Payment):
    def pay(self):
        print("Payment through Credit Card")
class NetBanking(Payment):
    def pay(self):
        print("Payment through Net Banking")
UPI().pay()
CreditCard().pay()
NetBanking().pay()