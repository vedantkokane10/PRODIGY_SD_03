import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for name, info in contacts.items():
            print(f"{name}: {info['phone']} | {info['email']}")

def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    
    if name in contacts:
        print("Current contact details:")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        
        contacts[name]['phone'] = input("Enter the new phone number (press Enter to keep existing): ") or contacts[name]['phone']
        contacts[name]['email'] = input("Enter the new email address (press Enter to keep existing): ") or contacts[name]['email']

        print(f"Contact {name} edited successfully!")
    else:
        print(f"No contact found with the name {name}.")

def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"No contact found with the name {name}.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
