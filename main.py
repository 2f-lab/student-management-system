# main.py
from storage import load_students, save_students
from school import School


def get_valid_age(prompt):
    """Repeatedly ask for an integer age until valid."""
    while True:
        try:
            age = int(input(prompt))
            return age
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_non_empty_string(prompt):
    """Ask for input until a non‑empty string is given."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def display_menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. View all students")
    print("2. Add a new student")
    print("3. Search for a student")
    print("4. Update a student")
    print("5. Delete a student")
    print("6. Save and exit")
    print("=====================================")


def main():
    # Load existing students
    students = load_students()
    school = School()
    school.people = students

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("\n--- All Students ---")
            school.show_people()

        elif choice == "2":
            print("\n--- Add a New Student ---")
            name = get_non_empty_string("Enter student name: ")
            age = get_valid_age("Enter student age: ")
            school.add_student(name, age)

        elif choice == "3":
            print("\n--- Search for a Student ---")
            name = get_non_empty_string("Enter student name to search: ")
            student = school.search_student(name)
            if student:
                print(f"Found: {student}")
            else:
                print(f"No student named '{name}' found.")

        elif choice == "4":
            print("\n--- Update a Student ---")
            name = get_non_empty_string("Enter the current student name: ")
            student = school.search_student(name)
            if not student:
                print(f"Student '{name}' not found.")
                continue

            print(f"Current details: {student}")
            new_name = input("Enter new name (press Enter to keep unchanged): ").strip()
            if not new_name:
                new_name = None

            new_age_input = input("Enter new age (press Enter to keep unchanged): ").strip()
            new_age = None
            if new_age_input:
                try:
                    new_age = int(new_age_input)
                except ValueError:
                    print("Invalid age. Keeping old age.")
                    new_age = None

            school.update_student(name, new_name, new_age)

        elif choice == "5":
            print("\n--- Delete a Student ---")
            name = get_non_empty_string("Enter student name to delete: ")
            school.delete_student(name)

        elif choice == "6":
            print("\nSaving data...")
            save_students(school.people)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()