# import unittest
#
# from Functions import bank
# from Functions.account import Account
#
#
# class TestBank(unittest.TestCase):
#     def setUp(self):
#         self.bank = bank.Banks()
#
#         first_acct_pin = "1234"
#         first_acct_name = "stephen"
#
#         second_acct_pin = "5678"
#         second_acct_name = "john"
#
#         self.acct1 = self.bank.create_account(first_acct_pin, first_acct_name)
#         self.acct2 = self.bank.create_account(second_acct_pin, second_acct_name)
#
#     def test_account_creation(self):
#         self.assertEqual(len(self.bank.accounts), 2)
#         self.assertEqual(self.acct1,1000)
#         self.assertEqual(self.acct2, 1001)
#
#         with self.assertRaises(ValueError):
#
#             pin = "9999"
#             name = "stephen"
#             self.bank.create_account(pin, name)
#
#     def test_bank_can_deposit(self):
#         self.bank.deposit(self.acct1, 1000)
#         self.assertEqual(self.bank.get_account(self.acct1).deposited, 1000)
# if __name__ == '__main__':
#     unittest.main()
