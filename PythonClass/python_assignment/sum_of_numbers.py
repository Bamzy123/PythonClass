def print_sum_of_numbers(numbers):

	total = 0

	for digit in numbers:

		total += digit

	print("The sum of list is: ", total)

numbers = [1,2,3,4,5]
print_sum_of_numbers(numbers)