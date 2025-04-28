import unittest

from corn.special_character import remove_special_characters

class TestSpecialCharacter(unittest.TestCase):
    def test_remove_special_characters_hello(self):
        self.assertEqual(remove_special_characters("he,ll.o"), "hello")

    def test_remove_special_characters_python123(self):
        self.assertEqual(remove_special_characters("!@#Python123"), "Python123")

    def test_remove_special_characters_Cisgreat(self):
        self.assertEqual(remove_special_characters("C++ is great!"), "Cisgreat")

    def test_remove_special_characters_abcd(self):
        self.assertEqual(remove_special_characters("a_b-c=d"), "abcd")

    def test_remove_special_characters_HelloWorld(self):
        self.assertEqual(remove_special_characters("Hello, World!"), "HelloWorld")


if __name__ == "__main__":
    unittest.main()