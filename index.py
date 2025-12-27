import json
import os

# File to store student data
FILE_NAME = "students.json"

# Load existing data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save data to file
def save_data(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add a student
def add_student(students):
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students[roll] = {"name": name, "age": age, "course": course}
    save_data(students)
    print("Student added successfully!")

# Search for a student
def search_student(students):
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print("Student Found:")
        print(f"Name: {students[roll]['name']}")
        print(f"Age: {students[roll]['age']}")
        print(f"Course: {students[roll]['course']}")
    else:
        print("Student not found!")

# Delete a student
def delete_student(students):
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        save_data(students)
        print("Student deleted successfully!")
    else:
        print("Student not found!")

# Update student details
def update_student(students):
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        print("1. Update Name")
        print("2. Update Age")
        print("3. Update Course")
        choice = input("Enter choice: ")

        if choice == "1":
            students[roll]["name"] = input("Enter new name: ")
        elif choice == "2":
            students[roll]["age"] = input("Enter new age: ")
        elif choice == "3":
            students[roll]["course"] = input("Enter new course: ")
        else:
            print("Invalid choice!")
            return

        save_data(students)
        print("Details updated successfully!")
    else:
        print("Student not found!")

# Display all students
def display_students(students):
    if not students:
        print("No records found!")
        return

    print("\nStudent Records:")
    for roll, details in students.items():
        print(f"\nRoll No: {roll}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Course: {details['course']}")
    print()

# Main menu
def main():
    students = load_data()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            search_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            display_students(students)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

main()
