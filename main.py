from school import School

school = School()

while True:

    print("\n" + "=" * 35)
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("=" * 35)

    print("1. View Students")
    print("2. Add Student")
    print("3. Remove Student")
    print("4. Search Student")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        school.show_students()

    elif choice == "2":

        name = input("Enter student name: ")

        while True:

            try:
                age = int(input("Enter age: "))
                break

            except ValueError:
                print("Please enter a valid age.")

        school.add_student(name, age)

    elif choice == "3":

        name = input("Enter student name to remove: ")

        school.remove_student(name)

    elif choice == "4":

        name = input("Enter student name to search: ")

        school.search_student(name)

    elif choice == "5":

        print("\nGoodbye!")

        break

    else:

        print("\nInvalid choice. Please try again.")