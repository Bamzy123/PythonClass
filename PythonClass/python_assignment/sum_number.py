def sum_number(numbers):

	value = 0

	total = 0

	while value < len(numbers):

		total += numbers[value]

		value += 1
	
	return total

numbers = [2, 3, 4, 5, 6, 7]

result = sum_number(numbers)

print("The sum is: ", result)