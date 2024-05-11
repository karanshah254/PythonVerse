# create a account class with 2 atrributes - balance & account number,
# create a method for credit, debit and showing balance


class Account:
    def __init__(self, accountNUmber, balance):
        self.accountNUmber = accountNUmber
        self.balance = balance

    def debit(self, amount):
        self.balance = self.balance - amount
        print("Debited amount of", amount, "Rs.")
        print("New balance is", self.showBalance(), "Rs.")

    def credit(self, amount):
        self.balance += amount
        print("Credited with", amount, "Rs.")
        print("New balance is", self.showBalance(), "Rs.")

    def showBalance(self):
        return self.balance


acc1 = Account(1, 10000)
print("For account number", acc1.accountNUmber, "balance is", acc1.balance)
acc1.debit(2000)
acc1.credit(5000)
