def average(first, *args):
	
	numbers = [first] + list(args)

	total_sum = sum(numbers)
	count = len(numbers)

	avg = total_sum / count

	return avg

result_one = average(55)
print(result_one)

result_two = average(55, 20, 10,40)
print(result_two)

try:
	result_three = average()
except TypeError as a:
	print(a)