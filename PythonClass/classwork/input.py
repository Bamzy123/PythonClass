"""
input: 4
dictionaty = {}
dictionaty[1] = n
dictionaty[2] = ?
return dictionaty

output: {1:4, 2:16}
"""

def get_generate_squares(n):

    result = [f"{i}:{i**4}" for i in range(1, 3)]
    return result


input_number = 4
output = get_generate_squares(input_number)
print(output)




