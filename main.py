from course import Course
from teacher import Teacher

if __name__ == '__main__':
  c1 = Course(3, ['PHP', 'Python', 'Node.Js'])
  c2 = Course(2, ['Dart', 'Go'])
  c3 = Course(1, ['React-Native'])
  t = Teacher(3, [c1, c2, c3])
  t.getCourses()
