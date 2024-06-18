class Account:
    def __init__(self, account_holder, balance=0):
        self.__balance = balance
        self._account_holder = account_holder
    
    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self._account_holder
    

account = Account('Dave Bee', 1000)

print(f"Account holder: {account.get_account_holder()}")
print(f"Balance: {account.get_balance()}")