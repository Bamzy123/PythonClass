import unittest

from school_management.abstract_class import User


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User("john", "doe", "stephenomotos@gmail.com")

    def test_to_create_a_user(self):
        assert self.user.get_first_name() == "john"
        assert self.user.get_last_name() == "doe"
        assert self.user.get_email() == "stephenomotos@gmail.com"
        assert self.user.get_full_name() == "john doe"

    def test_for_user_information(self):
        assert self.user.user_info()
        pass
if __name__ == '__main__':
    unittest.main()
