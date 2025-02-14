import unittest

from Functions.account import Account

class TestAccount(unittest.TestCase):
    def test_That_account_exist(self):
        pin = "1234"
        name = "stephen"
        account = Account(pin, name)
        self.assertTrue(account.itExist())

    def test_That_account_does_not_exist(self):
        pin = "1234"
        name = "stephen"
        account = Account(pin, name)
        self.assertFalse(account.notExist())

    def test_that_account_can_add_money(self):
        pin = "1234"
        name = "stephen"
        account = Account(pin, name)
        self.assertEqual(account.getBalance(), 0)
        account.add(1000)
        self.assertEqual(account.getBalance(), 1000)

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
        self.assertEqual(account.getBalance(), 1000)
        account.check_balance(pin)
        self.assertEqual(account.check_balance(), 1000)
if __name__ == '__main__':
    unittest.main()