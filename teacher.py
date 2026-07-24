from person import Person


class Teacher(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def introduce(self):
        super().introduce()
        print("I am a teacher.")

    def view_details(self):
        print("------ TEACHER ------")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")