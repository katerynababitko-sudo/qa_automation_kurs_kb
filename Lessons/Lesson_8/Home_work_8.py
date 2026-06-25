class Student:
    def __init__(self, name: str, surname: str, age: int, average_grade: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def set_average_student_grade(self, average_grade: float):
        """
        Method to set a new average grade for the defined student.
        :param average_grade: float.
        """
        self.average_grade = average_grade


# Task_1

student = Student("Petro", "Petrenko", 18, 4.5)

print(f"The new Student is added:\n {student.name} {student.surname},\n age: {student.age},\n "
      f"average grade: {student.average_grade}")

student.set_average_student_grade(4.6)

print(f"The information is updated for Student:\n {student.name} {student.surname},\n age: {student.age},\n "
      f"new average grade: {student.average_grade}")
