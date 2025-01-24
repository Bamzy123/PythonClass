input_list = [1, 2, 3, 6, 8, 10, 1]
output = [number for number, value in enumerate(input_list) if 3 < value <= 8]
print(output)
