my_dict = {"name":"Alice","age": 25}

new_data = {"city":"New York","age": 26}

for Key,value in new_data.items():

	my_dict[Key] = value

print(my_dict)