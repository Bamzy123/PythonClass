def get_merge_and_sort(number, digit):
    value1 = number + digit
   
    value1.sort()

    return value1

number = [3, 4, 9, 10]
digit = [1, 5, 7, 8]

result = get_merge_and_sort(number, digit)
print(result)
