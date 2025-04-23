from student import Student 
from student_repo import StudentRepository

class StudentService:
    """Implements business logic for student record management."""

    def __init__(self):
        self.repo = StudentRepository()

    def add_student(self, student_id, name, age, grade):
        """Validate student data and add them to the repository."""
        if age <= 15:
            print("Error: age must be greater than 15!")
            return False
        if grade <= 70:
            print("Error: grade must be greater than 70!")
            return False
        
        student = Student(student_id, name, age, grade)
        self.repo.add_student(student)
        print("Student added successfully!")
        return True

    def get_students(self):
        """Retrieve and return all student records."""
        students = self.repo.get_students()
        return students
    
    def delete_student(self, student_id):
        """Delete a student record using the repository layer."""
        self.repo.delete_student(student_id)
        print(f"Student with ID {student_id} deleted successfully!")

    def close(self):
        """Close the repository connection."""
        self.repo.close()

