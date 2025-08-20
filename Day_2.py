# Student Database Program using Dictionary

def main():
    student_db = {}
    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add student")
        print("2. Update student")
        print("3. Remove student")
        print("4. View all students")
        print("5. Search student")
        print("6. Show total number of students")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            roll = input("Enter roll number: ")
            name = input("Enter student name: ")
            student_db[roll] = name
            print(f"Student added: {roll} - {name}")

        elif choice == '2':
            roll = input("Enter roll number to update: ")
            if roll in student_db:
                name = input("Enter new name: ")
                student_db[roll] = name
                print(f"Student updated: {roll} - {name}")
            else:
                print("Roll number not found.")

        elif choice == '3':
            roll = input("Enter roll number to remove: ")
            if roll in student_db:
                removed = student_db.pop(roll)
                print(f"Removed student: {roll} - {removed}")
            else:
                print("Roll number not found.")

        elif choice == '4':
            if student_db:
                print("\nAll Students:")
                for roll, name in student_db.items():
                    print(f"Roll: {roll}, Name: {name}")
            else:
                print("No students in database.")

        elif choice == '5':
            roll = input("Enter roll number to search: ")
            if roll in student_db:
                print(f"Found: {roll} - {student_db[roll]}")
            else:
                print("Student not found.")

        elif choice == '6':
            print(f"Total students: {len(student_db)}")

        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
