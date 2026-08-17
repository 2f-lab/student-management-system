from school import School
from exceptions import InvalidAgeError


school = School()

try:
    school.add_student("Brian", 25)
    school.add_teacher("Mr Kim", 45)

except InvalidAgeError as error:
    print(f"Error: {error}")

else:
    print("People added successfully.")

school.show_people()