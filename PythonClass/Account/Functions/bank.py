from Functions.account import Account


class Banks:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1000

    def create_account(self,name, pin):
       if any(acct.name == name for acct in self.accounts.values()):
           raise ValueError("Account with name {} already exists")
       account_number = self.next_account_number
       self.accounts[account_number] = Account(account_number,pin, name)
       self.next_account_number += 1
       return account_number