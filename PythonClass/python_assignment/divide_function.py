def divide(numerator, denominator):

	if denominator == 0:

		return 0.0

	return numerator / denominator

numerator = float(input("Enter a number: "))

denominator = float(input("Enter a number: "))

result = divide(numerator, denominator)

print("The quotient: ", result)