file_name = "records.txt"


def save_record():
    print("\n====== Save Record ======")

    user_text = input("Enter data to save: ")

    with open(file_name, "a") as file:
        file.write(user_text + "\n")

    print("Record saved successfully!")


def view_records():
    print("\n====== Saved Records ======")

    try:
        with open(file_name, "r") as file:
            data = file.readlines()

            if len(data) == 0:
                print("No records found.")
                return

            for number, line in enumerate(data, start=1):
                print(f"{number}. {line.strip()}")

    except FileNotFoundError:
        print("No file found yet!")


def search_record():
    print("\n====== Search Record ======")

    search_word = input("Enter keyword to search: ")

    found = False

    try:
        with open(file_name, "r") as file:
            for line in file:
                if search_word.lower() in line.lower():
                    print("Found:", line.strip())
                    found = True

        if not found:
            print("No matching record found.")

    except FileNotFoundError:
        print("File not found!")


def count_records():
    print("\n====== Record Counter ======")

    try:
        with open(file_name, "r") as file:
            total_lines = len(file.readlines())

        print("Total Saved Records:", total_lines)

    except FileNotFoundError:
        print("No file found!")


def clear_records():
    print("\n====== Clear Records ======")

    confirmation = input(
        "Are you sure? (yes/no): "
    ).lower()

    if confirmation == "yes":
        open(file_name, "w").close()
        print("All records deleted!")
    else:
        print("Cancelled.")


while True:
    print("\n")
    print("====== SMART FILE RECORD MANAGER ======")
    print("1. Save Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Count Records")
    print("5. Clear Records")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        save_record()

    elif choice == "2":
        view_records()

    elif choice == "3":
        search_record()

    elif choice == "4":
        count_records()

    elif choice == "5":
        clear_records()

    elif choice == "6":
        print("Program Closed Successfully!")
        break

    else:
        print("Invalid option! Try again.")
