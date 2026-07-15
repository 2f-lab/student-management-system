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

    print(f"\n{new_student} added successfully!")


show_title()

print("\n1. View Students")
print("2. Add Student")

choice = input("\nChoose an option: ")

if choice == "1":
    show_students()

elif choice == "2":
    add_student()
    show_students()

else:
    print("Invalid choice.")