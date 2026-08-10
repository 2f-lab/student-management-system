class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

    def __str__(self):
        return f"{self.name} ({self.age})"