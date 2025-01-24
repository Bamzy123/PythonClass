def remove_vowel(word_list):

	vowels = "aeiouAEIOU"
	return [' '.join([char for char in word if char not in vowels]) for word in word_list]

word_list = ["Orange", "Apple", "ice", "Beans", "Rice"]

print(remove_vowel(word_list))	