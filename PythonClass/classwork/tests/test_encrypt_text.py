import unittest
from PythonClass.classwork import encrypt_text

class TestSetExercise(unittest.TestCase):
    def test_that_the_class_exists(self):
        pass

    def test_encrypt_text(self):
        actual = encrypt_text.get_encrypt_text("Hello, World")
        expected = "Uryyb, Jbeyq"

    def test_numbers_in_string(self):
        actual = encrypt_text.get_encrypt_text("Hello123World")
        expected = "Uryyb123Jbeyq"
        self.assertEqual(actual, expected)

    def test_only_numbers(self):
        actual = encrypt_text.get_encrypt_text("1234567890")
        expected = "1234567890"
        self.assertEqual(actual, expected)

    def test_numbers_with_symbols(self):
        actual = encrypt_text.get_encrypt_text("Test123!@#")
        expected = "Grfg123!@#"
        self.assertEqual(actual, expected)