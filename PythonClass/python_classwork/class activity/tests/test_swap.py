import unittest

from corn.swap import swap_first_last, merge_and_swap


class TestStringSwap(unittest.TestCase):
    def test_swap_first_last_abd(self):
        self.assertEqual(swap_first_last("abc"), "cba")

    def test_swap_first_last_xyz(self):
        self.assertEqual(swap_first_last("xyz"), "zyx")

    def test_swap_first_last_abd_a(self):
        self.assertEqual(swap_first_last("a"), "a")

    def test_swap_first_last_empty(self):
        self.assertEqual(swap_first_last(""), "")

    def test_merge_and_swap_abc_xyz(self):
        self.assertEqual(merge_and_swap("abc", "xyz"), "cba zyx")

    def test_merge_and_swap_hello_world(self):
        self.assertEqual(merge_and_swap("hello", "world"), "oellh dorlw")

    def test_merge_and_swap_a_b(self):
        self.assertEqual(merge_and_swap("a", "b"), "a b")

    def test_merge_and_swap_empty_string_test(self):
        self.assertEqual(merge_and_swap("", "test"), " test")

if __name__ == "__main__":
    unittest.main()