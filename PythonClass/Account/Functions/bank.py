from Functions.account import Account


class Banks:
    def __init__(self):
        self.accounts = {}

    def create_account(self, pin, name):
        if name in self.accounts:
            raise ValueError("Account with this name already exists")
        self.accounts[name] = Account(pin, name)

    def find_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None

    def deposit(self, amount, name):
        account = self.find_account(name)
        if account is not None:
            account.amount += amount