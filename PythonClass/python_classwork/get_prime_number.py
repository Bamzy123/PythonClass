def get_prime_number(number):
	if number <= 1:
		return False

	for numbers in range(2, int(number**0.5) + 1):
		if number % numbers == 0:
			print()
number = int(input("Enter ya number: "))

result = get_prime_number(number)

print(result)
