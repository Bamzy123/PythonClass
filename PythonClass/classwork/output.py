"""
input: "73H2AdsdF439dm"

output: [2,4]
"""

def even_number(input_string):
    even_digits = [int(char) for char in input_string if char.isdigit() and int(char) % 2 == 0]
    if not even_digits:
        return []
    #smallest = min(even_digits)
    #largest = max(even_digits)
    #return [input_string]


input_string = "73H2AdsdF439dm"
output = even_number(input_string)
print(output)
