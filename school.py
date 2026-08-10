from student import Student
from teacher import Teacher


class School:

    def __init__(self):
        self.people = []

    def add_student(self, name, age):

        student = Student(name, age)

        self.people.append(student)

        print(f"{name} added successfully as a Student!")

    def add_teacher(self, name, age):

        teacher = Teacher(name, age)

        self.people.append(teacher)

        print(f"{name} added successfully as a Teacher!")

    def show_people(self):

        print("\n===== PEOPLE =====")

        if len(self.people) == 0:

            print("No people found.")

        else:

            for person in self.people:

                person.introduce()

                print()