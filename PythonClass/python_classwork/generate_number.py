import random

def generate_question():
	number = random.randint(1, 1000)
	question = f"What is the sum of {number} + 2?"
	question_one = f"What is the sum of {number} + 2?"
	return number, question
	return number, question_one

def get_user_answer():
	number, question = generate_question()
	print(question)
	print(question_one)
	user_answer = int(input("Your answer: "))
	correct_answer = number + 2
		if user_answer == correct_answer:
	print("Correct!")
	else:
		print(f"Incorrect. The correct answer is {correct_answer}.")

get_user_answer()
