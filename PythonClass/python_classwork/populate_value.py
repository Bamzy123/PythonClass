"""
def populate_value():

	my_list = []

	for number in range(1, 6):
		my_list.append(number)
	return my_list
result = populate_value()
print(result)


def stephen():

	return(total([1,2,3,4,5]))

def total(number):

	total = 0
	for i in number:
		total = i + total
	return total


def cube_root():
	my_list = [1,2,3,4,5]
	cube_list = []
	for number in my_list:
		cube_list.append(number**3)
	return cube_list


print(cube_root())

def cube_root():
	my_list = [1,2,3,4,5]
	cube_list = [number**3 for number in my_list]
	return cube_list
result = cube_root()

print(result)

def cube_root():
	number = [1,2,3,4,5]
	return[(i**3) for i in number]
print(cube_root())


def sum_even_number():
	numbers = [2, 7, 9, 17, 19, 2, 10]
	return sum([value for value in numbers if value % 2 == 0])
print(sum_even_number())

def odd_number():
	value = [2, 7, 9, 17, 19, 2, 10]
	return sum([number for number in value if number % 2 != 0])
print(odd_number())
"""