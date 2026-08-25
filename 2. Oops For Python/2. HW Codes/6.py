class Bank:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = Bank(1000)

account.deposit(500)
print(account.balance)