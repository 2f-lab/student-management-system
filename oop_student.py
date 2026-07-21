class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def introduce(self):

        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")


student1 = Student("Brian", 25)

student1.introduce()