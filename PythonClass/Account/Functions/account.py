class Account:
    def __init__(self, account_number, pin, name):
        self.account_number = account_number
        self.pin = pin
        self.name = name
        self.balance = 0

    def it_exist(self):
        return self.pin is not None and self.name is not None

    def not_exist(self):
        return not self.it_exist()

    def add(self, amount):
        if self.it_exist():
            if amount <= 0:
                raise ValueError('Amount must be greater than 0')
            self.balance += amount

    def get_balance(self):
        return self.balance

    def check_balance(self, pin):
        return self.balance == pin

    def transfer(self, amount, receiver, sender_pin):
        if sender_pin != self.pin:
            raise PermissionError('Current PIN does not match')
        if amount <= 0:
            raise ValueError('Amount must be greater than 0')
        if amount > self.balance:
            raise ValueError('Amount cannot be greater than balance')
        self.balance -= amount
        receiver.balance += amount