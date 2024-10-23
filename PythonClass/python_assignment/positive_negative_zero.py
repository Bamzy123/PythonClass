positive_count = 0
negative_count = 0
zero_count = 0

for count in range(5):
	number = float(input(f"Enter number {count+1}: "))
	if number > 0:
	   positive_count +=1
	elif number < 0:
	   negative_count +=1
	else:
	   zero_count +=1

print(f"Number of positive: {positive_count}")
print(f"Number of negative: {negative_count}")
print(f"Number of zeros: {zero_count}")