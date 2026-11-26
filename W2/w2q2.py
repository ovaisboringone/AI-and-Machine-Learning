class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print("Balance:", self._balance)

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print("Balance:", self._balance)
        else:
            print("Insufficient funds.")

account = BankAccount("12345")
account.deposit(500)
account.withdraw(200)
account.withdraw(400)