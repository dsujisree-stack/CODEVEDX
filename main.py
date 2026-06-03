import random
import string

password_storage = []


def build_secure_password():
    print("\n====== SecurePass Lab ======")

    account_name = input("Password label (Ex: Gmail): ")

    try:
        password_size = int(input("Choose password length: "))
    except ValueError:
        print("Numbers only allowed!")
        return

    if password_size < 6:
        print("Password too short! Minimum 6 characters.")
        return

    add_symbols = input(
        "Need special symbols? (yes/no): "
    ).lower()

    base_characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits
    )

    if add_symbols == "yes":
        base_characters += "@#$%&*!?"

    generated_password = ""

    for _ in range(password_size):
        generated_password += random.choice(base_characters)

    password_score = evaluate_password(generated_password)

    password_storage.append({
        "label": account_name,
        "password": generated_password,
        "score": password_score
    })

    print("\nPassword Created Successfully!")
    print("Account :", account_name)
    print("Password:", generated_password)
    print("Security Score:", password_score, "/10")

    random_security_advice()


def evaluate_password(password):
    points = 0

    if len(password) >= 8:
        points += 2

    if any(letter.isupper() for letter in password):
        points += 2

    if any(letter.islower() for letter in password):
        points += 2

    if any(letter.isdigit() for letter in password):
        points += 2

    special_symbols = "@#$%&*!?"
    if any(letter in special_symbols for letter in password):
        points += 2

    return points


def show_saved_passwords():
    print("\n====== Saved Password List ======")

    if len(password_storage) == 0:
        print("No passwords saved.")
        return

    for item_number, item in enumerate(password_storage, start=1):
        print("\n----------------------------")
        print("No       :", item_number)
        print("Account  :", item["label"])
        print("Password :", item["password"])
        print("Score    :", item["score"], "/10")


def random_security_advice():
    advice_list = [
        "Never use your birth date as password.",
        "Use different passwords for each account.",
        "Strong passwords reduce hacking risk.",
        "Use both numbers and symbols."
    ]

    print("\nSecurity Advice:")
    print(random.choice(advice_list))


while True:
    print("\n")
    print("====== SECUREPASS LAB ======")
    print("1. Generate Secure Password")
    print("2. View Saved Passwords")
    print("3. Exit")

    selected_option = input("Choose option: ")

    if selected_option == "1":
        build_secure_password()

    elif selected_option == "2":
        show_saved_passwords()

    elif selected_option == "3":
        print("SecurePass Lab Closed!")
        break

    else:
        print("Invalid option selected!")