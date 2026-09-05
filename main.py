# main.py
from storage import load_students, save_students
from school import School


def main():
    # Load any existing students from file
    students = load_students()

    # Create a school and add the loaded students
    school = School()
    school.people = students  # Direct assignment because School uses self.people list

    # Show current students
    print("Current students loaded from file:")
    if school.people:
        for person in school.people:
            print(person)
    else:
        print("No students found.")

    # Add a new student (for testing persistence)
    print("\nAdding a new student...")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    school.add_student(name, age)

    # Show updated list
    print("\nUpdated student list:")
    for person in school.people:
        print(person)

    # Save all students back to file
    save_students(school.people)
    print("\nStudents saved to students.txt")


if __name__ == "__main__":
    main()