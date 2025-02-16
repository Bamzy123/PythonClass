from Functions.account import Account

class Banks:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1000

    def create_account(self, pin, name):
        if any(acct.name == name for acct in self.accounts.values()):
            raise ValueError("Account with name {} already exists".format(name))
        account_number = self.next_account_number
        self.accounts[account_number] = Account(account_number, pin, name)
        self.next_account_number += 1
        return account_number

    def get_account(self, account_number):
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Account not found")
        return account

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number, amount, pin):
        account = self.get_account(account_number)
        account.withdraw(amount, pin)

    def transfer(self, sender_account_number, receiver_account_number, amount, sender_pin):
        sender = self.get_account(sender_account_number)
        receiver = self.get_account(receiver_account_number)
        sender.transfer(amount, receiver, sender_pin)

    def update_pin(self, account_number, old_pin, new_pin):
        account = self.get_account(account_number)
        account.update_pin(old_pin, new_pin)
