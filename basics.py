from abc import ABC, abstractmethod


# Interface for transactions
class Transaction(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# Abstract base class for accounts
class Account(Transaction):
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Encapsulation
        self.__balance = balance                # Encapsulation

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance


# Inheritance and Polymorphism
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            new_balance = self.get_balance() + amount
            self.set_balance(new_balance)
            print(f"Deposited {amount}. New balance: {self.get_balance()}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)
            print(f"Withdrew {amount}. New balance: {self.get_balance()}")
        else:
            print("Insufficient balance or invalid amount.")


class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            new_balance = self.get_balance() + amount
            self.set_balance(new_balance)
            print(f"Deposited {amount}. New balance: {self.get_balance()}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= (self.get_balance() + self.overdraft_limit):
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)
            print(f"Withdrew {amount}. New balance: {self.get_balance()}")
        else:
            print("Overdraft limit exceeded or invalid amount.")


# Example usage
def main():
    accounts = [
        SavingsAccount("SA123", 1000, 0.03),
        CurrentAccount("CA456", 500, 1000)
    ]

    for account in accounts:
        account.deposit(200)
        account.withdraw(100)
        print(f"Final balance for account {account.__class__.__name__}: {account.get_balance()}\n")


if __name__ == "__main__":
    main()
