from Functions.account import Account

class Banks:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1000

    def create_account(self, pin, name):
       if any(acct.name == name for acct in self.accounts.values()):
           raise ValueError("Account with name {} already exists")
       account_number = self.next_account_number
       self.accounts[account_number] = Account(account_number,pin, name)
       self.next_account_number += 1
       return account_number

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def deposit(self, acct1, amount):
        account = self.get_account(acct1)
        if not account:
            raise ValueError("Account not found")
        account.deposit(amount)