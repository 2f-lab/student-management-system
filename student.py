class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def introduce(self):

        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

    def birthday(self):

        self.age += 1

        print(f"Happy Birthday {self.name}!")

    def view_details(self):

        print("------ STUDENT ------")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")