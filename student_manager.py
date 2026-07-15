students = ["Brian", "Sarah", "James"]


def show_title():
    print("=" * 35)
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("=" * 35)


def show_students():
    print("\nCurrent Students:\n")

    for student in students:
        print(student)

    print(f"\nTotal Students: {len(students)}")


def add_student():
    print("\nADD NEW STUDENT")

    new_student = input("Enter student name: ")

    students.append(new_student)

    print(f"{new_student} added successfully!")


show_title()

show_students()

add_student()

show_students()