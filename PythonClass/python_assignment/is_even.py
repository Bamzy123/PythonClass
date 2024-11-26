def is_even(integer):

	if integer % 2 == 0:

		return True

	elif integer % 2 != 0:

		return False

integer = int(input("Please enter any number: "))

result = is_even(integer)
print(result)