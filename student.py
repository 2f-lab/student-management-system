class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age cannot be negative.")

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

    def __str__(self):

        return f"{self.name} ({self.age})"