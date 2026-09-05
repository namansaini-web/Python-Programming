class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

account = Bank(1000)
account.withdraw(200)
account.withdraw(300)

print(account.balance)