while True:
    number_one = int(input("Enter first number: "))
    number_two = int(input("Enter second number: "))
    total_sum = number_one + number_two
    print(f"The total sum is: {total_sum}")

    ask = input("Do you want to perform another task? (y/n): ")
    if ask.lower() != 'y':
        break