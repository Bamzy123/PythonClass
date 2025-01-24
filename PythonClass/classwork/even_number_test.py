import unittest

import even_nmber

class evennumber(unittest.TestCase):
	def test_check_that_is_even_number_exist(self):
		even_nmber.is_even_number([4])

	def test_is_even_number(self):
		number = [2, 7, 9, 17, 19, 2, 10, 10]
		value = even_nmber.is_even_number(number)
		expected = 24
		self.assertEqual(value,expected)



import get_prime_number

class primenumber(unittest.TestCase):
	def test_that_get_prime_number(number):
		pass

import populate_value

class evencount(unittest.TestCase):
	def test_check_that_even_count_exist(self):
		pass