from tabulate import tabulate


def student_score():
 
    students_scores = []
    
    
    for i in range(1, 11):
        print(f"Enter scores for Student {i} (Python, Java, Data Science, Design thinking) between 0 and 100:")
        python_score = int(input("Python: "))
        java_score = int(input("Java: "))
        data_science_score = int(input("Data Science: "))
        design_thinking_science_score = int(input("Design thinking: "))
        
        
        if not all(1 <= score <= 100 for score in [python_score, java_score, design_thinking_score, data_science_score]):
            print("Invalid input. Please enter scores between 1 and 100.")
            return

        # Store the student's scores as a list
        students_scores.append([python_score, java_score, design_thinking_score, data_science_score])

    # Prepare the table headers
    headers = ["Student", "Highest Score", "Lowest Score"]

    # Prepare the rows for the table
    table_data = []
    for i, scores in enumerate(students_scores, start=1):
        highest_score = max(scores)
        lowest_score = min(scores)
        table_data.append([i, highest_score, lowest_score])

    # Print the table using tabulate
    print("\nScores Summary:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Call the function
find_highest_and_lowest_scores()
