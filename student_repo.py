import sqlite3
from student import Student

class StudentRepository:
    """Handles database interactions for student records."""

    def __init__(self, db_name = "students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Ensures the student table exists before performing operations."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE,
                    age INTEGER NOT NULL CHECK(age >= 5 AND age<=120),
                    grade INTEGER NOT NULL
                    )
        """)
        self.conn.commit()

    def add_student(self, student):
        """Insert a new student record into the database."""
        self.cursor.execute("INSERT INTO students (student_id, name, age, grade) VALUES (?, ?, ?, ?)", 
                            (student.student_id, student.name, student.age, student.grade))
        self.conn.commit()

    def get_students(self):
        """Retrieve all students from the database."""
        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()
        return [Student(*row) for row in rows]

    def delete_student(self, student_id):
        """Delete a student record based on student ID."""
        self.cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        self.conn.close()



