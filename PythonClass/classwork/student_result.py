def print_student_scores():
    
    students = []
    

    for number in range(10):

        name = input(f"Enter the name of student {number + 1}: ")

        print()

        python_score = int(input(f"Enter {name} score for Python (1-100): "))

        print()

        java_score = int(input(f"Enter {name} score for Java (1-100): "))

        print()

        design_thinking_score = int(input(f"Enter {name} score for Design Thinking (1-100): "))

        print()

        data_science_score = int(input(f"Enter {name} score for Data Science (1-100): "))
        
        
        students.append({
            "name": name,
            "python": python_score,
            "java": java_score,
            "design_thinking": design_thinking_score,
            "data_science": data_science_score
        })
    
    
    print(f"\n{'Student Name'} | {'Python':<7} | {'Java':<5} | {'Design Thinking':<15} | {'Data Science':<12} | {'Highest Score':<13} | {'Lowest Score':<12}")
    print("-" * 95)
    

    for student in students:

        scores = [student['python'], student['java'], student['design_thinking'], student['data_science']]
        
        
        highest_score = max(scores)
        lowest_score = min(scores)
        
        
        print(f"{student['name']:<15} | {student['python']:<7} | {student['java']:<5} | {student['design_thinking']:<15} | {student['data_science']:<12} | {highest_score:<13} | {lowest_score:<12}")
  
        

print_student_scores()
