def get_string_number(word_list, number):

	return[word for word in word_list if len(word) >= number]

word_list = ["apple", "fish", "orange", "ice", "lime"]

print(get_string_number(["apple", "fish", "orange", "ice", "lime"], 5))