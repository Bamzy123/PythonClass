number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
number_three = int(input("Enter three number: "))

if (number_one == number_two) or (number_one == number_three) or (number_two == number_three):
   print("This is a palindrome.")
else:
   print("This is not a palindrome")