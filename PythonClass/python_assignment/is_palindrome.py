def is_palindrome(number):

	return str(number) == str (number)[:: - 1]

number = int(input("Enter a number: "))

result = is_palindrome(number)

print("The palindrome number is: ", result)