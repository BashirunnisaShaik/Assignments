class UPIPayment:
    def pay(self):
        print("Payment through UPI")
class CardPayment:
    def pay(self):
        print("Payment through Card")
class CashPayment:
    def pay(self):
        print("Payment through Cash")
upi=UPIPayment()
card=CardPayment()
cash=CashPayment()
upi.pay()
card.pay()
cash.pay()