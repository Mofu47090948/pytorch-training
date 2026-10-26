from bank_account import BankAccount

account = BankAccount("まや")

print(account.name)
print(account.balance)

account.deposit(1000)
print(account.balance)

account.withdraw(300)
print(account.balance)

print(account.get_balance())

account.set_interest_rate(0.1)
account.apply_interest()
print(account.get_balance())

another = BankAccount("たろう")
another.deposit(500)

print(account.get_balance())
print(another.get_balance())