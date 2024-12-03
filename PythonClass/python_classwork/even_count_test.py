import unittest

import even_count

class evennumber(unittest.TestCase):
	def test_check_if_get_even_count_exist(self):
		even_count.get_even_count([5])


	def test_even_count(self):
		number = [1,5,7,3,2,9,8,10]
		value = even_count.get_even_count(number)
		expected = 3
		self.assertEqual(value, expected)

import boolean

class booleanvalue(unittest.TestCase):
	def test_check_if_get_boolean_exist(self):
		boolean.get_boolean([true])

	def test_get_boolean(self):
		number 