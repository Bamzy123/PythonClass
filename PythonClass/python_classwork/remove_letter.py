""" 
def remove_letter(letters):

	return ' '.join(filter(str.isdigit, letters))

letters = 'abc123def456'

print(remove_letter(letters))
"""
def remove_letter(letters):

	return ' '.join([char for char in letters if char.isdigit()])

letters = 'abc123def456'

print(remove_letter(letters))