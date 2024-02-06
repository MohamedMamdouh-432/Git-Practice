from course import Course
from student import Student
from teacher import Teacher

if __name__ == '__main__':
  c1 = Course(3, ['PHP', 'Python', 'Node.Js'])
  c2 = Course(2, ['Dart', 'Go'])
  c3 = Course(1, ['React-Native'])
  t1 = Teacher(2, [c1, c2])
  t2 = Teacher(2, [c2, c3])
  s = Student(2, [t1, t2])
  s.getTeachers()
