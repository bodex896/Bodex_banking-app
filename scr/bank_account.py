class BankAccount:
    def __init__(self, balance=1_000_000_000, account_number="81******63"):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount
        return self.balance

    def transfer(self, amount, recipient):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if not recipient.strip():
            raise ValueError("Enter the recipient's account number.")

        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount
        return self.balance
