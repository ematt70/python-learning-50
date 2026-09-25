"""
Exercise 20 — Mini-Project: Contact Book

Task:
    Build a simple contact book that supports:
        - Add contact
        - List contacts
        - Search contacts
        - Delete contacts
"""

contacts = {}

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Added {name}")

def list_contacts():
    if not contacts:
        print("No contacts.")
        return
    for name, info in contacts.items():
        print(f"{name}: {info['phone']} ({info['email']})")

def search_contact():
    name = input("Search name: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"{name}: {info['phone']} ({info['email']})")
    else:
        print("Not found.")

def delete_contact():
    name = input("Delete name: ").strip()
    if name in contacts:
        del contacts[name]
        print("Deleted.")
    else:
        print("Not found.")

def main():
    while True:
        print("\n1) Add  2) List  3) Search  4) Delete  5) Quit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
