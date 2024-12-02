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
4. 
"""


import random
import time

# Function to generate subtraction problems and calculate score
def generate_subtraction_problems():
    correct_answers = 0
    total_questions = 10
    
    # Record the start time
    start_time = time.time()
    
    # Loop through 10 questions
    for i in range(1, total_questions + 1):
        # Generate a random minuend (first number) and subtrahend (second number)
        minuend = random.randint(10, 100)  # Ensure the minuend is between 10 and 100
        subtrahend = random.randint(1, minuend - 1)  # Ensure the subtrahend is smaller than the minuend
        
        # Display the problem
        print(f"Problem {i}: {minuend} - {subtrahend} = ?")
        
        # Get the user's answer
        user_answer = int(input("Your answer: "))
        
        # Check if the answer is correct
        if user_answer == (minuend - subtrahend):
            correct_answers += 1
    
    # Record the end time
    end_time = time.time()
    
    # Calculate the total time taken
    time_taken = round(end_time - start_time, 2)
    
    # Display the final score and time taken
    print(f"\nYour final score is {correct_answers} out of {total_questions}.")
    print(f"Total time taken: {time_taken} seconds.")

# Call the function to start the quiz
generate_subtraction_problems()
