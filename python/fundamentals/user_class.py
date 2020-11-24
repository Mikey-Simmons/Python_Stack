class User:
    def __init__(self,name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance = self.account_balance - amount
        return self
    def display_user_balance(self):
        print(f"{self.name} balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user,amount):
        self.account_balance = self.account_balance + amount
        other_user.account_balance = other_user.account_balance - amount

anna = User('anna','annasemail@gmail.com')
joe = User('joe','jojosmith@gmail.com')
anna.make_deposit(1000)
joe.make_deposit(1000).make_deposit(10).make_withdrawal(99).display_user_balance()


