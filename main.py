student_records = []


def generate_student_id():
    return f"STU{len(student_records) + 1:03}"


def calculate_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 75:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    else:
        return "Fail"


def add_new_student():
    print("\n========== Add Student ==========")

    student_name = input("Enter Student Name: ")
    roll_number = input("Enter Roll Number: ")

    try:
        student_marks = float(input("Enter Marks (0-100): "))

        if student_marks < 0 or student_marks > 100:
            print("Marks should be between 0 and 100!")
            return

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    student_data = {
        "id": generate_student_id(),
        "name": student_name,
        "roll": roll_number,
        "marks": student_marks,
        "grade": calculate_grade(student_marks)
    }

    student_records.append(student_data)

    print("\n✅ Student Added Successfully!")
    print("Student ID:", student_data["id"])


def display_all_students():
    print("\n========== Student Records ==========")

    if len(student_records) == 0:
        print("No student data available.")
        return

    for student in student_records:
        print("\n--------------------------------")
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Roll No    :", student["roll"])
        print("Marks      :", student["marks"])
        print("Grade      :", student["grade"])


def search_student():
    print("\n========== Search Student ==========")

    search_roll = input("Enter Roll Number: ")

    found = False

    for student in student_records:
        if student["roll"] == search_roll:
            print("\nStudent Found!")
            print("---------------------------")
            print("Student ID :", student["id"])
            print("Name       :", student["name"])
            print("Marks      :", student["marks"])
            print("Grade      :", student["grade"])
            found = True
            break

    if not found:
        print("Student not found!")


while True:
    print("\n")
    print("===== SMART STUDENT RECORD HUB =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    user_choice = input("Select Option: ")

    if user_choice == "1":
        add_new_student()

    elif user_choice == "2":
        display_all_students()

    elif user_choice == "3":
        search_student()

    elif user_choice == "4":
        print("Program Closed Successfully!")
        break

    else:
        print("Invalid Option! Please try again.")