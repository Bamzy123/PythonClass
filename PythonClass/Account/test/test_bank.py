import unittest

from Functions import bank


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = bank.Banks()

    def test_that_bank_can_deposit(self):
        pin = "1234"
        name = "stephen"
        self.bank.create_account(pin, name)
        self.bank.deposit(1000, name)
        account = self.bank.find_account(name)
        self.assertIsNotNone(account)
        self.assertEqual(1000, account.get_balance())
if __name__ == '__main__':
    unittest.main()
