"""import math

def get_divide_or_square(number):
	if number 
"""

import math

def divide_or_square(number):

    if not isinstance(number, (int, float)):
        return "Input must be a number."
    

    if number < 0:
        return "Cannot calculate the square root of a negative number."
    

    if number % 5 == 0:
        return round(math.sqrt(number), 2)
    else:
        return number % 5

print(divide_or_square(10))
print(divide_or_square(7))
print(divide_or_square(-5))
print(divide_or_square("a"))