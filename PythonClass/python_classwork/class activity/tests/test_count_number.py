import unittest
from corn import count_number

class MyTestCase(unittest.TestCase):

    def test_for_expected_output_for_semicolon_africa(self):
        actual = count_number.count_number('semicolon.africa')
        expect = {'s': 1, 'e': 1, 'm': 1, 'i': 2, 'c': 2, 'o': 2, 'l': 1, 'n': 1,
                  '.': 1, 'a': 2, 'f': 1, 'r': 1}
        self.assertEqual(actual, expect)
if __name__ == '__main__':
    unittest.main()