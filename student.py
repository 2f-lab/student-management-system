from person import Person


class Student(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def introduce(self):
        super().introduce()
        print("I am a student.")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}!")

    def view_details(self):
        print("------ STUDENT ------")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")