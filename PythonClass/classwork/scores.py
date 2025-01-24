number_of_pass = 0
number_of_fail = 0

for count in range (1, 16):
	student = int(input("Enter your score: "))
	if student >= 45:
		number_of_pass+=1
	else:
		number_of_fail+=1

print(f"The number of pass is: {number_of_pass}")

print(f"The number of fail is: {number_of_fail}")