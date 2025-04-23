class Student:
    """Represents a student with an ID, name, age, and grade. """

    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student({self.student_id}, {self.name}, {self.age}, {self.grade})"