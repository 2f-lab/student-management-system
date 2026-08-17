from student import Student
from teacher import Teacher


class School:

    def __init__(self):
        self.people = []

    def add_student(self, name, age):
        student = Student(name, age)
        self.people.append(student)

    def add_teacher(self, name, age):
        teacher = Teacher(name, age)
        self.people.append(teacher)

    def show_people(self):

        for person in self.people:
            person.introduce()
            print()