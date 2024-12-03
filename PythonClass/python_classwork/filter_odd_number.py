"""
def is_odd(x):

	return x % 2 != 0

numbers = [10,3,7,1,9,4,2,8,5,6]

holder = list(filter(is_odd, numbers))

print(holder)


numbers  = [10,3,7,1,9,4,2,8,5,6]

holder = list(filter(lambda x:x % 2 != 0, numbers))

print(holder)


def number(x, y):

	return x + y

add_number = lambda x, y:x + y

result = add_number(5, 2)

print(result)


def square(x):

	return x + x

numbers = [2, 3, 4, 5, 6, 7, 8]

square_number = map(square, numbers)

print(list(square_number))
"""

numbers = [2, 3, 4, 5, 6, 7, 8]

square_number = map(lambda num:num * 2, numbers)

print(list(square_number))