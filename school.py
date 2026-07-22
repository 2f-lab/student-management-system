from student import Student


class School:

    def __init__(self):

        self.students = []
        self.load_students()

    def add_student(self, name, age):

        student = Student(name, age)

        self.students.append(student)

        self.save_students()

        print(f"{name} added successfully!")

    def remove_student(self, name):

        for student in self.students:

            if student.name.lower() == name.lower():

                self.students.remove(student)

                self.save_students()

                print(f"{name} removed successfully!")

                return

        print("Student not found.")

    def show_students(self):

        print("\n===== STUDENTS =====")

        if len(self.students) == 0:

            print("No students.")

        else:

            for student in self.students:

                print(student)

    def save_students(self):

        file = open("students.txt", "w")

        for student in self.students:

            file.write(f"{student.name},{student.age}\n")

        file.close()

    def load_students(self):

        try:

            file = open("students.txt", "r")

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                name, age = line.split(",")

                student = Student(name, int(age))

                self.students.append(student)

            file.close()

        except FileNotFoundError:

            file = open("students.txt", "w")

            file.close()