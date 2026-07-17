import json
import os

FILE_NAME = "passwords.json"


def load_passwords():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_passwords(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_password():
    website = input("Enter Website: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    data = load_passwords()
    data[website] = {
        "username": username,
        "password": password
    }

    save_passwords(data)
    print("✅ Password Saved Successfully!")


def view_passwords():
    data = load_passwords()

    if not data:
        print("No passwords saved.")
        return

    print("\nSaved Passwords:\n")

    for website, details in data.items():
        print(f"Website : {website}")
        print(f"Username: {details['username']}")
        print(f"Password: {details['password']}")
        print("-" * 30)


def search_password():
    website = input("Enter Website to Search: ")

    data = load_passwords()

    if website in data:
        print("\nPassword Found")
        print(f"Username: {data[website]['username']}")
        print(f"Password: {data[website]['password']}")
    else:
        print("❌ Website not found.")


def delete_password():
    website = input("Enter Website to Delete: ")

    data = load_passwords()

    if website in data:
        del data[website]
        save_passwords(data)
        print("✅ Password Deleted Successfully!")
    else:
        print("❌ Website not found.")


while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        search_password()
    elif choice == "4":
        delete_password()
    elif choice == "5":
        print("Thank you for using Password Manager!")
        break
    else:
        print("Invalid Choice!")
