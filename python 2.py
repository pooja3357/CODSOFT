contacts = {}
def add_contact(name, phone, email):
    contacts[name] = {'Phone': phone, 'Email': email}
    print(f"Contact {name} added successfully!")
def view_contacts():
    if contacts:
        print("\n*** Contact List ***")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}\n")
    else:
        print("\nNo contacts found!")
def search_contact(name):
    if name in contacts:
        print("\n*** Contact Found ***")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}\n")
    else:
        print("\nContact not found!")
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("\nContact not found!")
while True:
    print("\n*****Contact Book Menu*****")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter the name to search: ")
        search_contact(name)
    elif choice == '4':
        name = input("Enter the name to delete: ")
        delete_contact(name)
    elif choice == '5':
        print("Exiting the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")