# storage.py
from student import Student


def save_students(students):
    """Write the current list of Student objects to students.txt."""
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"{student.name},{student.age}\n")


def load_students():
    """Read students.txt and return a list of Student objects."""
    students = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, age = line.split(",")
                age = int(age)

                student = Student(name, age)
                students.append(student)

    except FileNotFoundError:
        # If the file doesn't exist yet, return an empty list
        return []

    return students