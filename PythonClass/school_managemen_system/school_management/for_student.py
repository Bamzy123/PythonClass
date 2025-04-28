from school_management.abstract_class import User

class Student(User):
    def __init__(self, first_name: str, last_name: str, email: str):
        super().__init__(first_name, last_name, email)
        self.courses = []
        self.__per_course_grades: float = 0.0

    def get_courses(self):
        return self.courses

    def get_grade(self):
        return self.__per_course_grades

    def add_course(self, course_name: str):
        if course_name in self.courses:
            raise ValueError("Course already exists")
        self.courses.append(course_name)

    def user_info(self):
        return (f"Student: {self.get_full_name()}," 
                f"email: {self.get_email()},"
                f"Courses: {self.get_courses()},"
                f"Grade: {self.get_grade()}")