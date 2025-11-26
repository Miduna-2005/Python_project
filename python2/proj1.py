# Student Record Management System
# Using: dictionary, list, tuple, set

students = {}           # to store student records
student_ids = set()     # to avoid duplicate IDs
courses = ("CSE", "CDS", "ML", "AI", "EEE", "ECE")  # tuple (fixed courses list)


def add_student():
    sid = input("Enter Student ID: ")

    if sid in student_ids:
        print("❌ Student ID already exists!")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input(f"Enter Course {courses}: ")
    marks = float(input("Enter Marks: "))

    student = {
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    } #dictionary

    students[sid] = student      # add to dictionary
    student_ids.add(sid)         # add to set

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students available")
        return

    print("\n--- Student Records ---")
    for sid, details in students.items():
        print(f"ID: {sid} -> {details}")


def search_student():
    sid = input("Enter Student ID to search: ")

    if sid in students:
        print(f"Student Found: {students[sid]}")
    else:
        print("Student not found")


def delete_student():
    sid = input("Enter Student ID to delete: ")

    if sid in students:
        del students[sid]
        student_ids.remove(sid)
        print("Student deleted successfully")
    else:
        print("Student not found")


while True:
    print("\n====== Student Management Menu ======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again")