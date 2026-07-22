from school import School

school = School()

while True:

    print("\n===== MENU =====")
    print("1. View Students")
    print("2. Add Student")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":

        school.show_students()

    elif choice == "2":

        try:

            name = input("Student Name: ")

            age = int(input("Age: "))

            school.add_student(name, age)

        except ValueError as e:

            print(f"\nError: {e}")

    elif choice == "3":

        print("Goodbye!")

        break

    else:

        print("Invalid choice.")