def get_palindrome(value):

	return[True if words == words[::-1] else False for words in value]
value = ['madam', 'apple', 'racecar']
print(get_palindrome(value))