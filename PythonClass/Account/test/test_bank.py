import unittest

from Functions import bank
from Functions.account import Account


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = bank.Banks()

        first_acct_pin = "1234"
        first_acct_name = "stephen"

        second_acct_pin = "5678"
        second_acct_name = "john"

        self.acct1 = self.bank.create_account(first_acct_pin, first_acct_name)
        self.acct2 = self.bank.create_account(second_acct_pin, second_acct_name)

    def test_account_creation(self):
        self.assertEqual(len(self.bank.accounts), 2)
        self.assertEqual(self.acct1, 1000)
        self.assertEqual(self.acct2, 1001)

        with self.assertRaises(ValueError):
            pin = "9999"
            name = "stephen"
            self.bank.create_account(pin, name)

    def test_bank_can_deposit(self):
        self.bank.deposit(self.acct1, 1000)
        self.assertEqual(self.bank.get_account(self.acct1).get_balance(), 1000)

    def test_bank_can_withdraw(self):
        pin = "1234"
        self.bank.deposit(self.acct1, 1000)
        self.bank.withdraw(self.acct1, 500, pin)
        self.assertEqual(self.bank.get_account(self.acct1).get_balance(), 500)

    def test_bank_withdraw_invalid_pin(self):
        wrong_pin = "1111"
        self.bank.deposit(self.acct1, 1000)

        with self.assertRaises(PermissionError):
            self.bank.withdraw(self.acct1, 500, wrong_pin)

    def test_bank_withdraw_insufficient_funds(self):
        pin = "1234"
        self.bank.deposit(self.acct1, 1000)

        with self.assertRaises(ValueError):
            self.bank.withdraw(self.acct1, 1500, pin)

    def test_bank_can_transfer(self):
        sender_pin = "1234"
        self.bank.deposit(self.acct1, 1000)
        self.bank.transfer(self.acct1, self.acct2, 300, sender_pin)
        self.assertEqual(self.bank.get_account(self.acct1).get_balance(), 700)
        self.assertEqual(self.bank.get_account(self.acct2).get_balance(), 300)

    def test_bank_transfer_invalid_pin(self):
        sender_wrong_pin = "1111"
        self.bank.deposit(self.acct1, 1000)

        with self.assertRaises(PermissionError):
            self.bank.transfer(self.acct1, self.acct2, 300, sender_wrong_pin)

    def test_bank_pin_update(self):
        old_pin = "1234"
        new_pin = "5678"
        self.bank.deposit(self.acct1, 1000)
        self.bank.update_pin(self.acct1, old_pin, new_pin)
        self.assertEqual(self.bank.get_account(self.acct1).check_balance(new_pin), 1000)

        with self.assertRaises(PermissionError):
            self.bank.get_account(self.acct1).check_balance(old_pin)

if __name__ == '__main__':
    unittest.main()