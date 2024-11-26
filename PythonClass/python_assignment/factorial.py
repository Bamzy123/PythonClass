def factorial(number):

	answer = 1

	for value in range(1, number + 1):

		answer *= value

	return answer

number = int(input("Enter a number: "))

result = factorial(number)

print(f"The factorial of {number} is: {result}")