students = []


def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\n===== Student List =====")

        for student in students:
            print("--------------------")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])


def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\n===== Student Found =====")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])

            found = True

    if not found:
        print("Student not found.")


def update_student():
    search_name = input("Enter student name to update: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():

            print("\nStudent found!")
            print("Current Name:", student["name"])
            print("Current Age:", student["age"])
            print("Current Course:", student["course"])

            new_name = input("Enter new name: ")
            new_age = input("Enter new age: ")
            new_course = input("Enter new course: ")

            student["name"] = new_name
            student["age"] = new_age
            student["course"] = new_course

            print("Student updated successfully!")

            found = True

    if not found:
        print("Student not found.")


def delete_student():
    search_name = input("Enter student name to delete: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():

            students.remove(student)

            print("Student deleted successfully!")

            found = True
            break

    if not found:
        print("Student not found.")


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")