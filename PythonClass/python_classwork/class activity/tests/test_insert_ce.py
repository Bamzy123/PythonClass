import unittest
from corn.insert import insert_ce

class TestInsert(unittest.TestCase):
    def test_insert_ce_helloo(self):
        self.assertEqual(insert_ce("helloo"), "helceloo")

    def test_insert_ce_joy(self):
        self.assertEqual(insert_ce("joy"), "joyce")

    def test_insert_ce_test(self):
        self.assertEqual(insert_ce("test"), "tecest")

    def test_insert_ce_abcd(self):
        self.assertEqual(insert_ce("abcd"), "abcecd")

    def test_insert_ce_a(self):
        self.assertEqual(insert_ce("a"), "ace")

if __name__ == "__main__":
    unittest.main()
