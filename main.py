from student_service import StudentService

def main():
    """Runs the command-line interface for the student management system."""
    service = StudentService()

    while True:
        print("\n Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                student_id = int(input("Enter student ID: "))
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                grade = int(input("Enter student grade: "))

                service.add_student(student_id, name, age, grade)
            except ValueError:
                print("Invalid input! Please enter valid numbers for ID, age, and grade.")

        elif choice == "2":
            students = service.get_students()
            if not students:
                print("No students found")
            else:
                print("\n Student List:")
                for student in students:
                    print(f"ID: {student.student_id} | {student.name} | Age: {student.age} | Grade: {student.grade}")

        elif choice == "3":
            try:
                student_id = int(input("Enter student ID to delete: "))
                service.delete_student(student_id)
            except ValueError:
                print("Invalid input! Enter a valid student ID.")

        elif choice == "4":
            print("Exiting... Goodbye!")
            service.close()
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()