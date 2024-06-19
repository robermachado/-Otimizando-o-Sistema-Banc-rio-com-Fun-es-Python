class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

def deposit(account, amount):
    if amount > 0:
        account.balance += amount
        print(f"Deposit of {amount} successful. New balance: {account.balance}")
    else:
        print("Invalid deposit amount. Please try again.")

def withdraw(account, amount):
    if 0 < amount <= account.balance:
        account.balance -= amount
        print(f"Withdrawal of {amount} successful. New balance: {account.balance}")
    elif amount <= 0:
        print("Invalid withdrawal amount. Please try again.")
    else:
        print("Insufficient funds. Please try again.")

def statement(account):
    print(f"Account Statement for {account.account_holder}:")
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")

# Example usage:
account = BankAccount("123456", "John Doe", 1000.0)

deposit(account, 500.0)
withdraw(account, 200.0)
statement(account)