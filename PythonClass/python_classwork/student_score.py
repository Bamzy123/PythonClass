def find_highest_and_lowest_scores():
    # Initialize a list to store scores for each student
    students_scores = []
    
    # Get scores for 10 students
    for i in range(1, 11):
        print(f"Enter scores for Student {i} (Python, Java, Design Thinking, Data Science) between 1 and 100:")
        python_score = int(input("Python: "))
        java_score = int(input("Java: "))
        design_thinking_score = int(input("Design Thinking: "))
        data_science_score = int(input("Data Science: "))
        
        # Check if the scores are valid
        if not all(1 <= score <= 100 for score in [python_score, java_score, design_thinking_score, data_science_score]):
            print("Invalid input. Please enter scores between 1 and 100.")
            return

        # Store the student's scores as a tuple
        students_scores.append([python_score, java_score, design_thinking_score, data_science_score])

    # Flatten the list of students' scores into a single list to find highest and lowest scores
    all_scores = [score for student in students_scores for score in student]
    
    # Find the highest and lowest scores
    highest_score = max(all_scores)
    lowest_score = min(all_scores)

    print(f"The highest score is: {highest_score}")
    print(f"The lowest score is: {lowest_score}")

# Call the function
find_highest_and_lowest_scores()
