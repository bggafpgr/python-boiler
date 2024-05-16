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

    @property
    def account_number(self):
        return self.__account_number

class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # Composition: Customer has an Address

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def list_customers(self):
        for customer in self.customers:
            print(f"{customer.name} - {customer.address.street}, {customer.address.city}, {customer.address.zip_code}")

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

# Multiple Inheritance and Polymorphism
class Rewards:
    def __init__(self, rewards_points):
        self.rewards_points = rewards_points

    def add_points(self, points):
        self.rewards_points += points
        print(f"Added {points} points. Total rewards: {self.rewards_points}")

class RewardsSavingsAccount(SavingsAccount, Rewards):
    def __init__(self, account_number, balance, interest_rate, rewards_points):
        SavingsAccount.__init__(self, account_number, balance, interest_rate)
        Rewards.__init__(self, rewards_points)

# Example usage
def main():
    address = Address("123 Main St", "Anytown", "12345")
    customer = Customer("Alice", address)

    bank = Bank("Bank of Python")
    bank.add_customer(customer)
    bank.list_customers()

    accounts = [
        SavingsAccount("SA123", 1000, 0.03),
        CurrentAccount("CA456", 500, 1000),
        RewardsSavingsAccount("RSA789", 1500, 0.05, 100)
    ]

    for account in accounts:
        account.deposit(200)
        account.withdraw(100)
        print(f"Final balance for account {account.account_number}: {account.get_balance()}\n")
        if isinstance(account, RewardsSavingsAccount):
            account.add_points(50)

if __name__ == "__main__":
    main()
