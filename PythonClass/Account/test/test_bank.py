import unittest

from Functions import bank
from Functions.account import Account


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = bank.Banks()
        first_acct_name = "stephen"
        first_acct_pin = "1234"
        second_acct_name = "john"
        second_acct_pin = "5678"
        self.acct1 = self.bank.create_account(first_acct_name, first_acct_pin)
        self.acct2 = self.bank.create_account(second_acct_name, second_acct_pin)

    def test_account_creation(self):
        self.assertEqual(len(self.bank.accounts), 2)
        self.assertEqual(self.acct1,1000)
        self.assertEqual(self.acct2, 1001)

        with self.assertRaises(ValueError):
            name = "stephen"
            pin = "9999"
            self.bank.create_account(name, pin)
if __name__ == '__main__':
    unittest.main()
