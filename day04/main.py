from person import Person
from bank_account import BankAccount

# Person example
person = Person("Krishnam Singh", 22, "Python Developer")
print(person.introduce())

# Bank Account example
account = BankAccount("Krishnam Singh", 5000)
print(account.deposit(2000))
print(account.withdraw(1500))
print(account.get_balance())
