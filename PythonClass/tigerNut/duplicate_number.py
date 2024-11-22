def get_duplicate_number(numbers):
	for value in range(len(numbers)):
		for digit in range(value + 1, len(numbers)):
			if numbers[value] == numbers[digit]:
				print(numbers[value], end = " ")
	return True