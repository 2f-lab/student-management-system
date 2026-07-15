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


show_title()
show_students()