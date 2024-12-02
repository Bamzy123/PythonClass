"""
write a program that prompts the user to enter three integers and displays them in increasing order.

here is a sample run
enter first number:6
enter second number:4
enter third number:7
output:4,6,7

pseudocode
1. Prompt the user to enter three integers
2. Create a list of the numbers
3. Sort the list in increasing order
4. Display the numbers in increasing order
"""

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

numbers = [first_number, second_number, third_number]

numbers.sort()

print(f"Output: {numbers[0]},{numbers[1]},{numbers[2]}")
