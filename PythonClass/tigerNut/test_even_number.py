import unittest

import even_number

class Testevennumber(unittest.TestCase):
	def test_check_if_even_number_exist(self):
		even_number.get_even_number([56, 6])
	
	def test_even_number(self):
		number = [1,2,3,4,5]
		value = even_number.get_even_number(number)
		expected = 6
		self.assertEqual(value,expected)

	
	def test_even_number_poitive(self):
		number = [1,2,3,4,5]
		value = even_number.get_even_number(number)
		expected = 6
		self.assertEqual(value,expected)


import odd_digit

class Testoddnumber(unittest.TestCase):
	def test_check_if_get_odd_number_exit(self):
		odd_digit.get_odd_number([23, 4])

	def test_odd_number(self):
		positive = [1,2,3,4,5]
		digit = odd_digit.get_odd_number(positive)
		expected = 9
		self.assertEqual(digit,expected)

	def test_odd_number_positive(self):
		positive = [1,2,3,4,5]
		digit = odd_digit.get_odd_number(positive)
		expected = 9
		self.assertEqual(digit,expected)

import sum_digit

class Testsumdigit(unittest.TestCase):
	def test_check_if_get_sum_number_exit(self):
		sum_digit.get_sum_number([5, 6])

	def test_sum_digit(self):
		value = [1,2,3,4,5]
		number = sum_digit.get_sum_number(value)
		expected = 15
		self.assertEqual(number,expected)

	def test_sum_digit_positive(self):
		value = [1,2,3,4,5]
		number = sum_digit.get_sum_number(value)
		expected = 15
		self.assertEqual(number,expected)

import merge_and_sort

class Testmergeandsort(unittest.TestCase):
	def test_merge_and_sort(self):
		number = [3,4,9,10]
		digit = [1, 5, 7, 8,0,-6]
		value = merge_and_sort.get_merge_and_sort(number,digit)
		expected = [-6,0,1,3,4,5,7,8,9,10]
		self.assertEqual(value,expected)
		print(expected)

import duplicate_number

class Testduplicatenumber(unittest.TestCase):
	def test_check_if_get_duplicate_number_exit(self):
		duplicate_number.get_duplicate_number([False])

	def test_duplicate_number(self):
		numbers = [1, 2, 3, 4, 5, 2]
		value = duplicate_number.get_duplicate_number(numbers)
		expected = True
		self.assertEqual(value,expected)

	def test_duplicate_number_positive(self):
		numbers = [1, 2, 3, 4, 5, 2]
		value = duplicate_number.get_duplicate_number(numbers)
		expected = True
		self.assertEqual(value,expected)

import vowel_to_string

class Testvoweltostring(unittest.TestCase):
	def test_check_if_get_count_vowels_exit(self):
		vowel_to_string.get_count_vowels(["5"])

	def test_vowel_to_string(self):
		word = "python is sweet"
		string = vowel_to_string.get_count_vowels(word)
		expected = 4
		self.assertEqual(string,expected)

	def test_vowel_to_string_positive(self):
		word = "python is sweet"
		string = vowel_to_string.get_count_vowels(word)
		expected = 4
		self.assertEqual(string,expected)

	def test_vowel_to_string(self):
		empty_string = ""
		result = vowel_to_string.get_count_vowels(empty_string)
		expected = 0
		self.assertEqual(result,expected)

	def test_vowel_to_string(self):
		no_vowel = "bcdfghjklmnpqrstvwxyz"
		result = vowel_to_string.get_count_vowels(no_vowel)
		expected = 0
		self.assertEqual(result,expected)


import palindrome_to_string

class Testpalindrometostring(unittest.TestCase):
	
	def test_palindrome_to_string(self):
		word = "madam"
		strings = palindrome_to_string.get_is_palindrome(word)
		expected = True
		self.assertEqual(strings,expected)


	def test_palindrome_to_string(self):
		words = "racecar"
		letter = palindrome_to_string.get_is_palindrome(words)
		expected = True
		self.assertEqual(letter,expected)


import prime_number

class Testprimenumber(unittest.TestCase):

	def test_get_is_prime(self):
		number = 7
		value = prime_number.get_is_prime(number)
		expected = True
		self.assertEqual(value,expected)

	def test_get_is_prime(self):
		numbers = 10
		values = prime_number.get_is_prime(numbers)
		expected = False
		self.assertEqual(values,expected)


import average_number

class Testaveragenumber(unittest.TestCase):
	def test_check_if_get_calculate_average_exit(self):
		average_number.get_calculate_average([26.0])


	def test_get_calculate_average(self):
		number = [10,20,30,40]
		digit = average_number.get_calculate_average(number)
		expected = 25.0
		self.assertEqual(digit,expected)