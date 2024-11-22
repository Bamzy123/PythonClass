def get_calculate_average(numbers):

    if len(numbers) == 0:
        return 0

    total_sum = sum(numbers)
    
    average = total_sum / len(numbers)
    
    return average

print(get_calculate_average([10, 20, 30, 40]))
