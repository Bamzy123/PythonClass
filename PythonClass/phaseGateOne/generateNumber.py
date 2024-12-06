"""
Write a program in Python that generates two integers under 100 and prompts the user to enter the sum of these two integers. The program then reports true if the answer is correct or false otherwise.

pseudocode

1. create a function call generate number
2. assign random.randint(1, 99) to num1
3. assign random.randint(1, 99) to num2
4. prompt user to enter answer
5. sum num1 and num2 and assign it to a variable correct answer
6. if user_answer equals correct_answer
7. print true
8. else false
"""


import random 
def generate_number():

    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)

    print(f"What is the sum of {num1} + {num2}?")
    user_answer = int(input("Your answer: "))

   
    correct_answer = num1 + num2

  
    if user_answer == correct_answer:
        print("True")
    else:
        print("False")

generate_number()


