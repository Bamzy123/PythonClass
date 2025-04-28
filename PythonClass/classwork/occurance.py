numbers = [2, 2, 1, 3, 5, 5]
count_dict = {}
for number in numbers:
	if number in count_dict:
		count_dict[number] += 1
	else:
		count_dict[number] = 1

for key, value in count_dict.items():
	print(f'{key} : {value}')