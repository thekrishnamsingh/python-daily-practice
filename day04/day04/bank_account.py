class BankAccount:
    def __init__(self, holder_name, balance=0):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"₹{amount} deposited. New balance: ₹{self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"₹{amount} withdrawn. Remaining balance: ₹{self.balance}"

    def get_balance(self):
        return f"Current balance: ₹{self.balance}"
