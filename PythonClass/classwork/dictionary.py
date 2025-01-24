def dictionary(Keys, values):

	my_dict = {}


	for Key,value in zip(Keys,values):
		my_dict[Key] = value

	return my_dict

Keys = ["name", "age", "city"]

values = ["Alice", "25", "Lagos"]

print(dictionary(Keys,values))

def dictionary(Keys, Values)