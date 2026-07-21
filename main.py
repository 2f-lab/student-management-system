from school import School

school = School()

while True:

    print("\n===== MENU =====")
    print("1. View Students")
    print("2. Add Student")
    print("3. Remove Student")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        school.show_students()

    elif choice == "2":

        name = input("Student Name: ")

        while True:
            try:
                age = int(input("Age: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        school.add_student(name, age)

    elif choice == "3":

        name = input("Student name to remove: ")

        school.remove_student(name)

    elif choice == "4":

        print("Goodbye!")

        break

    else:

        print("Invalid choice.")