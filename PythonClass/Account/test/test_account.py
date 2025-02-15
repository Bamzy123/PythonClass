import unittest

from Functions.account import Account

class TestAccount(unittest.TestCase):
    def test_That_account_exist(self):
        pin = "1234"
        name = "stephen"
        account = Account(pin, name)
        self.assertTrue(account.it_exist())

    def test_That_account_does_not_exist(self):
        pin = "1234"
        name = "stephen"
        account = Account(pin, name)
        self.assertFalse(account.not_exist())

    def test_that_account_can_add_money(self):
        pin = "1234"
        name = "stephen"
        account = Account(pin, name)
        self.assertEqual(account.get_balance(), 0)
        account.add(1000)
        self.assertEqual(account.get_balance(), 1000)

    def test_negative_adding(self):
        pin = "1234"
        name = "stephen"
        account = Account(pin, name)
        with self.assertRaises(ValueError) as context:
            account.add(-1000)
            self.assertIn("Deposit amount must be greater than 0", str(context.exception))

    def test_check_balance(self):
        pin = "1234"
        name = "stephen"
        account = Account(pin, name)
        account.add(1000)
        self.assertEqual(account.get_balance(), 1000)
        self.assertEqual(account.check_balance(pin), 1000)

    def test_that_account_can_transfer_money(self):
        sender_pin = "1234"
        sender_name = "stephen"
        receiver_pin = "5678"
        receiver_name = "daniel"

        sender = Account(sender_pin, sender_name)
        receiver = Account(receiver_pin, receiver_name)

        sender.add(1000)
        self.assertEqual(sender.get_balance(), 1000)
        self.assertEqual(receiver.get_balance(), 0)

        sender.transfer(500, receiver, sender_pin)
        self.assertEqual(sender.get_balance(), 500)
        self.assertEqual(receiver.get_balance(), 500)

    def test_that_account_cannot_transfer_more_than_the_actual_balance(self):
        sender_pin = "1234"
        sender_name = "stephen"
        receiver_pin = "5678"
        receiver_name = "daniel"

        sender = Account(sender_pin, sender_name)
        receiver = Account(receiver_pin, receiver_name)

        with self.assertRaises(ValueError) as context:
            sender.transfer(600, receiver, sender_pin)
            self.assertIn("Deposit amount must be greater than 0", str(context.exception))
            self.assertEqual(sender.get_balance(), 500)
            self.assertEqual(receiver.get_balance(), 500)

    def test_that_account_cannot_transfer_with_invalid_pin(self):
        sender_pin = "1234"
        sender_name = "stephen"
        receiver_pin = "5678"
        receiver_name = "daniel"
        wrong_pin = "1111"

        sender = Account(sender_pin, sender_name)
        receiver = Account(receiver_pin, receiver_name)

        with self.assertRaises(PermissionError) as context:
            receiver.transfer(100, receiver, wrong_pin)
            self.assertIn("Invalid PIN", str(context.exception))
            self.assertEqual(sender.get_balance(), 500)
            self.assertEqual(receiver.get_balance(), 500)

    def test_that_account_cannot_transfer_negative_amount(self):
        sender_pin = "1234"
        sender_name = "stephen"
        receiver_pin = "5678"
        receiver_name = "daniel"

        sender = Account(sender_pin, sender_name)
        receiver = Account(receiver_pin, receiver_name)

        with self.assertRaises(ValueError) as context:
            sender.transfer(-500, receiver, sender_pin)
            self.assertIn("Amount must be greater than 0", str(context.exception))

if __name__ == '__main__':
    unittest.main()