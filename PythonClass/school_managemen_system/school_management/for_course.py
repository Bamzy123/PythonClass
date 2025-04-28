class Course:
    def __init__(self, course_name:str, lecturer_name:str):
        self.course_name = course_name
        self.lecturer_name = lecturer_name
        self.students = []

    def get_course_name(self) -> str:
        return self.course_name

    def get_list_of_students(self) -> list:
        return self.students

    def get_list_of_lecturers(self) -> str:
        return self.lecturer_name

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            raise ValueError("Student has not enrolled this course")