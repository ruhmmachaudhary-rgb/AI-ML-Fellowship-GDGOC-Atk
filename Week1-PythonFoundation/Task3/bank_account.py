# bank_account.py

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

# Example usage
if __name__ == "__main__":
    acc = BankAccount("Ali", 1000)
    print(acc)
    acc.deposit(500)
    acc.withdraw(200)
    acc.withdraw(2000)

