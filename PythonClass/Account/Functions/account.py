class Account:
    def __init__(self, account_number, pin, name):
        self.account_number = account_number
        self.pin = pin
        self.name = name
        self.balance = 0

    def it_exist(self):
        return (
            self.account_number is not None and
            self.pin is not None and
            self.name is not None
        )

    def not_exist(self):
        return not self.it_exist()

    def deposit(self, amount):
        if not self.it_exist():
            raise ValueError("Account does not exist")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self.balance += amount

    def get_balance(self):
        return self.balance

    def check_balance(self, pin):
        if pin != self.pin:
            raise PermissionError("Invalid PIN")
        return self.balance

    def transfer(self, amount, receiver, sender_pin):
        if sender_pin != self.pin:
            raise PermissionError("Invalid PIN")
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than 0")
        if amount > self.balance:
            raise ValueError("Amount cannot be greater than balance")
        self.balance -= amount
        receiver.balance += amount

    def withdraw(self, amount, pin):
        if pin != self.pin:
            raise PermissionError("Invalid PIN")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        if amount > self.balance:
            raise ValueError("Amount cannot be greater than balance")
        self.balance -= amount

    def update_pin(self, old_pin, new_pin):
        if old_pin != self.pin:
            raise PermissionError("Invalid PIN")
        if not new_pin or new_pin.strip() == "":
            raise ValueError("New PIN cannot be empty")
        self.pin = new_pin