def get_even_count(number):
	
	return len([i for i in number if i % 2 == 0])
number = [1,5,7,3,2,9,8,10]
print(get_even_count(number))