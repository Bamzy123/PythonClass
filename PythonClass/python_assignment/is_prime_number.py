def is_prime_number(integer):
	if integer <= 1:
		return False
	for number in range(2, int(integer**0.5) + 1):
		if integer % number == 0:
			return False
	return True

integer = int(input("Please enter ya number: "))

result = is_prime_number(integer)

print(result)