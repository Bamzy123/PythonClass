def factor_of(integer):

	if integer <= 0:

		return 0

	factors = 0

	for number in range(1, integer + 1):
		if integer % number == 0:

			factors += 1
	return factors

integer = int (input("Enter a number: "))

result = factor_of(integer)

print("The factor is: ",result)