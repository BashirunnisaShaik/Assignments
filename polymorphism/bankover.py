class BankAccount:
    def calculate_interest(self):
        print("Bank interest")
class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings interest: 5%")
class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current account interest: 3%")
SavingsAccount().calculate_interest()
CurrentAccount().calculate_interest()