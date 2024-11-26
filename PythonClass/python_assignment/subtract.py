def subtract(first_integer, second_integer):

	return abs(first_integer - second_integer)

first_integer = int (input("Enter a number: "))

second_integer = int (input("Enter a number: "))

result = subtract(first_integer, second_integer)

print("The positive difference: ", result)