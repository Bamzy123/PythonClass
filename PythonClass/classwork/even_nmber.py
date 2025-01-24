def is_even_number(integers):
    count = 0
    for integer in integers:
        if integer % 2 == 0:
            count += integer
    return count

integer_list = [2, 7, 9, 17, 19, 2, 8, 10]

result = is_even_number(integer_list)
print(result)