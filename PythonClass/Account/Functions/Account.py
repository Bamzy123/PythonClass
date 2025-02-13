class Account:
    def __init__(self, pin, name):
        self.pin = pin
        self.name = name
        self.balance = 0

    def itExist(self):
        return self.pin is not None and self.name is not None

    def notExist(self):
        return not self.itExist()

    def add(self, amount):
        if self.itExist():
            if amount <= 0:
                raise ValueError('Amount must be greater than 0')
            self.balance += amount

    def getBalance(self):
        return self.balance