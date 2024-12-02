"""
write a program that reads an integer between 0 and 1000 and add all the digits in the integer. example, if an integer is 932, the sum of all its digits is 14.


1. prompt the user to enter the number
2. make sure the number is not more than 1000
3. calculate the sum of digits
""" 
def sum_of_digits():
   
    number = int(input("Enter an integer between 0 and 1000: "))

    
    if 0 <= number <= 1000:
        
        digit_sum = sum(int(digit) for digit in str(number))
        print(f"The sum of all digits in {number} is {digit_sum}.")
    else:
        print("The number is out of range. Please enter a number between 0 and 1000.")

sum_of_digits()