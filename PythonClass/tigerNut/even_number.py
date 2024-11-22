def get_even_number(number_list):
	total = 0
	for number in number_list:
		if number % 2 == 0:
			total += number
	return total

