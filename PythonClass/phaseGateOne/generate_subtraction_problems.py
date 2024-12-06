"""
1. Generate random subtraction problems:
	ensure the minuend(first number) is greater than the subtrahend(second number) to avoid negative results.
2. Presents problems in correct order:
	Display each problem sequentially.
3. Allows user to take up to 10 questions:
	Give the user 1 attempt per problem
4. Calculate and display a final score:
	Determine the score based on the number of correct answers.
5. Measure and display time taken:
	Record the start and end times to calculate the total time in seconds.

pseudocode

1. import random
2. import time
3. create a function called generate subtraction problems
4. Correct number equals zero
5. total questions equal ten
6. record the start time
7. loop through ten questions
8. Generate a random minuend (first number) and subtrahend (second number)
9. Ensure the minuend is between ten and hundred
10. Ensure the subtrahend is smaller than the minuend
11. Display the problem to solve
12. Get the  user's answer
13. Check if the answer is correct
14. Record the end of start time
15. Calculate the total time taken
16. Display the final score and time taken
17. Call the function to start the quiz 
"""


import random
import time

def generate_subtraction_problems():
    correct_answers = 0
    total_questions = 10
    
    start_time = time.time()
    
    for number in range(1, total_questions + 1):

        minuend = random.randint(10, 100)
        subtrahend = random.randint(1, minuend - 1)
        
 
        print(f"Problem {number}: {minuend} - {subtrahend} = ")
        

        user_answer = int(input("Your answer: "))
        

        if user_answer == (minuend - subtrahend):
            correct_answers += 1
    
    end_time = time.time()
    

    time_taken = round(end_time - start_time, 2)
    
    print(f"\nYour final score is {correct_answers} out of {total_questions}.")
    print(f"Total time taken: {time_taken} seconds.")

generate_subtraction_problems()
