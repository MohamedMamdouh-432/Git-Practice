class Student:
    def __init__(self, n: int, teachers: list):
        self.teachersNumber = n
        self.teachersList = teachers
    def getTeachers(self):
        print(self.teachersList)