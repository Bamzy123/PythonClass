def get_number_multiple(number):

	return[num ** 2 for num in range(1, number + 1)]

number = 5

print(get_number_multiple(number))