# main.py
from storage import load_students, save_students
from school import School


def display_menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. View all students")
    print("2. Add a new student")
    print("3. Search for a student")
    print("4. Delete a student")
    print("5. Save and exit")
    print("=====================================")


def main():
    # Load existing students
    students = load_students()
    school = School()
    school.people = students

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\n--- All Students ---")
            school.show_people()

        elif choice == "2":
            print("\n--- Add a New Student ---")
            name = input("Enter student name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            try:
                age = int(input("Enter student age: "))
            except ValueError:
                print("Invalid age. Please enter a number.")
                continue
            school.add_student(name, age)

        elif choice == "3":
            print("\n--- Search for a Student ---")
            name = input("Enter student name to search: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            student = school.search_student(name)
            if student:
                print(f"Found: {student}")
            else:
                print(f"No student named '{name}' found.")

        elif choice == "4":
            print("\n--- Delete a Student ---")
            name = input("Enter student name to delete: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            school.delete_student(name)

        elif choice == "5":
            print("\nSaving data...")
            save_students(school.people)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1-5.")

    # Final save (just in case)
    save_students(school.people)


if __name__ == "__main__":
    main()