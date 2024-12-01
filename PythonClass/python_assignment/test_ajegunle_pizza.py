import unittest
from unittest.mock import patch
import math
import AjegunlePizza  # Replace with the correct import path

class TestPizzaOrder(unittest.TestCase):

    def test_valid_order(self):
        # Test case: Order 10 slices of "Sapa size" pizza
        result = calculate_order(10, 1)
        self.assertEqual(result["pizza_name"], "Sapa size")
        self.assertEqual(result["price_per_box"], 2500)
        self.assertEqual(result["number_of_boxes"], 3)
        self.assertEqual(result["leftovers"], 2)
        self.assertEqual(result["total_price"], 7500)

    def test_exact_slices(self):
        # Test case: Order 12 slices of "Odogwu" pizza
        result = calculate_order(12, 4)
        self.assertEqual(result["pizza_name"], "Odogwu")
        self.assertEqual(result["number_of_boxes"], 1)
        self.assertEqual(result["leftovers"], 0)

    def test_invalid_pizza_type(self):
        # Test case: Invalid pizza type selected
        with self.assertRaises(ValueError):
            calculate_order(10, 5)

    def test_zero_people(self):
        # Test case: Order for 0 people
        result = calculate_order(0, 1)
        self.assertEqual(result["number_of_boxes"], 0)
        self.assertEqual(result["total_price"], 0)

    def test_negative_people(self):
        # Test case: Invalid number of people
        with self.assertRaises(ValueError):
            calculate_order(-1, 1)

    @patch("builtins.input", side_effect=["10", "2"])  # Mock user input
    @patch("builtins.print")  # Mock print function
    def test_user_interaction(self, mock_print, mock_input):
        # Call the main function, which will call the `input` and `print` functions
        from your_script_name import main  # Replace with the correct import path
        main()
        
        # Check that print was called with expected values
        mock_print.assert_any_call("You ordered for the Small Money pizza costing 2900 per box.")
        mock_print.assert_any_call("Number of boxes of pizza to buy: 2 boxes")
        mock_print.assert_any_call("Number of leftover slices after serving: 0 slices")
        mock_print.assert_any_call("Total price: 5800 Naira")

if __name__ == "__main__":
    unittest.main()
