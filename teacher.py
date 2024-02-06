class Teacher:
    def __init__(self, n: int, courses: list):
        self.coursesNumber = n
        self.coursesList = courses
    def getCourses(self):
        print(self.coursesList)