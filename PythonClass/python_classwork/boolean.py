def get_boolean(value):

	return[True if i % 2 == 0 else False for i in value]
value = [10,3,7,1,9,4,2,8,5,6]
print(get_boolean(value))