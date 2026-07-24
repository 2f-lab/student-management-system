from person import Person


class Student(Person):

    def __init__(self, name, age):

        super().__init__(name, age)

    def view_details(self):

        print("------ STUDENT ------")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")