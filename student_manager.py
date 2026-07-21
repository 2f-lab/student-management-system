students = []

file = open("students.txt", "r")

for line in file:
    students.append(line.strip())

file.close()


def save_students():

    file = open("students.txt", "w")

    for student in students:
        file.write(student + "\n")

    file.close()


def show_title():
    print("=" * 35)
    print("   STUDENT MANAGEMENT SYSTEM")
    print("=" * 35)


def show_students():

    print("\nCurrent Students:\n")

    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print(student)

    print(f"\nTotal Students: {len(students)}")


def add_student():

    print("\nADD NEW STUDENT")

    new_student = input("Enter student name: ").strip()

    if new_student == "":
        print("\nStudent name cannot be empty.")
        return

    if new_student in students:
        print("\nStudent already exists.")
        return

    students.append(new_student)

    save_students()

    print(f"\n{new_student} added successfully!")


def remove_student():

    print("\nREMOVE STUDENT")

    student_name = input("Enter student name to remove: ").strip()

    if student_name in students:
        students.remove(student_name)

        save_students()

        print(f"\n{student_name} removed successfully!")

    else:
        print("\nStudent not found.")


def search_student():

    print("\nSEARCH STUDENT")

    student_name = input("Enter student name to search: ").strip()

    if student_name in students:
        print(f"\n✓ {student_name} is in the student list.")
    else:
        print(f"\n✗ {student_name} was not found.")


while True:

    show_title()

    print("\n1. View Students")
    print("2. Add Student")
    print("3. Remove Student")
    print("4. Search Student")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        show_students()

    elif choice == "2":
        add_student()

    elif choice == "3":
        remove_student()

    elif choice == "4":
        search_student()

    elif choice == "5":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")