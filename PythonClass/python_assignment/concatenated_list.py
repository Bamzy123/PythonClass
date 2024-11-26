def concatenate(letters, numbers):

	result = letters + [str(value) for value in numbers]

	return result

letters = ["a", "b", "c"]

numbers = [1, 2, 3]

concatenated_list = concatenate(letters, numbers)

print("The concatenated list: ", concatenated_list)