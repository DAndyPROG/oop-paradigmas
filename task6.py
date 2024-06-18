class Account:
    def __init__(self, account_holder, initial_balance=0):
        self.__balance = initial_balance
        self._account_holder = account_holder
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self.__balance = amount

        else:
            raise ValueError('Balance must be more than 0')
        
    
    def get_account_holder(self):
        return self._account_holder
    

account = Account('Dave Bee', 1000)

print(f"Account holder: {account.get_account_holder()}")
print(f"Balance: {account.balance}")


account.balance = 1500
print(f"NEW Balance: {account.balance}")

try:
    account.balance = -500

except ValueError as e:
    print(e)