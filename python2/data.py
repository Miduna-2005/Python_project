import csv
import os

filename = "students.csv"

# Create file if not exists
def create_file():
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Marks"])
        print("Student file created!\n")


# Add Student
def add_student():
    id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id, name, marks])

    print("Student Added!\n")


# View all students
def view_students():
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()


# Search student by ID
def search_student():
    sid = input("Enter ID to search: ")
    found = False

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == sid:
                print("Student Found:", row)
                found = True
                break

    if not found:
        print("No student with this ID.\n")


# Update student record
def update_student():
    sid = input("Enter ID to update: ")
    rows = []
    updated = False

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == sid:
                name = input("Enter new name: ")
                marks = input("Enter new marks: ")
                rows.append([sid, name, marks])
                updated = True
            else:
                rows.append(row)

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if updated:
        print("Student Updated!\n")
    else:
        print("ID not found!\n")


# Delete Student
def delete_student():
    sid = input("Enter ID to delete: ")
    rows = []
    deleted = False

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != sid:
                rows.append(row)
            else:
                deleted = True

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if deleted:
        print("Student Deleted!\n")
    else:
        print("ID not found!\n")


# ------------------------------
# MAIN MENU
# ------------------------------

create_file()  # create csv if missing

while True:
    print("====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. View All Students")
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
        print("Exiting...")
        break
    else:
        print("Invalid option! Try again.\n")
