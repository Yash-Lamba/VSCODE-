#dictionary to store contacts
contacts = {"Raj": {"number": "1234567890", "email": "raj@example.com", "age": "25"}}

#add contacts
def add_contact():
    name = input("Enter contact name:").title().strip()
    number = input("Enter contact Number:")  
    email = input("Enter contact email:")
    age = input("Enter contact age:")
    contacts[name] = {'number': number, 'email': email, 'age': age}
#delete contacts
def delete_contact():
    name = input("Enter contact name to delete:").title().strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")
#list contacts
def list_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Number: {info['number']}, Email: {info['email']}, Age: {info['age']}")
    else:
        print("No contacts found.")
#view a contact
def view_contact():
    name = input("Enter contact name to view:").title().strip()
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}, Number: {info['number']}, Email: {info['email']}, Age: {info['age']}")
    else:
        print(f"Contact {name} not found.")
#edit a contact
def edit_contact():
    name = input("Enter contact to edit:").title().strip()
    edits = input("Enter the field to edit (number/email/age):")
    if name in contacts:
        info = contacts[name]
        if edits in info:
            new_value = input(f"Enter new value for {edits}:")
            info[edits] = new_value
            print(f"Contact {name} updated.")
        else:
            print(f"Field {edits} not found.")
    else:
        print(f"Contact {name} not found.")

#main function
def main():
    print("Contact Manager")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. List Contacts")
    print("4. View Contact")
    print("5. Edit Contact")
    print("6. Exit")
    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            delete_contact()
        elif choice == '3':
            list_contacts()
        elif choice == '4':
            view_contact()
        elif choice == '5':
            edit_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

main()