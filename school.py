# school.py
from student import Student
from teacher import Teacher


class School:
    def __init__(self):
        self.people = []

    def add_student(self, name, age):
        student = Student(name, age)
        self.people.append(student)
        print(f"Student {name} added.")

    def add_teacher(self, name, age):
        teacher = Teacher(name, age)
        self.people.append(teacher)
        print(f"Teacher {name} added.")

    def show_people(self):
        if not self.people:
            print("No people in the school.")
            return
        for person in self.people:
            print(person)

    def search_student(self, name):
        """Return the first student with matching name (case‑sensitive)."""
        for person in self.people:
            if isinstance(person, Student) and person.name == name:
                return person
        return None

    def delete_student(self, name):
        """Remove the first student with matching name."""
        for i, person in enumerate(self.people):
            if isinstance(person, Student) and person.name == name:
                del self.people[i]
                print(f"Student {name} deleted.")
                return True
        print(f"Student {name} not found.")
        return False