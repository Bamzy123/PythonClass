"""import math

def get_divide_or_square(number):
	if number 
"""

import math

def divide_or_square(number):
    # Check if the input is a number
    if not isinstance(number, (int, float)):
        return "Input must be a number."
    
    # Handle negative numbers
    if number < 0:
        return "Cannot calculate the square root of a negative number."
    
    # Check if the number is divisible by 5
    if number % 5 == 0:
        return round(math.sqrt(number), 2)
    else:
        return number % 5

# Example usage
print(divide_or_square(10))  # Output: 3.16
print(divide_or_square(7))   # Output: 2
print(divide_or_square(-5))  # Output: Cannot calculate the square root of a negative number.
print(divide_or_square("a")) # Output: Input must be a number.