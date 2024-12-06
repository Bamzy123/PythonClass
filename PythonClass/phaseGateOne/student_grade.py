"""
def student_grade():

	total_student = int(input("How many students do you have? "))

	total_subject = int(input("How many subjects do they offer? "))

	
	student = [[0] * total_subject for number in range(total_student)]

	sum_scores = [0] * total_student

	total_sum = [0] * total_student

	average = [0.0] * total_student

	position = [0] * total_student


	for student_number in range(total_student):

		total = 0

		for subject_number in range(total_subject):

			score = int(input(f"Enter the score of student {student_number + 1} \n Enter the score of subject {subject_number + 1}: "))

			student[student_number][subject_number] = score

			print("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

			print("Saved successfully")

			print("===========================================================")

			total += score

		sum_scores[student_number] = total

		total_sum[student_number] = total

		average[student_number] = total / total_subject


	sorted_total_sum = sorted(total_sum, reverse = True)

	for student_number in range(total_student):

		position[student_number] = total_student - sorted_total_sum.index(sum_scores[student_number])

	print("STUDENT", end = "")

	for subject_number in range(1, total_subject):

		print(f"{'SUB' + str(subject_number):>10}", end = "")


	print(f"{'TOT':>10}{'AVE':>10}{'POS':>10}")

	print("=" * 70)

	for student_number in range(total_student):

		print(f"student{student_number + 1}", end = "")

		for subject_number in range(total_subject):

			print(f"{student[student_number][subject_number]:>10}", end = "")

		print(f"{sum_scores[student_number]:>8}{average[student_number]:>9.2f}{position[student_number]:>10}")

		print("=" * 70)

		print()

	print("\nSUBJECT SUMMARY")

	for subject_number in range(total_subject):

		largest = -1

		smallest = 101

		higest_student = 0

		lowest_student = 0

		total_score_of_subject = 0

		pass_count = 0

		fail_count = 0

		for student_number in range(total_student):

			total_score_of_subject += student[student_number][subject_number]

			if student[student_number][subject_number] >= 40:

				pass_count += 1

			else:
				fail_count += 1

			if student[student_number][subject_number] > largest:

				largest = student[student_number][subject_number]

				highest_student = student_number + 1

			if student[student_number][subject_number] < smallest:

				smallest = student[student_number][subject_number]

				lowest_student = student_number + 1

		  average_score_of_subject = total_score_of_subject / total_student

		print(f"\nSubject {subject_number + 1}")

		print(f"Highest scoring student is: student {highest_student} scoring {largest}")

		print(f"Lowest scoring student is: student {lowest_student} scoring {smallest}")

		print(f"Total score is: {total_score_of_subject}")

		print(f"Average score is: {average_score_of_subject:.2f}")

		print(f"\nNumber of passes: {pass_count} \nNumber of fails: {fail_count}")

student_grade()
"""

def main():
    total_student = int(input("How many students do you have? "))
    total_subject = int(input("How many subjects do they offer? "))

    student = [[0] * total_subject for _ in range(total_student)]
    sum_scores = [0] * total_student
    total_sum = [0] * total_student
    average = [0.0] * total_student
    position = [0] * total_student

    # Collecting student scores
    for student_number in range(total_student):
        total = 0
        for subject_number in range(total_subject):
            score = int(input(f"Enter the score of student {student_number + 1}\nEnter the score of subject {subject_number + 1}: "))
            student[student_number][subject_number] = score
            print("Saving >>>>>>>>>>>>>>>>>>>>>>>>>\n")
            print("Saved successfully")
            print("======================================================================")
            total += score

        sum_scores[student_number] = total
        total_sum[student_number] = total
        average[student_number] = total / total_subject

    # Sorting to get positions based on total scores
    sorted_total_sum = sorted(total_sum, reverse=True)
    for student_number in range(total_student):
        position[student_number] = total_student - sorted_total_sum.index(sum_scores[student_number])

    # Displaying student details
    print("STUDENT", end="")
    for subject_number in range(1, total_subject + 1):
        print(f"{'SUB' + str(subject_number):>10}", end="")
    
    print(f"{'TOT':>10}{'AVE':>10}{'POS':>10}")
    print("=" * 70)

    for student_number in range(total_student):
        print(f"student {student_number + 1}", end="")
        for subject_number in range(total_subject):
            print(f"{student[student_number][subject_number]:>10}", end="")
        print(f"{sum_scores[student_number]:>8}{average[student_number]:>9.2f}{position[student_number]:>10}")
        print("=" * 70)
        print()

    # Subject summary
    print("\nSUBJECT SUMMARY")
    for subject_number in range(total_subject):
        largest = -1
        smallest = 101
        highest_student = 0
        lowest_student = 0
        total_score_of_subject = 0
        pass_count = 0
        fail_count = 0

        for student_number in range(total_student):
            total_score_of_subject += student[student_number][subject_number]
            if student[student_number][subject_number] >= 40:
                pass_count += 1
            else:
                fail_count += 1

            if student[student_number][subject_number] > largest:
                largest = student[student_number][subject_number]
                highest_student = student_number + 1

            if student[student_number][subject_number] < smallest:
                smallest = student[student_number][subject_number]
                lowest_student = student_number + 1

        average_score_of_subject = total_score_of_subject / total_student
        print(f"\nSubject {subject_number + 1}")
        print(f"Highest scoring student is: Student {highest_student} scoring {largest}")
        print(f"Lowest scoring student is: Student {lowest_student} scoring {smallest}")
        print(f"Total score is: {total_score_of_subject}")
        print(f"Average score is: {average_score_of_subject:.2f}")
        print(f"\nNumber of passes: {pass_count}\nNumber of fails: {fail_count}")

if __name__ == "__main__":
    main()
