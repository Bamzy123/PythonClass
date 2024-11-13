number = int(input("Enter a number: "))

for digit in range (1,number +1):
	for count in range (1,digit +1):
		print(count, end = " ")
	print()

for digit in range (number, 0, -1):
	for count in range (1, digit +1):
		print (count, end = " ")
	print()