import unittest
from Functions.account import Account

class TestAccount(unittest.TestCase):
    def test_That_account_exist(self):
        account_number = "ACC001"
        pin = "1234"
        name = "stephen"
        account = Account(account_number, pin, name)
        self.assertTrue(account.it_exist())

    def test_That_account_does_not_exist(self):
        account_number = None
        pin = None
        name = None
        account = Account(account_number, pin, name)
        self.assertTrue(account.not_exist())

    def test_that_account_can_add_money(self):
        account_number = "ACC001"
        pin = "1234"
        name = "stephen"
        account = Account(account_number, pin, name)
        self.assertEqual(account.get_balance(), 0)
        account.deposit(1000)
        self.assertEqual(account.get_balance(), 1000)

    def test_negative_adding(self):
        account_number = "ACC001"
        pin = "1234"
        name = "stephen"
        account = Account(account_number, pin, name)
        with self.assertRaises(ValueError) as context:
            account.deposit(-1000)
        self.assertIn("Deposit amount must be greater than 0", str(context.exception))

    def test_check_balance(self):
        account_number = "ACC001"
        pin = "1234"
        name = "stephen"
        account = Account(account_number, pin, name)
        account.deposit(1000)
        self.assertEqual(account.get_balance(), 1000)
        self.assertEqual(account.check_balance(pin), 1000)

        with self.assertRaises(PermissionError):
            account.check_balance("wrong")

    def test_that_account_can_transfer_money(self):
        sender_account_number = "ACC001"
        sender_pin = "1234"
        sender_name = "stephen"
        receiver_account_number = "ACC002"
        receiver_pin = "5678"
        receiver_name = "daniel"

        sender = Account(sender_account_number, sender_pin, sender_name)
        receiver = Account(receiver_account_number, receiver_pin, receiver_name)

        sender.deposit(1000)
        self.assertEqual(sender.get_balance(), 1000)
        self.assertEqual(receiver.get_balance(), 0)

        sender.transfer(500, receiver, sender_pin)
        self.assertEqual(sender.get_balance(), 500)
        self.assertEqual(receiver.get_balance(), 500)

    def test_that_account_cannot_transfer_more_than_the_actual_balance(self):
        sender_account_number = "ACC001"
        sender_pin = "1234"
        sender_name = "stephen"
        receiver_account_number = "ACC002"
        receiver_pin = "5678"
        receiver_name = "daniel"

        sender = Account(sender_account_number, sender_pin, sender_name)
        receiver = Account(receiver_account_number, receiver_pin, receiver_name)

        sender.deposit(500)
        with self.assertRaises(ValueError) as context:
            sender.transfer(600, receiver, sender_pin)
        self.assertIn("Amount cannot be greater than balance", str(context.exception))
        self.assertEqual(sender.get_balance(), 500)
        self.assertEqual(receiver.get_balance(), 0)

    def test_that_account_cannot_transfer_with_invalid_pin(self):
        sender_account_number = "ACC001"
        sender_pin = "1234"
        sender_name = "stephen"
        receiver_account_number = "ACC002"
        receiver_pin = "5678"
        receiver_name = "daniel"
        wrong_pin = "1111"

        sender = Account(sender_account_number, sender_pin, sender_name)
        receiver = Account(receiver_account_number, receiver_pin, receiver_name)

        sender.deposit(500)
        with self.assertRaises(PermissionError) as context:
            sender.transfer(100, receiver, wrong_pin)
        self.assertIn("Invalid PIN", str(context.exception))
        self.assertEqual(sender.get_balance(), 500)
        self.assertEqual(receiver.get_balance(), 0)

    def test_that_account_cannot_transfer_negative_amount(self):
        sender_account_number = "ACC001"
        sender_pin = "1234"
        sender_name = "stephen"
        receiver_account_number = "ACC002"
        receiver_pin = "5678"
        receiver_name = "daniel"

        sender = Account(sender_account_number, sender_pin, sender_name)
        receiver = Account(receiver_account_number, receiver_pin, receiver_name)

        sender.deposit(1000)
        with self.assertRaises(ValueError) as context:
            sender.transfer(-500, receiver, sender_pin)
        self.assertIn("Transfer amount must be greater than 0", str(context.exception))

    def test_withdraw_success(self):
        account_number = "ACC001"
        pin = "1234"
        name = "stephen"
        account = Account(account_number, pin, name)
        account.deposit(1000)
        account.withdraw(500, pin)
        self.assertEqual(account.get_balance(), 500)

    def test_withdraw_negative_amount(self):
        account_number = "ACC001"
        pin = "1234"
        name = "stephen"
        account = Account(account_number, pin, name)
        account.deposit(1000)
        with self.assertRaises(ValueError) as context:
            account.withdraw(-500, pin)
        self.assertIn("Withdrawal amount must be greater than 0", str(context.exception))

    def test_withdraw_invalid_pin(self):
        account_number = "ACC001"
        pin = "1234"
        name = "stephen"
        account = Account(account_number, pin, name)
        account.deposit(1000)
        with self.assertRaises(PermissionError) as context:
            account.withdraw(500, "wrong")
        self.assertIn("Invalid PIN", str(context.exception))

    def test_withdraw_insufficient_balance(self):
        account_number = "ACC001"
        pin = "1234"
        name = "stephen"
        account = Account(account_number, pin, name)
        account.deposit(1000)
        with self.assertRaises(ValueError) as context:
            account.withdraw(1500, pin)
        self.assertIn("Amount cannot be greater than balance", str(context.exception))

    def test_update_pin_success(self):
        account_number = "ACC001"
        old_pin = "1234"
        new_pin = "4321"
        name = "stephen"
        account = Account(account_number, old_pin, name)
        account.deposit(1000)
        account.update_pin(old_pin, new_pin)
        self.assertEqual(account.pin, new_pin)
        self.assertEqual(account.check_balance(new_pin), 1000)

    def test_update_pin_invalid_old_pin(self):
        account_number = "ACC001"
        old_pin = "1234"
        wrong_old_pin = "0000"
        new_pin = "4321"
        name = "stephen"
        account = Account(account_number, old_pin, name)
        with self.assertRaises(PermissionError) as context:
            account.update_pin(wrong_old_pin, new_pin)
        self.assertIn("Invalid PIN", str(context.exception))

    def test_update_pin_empty_new_pin(self):
        account_number = "ACC001"
        old_pin = "1234"
        new_pin = ""
        name = "stephen"
        account = Account(account_number, old_pin, name)
        with self.assertRaises(ValueError) as context:
            account.update_pin(old_pin, new_pin)
        self.assertIn("New PIN cannot be empty", str(context.exception))

if __name__ == '__main__':
    unittest.main()
