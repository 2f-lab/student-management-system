# school.py
from student import Student
from teacher import Teacher


class School:
    def __init__(self):
        self.people = []

    def add_student(self, name, age):
        # Check for duplicate (optional but good practice)
        if self.search_student(name):
            print(f"Student '{name}' already exists.")
            return False
        student = Student(name, age)
        self.people.append(student)
        print(f"Student {name} added.")
        return True

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

    def update_student(self, name, new_name=None, new_age=None):
        """Update a student's name and/or age."""
        student = self.search_student(name)
        if not student:
            print(f"Student '{name}' not found.")
            return False

        # Update name if provided
        if new_name:
            # Check if new name already exists (to avoid duplicates)
            if new_name != name and self.search_student(new_name):
                print(f"A student with name '{new_name}' already exists.")
                return False
            student.name = new_name
            print(f"Name updated to '{new_name}'.")

        # Update age if provided
        if new_age is not None:
            # Age validation is handled inside the property setter of Person
            student.age = new_age
            print(f"Age updated to {new_age}.")

        return True

    def delete_student(self, name):
        """Remove the first student with matching name."""
        for i, person in enumerate(self.people):
            if isinstance(person, Student) and person.name == name:
                del self.people[i]
                print(f"Student {name} deleted.")
                return True
        print(f"Student {name} not found.")
        return False