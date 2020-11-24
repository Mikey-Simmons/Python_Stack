class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
    def display_account_info(self):
        print(f"balance: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance *(self.int_rate) / 100 + self.balance
        return self

class User:
    def __init__(self,name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self , amount):
        self.account.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account.balance = self.account.balance - amount
        return self
    def display_user_balance(self):
        print(f"{self.name} balance: {self.account.balance}")
        return self
    def transfer_money(self, other_user,amount):
        self.account_balance = self.account_balance + amount
        other_user.account_balance = other_user.account_balance - amount


joe = User('joe','jojosmi@aol.com')

joe.make_deposit(10)
joe.make_withdrawal(9)
joe.display_user_balance()

