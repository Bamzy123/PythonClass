import math

def is_square(integer):

	return int(math.sqrt(integer)) ** 2 == integer

integer = int(input("Enter a number: "))

result = is_square(integer)

print(result)