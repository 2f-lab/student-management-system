from exceptions import InvalidAgeError


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value < 0:
            raise InvalidAgeError("Age cannot be negative.")

        if value > 100:
            raise InvalidAgeError("Age cannot be above 100.")

        self._age = value

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

    def __str__(self):
        return f"{self.name} ({self.age})"