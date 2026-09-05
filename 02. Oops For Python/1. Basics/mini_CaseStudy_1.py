#  A bank wants to build a simple system to manage customer accounts using Object-Oriented Programming (OOP).

#  Create a class named BankAccount with the following requirements:

#  Requirements -->
#  The class should have a constructor (__init__) that accepts:
#  Account holder's name (holder)
#  Initial account balance (balance)

#  Create a method named deposit(amount) that adds the given amount to the account balance.

#  Create a method named withdraw(amount) that:
#  Deducts the given amount from the balance if sufficient funds are available.

#  Otherwise, displays the message:
#  Insufficient Balance

#  Create a method named show_balance() that displays the current account balance.


class BankAccount:
    def __init__(self, Name, Balance):
        self.Name = Name
        self.Balance = Balance

    def deposit(self, amount):
        self.Balance += amount

    def withdraw(self, amount):
        if (amount > self.Balance):
            print("Insufficient Balance")
        else:
            self.Balance -= amount

    def Show_balance(self):
        print(self.Balance)

bank_acc1 = BankAccount("Naman", 100)
print(bank_acc1.Name)
print(bank_acc1.Balance)

bank_acc1.deposit(50)
bank_acc1.Show_balance()

bank_acc1.withdraw(80)
bank_acc1.Show_balance()