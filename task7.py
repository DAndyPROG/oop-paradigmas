from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Customer(Person):
    def __init__(self, name, email, customer_id):
        super().__init__(name, email)
        self.customer_id = customer_id

    def get_customer_info(self):
        return {
            "name": self.name,
            "email": self.email,
            "customer_id": self.customer_id
        }


class BankAccount(ABC):
    def __init__(self, owner, account_number, initial_balance=0):
        self._balance = initial_balance
        self._owner = owner
        self._account_number = account_number

    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner

    @property
    def account_number(self):
        return self._account_number

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_account_number(self):
        return self._account_number


class CheckingAccount(BankAccount):
    def __init__(self, owner, account_number, initial_balance=0):
        super().__init__(owner, account_number, initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return self._balance
        else:
            raise ValueError("Deposit amount must be greater than 0")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                return self._balance
            else:
                raise ValueError("Insufficient funds")
        else:
            raise ValueError("Withdrawal amount must be greater than 0")


customer = Customer("Alphred Gold", "alphy.gold@example.com", "CUST12345")
print("Customer Info:", customer.get_customer_info())

account = CheckingAccount(customer, "ACC123456789", 1000)
print(f"Account Number: {account.get_account_number()}")
print(f"Initial Balance: {account.balance}")

account.deposit(500)
print(f"Balance after deposit: {account.balance}")

try:
    account.withdraw(300)
    print(f"Balance after withdraw: {account.balance}")
except ValueError as e:
    print(e)

try:
    account.withdraw(1500)
except ValueError as e:
    print(e)
