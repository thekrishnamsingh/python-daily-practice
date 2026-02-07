class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Krishnam", 50000)
account.deposit(2000)
print("Balance:", account.get_balance())
