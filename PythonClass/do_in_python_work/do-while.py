while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    total_sum = num1 + num2
    print(f"The total sum is: {total_sum}")

    ask = input("Do you want to perform another task? (y/n): ")
    if ask.lower() != 'y':
        break