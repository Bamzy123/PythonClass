def get_squared_odd():
    number = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
    
    return [i**2 for i in number if i % 2 != 0]

print(get_squared_odd())  