"""
Exercise 20 — Mini-Project: Contact Book

Task:
    Build a simple contact book that supports:
        - Add contact
        - List contacts
        - Search contacts
        - Delete contacts

Instructions:
    - Store contacts in a dictionary.
    - Use a loop to show a menu.
    - Each contact should have name, phone, email.

Expected Interaction:
    1) Add  2) List  3) Search  4) Delete  5) Quit
"""

import time

contacts = {}

def printMainMenu():
    print("1) Add  2) List  3) Search  4) Delete  5) Quit")
    userSelection = input("Select an option (1-5): ")

    if userSelection == "1":
        print("\033[2J\033[H", end="")
        addContact()
    elif userSelection == "2":
        print("\033[2J\033[H", end="")
        listContacts()
    elif userSelection == "3":
        print("\033[2J\033[H", end="")
    elif userSelection == "4":
        print("\033[2J\033[H", end="")
    elif userSelection == "5":
        print("\033[2J\033[H", end="")
        quit = True
        return quit
    else:
        print("Invalid selection.")
        time.sleep(2)
        print("\033[2J\033[H", end="")
        printMainMenu()

def addContact():
    name = input("Enter a name: ").strip()
    email = input("Enter an email: ").strip()
    phone = input("Enter a phone number: ").strip()
    contacts[name] = {
        "email": email,
        "phone": phone
    }
    print(f"Contact {name} added.")
    time.sleep(2)
    print("\033[2J\033[H", end="")
    printMainMenu()

def listContacts():
    for key, value in contacts.items():
        print(f"{key}: {value}")

def searchContacts():
    search = input("Enter a name to search for: ")
    if search in contacts:
        contactInfo = contacts[search]  
        print(f"{search}: {contactInfo['email']} ({contactInfo['phone']})")
    else:
        print(f"Contact {search} not found.")

def deleteContact():
    delete = input("Enter a contact to delete:").strip()
    if delete in contacts:
        del contacts[delete]
        print(f"Contact {delete} deleted.")
    else:
        print(f"Contact {delete} not in contacts list.")
    
def main():
    # Write your code below:
    quit = False
    while quit == False:
        printMainMenu()
    print("Goodbye!")



if __name__ == "__main__":
    main()
