from student import Student


class School:

    def __init__(self):

        self.students = []

    def add_student(self, name, age):

        student = Student(name, age)

        self.students.append(student)

        print(f"{name} added successfully!")

    def show_students(self):

        print("\n===== STUDENTS =====")

        if len(self.students) == 0:

            print("No students.")

        else:

            for student in self.students:

                student.view_details()

                print()