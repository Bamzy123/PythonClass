
import random

number = random.randint(1, 10)
#print (number)
guess_input = 0

while guess_input != number:
	guess_input = int(input("Enter your guess number: "))
	if guess_input > number:
   		print("Too high, try again.")

	elif guess_input < number:
	   	print("Too low, try again.")

	else: 
		print("correct guess")
	   	
