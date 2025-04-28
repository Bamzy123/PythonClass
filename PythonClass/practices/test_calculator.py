from unittest import TestCase

import unittest

from calculator import evaluate_expression

class Test(TestCase):
    def test_evaluate_expression(self):
        self.assertEqual(evaluate_expression("2*2"), 4)

    def test_with_parentheses(self):
        self.assertEqual(evaluate_expression("(2 + 2) * (2 + 2)"), 16)

    def test_operator_precedence(self):
        self.assertEqual(evaluate_expression("2 + 2 * 2 + 2"), 8)

    def test_invalid_expression(self):
        result = evaluate_expression("2 + ")
        self.assertTrue("Error" in result)

    def test_with_division(self):
        self.assertEqual(evaluate_expression("10 / 2"), 5.0)

    def test_with_subtraction(self):
        self.assertEqual(evaluate_expression("10 - 3 - 2"), 5)

if __name__ == "__main__":
    unittest.main()