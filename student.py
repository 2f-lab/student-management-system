from person import Person


class Student(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("I am a student.")