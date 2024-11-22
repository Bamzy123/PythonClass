def get_odd_number(digit):
	total = 0

	for number in digit:
		if number % 2 != 0:
			total += number
	return total