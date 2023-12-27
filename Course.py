class Course:
    def __init__(self, n, courses):
        self.numberOfCourses = n
        self.coursesData = courses
    
    def getAllCourseTeachers(self):
        return self.coursesData
